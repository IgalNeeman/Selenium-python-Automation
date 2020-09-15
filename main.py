from getproxy import get_proxy
from setproxy import set_proxy
from fakeuseragent import myfakeuseragent
from driverconfig import mydriverconfig
import time

from random import choice
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

get_proxy()
set_proxy()
mydriverconfig()
driver = webdriver.Chrome(executable_path="C:/Users/Owner/chromedriver_win32/chromedriver.exe", chrome_options=myfakeuseragent())
driver.get('https://tipcracker.net')
#time.sleep(10)
driver.implicitly_wait(10)

NoInternet = driver.find_element_by_id("main-message").is_enabled()
#NoInternet2 = driver.find_element_by_class_name("current").is_enabled()
while(NoInternet):
    time.sleep(10)
    #NoInternet = driver.find_element_by_id("main-message").is_enabled()
    #if(NoInternet == False):
    #    break
    #print("proxy not good.. close browser!")
    
    #set_proxy()
    time.sleep(5)
    driver.quit()
    time.sleep(3)
    # time.sleep(5)
    time.sleep(3)

    #options.add_argument('--proxy-server=http://%s' % proxy1['http'])
    driver = webdriver.Chrome(executable_path="C:/Program Files (x86)/Microsoft Visual Studio/Shared/Python36_64/chromedriver.exe", chrome_options=myfakeuseragent())

    time.sleep(3)
    driver.get('https://tipcracker.net')

driver.get('https://tipcracker.net/')

# try:
#     time.sleep(3)
#     OneMoreStep = driver.find_element_by_name("One more step").is_enabled()
# except OneMoreStep:
#     print ("ElementNotVisibleException OneMoreStep")
# try:
#     time.sleep(3)
#     YesInfected = driver.find_element_by_name("Yes (Infected)").is_enabled()
# except YesInfected:
#     print ("NoSuchElementException YesInfected")
# try:
#     time.sleep(3)
#     YesInfected2 = driver.find_element_by_name("Yes (Unauthenticated SMTP / Infected)").is_enabled()
# except YesInfected2:
#     print ("ElementNotVisibleException YesInfected2 ")
# try:
#     time.sleep(3)
#     CantBeReached=driver.find_element_by_name("This site can’t be reached").is_enabled()
# except CantBeReached:
#     print ("InvalidSelectorException CantBeReached")
# try:
#     time.sleep(3)
#     NotPrivate = driver.find_element_by_name("Your connection is not private").is_enabled()
# except:
#     print ("Other exception types possible NotPrivate")
#     raise


# if (NoInternet): #or (CantBeReached) or (OneMoreStep) or (NotPrivate)):
#         print("proxy not good.. close browser!")
#         driver.quit()
#         time.sleep(3)
#         get_proxy()

#     #driver.quit()
#     #time.sleep(10)
#     #get_proxy()
#         #options.add_argument('--proxy-server=%s' % PROXY)
#         #driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
#     #driver = webdriver.Chrome(chromedriver, options=chrome_options)
#         #driver.get("")   #and here is the change, just https
# else:
#         time.sleep(10)
#         if YesInfected or YesInfected2:
#             driver.get('http://infected.com/')
#         else:
#             driver.close()
#             time.sleep(5)
#             get_proxy()


#goodproxy = "No (Unauthenticated SMTP)"
# time.sleep(10)
# if (goodproxy in driver.page_source):
#    driver.get('https://tipcracker.net/')
# else:
#     driver.close()
#     time.sleep(10)
#     get_proxy()

# time.sleep(60000)
# driver.close()
