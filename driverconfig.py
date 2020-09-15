import time
import psutil
from random import choice
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from fakeuseragent import myfakeuseragent
def mydriverconfig():
    driver = webdriver.Chrome(executable_path="C:/Users/Owner/chromedriver_win32/chromedriver.exe", chrome_options=myfakeuseragent())    
    driver.set_window_size(1024, 600)
    driver.maximize_window()