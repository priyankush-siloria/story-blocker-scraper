# for call spider
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from collections import defaultdict
from driver import ChromeDriver


class ReadCsv(object):
	"""docstring for ReadCsv"""
	def __init__(self):
		super(ReadCsv, self).__init__()
		self.file = 'video_links.csv'

	def getLinks(self):
		result_list = []
		df = pd.read_csv(self.file)
		for i,row in df.iterrows():
			links = row['Video Links']
			remove_domain = links.split("video/stock/",1)[1]
			result_list.append(remove_domain)

		return result_list


class MyScrapper(object):
	"""docstring for MyScrapper"""
	def __init__(self):
		super(MyScrapper, self).__init__()
		self.chromedriver = ChromeDriver()
		self.driver = self.chromedriver.drivers()
		self.user = 'Iexplain3723'
		self.password = 'IEXPLAIN@@@23377'
		self.download_url = 'https://5f56f298ac5ad2bc0c9c79ab.imnuke.app/video/stock/'
		self.required_login()
		self.downloadVideos()


	def get_xpath(self,path):
		element = self.driver.find_element_by_name(path)
		return element

	def check_size(self,text):
		val= text.split("-")[1].replace("MB",'').strip()
		return float(val) if val else None
	def required_login(self):

		url = 'https://imnuke.app/auth/login'
		self.driver.get(url)
		sleep = self.chromedriver.wait_random()
		name_elem = self.get_xpath('login')
		password_elem = self.get_xpath('password')
		name_elem.send_keys(self.user)
		sleep = self.chromedriver.wait_random()
		password_elem.send_keys(self.password)
		sleep = self.chromedriver.wait_random()
		login_box = self.driver.find_element_by_class_name('btn-second').click()
		sleep = self.chromedriver.sleep_time(5)
		paid_button = self.driver.find_element_by_xpath('//*[text()="Only Paid"]').click()
		sleep = self.chromedriver.sleep_time(8)
		video_box = self.driver.find_element_by_xpath('//img[contains(@src,"https://imgur.com/PO6GNDr.png")]').click()
		sleep = self.chromedriver.sleep_time(7)

	def downloadVideos(self):
		csv_instance = ReadCsv()
		links_list = csv_instance.getLinks()
		sleep = self.chromedriver.sleep_time(7)
		for link in links_list:
			sleep = self.chromedriver.sleep_time(3)
			self.driver.get(self.download_url+link)
			sleep = self.chromedriver.sleep_time(10)
			# 4K
			min_quality = self.driver.find_element_by_id('4KMP4')
			min_quality_int=self.check_size(min_quality.text)

			# HDMOV
			hd_button = self.driver.find_element_by_id('HDMOV')
			hd_button_int=self.check_size(hd_button.text)

			# HDMP4
			hdmp4_button = self.driver.find_element_by_id('HDMOV')
			hdmp4_button_int=self.check_size(hdmp4_button.text)
			
			if min_quality_int <= 150:
				min_quality.click()

			elif hd_button_int < min_quality_int and hd_button_int < hdmp4_button_int:
				hd_button.click()
			elif hdmp4_button_int < min_quality_int and hdmp4_button_int < hd_button_int:
				hdmp4_button.click()
			sleep = self.chromedriver.sleep_time(2)
			download_button = self.driver.find_element_by_class_name('PrimaryButton').click()
			sleep = self.chromedriver.sleep_time(6)

		self.driver.close()


if __name__ == '__main__':
	MyScrapper()