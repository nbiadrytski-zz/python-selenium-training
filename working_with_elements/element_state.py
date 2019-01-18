from selenium import webdriver
import time

class ElementState():

    def is_enabled(self):
        base_url = "http://www.google.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        e1 = driver.find_element_by_xpath("//input[@name='q']")
        e1_state = e1.is_enabled()
        print("Element is enabled: " + str(e1_state))
        e1.send_keys("test")

        time.sleep(3)


chrome_instance = ElementState()
chrome_instance.is_enabled()
