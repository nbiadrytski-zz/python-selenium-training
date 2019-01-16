from selenium import webdriver
from selenium.webdriver.common.by import By


class ByDemo():
    def test(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(base_url)

        element_by_id = driver.find_element(By.ID, "name")
        if element_by_id is not None:
            print("Element by id found")

        element_by_xpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        if element_by_xpath is not None:
            print("Element by xpath found")

        element_by_link = driver.find_element(By.LINK_TEXT, "Login")
        if element_by_link is not None:
            print("Element by link found")


chrome_instance = ByDemo()
chrome_instance.test()