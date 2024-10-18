import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

# import random
# import os

# from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://jett.autohub.jo/auth/login")

# ----------------------------------------Generic Log-In Handling----------------------------------

email = "admin@jett.com"
old_password = "123123"
new_password = "123456"

driver.find_element(By.NAME, "email").send_keys(email)
driver.find_element(By.NAME, "password").send_keys(old_password)
driver.find_element(By.CLASS_NAME, "btn").click()
time.sleep(5)

# Check if the password reset screen is displayed
try:
    reset_password_header = driver.find_element(By.XPATH, "//button[@type='submit']")

    if reset_password_header.is_displayed():
        print("Password has expired. Resetting password...")

        # Enter the new password and confirm it
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(new_password)
        time.sleep(5)
        driver.find_element(By.XPATH, "//input[@name='confirm_password']").send_keys(new_password)

        # Click the reset password button
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)

    enter_new_password_header = driver.find_element(By.XPATH, "//input[@name='email']")

    if enter_new_password_header.is_displayed():
        print("Entering the Email & New Password to the Log_in Page:")
        # Re-enter the email and new password to login
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys(new_password)
        driver.find_element(By.CLASS_NAME, "btn").click()

        print("Password has been successfully reset and logged in.")

    else:
        print("Password did not expire, logging in successfully.")

except Exception as e:
    print("Password did not expire or error in resetting password, logging in successfully.")
    print(f"Error: {e}")

time.sleep(5)

driver.find_element(By.XPATH,
                    "//div[@class='ng-select-container ng-has-value']//span[@class='ng-arrow-wrapper']").click()
print("branch Dropdown has been selected:")

time.sleep(5)

driver.find_element(By.XPATH,
                    "/html[1]/body[1]/app-root[1]/app-full-layout[1]/div[1]/nav[1]/div[1]/div[3]/div[1]/ng-select[1]/ng-dropdown-panel[1]/div[1]/div[2]/div[3]/span[1]").click()

print("The Specific branch Aqaba has been selected:")
time.sleep(5)