from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
import csv
import math
import numpy as np
import difflib
import string
import random
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://chaldal.com/")

wait = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "searchBox"))
)
search = driver.find_element_by_class_name("searchBox")
search.send_keys("fish")
time.sleep(3)

wait = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "buyText"))
)
Data = driver.find_elements_by_class_name("buyText")

for i in range(0, 30):
    if Data[i].text == "Add to bag":
        Data[i].click()

wait = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "remove"))
)
cartdata = driver.find_elements_by_class_name("remove")
print(len(cartdata))

for j in range(0, 30):
    if cartdata[j].get_attribute("title") == "Remove from bag":
        cartdata[j].click()
        time.sleep(1)

driver.close()