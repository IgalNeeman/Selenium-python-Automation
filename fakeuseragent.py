from fake_useragent import UserAgent
from random import choice
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.options import Options
import psutil
from selenium.webdriver.common.keys import Keys


def myfakeuseragent():
    options = Options()
    options.add_argument("window-size=1400,600")
    ua = UserAgent()
    user_agent = ua.random
    print(user_agent)
    options.add_argument(f'user-agent={user_agent}')
   
