#!/usr/bin/env python3
import sys
from samsungtvws import SamsungTVWS

# TV IP
TV_IP = "192.168.0.30"
TOKEN_FILE = "samsung_token.txt"

def send_key(key):
    tv = SamsungTVWS(TV_IP, token_file=TOKEN_FILE)
    try:
        tv.send_key(key)
        print(f"Sent: {key}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./tv-control.py <KEY>")
        print("Examples: KEY_POWER, KEY_VOLUP, KEY_HOME, KEY_EXIT")
        sys.exit(1)
    
    send_key(sys.argv[1])
