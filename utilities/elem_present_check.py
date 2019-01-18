from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.handy_wrappers import HandyWrappers


class ElementPresentCheck():
    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)

        hw = HandyWrappers(driver)
        driver.get(base_url)

        elem_result1 = hw.is_elem_present("name", By.ID)
        print(str(elem_result1))

        elem_result2 = hw.are_elems_present("//input[@id='name']", By.XPATH)
        print(str(elem_result2))


ff = ElementPresentCheck()
ff.test()