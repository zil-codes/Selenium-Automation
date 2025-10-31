from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import title_is
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time


def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver


def fill_text_inputs(driver):
    driver.get("https://demoqa.com/text-box")
    time.sleep(1)
    name_text = driver.find_element(By.ID, "userName")
    name_text.send_keys("Md Zillur Rahman")
    time.sleep(1)
    email_text = driver.find_element(By.ID, "userEmail")
    email_text.send_keys("zill.sqa@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID, "currentAddress").send_keys("Los Angeles, USA")
    time.sleep(1)
    address = driver.find_element(By.ID, "permanentAddress")
    address.send_keys("California, USA")
    driver.find_element(By.ID, "submit").click()

    act_title = driver.title
    exp_title = "DEMOQA"

    if act_title == exp_title:
        print("Testing pass")
    else:
        print("Testing fail")


time.sleep(5)

driver = setup_driver()
fill_text_inputs(driver)
driver.quit()

