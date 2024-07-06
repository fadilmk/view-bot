from selenium import webdriver
import time
import random

views = int(input('enter the number of views : '))
url = input('enter url of video : ')
min = int(input('enter the minimum time : '))
max = int(input('enter the maximum time : '))

browser = webdriver.Chrome()

for i in range(views):
    browser.get(url)
    time.sleep(random.randint(min, max))
    print(f'view {i+1} completed')
browser.close()
print('all views completed')
input('press any key to exit')