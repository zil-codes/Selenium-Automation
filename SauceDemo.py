
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

def setup_browser_incognito():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    driver.maximize_window()
    return driver


driver = setup_browser_incognito()

driver.get("https://www.saucedemo.com/")
time.sleep(1)
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(1)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(1)
driver.find_element(By.ID,'login-button').click()
time.sleep(1)
driver.find_element(By.ID,'add-to-cart-sauce-labs-backpack').click()
time.sleep(1)
driver.find_element(By.XPATH,"//span[@class='shopping_cart_badge']").click()
time.sleep(1)
driver.find_element(By.ID, "checkout").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='first-name']").send_keys("md")
driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("rahman")
driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("9005")
driver.find_element(By.XPATH,"//input[@id='continue']").click()
driver.find_element(By.XPATH,"//button[@id='finish']").click()
time.sleep(2)
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(2)
driver.find_element(By.ID, "logout_sidebar_link").click()
time.sleep(2)

driver.quit()


