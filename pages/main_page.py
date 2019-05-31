from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, locators_config_section='main_page')

        self._search_courses_field = self.locators_cfg.get_locator('search_courses_field')
        self._search_course_button = self.locators_cfg.get_locator('search_course_button')
        self._java_course = self.locators_cfg.get_locator('java_course')

    def enter_course_name(self, course):
        self._driver.type_keys(course, self._search_courses_field)

    def click_search_course_button(self):
        self._driver.click_element(self._search_course_button)

    def find_courses(self, course):
        self.enter_course_name(course)
        self.click_search_course_button()

    def java_course_present(self):
        if self._driver.is_element_present(self._java_course, 'xpath'):
            self.logger.info(f'Java course is present.')
            return True
        else:
            self.logger.error(f'Java course is missing.')
            return False
