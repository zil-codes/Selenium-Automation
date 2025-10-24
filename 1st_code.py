
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
    time.sleep(5)


driver = setup_driver()
fill_text_inputs(driver)
driver.quit()



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
#
#
# #Open web browser driver
# driver = webdriver. Chrome ()
# driver.maximize_window()
# driver.delete_all_cookies ()
#
# #Navigate to our webpage
# driver.get ("https://www.facebook.com/")
# # name_text = driver.find_element(By.ID, "userName")
# # name_text.send_keys("Md Zillur Rahman")
# time. sleep (3)
# #
# # email_text = driver.find_element(By.ID, "userEmail").send_keys("zil234@gmail.com")
# # time. sleep (3)
# #
# # currentAdd_text = driver.find_element(By.ID, "currentAddress").send_keys("3043, walton street 203")
# # time. sleep (3)
# #
# #
# # permAddress_text = driver.find_element(By.ID, "permanentAddress")
# # permAddress_text.send_keys("5043, washington usa 203")
# #
# # driver.find_element(By.ID, "submit").click()
# # time. sleep (3)
# #
# #
# # actual_titel = driver.title
# # exppected_titel = ""
# #
# # #Close webbrowser
# # driver.close ()
# #
# #
# # print(" Text input filled and submitted.")
#
#
# driver.find_element(By.XPATH,"//input[@id='email']").send_keys("zil234@gmail.com")
#
# time. sleep (3)
