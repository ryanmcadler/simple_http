import json
import time
import requests
from requests.auth import AuthBase
from colorama import Fore, Back, Style

TOKEN = "1234abbc"

VERB = "post"
URL = "https://staging.planet.com/internal/validate/"

BODY = {
    "test": True
}

DRY_RUN = True
DELAY=3

class SimpleAuth(AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["Authorization"] = f"Bearer {self.token}"
        return r


class SimpleHTTP:
    def execute():
        print("\n" + Fore.RED + "S" + Fore.YELLOW + "i" + Fore.BLUE + "m" + Fore.LIGHTMAGENTA_EX + "p" + Fore.GREEN + "l" + Fore.CYAN + "e" + Fore.WHITE+ "HTTP")
        print(Style.RESET_ALL + "\n")
        if not DRY_RUN:
            print(Fore.RED)
            print(f"Making {VERB} request...\n")
            print(f"url: {URL}\n")
            print("payload:\n")
            print(json.dumps(BODY, indent=4))
            print(Style.RESET_ALL)
            time.sleep(DELAY)
            response = requests.request(VERB, url=URL, json=BODY, auth=SimpleAuth(TOKEN))            
            print("Response...\n")
            print(f"status: {response.status_code}\n")
            print("response body:\n")
            print(json.dumps(response.json, indent=4))
        else:
            print(Fore.GREEN)
            print("Dry run...\n")
            print(f"method: {VERB}\n")
            print(f"url: {URL}\n")
            print("body:\n")
            print(json.dumps(BODY, indent=4))
        print("\n")


if __name__ == "__main__":
    SimpleHTTP.execute()
