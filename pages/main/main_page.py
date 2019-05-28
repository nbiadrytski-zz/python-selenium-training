from base.base_webdriver import BaseWebDriver


class MainPage(BaseWebDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _search_courses_field = 'search-courses'
    _search_course_button = 'search-course-button'
    _java_course = "//div[@data-course-url='/p/selenium-webdriver-with-java']"

    def enter_course_name(self, course):
        self.type_keys(course, self._search_courses_field)

    def click_search_course_button(self):
        self.click_element(self._search_course_button)

    def find_courses(self, course):
        self.enter_course_name(course)
        self.click_search_course_button()

    def java_course_present(self):
        if self.is_element_present(self._java_course, 'xpath'):
            self.logger.info(f'Java course is present.')
            return True
        else:
            self.logger.error(f'Java course is missing.')
            return False
