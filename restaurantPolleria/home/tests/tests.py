from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.urls import reverse_lazy,resolve

from home.models import Factura
from .utils import UserBaseSeleniumTestCase

from django.db.models import Q
from django.template.loader import render_to_string
from django.http import HttpRequest
from home.views import search
from home.views import (
    PostListView
)


class HomeSeleniumTest(UserBaseSeleniumTestCase,TestCase):
    def setUp(self):
        super(HomeSeleniumTest, self).setUp()

     
    def test_root_url(self):
        #self.login()
        found = resolve('/')
        self.assertEqual(found.func.view_class,PostListView)
    
    def test_table(self):
        self.login()
        table = self.browser.find_element_by_id('id-table')
        rows = table.find_elements_by_tag_name('tr')
        factura = 'F001-00001382 2019-11-09 20327881494 ver descargar'
        
        self.assertIn(factura,[row.text for row in rows])
    
    def test_search(self):
        self.login()
        element = self.browser.find_element_by_name('q')
        submit = self.browser.find_element_by_id('id_search')
        
        element.send_keys("00001382")
        submit.click()
        
        table = self.browser.find_element_by_id('id-table')
        rows = table.find_elements_by_tag_name('tr')
        factura = 'F001-00001382 2019-11-09 20327881494 ver descargar'
        
        self.assertIn(factura,[row.text for row in rows])


