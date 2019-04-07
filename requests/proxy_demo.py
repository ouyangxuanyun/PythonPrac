# pip install requests[socks]
import requests
import socket
import socks

def proxy_get():
    # socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
    # socket.socket = socks.socksocket
    proxies={'http':'socks5://127.0.0.1:1080','https':'socks5://127.0.0.1:1080'}
    response=requests.get('https://www.google.com/',proxies=proxies, timeout=15)
    print(response.status_code)


proxy_get()