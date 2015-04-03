#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: home
# @Date:   2015-03-06 12:53:44
# @Last Modified by:   home
# @Last Modified time: 2015-03-06 13:01:18

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()