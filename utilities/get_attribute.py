from selenium import webdriver
import time


class GetAttribute:
    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(5)

        elem = driver.find_element_by_id("name")
        result = elem.get_attribute("class")
        print("Value of attribute class is: " + result)
        time.sleep(2)

        driver.quit()


ff = GetAttribute()
ff.test()
