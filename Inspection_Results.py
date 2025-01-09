import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import load_workbook
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException
# import random
import os

# from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://jett.autohub.jo/auth/login")

# ----------------------------------------Generic Log-In Handling----------------------------------

email = "admin@jett.com"
old_password = "12341234"
new_password = "123123"

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
print("The Branch Dropdown has been selected:")

time.sleep(5)

driver.find_element(By.XPATH,
                    "/html[1]/body[1]/app-root[1]/app-full-layout[1]/div[1]/nav[1]/div[1]/div[3]/div[1]/ng-select[1]/ng-dropdown-panel[1]/div[1]/div[2]/div[3]/span[1]").click()

print("The Specific branch Aqaba has been selected:")
time.sleep(10)

#---------------------Filter the newly created Job Card and assign the Supervisor to the Job Card-------.

# Selenium code to use the job card number
filter_btn = driver.find_element(By.XPATH, "//button[@id='togglefilter']")
print("The Bot finds the Filter Path:")
filter_btn.click()
print("The filter button has been clicked by the Bot:")
time.sleep(3)

Job_filter_with_Job_Card_Number = driver.find_element(By.XPATH, "//input[@placeholder='Job Number, Customer Name or Plate Number']")
print("The system finds the filter field path successfully:")
Job_filter_with_Job_Card_Number.send_keys("AQ16122401")
print("The bot successfully enter the Job Card Number to the filter field:")
time.sleep(3)

apply_filter_btn = driver.find_element(By.XPATH, "//button[@id='getJobListBtn']")
print("The bot finds the Apply button path")
apply_filter_btn.click()
print("The Apply button has been successfully clicked by the bot:")
time.sleep(5)

assign_inspection_results = driver.find_element(By.XPATH,
                                                "//li[contains(@class,'pn-ProductNav_LinkOne current-process')]//i[contains(@class,'fas fa-edit mx-1 primary-dark-font')]")
print("The bot finds the assign IR button successfully: ")
assign_inspection_results.click()
print("The assign IR button has been clicked by the bot:")
time.sleep(5)

inspection_results_dropdown = driver.find_element(By.XPATH,
                                                  "//ng-select[@id='Inspection Results1']//input[contains(@role,'combobox')]")
print("The bot finds the path of the IR dropdown:")
inspection_results_dropdown.click()
print("The IR dropdown click by the bot:")
time.sleep(2)

select_specific_inspection_technician = driver.find_element(By.XPATH, "//div[@id='ad976e384421-4']//span[contains(@class,'ng-option-label')]//span[1]")

print("The bot finds the specific IR technician path successfully:")
driver.execute_script("arguments[0].scrollIntoView(true);", select_specific_inspection_technician)
select_specific_inspection_technician.click()
print("The specific IR technician has been selected by the bot:")
time.sleep(2)

save_ir_technician = driver.find_element(By.XPATH, "//button[normalize-space()='Yes']")
save_ir_technician.click()
time.sleep(5)

Log_out_admin = driver.find_element(By.XPATH, "//i[@class='fa fa-power-off']")
Log_out_admin.click()
time.sleep(5)

#----------------------------------Inspection Technician Log-In to work on the assigned tasks.-----

clear_email_field = driver.find_element(By.XPATH, "//input[@name='email']")
clear_email_field.clear()

clear_password_field = driver.find_element(By.XPATH, "//input[@name='password']")
clear_password_field.clear()

time.sleep(5)

email = "supervisor@autohub.jo"
old_password = "P@$$w0rd@autohub"
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

# -------------------Find the specific Job Card to interact with----------------

try:
    # Wait until the job card element is visible and enabled
    wait = WebDriverWait(driver, 10)  # 10 seconds timeout
    selected_job_card = wait.until(EC.element_to_be_clickable((By.NAME, "AQ03122402")))

    if selected_job_card.is_displayed():
        print("The system finds the selected Job Card.")

        # Optional: Move to element before clicking (in case it's partially visible)
        ActionChains(driver).move_to_element(selected_job_card).perform()

        selected_job_card.click()
    else:
        print("Job Card is not visible.")

except TimeoutException:
    print("Job Card was not found within the given timeout.")
except ElementNotInteractableException:
    print("Job Card is not interactable.")
except NoSuchElementException:
    print("Job Card with the specified name does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

dashboard_edit_button = driver.find_element(By.XPATH,
                                            "//div[@id='job-list']//div[1]//div[1]//div[2]//div[1]//div[1]//span[1]//i[2]")
dashboard_edit_button.click()
time.sleep(8)

select_services_tab = driver.find_element(By.XPATH, "//span[@class='nav-text small-font primary-font']")
select_services_tab.click()
time.sleep(5)
