
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time



class testprojectlistpage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_no_option_chosen(self):
        self.browser.get(self.live_server_url)

        alert = self.browser.find_element_by_class_name('homepg')
        self.assertEquals(
            alert.find_element_by_tag_name('h1').text,'You can calculate you BMI or retirement goal'
        )

    def test_bmi_option_on_homepage(self):
        self.browser.get(self.live_server_url)

        add_url = self.live_server_url + reverse('bmi_cal:bmi')
        self.browser.find_element_by_link_text('Calculate BMI').click()
        self.assertEquals(
            self.browser.current_url,add_url
        )
        time.sleep(30)

    def test_retirement_option_on_homepage(self):
        self.browser.get(self.live_server_url)

        add_url = self.live_server_url + reverse('bmi_cal:retr')
        self.browser.find_element_by_link_text('Retirement goal').click()
        self.assertEquals(
            self.browser.current_url,add_url
        )