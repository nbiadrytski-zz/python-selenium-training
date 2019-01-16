from selenium import webdriver


class FindByXpathCssName():
    def test(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(base_url)
        element_by_xpath = driver.find_element_by_xpath("//input[@id='name']")

        if element_by_xpath is not None:
            print("Element by xpath found")

        element_by_css = driver.find_element_by_css_selector("#displayed-text")

        if element_by_css is not None:
            print("Element by css found")


chrom = FindByXpathCssName()
chrom.test()