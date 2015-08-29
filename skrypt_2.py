from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


# create a new instance of the Firefox driver
driver = webdriver.Firefox()

# go to the 'sii' page 
driver.get("http://sii.pl/oddzialy/gdansk/")

# check presentation of phone number and show message
try: 
	driver.find_element_by_xpath("//*[contains(text(),'58 32 17 800')]")
	print 'Numer telefonu 58 32 17 800 jest prezentowany na stronie.'
except NoSuchElementException:
	print 'Brak prezentacji numeru telefonu 58 32 17 800 na stronie.'

# check presentation of email adress and show message
try: 
	driver.find_element_by_xpath("//*[contains(text(),'informacja-gdansk@pl.sii.eu')]")
	print 'Adres email informacja-gdansk@pl.sii.eu jest prezentowany na stronie.'
except NoSuchElementException:
	print 'Brak prezentacji adresu email informacja-gdansk@pl.sii.eu na stronie.'

driver.close()
