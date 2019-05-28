class TestLogin:

    def test_valid_login(self, welcome_page):
        login_page = welcome_page.click_login_link()
        login_page.login('test@email.com', 'abcabc')

        assert login_page.user_is_logged_in()

    def test_invalid_login(self, welcome_page):
        login_page = welcome_page.click_login_link()
        login_page.login('test@email.com', 'abcabcabc')

        assert login_page.user_is_logged_in() is False
