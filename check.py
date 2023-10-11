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
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get("http://automationexercise.com")
time.sleep(3)
driver.maximize_window()

print(driver.title)

while True:
    try:
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Add to cart')]")))
        atc = driver.find_elements(By.XPATH, "//a[contains(text(),'Add to cart')]")
        driver.execute_script("arguments[0].scrollIntoView(true)", atc[3])

        driver.execute_script("arguments[0].click();", atc[3])
        break
    except:
        break

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'View Cart')]")))
driver.find_element(By.XPATH, "//*[contains(text(),'View Cart')]").click()

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Proceed To Checkout']")))
driver.find_element(By.XPATH, "//a[normalize-space()='Proceed To Checkout']").click()

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//u[normalize-space()='Register / Login']")))
driver.find_element(By.XPATH, "//u[normalize-space()='Register / Login']").click()

name = driver.find_element(By.XPATH, "//input[@placeholder='Name']")
email = driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")
signup = driver.find_element(By.XPATH, "//button[normalize-space()='Signup']")

name.send_keys("Username")
email.send_keys("username" + str(random.randint(100, 999)) + "@gmail.com")
signup.click()

while True:
    time.sleep(5)
    try:
        if driver.find_element(By.XPATH, "//p[normalize-space()='Email Address already exist!']").is_displayed():
            # email.send_keys(Keys.CONTROL, "a")
            # email.send_keys(Keys.DELETE)
            # email.clear()
            temp = driver.find_elements(By.XPATH, "//input[@name='email']")
            temp[1].clear()
            temp[1].send_keys("username" + str(random.randint(100, 999)) + "@gmail.com")
            time.sleep(5)
            su = driver.find_element(By.XPATH, "//button[normalize-space()='Signup']")
            driver.execute_script("arguments[0].click();", su)

    except:
        break

password = driver.find_element(By.XPATH, "//input[@id='password']")
driver.execute_script("arguments[0].scrollIntoView(true)", password)
password.send_keys("12345")

fn = driver.find_element(By.XPATH, "//input[@id='first_name']")
driver.execute_script("arguments[0].scrollIntoView(true)", fn)
fn.send_keys("User")

ln = driver.find_element(By.XPATH, "//input[@id='last_name']")
driver.execute_script("arguments[0].scrollIntoView(true)", ln)
ln.send_keys("Name LN")

add = driver.find_element(By.XPATH, "//input[@id='address1']")
driver.execute_script("arguments[0].scrollIntoView(true)", add)
add.send_keys("Dhaka")

state = driver.find_element(By.XPATH, "//input[@id='state']")
driver.execute_script("arguments[0].scrollIntoView(true)", state)
state.send_keys("state")

city = driver.find_element(By.XPATH, "//input[@id='city']")
driver.execute_script("arguments[0].scrollIntoView(true)", city)
city.send_keys("city")

zipcode = driver.find_element(By.XPATH, "//input[@id='zipcode']")
driver.execute_script("arguments[0].scrollIntoView(true)", zipcode)
zipcode.send_keys("1111")

mobile = driver.find_element(By.XPATH, "//input[@id='mobile_number']")
driver.execute_script("arguments[0].scrollIntoView(true)", mobile)
mobile.send_keys("01633333333")

create_account = driver.find_element(By.XPATH, "//button[normalize-space()='Create Account']")
create_account.click()

time.sleep(2)
continue_btn = driver.find_element(By.XPATH, "//a[normalize-space()='Continue']")
continue_btn.click()

time.sleep(3)

login_username = driver.find_element(By.XPATH, "//b[normalize-space()='Username']")
if login_username.text == "Username":
    print(login_username.text + " is same as required")

else:
    print("username is not matching")


#go to cart

cart_icon = driver.find_element(By.XPATH,"//a[normalize-space()='Cart']//i")
cart_icon.click()

time.sleep(1)
proceed = driver.find_element(By.XPATH,"//a[normalize-space()='Proceed To Checkout']")
proceed.click()

time.sleep(2)
descrip = driver.find_element(By.XPATH,"//textarea[@name='message']")
driver.execute_script("arguments[0].scrollIntoView(true)", descrip)
descrip.send_keys("nice product collection")

place_order =driver.find_element(By.XPATH,"//a[normalize-space()='Place Order']")
place_order.click()


#card details
time.sleep(3)
cname= driver.find_element(By.XPATH,"//input[@name='name_on_card']")
cnum = driver.find_element(By.XPATH,"//input[@name='card_number']")
cvc = driver.find_element(By.XPATH,"//input[@placeholder='ex. 311']")
mm = driver.find_element(By.XPATH,"//input[@placeholder='MM']")
yy =driver.find_element(By.XPATH,"//input[@placeholder='YYYY']")

cname.send_keys("Usename")
cnum.send_keys("1222654334567873")
cvc.send_keys("123")
mm.send_keys("10")
yy.send_keys("2025")


time.sleep(5)
