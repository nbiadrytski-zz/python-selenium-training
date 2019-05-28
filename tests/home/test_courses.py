class TestCourses:

    def test_courses(self, log_in):
        main_page = log_in('test@email.com', 'abcabc')
        main_page.find_courses('java')

        assert main_page.java_course_present()
