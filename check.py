import time

from selenium import webdriver
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


#page_title = driver.title
#driver.assertEqual(page_title, "Automation Exercise", f"Page title is not equal to 'Automation Exercise'")





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





time.sleep(5)