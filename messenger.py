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

#read from file to get username and passwords
lines_from_file = []
url_facebook = 'https://www.facebook.com/messages/'
login_file = open('login.txt', 'r')
for line in login_file:
	lines_from_file.append(line.strip())

def init():
	return webdriver.Chrome()

def login(driver):
	username = driver.find_element_by_id("email")
	username.send_keys(lines_from_file[2])
	password = driver.find_element_by_id("pass")
	password.send_keys(lines_from_file[1])
	login_button = driver.find_element_by_name("login")
	login_button.click()

def create_message(driver):
	new_message_button = driver.find_element_by_xpath("//*[@id=\"u_0_17\"]/button")
	new_message_button.click()

	name_line = driver.find_element_by_xpath("//*[@id=\"u_0_n\"]/div/div[2]/div/div[2]/div/table/tbody/tr/td[2]/div")
	name_line.clear()
	name_line.click()
	name_line.send_keys("Susan Huang")




def main():
	driver = init()
	driver.get(url_facebook)
	login(driver)
	create_message(driver)



main()

