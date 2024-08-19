import time
import calendar
import requests

url = "https://api.hamsterkombatgame.io/clicker/tap"

headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Authorization": "Bearer 'цензура']",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

}

while True:
    utc = time.gmtime()
    timeunix = calendar.timegm(utc)
    print(timeunix)

    data = {"count": 410, "availableTaps": 0, "timestamp": timeunix}
    #Сколько раз можно нажать при полной шкале, с учетом количесвта монет за тап

    response = requests.post(url, headers=headers, json=data)

    print(response.status_code)
    time.sleep(1800) #Сколько необходимо времени для заполнения шкалы