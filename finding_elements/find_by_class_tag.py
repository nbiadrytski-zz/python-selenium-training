from selenium import webdriver


class FindByClassTag():
    def test(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(base_url)
        element_by_class = driver.find_element_by_class_name("displayed-class")
        element_by_class.send_keys("Tesing The Element")

        if element_by_class is not None:
            print("Element by class found")

        element_by_tag = driver.find_element_by_tag_name("a")

        if element_by_tag is not None:
            print("Element by tag found")


chrom = FindByClassTag()
chrom.test()