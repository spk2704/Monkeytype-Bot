from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://monkeytype.com")

time.sleep(5)

textarea = driver.find_element(By.XPATH, "//textarea[@id='wordsInput']")
raw_words = driver.find_element(By.ID, "words")
words = raw_words.text.split()

for word in words:
    textarea.send_keys(word + " ")
    time.sleep(0.3)

time.sleep(120)