from selenium import webdriver
import time


class GetText():
    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(5)

        open_tab_elem = driver.find_element_by_id("opentab")
        elem_text = open_tab_elem.text
        print("Text on element is: " + elem_text)
        time.sleep(2)
        driver.quit()


ff = GetText()
ff.test()