# McDonalds Free Code Generator

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()


# reciept-code: xxxx-xxxx-xxxx
# SURVEY IS NOT THE SAME, use try and except
# MV9WYB7VX9HM - PRACTICE CODE
# Main problem is the fact the switch the questions and theres no set order, so you must use a bunch of exceptions


def getCode(reciept_code):
	driver.get('https://www.mcdfoodforthoughts.com/?AspxAutoDetectCookieSupport=1')
	driver.find_element_by_xpath('//*[@id="NextButton"]').click()
	driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/div[1]/div[2]/div[1]/span/span').click()
	driver.find_element_by_xpath('//*[@id="NextButton"]').click()
	driver.find_element_by_xpath('//*[@id="CN1"]').send_keys(reciept_code[:4])
	driver.find_element_by_xpath('//*[@id="CN2"]').send_keys(reciept_code[4:8])
	driver.find_element_by_xpath('//*[@id="CN3"]').send_keys(reciept_code[8:12])
	driver.find_element_by_xpath('//*[@id="Pound"]').send_keys('0')
	driver.find_element_by_xpath('//*[@id="Pence"]').send_keys('00')
	driver.find_element_by_xpath('//*[@id="NextButton"]').click()
	codefound = False
	while not codefound:
		try:
			code = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/div/div/div/div[1]/div/p[6]').text
			print(code)
			codefound = True
		except NoSuchElementException:
			codefound = False
			try:
				driver.find_element_by_xpath(
					'/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[3]/span').click()
				driver.find_element_by_xpath('//*[@id="NextButton"]').click()
			except NoSuchElementException:
				try:
					driver.find_element_by_xpath(
						'/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[3]/span').click()
					driver.find_element_by_xpath(
						'/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[3]/td[3]/span').click()
					driver.find_element_by_xpath(
						'/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[4]/td[3]/span').click()
					driver.find_element_by_xpath(
						'/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[5]/td[3]/span').click()
					driver.find_element_by_xpath(
						'/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[6]/td[3]/span').click()
					driver.find_element_by_xpath('//*[@id="NextButton"]').click()
				except NoSuchElementException:
					try:
						driver.find_element_by_xpath(
							'/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[3]/span').click()
						driver.find_element_by_xpath(
							'/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[3]/td[3]/span').click()
						driver.find_element_by_xpath('//*[@id="NextButton"]').click()
					except NoSuchElementException:
						try:
							driver.find_element_by_xpath('//*[@id="S000033"]').send_keys('Great')
							driver.find_element_by_xpath('//*[@id="NextButton"]').click()
						except NoSuchElementException:
							try:
								driver.find_element_by_xpath(
									'/html/body/div[1]/div[3]/div[2]/form/div/div[1]/div[2]/div/div[1]/span/span').click()
								driver.find_element_by_xpath('//*[@id="NextButton"]').click()
							except NoSuchElementException:
								try:
									driver.find_element_by_xpath(
										'/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[2]/span').click()
									driver.find_element_by_xpath('//*[@id="NextButton"]').click()
								except NoSuchElementException:
									try:
										driver.find_element_by_xpath(
											'/html/body/div[1]/div[3]/div[2]/form/div/div[1]/div[2]/div/div[1]/span/span').click()
										driver.find_element_by_xpath('//*[@id="NextButton"]').click()
									except NoSuchElementException:
										try:
											driver.find_element_by_xpath(
												'/html/body/div[1]/div[3]/div[2]/form/div/div[1]/div[2]/div/div[2]/span/span').click()
											driver.find_element_by_xpath('//*[@id="NextButton"]').click()
										except NoSuchElementException:
											try:
												driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/div[2]/div[2]/div/div[1]/span/span').click()
												driver.find_element_by_xpath('//*[@id="NextButton"]').click()
											except NoSuchElementException:
												print('New Path discovered')

	code = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/div/div/div/div[1]/div/p[6]').text
	# xpath text shows code
	print('Your voucher code is :' + code)


while 1 == 1:
	print('Code must be 12 numbers...')
	reciept_code = input('Enter the code:: ')
	getCode(reciept_code)
