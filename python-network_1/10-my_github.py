#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    token = sys.argv[2]

    r = requests.get("https://api.github.com/user", auth=(user, token))

    try:
        print(r.json().get("id"))
    except Exception:
        print("None")
