from selenium import webdriver
from selenium.webdriver.common.by import By


class DynamicXpath():
    def test(self):
        base_url = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(base_url)

        # Login
        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.ID, "user_email").send_keys("test@email.com")
        driver.find_element(By.ID, "user_password").send_keys("abcabc")
        driver.find_element(By.NAME, "commit").click()

        # Search for courses
        driver.find_element(By.ID, "search-courses").send_keys("JavaScript")
        driver.find_element(By.ID, "search-course-button").click()

        # Select course
        course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
        course_locator = course.format("JavaScript for beginners")
        course_elem = driver.find_element(By.XPATH, course_locator)
        course_elem.click()


ff = DynamicXpath()
ff.test()