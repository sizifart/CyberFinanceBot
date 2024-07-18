# CyberFinanceBot
🖱️ clicker for [https://t.me/CyberFinanceBot](https://t.me/CyberFinanceBot?start=cj1PQlVQOU1BWUFtelAmdT1yZWY=)


## Functionality
| Functional                                                                      | Supported |
|----------------------------------------------------------------|:---------:|
| Auto Upgrade Hammer                                            |     ✅     |
| Auto Upgrade Egg                                               |     ✅     |
| Auto Claim                                                     |     ✅     |
| Auto Clear Task                                                |     ✅     |
| Auto Refresh Token                                             |     ✅     |
| Add Limit Upgrade                                              |     ✅     |
| Multi Account Support                                          |     ✅     |


## Installation
| NO.                      | Step                                                                                    |
|------------------------------|-------------------------------------------------------------------------------------|
| 1.        | Install with Python Download Python 3.10+                                                                                   |
| 2.        | Install Required Modules: pip install requests colorama,Open CFI Bot on PC (Telegram Desktop)          |
| 3.        | Get Initialization Parameters Open Telegram Web/Desktop: Right-click and select Inspect (F12), Go to Application > Session Storage, Find -> Telegram_initparams, Copy tgwebappdata and save it in initdata.txt                                                                                                         |
| 4.        | Run the Script: python main.py                                                                                   |


## Settings data file
| Setting                      | Description                                                                                    |
|------------------------------|------------------------------------------------------------------------------------------------|
| query_id        | fill the `initdata.txt` file with your data, how to get data you can refer to [How to Get Data](#how-to-get-data)                      |


## Requirements
- Python 3.9 (you can install it [here](https://www.python.org/downloads/release/python-390/)) 
- How to Get Data (you can get them [here](#how-to-get-data))
  
## Auto Install/Run
- Click on Install.bat to automatically install the required dependencies 
- Then click on START.bat to run the project

## Menual Install/Run
1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
## Usage
1. Run the bot:
   ```bash
   python main.py
   ```
   
# How to Get Data
   
   1. Active web inspecting in telegram app
   2. Goto bot and open the apps
   3. Press `F12` on your keyboard to open devtool or right click on app and select `Inspect`
   4. Goto `console` menu and copy [javascript code](#javascript-command-to-get-telegram-data-for-desktop) then paste on `console` menu
   5. If you don't receive error message, it means you successfully copy telegram data then paste on `query.txt` (1 line for 1 telegram data)
   
   Example telegram data

   ```
   query_id=xxxxxxxxxx&user=xxxxxxfirst_namexxxxxlast_namexxxxxxxusernamexxxxxxxlanguage_codexxxxxxxallows_write_to_pmxxxxxxx&auth_date=xxxxxx&hash=xxxxxxxxxxxxxxxxxxxxx
   ```

   6. If you want to add more account. Just paste telegram second account data in line number 2.
   
   Maybe like this sample in below

   ```
   1.query_id=xxxxxxxxxx&user=xxxxxxfirst_namexxxxxlast_namexxxxxxxusernamexxxxxxxlanguage_codexxxxxxxallows_write_to_pmxxxxxxx&auth_date=xxxxxx&hash=xxxxxxxxxxxxxxxxxxxxx
   2.query_id=xxxxxxxxxx&user=xxxxxxfirst_namexxxxxlast_namexxxxxxxusernamexxxxxxxlanguage_codexxxxxxxallows_write_to_pmxxxxxxx&auth_date=xxxxxx&hash=xxxxxxxxxxxxxxxxxxxxx
   ```

# Javascript Command to Get Telegram Data for Desktop

```javascript
copy(Telegram.WebApp.initData)
```

# Discussion

If you have an question or something you can ask in here : [F.Davoodi](https://t.me/sizifart)

