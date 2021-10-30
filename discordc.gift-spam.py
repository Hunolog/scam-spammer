import requests
import threading
import random
import string


def logn():
    em_f_n = "".join(random.choices(string.ascii_letters, k=15))
    pw_f_n = "".join(random.choices(string.ascii_letters + string.digits, k=15))
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
        "Content-Type": "application/json",
    }
    content = {"login": em_f_n + "@gmail.com", "password": pw_f_n}
    r = requests.post(
        "https://discordc.gift/discord/login", headers=headers, json=content
    )
    print(r.text)


while True:
    if threading.active_count() < 100:
        threading.Thread(target=logn).start()








        