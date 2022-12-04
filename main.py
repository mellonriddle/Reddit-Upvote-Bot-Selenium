from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import random
import time

# Loading environment variables
load_dotenv(".env")
REDDIT_ID = os.getenv("Reddit_Username")
REDDIT_PASSWORD = os.getenv("Reddit_Password")

# Setting up our web driver
chrome_driver_path = r"C:\Development\chromedriver.exe"
my_service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=my_service)
driver.maximize_window()

# We need to sleep random times occasionally, because we don't want to be banned on Reddit

driver.get("https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F")
time.sleep(random.uniform(1, 2))

# Log in Reddit with our credentials
name_form = driver.find_element(By.NAME, "username")
name_form.send_keys(REDDIT_ID)

time.sleep(random.uniform(0, 1))
password_form = driver.find_element(By.NAME, "password")
password_form.send_keys(REDDIT_PASSWORD)

time.sleep(random.uniform(1, 2))
login_button = driver.find_elements(By.CSS_SELECTOR, "form fieldset button[type='submit']")
login_button[0].click()

# Find posts about Christopher Nolan
time.sleep(random.uniform(2, 3))
driver.get("https://www.reddit.com/search/?q=Christopher Nolan&t=day")
time.sleep(random.uniform(1, 2))
titles = driver.find_elements(By.CSS_SELECTOR, "a div h3")

# Loop through all posts about Christopher Nolan in the last 24 hours and upvote them
for i in range(len(titles)):
    driver.get("https://www.reddit.com/search/?q=Christopher Nolan&t=day")
    time.sleep(random.uniform(1, 2))
    titles = driver.find_elements(By.CSS_SELECTOR, "a div h3")
    titles[i].click()
    time.sleep(random.uniform(1, 2))
    upvote = driver.find_elements(By.CLASS_NAME, "icon-upvote")
    upvote[0].click()
    time.sleep(random.uniform(1, 2))
