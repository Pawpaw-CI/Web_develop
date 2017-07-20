# -*- coding:gbk-*-
__author__ = "duxiangyang"
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')
assert 'Django' in browser.title

