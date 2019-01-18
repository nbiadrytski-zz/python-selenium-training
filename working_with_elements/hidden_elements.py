from selenium import webdriver
import time


class HiddenElements():
    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(5)

        text_field = driver.find_element_by_id("displayed-text")
        text_field_state = text_field.is_displayed()
        print("Text is visible: " + str(text_field_state))
        time.sleep(2)

        # click Hide button
        driver.find_element_by_id("hide-textbox").click()
        text_field_state = text_field.is_displayed()
        text_field_state2 = text_field.is_enabled()
        print("Text is visible: " + str(text_field_state))
        print("Text is enabled: " + str(text_field_state2))
        time.sleep(2)

        # click Show button
        driver.find_element_by_id("show-textbox").click()
        text_field_state = text_field.is_displayed()
        print("Text is visible: " + str(text_field_state))
        time.sleep(2)

        driver.quit()


ff = HiddenElements()
ff.test()
