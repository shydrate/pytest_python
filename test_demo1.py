from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import pytest

def test_search():
    print("Running selenium test")
    try:
        driver = webdriver.Chrome(executable_path="D:\\Downloaded\\chromedriver.exe")
        driver.get("https://www.google.com/")
        driver.find_element_by_xpath("//input[@name='q']").send_keys("Saiprasad Shettar")
        driver.find_element_by_xpath("//input[@name='q']").send_keys(Keys.ENTER)
        time.sleep(2)
        print("Selenium test over")
        driver.close()
        driver.quit()
    except NoSuchElementException as NEA:
        print("Element not present :{}".format(NEA))

@pytest.mark.smoke
def test_shydrate():
    try:
        print("Selenium test for shydrate")
        driver = webdriver.Chrome(executable_path="D:\\Downloaded\\chromedriver.exe")
        driver.get("http://shydrate.com/")
        time.sleep(2)
        print("Selenium test for shydrate over")
    except NoSuchElementException as NA:
        print("Element not present :{}".format(NA))
