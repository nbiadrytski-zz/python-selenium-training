from selenium import webdriver
from utilities.handy_wrappers import HandyWrappers
import time


class UsingWrappers():

    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)

        hw = HandyWrappers(driver)

        driver.get(base_url)

        text_field1 = hw.find_elem("name")
        text_field1.send_keys("Test")
        time.sleep(2)

        text_field2 = hw.find_elem("//input[@id='name']", locator_type="xpath")
        text_field2.clear()


ff = UsingWrappers()
ff.test()
