from cuenta.tests.mixins import SeleniumScreenShotMixin
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse_lazy

from selenium import webdriver


class UserBaseSeleniumTestCase(SeleniumScreenShotMixin, StaticLiveServerTestCase):

    def setUp(self):
        self.user = User.objects.create_user("carloss", "todo@man.com", "angel..1")
        self.user.is_active = True
        self.user.save()
        self.browser = webdriver.Firefox()
        self.browser.get('http://127.0.0.1:8000/login')
        super(UserBaseSeleniumTestCase,self).setUp()

    def login(self):
        #self.browser.get('%s%s'%('http://127.0.0.1:8000/login',reverse_lazy("cuenta")))
        self.browser.find_element_by_id('id_username').send_keys("admin")
        self.browser.find_element_by_id('id_password').send_keys("admin")
        self.browser.find_element_by_id('submit_button').click()
