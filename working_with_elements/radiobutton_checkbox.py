from selenium import webdriver
import time


class RadioButtonCheckbox():
    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)

        bmw_radio_btn = driver.find_element_by_id("bmwradio")
        bmw_radio_btn.click()
        time.sleep(3)

        benz_radio_btn = driver.find_element_by_id("benzradio")
        benz_radio_btn.click()
        time.sleep(3)

        bmw_checkbox = driver.find_element_by_id("bmwcheck")
        bmw_checkbox.click()
        time.sleep(3)

        benz_checkbox = driver.find_element_by_id("benzcheck")
        benz_checkbox.click()
        time.sleep(3)

        print("BMW radio button is selected: " + str(bmw_radio_btn.is_selected()))
        print("Benz radio button is selected: " + str(benz_radio_btn.is_selected()))
        print("BMW checkbox is selected: " + str(bmw_checkbox.is_selected()))
        print("Benz checkbox is selected: " + str(benz_checkbox.is_selected()))


ff = RadioButtonCheckbox()
ff.test()