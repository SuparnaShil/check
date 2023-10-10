import time
import random

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

chrome_service = ChromeService(executable_path="D:\\chrome\\chromedriver.exe")
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get("http://automationexercise.com")
time.sleep(3)
driver.maximize_window()

print(driver.title)


while True:
    try:
        #WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Add to cart')]")))
        atc = driver.find_elements(By.XPATH, "//a[contains(text(),'Add to cart')]")
        driver.execute_script("arguments[0].scrollIntoView(true)", atc[3])

        driver.execute_script("arguments[0].click();", atc[3])
        break
    except:
        break

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//*[contains(text(),'View Cart')]")))
driver.find_element(By.XPATH,"//*[contains(text(),'View Cart')]").click()

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//a[normalize-space()='Proceed To Checkout']")))
driver.find_element(By.XPATH,"//a[normalize-space()='Proceed To Checkout']").click()

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//u[normalize-space()='Register / Login']")))
driver.find_element(By.XPATH,"//u[normalize-space()='Register / Login']").click()


name = driver.find_element(By.XPATH,"//input[@placeholder='Name']")
email = driver.find_element(By.XPATH,"//input[@data-qa='signup-email']")
signup = driver.find_element(By.XPATH,"//button[normalize-space()='Signup']")



name.send_keys("Username")
email.send_keys("username" +str(random.randint(100, 999))+"@gmail.com")
signup.click()

while True:
    time.sleep(5)
    if driver.find_element(By.XPATH,"//p[normalize-space()='Email Address already exist!']").is_displayed():

        #email.send_keys(Keys.CONTROL, "a")
        #email.send_keys(Keys.DELETE)
        #email.clear()
        temp =driver.find_elements(By.XPATH,"//input[@name='email']")
        temp[1].clear()
        temp[1].send_keys("username" +str(random.randint(100, 999)) + "@gmail.com")
        time.sleep(5)
        su = driver.find_element(By.XPATH,"//button[normalize-space()='Signup']")
        driver.execute_script("arguments[0].click();", su)

    else: break











time.sleep(5)