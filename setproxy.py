from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from getproxy import get_proxy
import time

def set_proxy(): 
    # get_proxy()
    # f=open('myproxylist.txt','r')
    # PROXY = f.read()
    # f.close()

    PROXY = get_proxy() 
    time.sleep(15)
    webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "noProxy": None,
    "proxyType": "MANUAL",
    "autodetect": False
    }