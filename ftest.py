from selenium import webdriver

driver = webdriver.Chrome('D:\\RTA\\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('localhost:4040')
html = driver.page_source
f = open("temp.txt", "w")
f.write(html)
f.close()
"""from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://python.org')

html = driver.page_source
print(html)"""
