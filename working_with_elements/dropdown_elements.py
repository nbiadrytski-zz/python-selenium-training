from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


class DropdownElements():
    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)

        element = driver.find_element_by_id("carselect")
        drop_down = Select(element)

        drop_down.select_by_value("benz")
        print("Select Benz by value")
        time.sleep(2)

        drop_down.select_by_index("2")
        print("Select Honda by index")
        time.sleep(2)

        drop_down.select_by_visible_text("BMW")
        print("Select BMW by visible text")
        time.sleep(2)

        drop_down.select_by_index(2)
        print("Select Honda by index")
        time.sleep(2)


ff = DropdownElements()
ff.test()