import requests
import datetime
import time
from colorama import init, Fore, Style
import sys
import os
init(autoreset=True)

def print_welcome_message():
    print(r"""
    ███████╗██╗███████╗     ██████╗ ██████╗ ██████╗ ███████╗██████╗ 
    ██╔════╝██║╚══███╔╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
    ███████╗██║  ███╔╝     ██║     ██║   ██║██║  ██║█████╗  ██████╔╝
    ╚════██║██║ ███╔╝      ██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗
    ███████║██║███████╗    ╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║
    ╚══════╝╚═╝╚══════╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
          """)
    print(Fore.GREEN + Style.BRIGHT + "Cyberfinance AUTO BOT")
    print(Fore.YELLOW + Style.BRIGHT + "Prepared and Developed by: F.Davoodi")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def fetch_access_token(init_data):
    url = "https://api.cyberfin.xyz/api/v1/game/initdata"
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://g.cyberfin.xyz',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://g.cyberfin.xyz/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'secret-key': 'cyberfinance',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36'
    }
    data = f'{{"initData":"{init_data}"}}'
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 201:
        return response.json()['message']['accessToken']
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{current_time} Failed to fetch access token")
        return None

def read_tokens():
    with open('initdata.txt', 'r') as file:
        return [line.strip() for line in file if line.strip()]

def info_balance(ini_token):
    url = "https://api.cyberfin.xyz/api/v1/game/mining/gamedata"
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'authorization': f'Bearer {ini_token}',  
        'dnt': '1',
        'if-none-match': 'W/"173-kqxt3jfCFv2BCBRPJM7mhgWVfbI"',
        'origin': 'https://g.cyberfin.xyz',
        'priority': 'u=1, i',
        'referer': 'https://g.cyberfin.xyz/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'secret-key': 'cyberfinance',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    crack_time = data['message']['miningData']['crackTime']
    now = datetime.datetime.now().timestamp()
    countdown = crack_time - now
    hours, remainder = divmod(countdown, 3600)
    minutes, seconds = divmod(remainder, 60)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{current_time} {Fore.BLUE+Style.BRIGHT}[ Cracking ]:", f"{Fore.BLUE+Style.BRIGHT}{int(hours):02} Hours {int(minutes):02} Minutes", f"{Fore.BLUE+Style.BRIGHT}until claim")

def claim_mining(ini_token):
    url = "https://api.cyberfin.xyz/api/v1/mining/claim"
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'authorization': f'Bearer {ini_token}',  
        'dnt': '1',
        'if-none-match': 'W/"173-kqxt3jfCFv2BCBRPJM7mhgWVfbI"',
        'origin': 'https://g.cyberfin.xyz',
        'priority': 'u=1, i',
        'referer': 'https://g.cyberfin.xyz/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'secret-key': 'cyberfinance',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{current_time} {Fore.YELLOW+Style.BRIGHT}[ Claim ]: {data['message']}")

def auto_upgrade_hammer(ini_token, max_level):
    url = "https://api.cyberfin.xyz/api/v1/mining/boost/apply"
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'authorization': f'Bearer {ini_token}',  
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://g.cyberfin.xyz',
        'priority': 'u=1, i',
        'referer': 'https://g.cyberfin.xyz/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'secret-key': 'cyberfinance',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    data = '{"boostType":"HAMMER"}'
    while True:
        response = requests.post(url, headers=headers, data=data)
        if response.status_code != 201:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sys.stdout.write(f"{current_time} {Fore.RED+Style.BRIGHT}[ Hammer ]: Insufficient balance\n")
            break
        response_data = response.json()
        current_level = response_data['message']['boostData']['hammerLevel']
        sys.stdout.write(f"\r{Fore.GREEN+Style.BRIGHT}[ Hammer ] Successful Upgrade. Level: {current_level}")
        if current_level >= max_level:
            sys.stdout.write(f"\n{Fore.GREEN+Style.BRIGHT}[ Hammer ] Already at level {current_level}\n")
            break

def auto_upgrade_egg(ini_token, max_level):
    url = "https://api.cyberfin.xyz/api/v1/mining/boost/apply"
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'authorization': f'Bearer {ini_token}',  
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://g.cyberfin.xyz',
        'priority': 'u=1, i',
        'referer': 'https://g.cyberfin.xyz/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'secret-key': 'cyberfinance',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    data = '{"boostType":"EGG"}'
    while True:
        response = requests.post(url, headers=headers, data=data)
        if response.status_code != 201:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sys.stdout.write(f"{current_time} {Fore.RED+Style.BRIGHT}[ Egg Level ]: Insufficient balance\n")
            break
        response_data = response.json()
        current_level = response_data['message']['boostData']['eggLevel']
        sys.stdout.write(f"\r{Fore.GREEN+Style.BRIGHT}[ Egg Level ] Successful Upgrade. Level: {current_level}")
        if current_level >= max_level:
            sys.stdout.write(f"\n{Fore.GREEN+Style.BRIGHT}[ Egg Level ] Already at level {current_level}\n")
            break

def fetch_uuids(ini_token):
    url = "https://api.cyberfin.xyz/api/v1/gametask/all"
    headers = {
        'Authorization': f'Bearer {ini_token}',  
        'accept': 'application/json',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'dnt': '1',
        'if-none-match': 'W/"173-kqxt3jfCFv2BCBRPJM7mhgWVfbI"',
        'origin': 'https://g.cyberfin.xyz',
        'priority': 'u=1, i',
        'referer': 'https://g.cyberfin.xyz/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'secret-key': 'cyberfinance',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        tasks = response.json()['message']
        return [(task['uuid'], task['description']) for task in tasks if not task['isCompleted']]
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{current_time} Failed to fetch tasks")
        return []

def complete_tasks(uuids, ini_token):
    base_url = "https://api.cyberfin.xyz/api/v1/gametask/complete/"
    headers = {
        'Authorization': f'Bearer {ini_token}',  
        'Content-Type': 'application/json'
    }
    for uuid, description in uuids:
        response = requests.patch(f"{base_url}{uuid}", headers=headers)
        response_data = response.json()
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if response.status_code == 200:
            print(f"{current_time} {Fore.GREEN+Style.BRIGHT}[ Task ]: {description} Completed")
        else:
            print(f"{current_time} {Fore.RED+Style.BRIGHT}[ Task ]: {description} Failed. {response_data['message']}")

def user_level(ini_token):
    url = "https://api.cyberfin.xyz/api/v1/mining/boost/info"
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'authorization': f'Bearer {ini_token}',  
        'dnt': '1',
        'if-none-match': 'W/"a4-LZ8zXP3aEql/rLf1iujkfLlL6Tk"',
        'origin': 'https://g.cyberfin.xyz',
        'priority': 'u=1, i',
        'referer': 'https://g.cyberfin.xyz/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'secret-key': 'cyberfinance',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()['message']
        return data
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{current_time} {Fore.RED+Style.BRIGHT}[ Failed to get user level information ]")

def get_mining_info(ini_token):
    url = "https://api.cyberfin.xyz/api/v1/game/mining/gamedata"
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {ini_token}',
        'cache-control': 'no-cache',
        'origin': 'https://g.cyberfin.xyz',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://g.cyberfin.xyz/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126", "Microsoft Edge WebView2";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'secret-key': 'cyberfinance',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()['message']
        balance = int(data['userData']['balance'])
        mining_rate = data['miningData']['miningRate']
        now = datetime.datetime.now().timestamp()
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{current_time} {Fore.YELLOW+Style.BRIGHT}[ Balance ]: {balance:,}")
        print(f"{current_time} {Fore.YELLOW+Style.BRIGHT}[ Mining Rate ]: {mining_rate}")
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{current_time} {Fore.RED+Style.BRIGHT}[ Failed to get mining information ]")

def main():
    print_welcome_message()
    user_input_task = input("Auto cleartask? (y / n): ")
    user_input_hammer = input("Auto upgrade hammer (Cracking Power)? (y / n): ")
    if user_input_hammer == 'y':
        max_hammer_level = int(input("Max Upgrade Until Level? : "))
    
    user_input_egg = input("Auto upgrade egg (Hours per Claim)? (y / n): ")
    if user_input_egg == 'y':
        max_egg_level = int(input("Max Upgrade Until Level? : "))
 
    clear_console()
    while True:
        print_welcome_message()
        tokens = read_tokens()  
        for index, init_data in enumerate(tokens):
            ini_token = fetch_access_token(init_data)
            if not ini_token:
                continue
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{current_time} {Fore.CYAN+Style.BRIGHT}============== [ Account {index + 1} ] ==============")
            get_mining_info(ini_token)  
            datauser = user_level(ini_token)
            if datauser:
                level_hammer = int(datauser['hammerLevel'])
                level_egg = int(datauser['eggLevel'])
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"{current_time} {Fore.BLUE+Style.BRIGHT}[ Hammer Level ]: {level_hammer}")
                print(f"{current_time} {Fore.BLUE+Style.BRIGHT}[ Egg Level ]: {level_egg}")
                if user_input_hammer.lower() == 'y':
                    if level_hammer >= max_hammer_level:
                        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        print(f"{current_time} {Fore.RED+Style.BRIGHT}[ Hammer Level ]: Already at level {level_hammer} ")
                    else:
                        auto_upgrade_hammer(ini_token, max_hammer_level)
                if user_input_egg.lower() == 'y':
                    if level_egg >= max_egg_level:
                        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        print(f"{current_time} {Fore.RED+Style.BRIGHT}[ Egg Level ]: Already at level {level_egg} ")
                    else:
                        auto_upgrade_egg(ini_token, max_egg_level)
            if user_input_task.lower() == 'y':
                uuids = fetch_uuids(ini_token)
                complete_tasks(uuids, ini_token)
            info_balance(ini_token)
            claim_mining(ini_token)
        for i in range(3600, 0, -1):
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sys.stdout.write(f"\r{current_time} {Fore.CYAN+Style.BRIGHT}============ Finished, waiting {i} seconds.. ============")
            sys.stdout.flush()
            time.sleep(1)
        print()
        clear_console()
        time.sleep(5)

if __name__ == "__main__":
    main()
