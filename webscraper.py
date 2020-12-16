from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()

driver.get("https://youtube.com")

search = driver.find_element_by_xpath('//input[@id="search"]') #represents search bar to interact with

search.send_keys("minecraft")
search.send_keys(Keys.RETURN)

time.sleep(2)
content_container = driver.find_element(By.XPATH, '//*[@id="contents"]')
videos = content_container.find_elements_by_tag_name('ytd-video-renderer')
for video in videos:
    header = video.find_element_by_id('video-title')
    print(header.text)
driver.quit()