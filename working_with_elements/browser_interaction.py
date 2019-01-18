from selenium import webdriver


class BrowserInteractions():
    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)

        title = driver.title
        print("Title of the web page: " + title)

        current_url = driver.current_url
        print("Current url of the web page: " + current_url)

        driver.refresh()
        print("Browser refreshed 1st time")

        driver.get(driver.current_url)
        print("Browser refreshed 2nd time")

        # Open another url
        driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")

        driver.back()
        print("Go one step back in browser history")

        driver.forward()
        print("Go one step forward in browser history")

        # print(driver.page_source)

        driver.quit()


firefox_instance = BrowserInteractions()
firefox_instance.test()