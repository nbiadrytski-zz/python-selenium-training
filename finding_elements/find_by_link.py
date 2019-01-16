from selenium import webdriver


class FindByLinkText():
    def test(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(base_url)
        element_by_link_text = driver.find_element_by_link_text("Login")

        if element_by_link_text is not None:
            print("Element by link_text found")

        element_by_partial_link_text = driver.find_element_by_partial_link_text("Pract")

        if element_by_partial_link_text is not None:
            print("Element by partial_link_text found")


chrom = FindByLinkText()
chrom.test()