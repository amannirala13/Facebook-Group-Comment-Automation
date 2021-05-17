from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pynput.keyboard import Key, Controller
import time

delay = 3
csv_data = []
keyboard = Controller()
browser = webdriver.Chrome("./chromedriver.exe")


def readCSVData():
    try:
        csv_file = open("data.csv", 'r').readlines()
        for line in csv_file:
            line = line.strip()
            csv_data.append(line.split(','))
        
    except FileNotFoundError:
        print("data.csv file is missing")
        

def commentNow(post_link, comment="Up", isFirst = False):
    browser.get(post_link)
    time.sleep(delay)
    if(isFirst):
        input("||||||||||||||||||||||||\nPress any key to start service ---\n||||||||||||||||||||||||")
        time.sleep(10)
    comment_field = browser.find_element_by_xpath("//form/div")
    comment_field.click()
    for ch in range(0, len(comment)):
        keyboard.press(str(comment[ch]))
        keyboard.release(str(comment[ch]))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def startService():
    for data in csv_data:
            commentNow(data[0], data[1],(data == csv_data[0]))
        
        

if __name__ == '__main__':
    readCSVData()
    browser.get('https://www.facebook.com')
    input("||||||||||||||||||||||||\nPress any button to continue once you are done with login ---\n||||||||||||||||||||||||")
    startService()
