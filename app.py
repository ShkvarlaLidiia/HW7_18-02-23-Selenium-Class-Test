from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Test:
    def __init__(self, driver):
        self.driver = driver
        
    def moveTo(self, url):
        self.driver.get(url)
        
    def find_element(self, by, value):
        time.sleep(2)
        sheacher = self.driver.find_element(by=by, value=value)
        return sheacher
        
    def sendData(self, by, value, text, k):        
        elem = self.driver.find_element(by=by, value=value)
        elem.send_keys(text)
        elem.send_keys(k)
        
    def screen (self, name):
        self.driver.save_screenshot(name)
        
    def clickOn(self, by, value):
        time.sleep(2)
        elem = self.driver.find_element(by=by, value=value)
        elem.click()

chrome_test = Test(webdriver.Chrome())

chrome_test.moveTo("https://rozetka.com.ua/ua/")
chrome_test.sendData(By.NAME, "search", "smartphone", Keys.ENTER)
time.sleep(5)

chrome_test.clickOn(By.CLASS_NAME, "ng-tns-c111-1")
time.sleep(5)

chrome_test.screen("screen.png")
time.sleep(5)

chrome_test.moveTo("https://www.youtube.com/")
chrome_test.sendData(By.NAME, "search_query", "лідія шкварла dance clip", Keys.ENTER)
time.sleep(5)

chrome_test.clickOn(By.ID, "title-wrapper")

time.sleep(10)

chrome_test.screen("screen2.png")



