from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('F:\python\house_crawling\chromedriver.exe')
driver.get('http://www.encar.com/db/db_carsinfo.do?method=newpricePop')
delay = 5
driver.implicitly_wait(delay)
"""리소스를 기다리는 시간(3초)"""