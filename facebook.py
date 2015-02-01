import webbrowser
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import WebDriverException

lines_from_file = []
url = 'http://www.facebook.com'
login_file = open('login.txt', 'r')
for line in login_file:
	lines_from_file.append(line.strip())

def init():
	return webdriver.Chrome()

def main():
	driver = init()

main()
