from selenium import webdriver


class FindByIdName():
    def test(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()  #webdriver.Firefox()
        driver.get(base_url)
        element_by_id = driver.find_element_by_id("name")

        if element_by_id is not None:
            print("Element by id found")

        element_by_name = driver.find_element_by_name("show-hide")

        if element_by_name is not None:
            print("Element by name found")


chrom = FindByIdName()
chrom.test()