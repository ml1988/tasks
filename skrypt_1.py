# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# create a new instance of the Firefox driver
driver = webdriver.Firefox()

# go to the 'google' page 
driver.get("http://www.google.pl")
inputElement = driver.find_element_by_name("q")
inputElement.send_keys("site:sii.pl www")
inputElement.submit()

# wait
time.sleep(3)

# defining search results 
searchResult = driver.find_element_by_xpath("//ol[@id='rso']/div[2]/div[4]/div").text
siiData = u"Gdańsk - Sii\nsii.pl/oddzialy/gdansk/\nMichał Ozdoba - Photographer http://www.facebook.com/. 200m do Stacji Kolejowej. fot. Michał Ozdoba - Photographer http://www.facebook.com/."

try: 
	assert searchResult==siiData
	print u'Wyrażenie: '
	print siiData
	print u'jest prezentowane na 4 miejscu wyników wyszukiwania.'
except AssertionError:
	print u'Wyrażenie: '
	print siiData
	print u'nie jest prezentowane na 4 miejscu wyników wyszukiwania.'

driver.close()

