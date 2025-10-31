
from selenium import webdriver
# Selenium is Package and Webdriver is Module

from selenium.webdriver.chrome.service import Service
# Service is Class

from selenium.webdriver.common.by import By
# By to find element (By.ID, By.NAME, By.XPATH, By.CSS_SELECTOR)

from selenium.webdriver.common.keys import Keys
# Keyboard keys such as Enter, Tab, Esc

from selenium.webdriver.support.expected_conditions import title_is
# this to find "expected condition" of the webpage. ex: WebDriverWait(driver, 10).until(title_is("Google"))

from selenium.webdriver.support.ui import WebDriverWait, Select
# WebDriverWait → ওয়েবড্রাইভারকে নির্দিষ্ট শর্ত পূরণ না হওয়া পর্যন্ত অপেক্ষা করায়।
# Select → ড্রপডাউন (যেমন <select> ট্যাগ) হ্যান্ডেল করার জন্য ব্যবহৃত হয়।

from selenium.webdriver.support import expected_conditions as EC
# এটি expected_conditions কে EC নামে শর্টকাট হিসেবে ব্যবহার করার সুবিধা দেয়।
# EC দিয়ে আমরা বিভিন্ন কন্ডিশন ব্যবহার করতে পারি — যেমন:

from selenium.webdriver.common.action_chains import ActionChains
#ActionChains ব্যবহার করে আমরা মাউস ও কীবোর্ডের জটিল অ্যাকশন করতে পারি — যেমন ড্র্যাগ-ড্রপ, হোভার করা, ডাবল-ক্লিক ইত্যাদি।

from webdriver_manager.chrome import ChromeDriverManager
# webdriver_manager প্যাকেজ স্বয়ংক্রিয়ভাবে ChromeDriver ডাউনলোড ও ম্যানেজ করে। ম্যানুয়ালি ড্রাইভার ডাউনলোড করতে হবে না।

import time
#Python-এর বিল্ট-ইন time মডিউল ইমপোর্ট করা হয়েছে। এটি সাধারণত time.sleep(সেকেন্ড) ব্যবহার করে প্রোগ্রামকে কিছু সময়ের জন্য থামিয়ে রাখে।

def setup_driver():
# এটিএকটি ফাংশন ঘোষণা।এর নামsetup_driver, অর্থাৎ এটি Chrome ্রাউজারের জন্য ড্রাইভার টআপ করবে। তুমি যখন setup_driver() কল করবে,
# এটি Chrome খুলবে এবং প্রস্তুত করে দেবে।

    service = Service(ChromeDriverManager().install())
#এখানে দুটো কাজ হচ্ছে:
# 1. ChromeDriverManager().install()
#এটি webdriver_manager প্যাকেজের একটি ফাংশন, যা স্বয়ংক্রিয়ভাবে ChromeDriver ডাউনলোড ও সেটআপ করে।
#তোমাকে আর ম্যানুয়ালি ChromeDriver ডাউনলোড করে PATH-এ রাখতে হয় না।

#2. Service(...)
#এটি সেই ড্রাইভার সার্ভিসকে তৈরি করে, যা ব্রাউজারের সাথে যোগাযোগ করবে।
# একে তুমি ChromeDriver-এর “engine starter” বলতে পারো। তাই এই লাইনটি ChromeDriver সার্ভিস তৈরি ও ইনিশিয়ালাইজ করে।

    driver = webdriver.Chrome(service=service)
# এখানে webdriver.Chrome() দিয়ে আসল Chrome ব্রাউজার চালু করা হচ্ছে।
# আর service=service প্যারামিটারটি আগের লাইন থেকে তৈরি করা সার্ভিসটি ব্যবহার করছে।
# অর্থাৎ এই লাইনটি Chrome ব্রাউজার ওপেন করে এবং সেটি নিয়ন্ত্রণের জন্য driver অবজেক্ট তৈরি করে।

    driver.maximize_window()
# এই লাইনটি ব্রাউজারের উইন্ডো পুরো স্ক্রিনে (maximize) করে দেয়।
# এটি ঐচ্ছিক, কিন্তু অনেক সময় দরকার হয় যেন সব উপাদান ভালোভাবে দেখা যায়।

    return driver
# এটি ফাংশনের শেষ লাইন।
# এই লাইনটি driver অবজেক্টটি রিটার্ন করে, যাতে তুমি অন্য জায়গায় সেটি ব্যবহার করতে পারো।


#সংক্ষেপে পুরো ফাংশনের কাজ:
#setup_driver()
#ChromeDriver স্বয়ংক্রিয়ভাবে সেটআপ করে
#Chrome ব্রাউজার চালু করে
#উইন্ডো maximize করে
#এবং সেই ড্রাইভার অবজেক্ট রিটার্ন করে, যেন তুমি ওয়েব অটোমেশন করতে পারো।

def fill_text_inputs(driver):
#এটি একটি ফাংশন ডিফিনিশন (function definition)।
#def → Python-এ নতুন ফাংশন বানাতে ব্যবহৃত কীওয়ার্ড।
#fill_text_inputs → ফাংশনের নাম। নাম দেখে বোঝা যায়, এটি কোনো ওয়েব ফর্মের টেক্সট ইনপুটগুলো পূরণ করবে (fill করবে)।
#(driver) → এটি ফাংশনের প্যারামিটার।
#অর্থাৎ, যখন তুমি ফাংশন কল করবে, তখন তুমি Selenium-এর driver অবজেক্টটি পাস করবে, যাতে ফাংশনটি জানে কোন ব্রাউজারে কাজ করতে হবে।

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
    exp_title ="DEMOQA"

    if act_title ==exp_title:
        print("Testing pass")
    else:
        print("Testing fail")


time.sleep(5)


driver = setup_driver()
#এটি Chrome খুলে ও Selenium-কে সেটি নিয়ন্ত্রণের ক্ষমতা দেয়।
fill_text_inputs(driver)
#ফর্মের ইনপুট ফিল্ডগুলো স্বয়ংক্রিয়ভাবে পূরণ হয়ে যায়।
driver.quit()
#এই লাইনটি Chrome ব্রাউজারটি সম্পূর্ণভাবে বন্ধ করে দেয়।

