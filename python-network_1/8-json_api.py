#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    q = sys.argv[1] if len(sys.argv) > 1 else ""

    r = requests.post(url, data={'q': q})

    try:
        data = r.json()
        if data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
