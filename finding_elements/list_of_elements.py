from selenium import webdriver
from selenium.webdriver.common.by import By


class ListOfElements():
    def test(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(base_url)

        element_list_by_classname = driver.find_elements_by_class_name("inputs")
        length1 = len(element_list_by_classname)
        if element_list_by_classname is not None:
            print("Size of element_list_by_classname: " + str(length1))

        element_list_by_tagname = driver.find_elements(By.TAG_NAME, "h1")
        length2 = len(element_list_by_tagname)
        if element_list_by_tagname is not None:
            print("Size of element_list_by_tagname: " + str(length2))


chrome_instance = ListOfElements()
chrome_instance.test()