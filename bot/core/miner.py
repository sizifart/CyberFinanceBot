import json
import time
import datetime
import requests
from math import ceil
from random import randint
import asyncio
from urllib.parse import unquote, quote
import requests
import lxml.etree
import lxml.html
from typing import Any, Tuple, Optional, Dict, List

import aiohttp
from aiohttp_proxy import ProxyConnector
from better_proxy import Proxy
from pyrogram import Client
from pyrogram.errors import Unauthorized, UserDeactivated, AuthKeyUnregistered
from pyrogram.raw.functions.messages import RequestWebView

from bot.utils import logger
from bot.exceptions import InvalidSession
from .headers import headers
from bot.config import settings


class Miner:
    def __init__(self, tg_client: Client):
        self.session_name = tg_client.name
        self.tg_client = tg_client

    async def get_tg_web_data(self, proxy: str | None) -> str:
        try:
            if proxy:
                proxy = Proxy.from_str(proxy)
                proxy_dict = dict(
                    scheme=proxy.protocol,
                    hostname=proxy.host,
                    port=proxy.port,
                    username=proxy.login,
                    password=proxy.password
                )
            else:
                proxy_dict = None

            self.tg_client.proxy = proxy_dict

            if not self.tg_client.is_connected:
                try:
                    await self.tg_client.connect()
                except (Unauthorized, UserDeactivated, AuthKeyUnregistered):
                    raise InvalidSession(self.session_name)

            web_view = await self.tg_client.invoke(RequestWebView(
                peer=await self.tg_client.resolve_peer('CyberFinanceBot'),
                bot=await self.tg_client.resolve_peer('CyberFinanceBot'),
                platform='android',
                from_bot_menu=False,
                url='https://game.cyberfinance.xyz/'
            ))

            auth_url = web_view.url
            tg_web_data = unquote(
                string=unquote(
                    string=auth_url.split('tgWebAppData=', maxsplit=1)[1].split('&tgWebAppVersion', maxsplit=1)[0]))

            res = ''
            params = tg_web_data.split('&')
            for param in params:
                pair = param.split('=')
                res += f"{pair[0]}={quote(pair[1])}&"

            if self.tg_client.is_connected:
                await self.tg_client.disconnect()

            return res

        except InvalidSession as error:
            raise error

        except Exception as error:
            logger.error(f"{self.session_name} | Unknown error during Authorization: {error}")
            await asyncio.sleep(delay=7)

    async def check_proxy(self, http_client: aiohttp.ClientSession, proxy: Proxy) -> None:
        try:
            response = await http_client.get(url='https://httpbin.org/ip', timeout=aiohttp.ClientTimeout(5))
            ip = (await response.json()).get('origin')
            logger.info(f"{self.session_name} | Proxy IP: {ip}")
        except Exception as error:
            logger.error(f"{self.session_name} | Proxy: {proxy} | Error: {error}")

    async def login(self, http_client: aiohttp.ClientSession, tg_web_data: str) -> str:
        try:
            response = await http_client.post(
                url='https://api.cyberfin.xyz/api/v1/game/initdata',
                json={"initData": tg_web_data})
            response.raise_for_status()

            response_json = await response.json()
            access_token = response_json['message']['accessToken']

            return access_token
        except Exception as error:
            logger.error(f"{self.session_name} | Unknown error while getting Access Token: {error}")
            await asyncio.sleep(delay=7)

    async def game_data(self, http_client: aiohttp.ClientSession) -> str:
        try:
            response = await http_client.get(
                url='https://api.cyberfin.xyz/api/v1/game/mining/gamedata',
                json={})
            response.raise_for_status()

            response_json = await response.json()
            game_data = response_json

            return game_data
        except Exception as error:
            logger.error(f"{self.session_name} | Unknown error while getting game data: {error}")
            await asyncio.sleep(delay=7)

    async def claim(self, http_client: aiohttp.ClientSession) -> str:
        try:
            response = await http_client.get(
                url='https://api.cyberfin.xyz/api/v1/mining/claim',
                json={})
            response.raise_for_status()

            response_json = await response.json()
            claim_data = response_json

            return claim_data
        except Exception as error:
            logger.error(f"{self.session_name} | Unknown error while claiming: {error}")
            await asyncio.sleep(delay=7)

    async def info(self, http_client: aiohttp.ClientSession) -> str:
        try:
            response = await http_client.get(
                url='https://api.cyberfin.xyz/api/v1/mining/boost/info',
                json={})
            response.raise_for_status()

            response_json = await response.json()
            info_data = response_json

            return info_data
        except Exception as error:
            logger.error(f"{self.session_name} | Unknown error while getting storage and speed: {error}")
            await asyncio.sleep(delay=7)

    async def upgrade_speed(self, http_client: aiohttp.ClientSession) -> str:
        try:
            response = await http_client.post(
                url='https://api.cyberfin.xyz/api/v1/mining/boost/apply',
                json={"boostType":"HAMMER"})
            response.raise_for_status()

            response_json = await response.json()
            info_data = response_json

            return info_data
        except Exception as error:
            logger.error(f"{self.session_name} | Unknown error while upgrading speed: {error}")
            await asyncio.sleep(delay=7)

    async def upgrade_storage(self, http_client: aiohttp.ClientSession) -> str:
        try:
            response = await http_client.post(
                url='https://api.cyberfin.xyz/api/v1/mining/boost/apply',
                json={"boostType":"EGG"})
            response.raise_for_status()

            response_json = await response.json()
            info_data = response_json

            return info_data
        except Exception as error:
            logger.error(f"{self.session_name} | Unknown error while upgrading storage: {error}")
            await asyncio.sleep(delay=7)

    async def run(self, proxy: str | None) -> None:
        access_token = None
        access_token_created_time = 0
        sleep_time = settings.DEFAULT_SLEEP
        proxy_conn = ProxyConnector().from_url(proxy) if proxy else None

        async with (aiohttp.ClientSession(headers=headers, connector=proxy_conn) as http_client):
            if proxy:
                await self.check_proxy(http_client=http_client, proxy=proxy)

            while True:
                try:
                    if not access_token or time.time() - access_token_created_time >= 3600:
                        tg_web_data = await self.get_tg_web_data(proxy=proxy)
                        access_token = await self.login(http_client=http_client, tg_web_data=tg_web_data)

                        if access_token:
                            http_client.headers["Authorization"] = f"Bearer {access_token}"
                            headers["Authorization"] = f"Bearer {access_token}"

                            access_token_created_time = time.time()

                    if access_token:
                        game_data = await self.game_data(http_client=http_client)

                        balance = float(game_data['message']['userData']['balance'])
                        logger.info(f"{self.session_name} | balance {balance} CFI")

                        crack_time = int(game_data['message']['miningData']['crackTime'])
                        if crack_time < time.time():
                            claim_data = await self.claim(http_client=http_client)
                            if claim_data:
                                balance = float(claim_data['message']['userData']['balance'])
                                crack_time = int(claim_data['message']['miningData']['crackTime'])
                                delta_time = str(datetime.timedelta(seconds=crack_time-time.time()))
                                logger.info(f"{self.session_name} | Claimed successfully, new balance {balance} CFI, time to next claim {delta_time}")

                                sleep_time = datetime.timedelta(seconds=crack_time-time.time()).total_seconds()

                        info_data = await self.info(http_client=http_client)
                        if settings.UPGRADE_SPEED:
                            speed_price = int(info_data['message']['hammerPrice'])
                            speed_level = int(info_data['message']['hammerLevel'])
                            if settings.SPEED_MAX_LEVEL >= speed_level and balance >= speed_price:
                                uograde_data = await self.upgrade_speed(http_client=http_client)
                                if uograde_data:
                                    balance = float(uograde_data['message']['userData']['balance'])

                                    crack_time = int(uograde_data['message']['miningData']['crackTime'])
                                    delta_time = str(datetime.timedelta(seconds=crack_time-time.time()))
                                    logger.info(f"{self.session_name} | Storage upgraded successfully, new balance {balance} CFI, time to next claim {delta_time}")
                                    sleep_time = datetime.timedelta(seconds=crack_time-time.time()).total_seconds()

                        if settings.UPGRADE_STORAGE:
                            storage_price = int(info_data['message']['eggPrice'])
                            storage_level = int(info_data['message']['eggLevel'])
                            if settings.STORAGE_MAX_LEVEL >= storage_level and balance >= storage_price:
                                uograde_data = await self.upgrade_storage(http_client=http_client)
                                if uograde_data:
                                    balance = float(uograde_data['message']['userData']['balance'])

                                    crack_time = int(uograde_data['message']['miningData']['crackTime'])
                                    delta_time = str(datetime.timedelta(seconds=crack_time-time.time()))
                                    logger.info(f"{self.session_name} | Storage upgraded successfully, new balance {balance} CFI, time to next claim {delta_time}")
                                    sleep_time = datetime.timedelta(seconds=crack_time-time.time()).total_seconds()
                    else:
                        sleep_time = 15

                except InvalidSession as error:
                    raise error

                except Exception as error:
                    logger.error(f"{self.session_name} | Unknown error: {error}")
                    await asyncio.sleep(delay=7)

                else:
                    logger.info(f"{self.session_name} | Sleeping for the next cycle {sleep_time}s")
                    await asyncio.sleep(delay=sleep_time)


async def run_miner(tg_client: Client, proxy: str | None):
    try:
        await Miner(tg_client=tg_client).run(proxy=proxy)
    except InvalidSession:
        logger.error(f"{tg_client.name} | Invalid Session")