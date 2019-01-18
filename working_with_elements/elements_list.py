from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ElementsList():
    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)

        radio_buttons_list = driver.find_elements(By.XPATH, "//input[contains(@type,'radio') and contains(@name,'cars')]")
        size = len(radio_buttons_list)
        print("Size of the list: " + str(size))

        for radio_button in radio_buttons_list:
            is_selected = radio_button.is_selected()
            if not is_selected:
                radio_button.click()
                time.sleep(2)


ff = ElementsList()
ff.test()