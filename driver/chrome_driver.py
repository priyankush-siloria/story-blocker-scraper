
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import random


class ChromeDriver(object):
	"""docstring for Config"""
	def __init__(self):
		super(ChromeDriver, self).__init__()
		self.driver = None
		self.wait_attrib = None
		
	def drivers(self):
		capa = DesiredCapabilities.CHROME
		capa["pageLoadStrategy"] = "none"
		options = Options()
		# options.add_argument('--headless')
		options.add_argument('start-maximized')
		options.add_experimental_option("useAutomationExtension", False)
		options.add_experimental_option("excludeSwitches",["enable-automation"])
		options.add_experimental_option("detach", True)
		self.driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options,desired_capabilities=capa)
		self.driver.maximize_window()
		return self.driver


	def wait_random(self):
		wait = WebDriverWait(self.driver, 10)
		slp = random.uniform(3.0, 5.0)
		wait_attrib = time.sleep(slp)
		return self.wait_attrib

	def sleep_time(self,duration):
		time.sleep(duration)
