from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://monkeytype.com")

time.sleep(2)

timer = 0

while timer < 30:
    timer+=1
    textarea = driver.find_element(By.XPATH, "//textarea[@id='wordsInput']")
    raw_words = driver.find_element(By.ID, "words")
    words = raw_words.text.split()

    for word in words:
        textarea.send_keys(word + " ")

time.sleep(10)