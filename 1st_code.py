from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    options = Options()
    options.add_argument("--start-maximized")
    # headless চালাতে চাইলে ঐচ্ছিক:
    # options.add_argument("--headless=new")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def fill_text_inputs(driver):
    driver.get("https://demoqa.com/text-box")
    wait = WebDriverWait(driver, 10)
    full_name = wait.until(EC.presence_of_element_located((By.ID, "userName")))
    full_name.send_keys("Rahman Zillur")
    # আরও ফিল্ড পূরণ করুণ...
    # শেষ হলে:
    # driver.quit()

if __name__ == "__main__":
    driver = setup_driver()
    try:
        fill_text_inputs(driver)
        input("Press Enter to close...")  # স্ক্রিপ্ট দেখার জন্য
    finally:
        driver.quit()