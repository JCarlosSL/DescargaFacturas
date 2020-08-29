from django.test import TestCase

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from home.tests.utils import UserBaseSeleniumTestCase
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.db.models import Q
from urllib.parse import urlparse
from django.template.loader import render_to_string
from django.urls import resolve
from django.http import HttpRequest
from home.views import (
    PostListView
)

class RegisterTestCase(UserBaseSeleniumTestCase):

    def setUp(self):
        super(RegisterTestCase, self).setUp()
        self.selenium = self.browser
    
    def tearDown(self):
        self.selenium.quit()
        self.user.delete()
        super(RegisterTestCase, self).tearDown()   
     
    def test_register(self):
        self.login()
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/register/')
        
        username = selenium.find_element_by_id('id_username')
        email = selenium.find_element_by_id('id_email')
        password1 = selenium.find_element_by_id('id_password1')
        password2 = selenium.find_element_by_id('id_password2')
        submit = selenium.find_element_by_id('register')

        username.send_keys('admin2')
        email.send_keys('yusuf@gmail.com')
        password1.send_keys('email.12')
        password2.send_keys('email.12')

        submit.click() #send_keys(Keys.RETURN)
        
        path = urlparse(selenium.current_url).path
        self.assertEqual('/', path)

        assert 'Polleria el Romancero' in selenium.page_source

        self.user = User.objects.filter(Q(username='admin2'))
    
    def test_failregister(self):
        self.login()
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/register/')

        username = selenium.find_element_by_id('id_username')
        email = selenium.find_element_by_id('id_email')
        password1 = selenium.find_element_by_id('id_password1')
        password2 = selenium.find_element_by_id('id_password2')
        submit = selenium.find_element_by_id('register')
        
        username.send_keys('admin1')
        email.send_keys('yusuf@gmail.com')
        password1.send_keys('email.12')
        #password2.send_keys('email.12')

        submit.click()
        path = urlparse(selenium.current_url).path
        self.assertEqual('/', path)
    


class LoginTestCase(LiveServerTestCase,TestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        self.user = User.objects.create_user(username="newuser",
                password="newS123", email="todo@todoapp.com")
        super(LoginTestCase,self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(LoginTestCase,self).tearDown()
    
    def test_login(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/login')
        

        username = selenium.find_element_by_id('id_username')
        contrasena = selenium.find_element_by_id('id_password')
        submit = selenium.find_element_by_id('submit_button')

        username.send_keys('admin')
        contrasena.send_keys('admin')

        submit.click() #send_keys(Keys.RETURN)

        path = urlparse(selenium.current_url).path
        self.assertEqual('/', path)
    
    def test_login_fail_password(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/login')

        username = selenium.find_element_by_id('id_username')
        submit = selenium.find_element_by_id('submit_button')

        username.send_keys('newuser')
        submit.click() #send_keys(Keys.RETURN)

        path = urlparse(selenium.current_url).path
        self.assertEqual('/', path)
        
        found = resolve('/')
        self.assertEqual(found.func.view_class,PostListView)
        
        response = self.client.get('/login/')
        self.assertEqual(response.status_code,200)


