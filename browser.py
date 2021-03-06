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
url = 'http://www.google.com'
url_game = 'http://www.mousehuntgame.com'
url_google = 'https://accounts.google.com'
url_mightytext = 'https://mail.google.com'
login_file = open('login.txt', 'r')
for line in login_file:
	lines_from_file.append(line.strip())



def init():
	return webdriver.Chrome()

def init_firefox():
	return webdriver.Firefox()

def login(driver):
	print driver.title
	username = driver.find_element_by_name('accountName')
	username.send_keys(lines_from_file[0])
	password = driver.find_element_by_name('password')
	password.send_keys(lines_from_file[1])
	checkbox = driver.find_element_by_name('remember')
	checkbox.click()
	login = driver.find_element_by_name('doLogin')
	login.click()

# function for warning users when a king's reward has come up
def facebook_warning():
	driver = init_firefox()
	driver.get(url_google)

	time.sleep(1)
	email = driver.find_element_by_name('Email')
	email.send_keys('kinglamb777@gmail.com')
	time.sleep(1)
	password = driver.find_element_by_name('Passwd')
	password.send_keys('naruto77')
	login = driver.find_element_by_name('signIn')
	login.click()

	driver.get(url_mightytext)
	time.sleep(5)
	compose_button = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[1]/table[1]/tbody/tr[1]/td/b/a')
	compose_button.click()

	time.sleep(1)
	address_line = driver.find_element_by_name('to')
	address_line.send_keys('felixmbx@gmail.com')
	time.sleep(1)
	# address_line.send_keys(Keys.RETURN)

	subject_line = driver.find_element_by_name('subject')
	subject_line.send_keys('KING REWARD, PLZ SOLVE')
	time.sleep(1)

	send_button = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/form/table[3]/tbody/tr/td/input[1]')
	send_button.click()

	driver.quit()

def switch_cheese(driver):
	try:
		bait_quantity = driver.find_element_by_xpath("//*[@id=\"hud_baitQuantity\"]")
	except NoSuchElementException:
		bait = driver.find_element_by_xpath("/html/body/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[3]/div[7]/div/a[4]")
		bait.click()
		#slight delay for the page to refresh
		time.sleep(2)
		target_bait = driver.find_element_by_xpath("/html/body/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[3]/div[2]/div[3]/div/div[1]/div[4]")
		target_bait.click()

def sound_the_horn(driver):
	driver.get(url_game)

	if 'Login' in driver.title:
		login(driver)
		time.sleep(3)
		temp_title = driver.title

	try:
		daily_rewards = driver.find_element_by_xpath('//*[@id=\"jsDialogAjaxSuffix\"]/input')
		daily_rewards.click()
	except NoSuchElementException:
		pass

	horn_timer_string = ""
	try:
		horn_timer = driver.find_element_by_id('huntTimer')
		horn_timer_string = horn_timer.text
	except NoSuchElementException:
		pass

	kings_reward_detector(driver)

	switch_cheese(driver)

	if (driver.title == 'MouseHunt | Hunter\'s Camp' 
			and 'min' not in horn_timer_string):
	
		sound_horn = driver.find_element_by_class_name('hornbutton')
		time.sleep(1)
		sound_horn.click()
		print 'sounding the horn'
		switch_cheese(driver)

	#just to make sure the horn is actually sounded
	# time.sleep(3)

	driver.refresh()
	kings_reward_detector(driver)


	wait_time = None

	while (wait_time is None):
		try:
			horn_timer = driver.find_element_by_id('huntTimer')
			horn_timer_string = horn_timer.text
			string_array = horn_timer_string.split(" ")
			wait_time = int(string_array[0])
		except (NoSuchElementException, ValueError) as e:
			time.sleep(1)
			driver.refresh()
			time.sleep(1)

	return wait_time


def kings_reward_detector(driver):
	try:
		puzzle_image = driver.find_element_by_id('puzzleImage')
		print "OH SHIT, KING'S REWARD"
		facebook_warning()
	except NoSuchElementException:
		print "not a king's reward yet, be careful"

def time_printer(actual_time):
	minutes = str(actual_time / 60)
	seconds = str(actual_time % 60)
	if len(seconds) == 1:
		seconds = "0" + seconds
	print "wait time: {0}:{1}".format(minutes, seconds)

def main():
	driver = init()
	while (True):
		wait_time = sound_the_horn(driver)
		temp_int = random.randrange(5, 90)
		actual_time = wait_time * 60 + temp_int
		time_printer(actual_time)
		time.sleep(actual_time)

main()
# facebook_warning()

