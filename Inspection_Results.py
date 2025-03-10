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
Admin_filter_btn = driver.find_element(By.XPATH, "//button[@id='togglefilter']")
print("The Bot finds the Filter Path:")
Admin_filter_btn.click()
print("The filter button has been clicked by the Bot:")
time.sleep(3)

Admin_Job_filter_with_Job_Card_Number = driver.find_element(By.XPATH,
                                                            "//input[@placeholder='Job Number, Customer Name or Plate Number']")
print("The system finds the filter field path successfully:")
Admin_Job_filter_with_Job_Card_Number.send_keys("AQ16122401")
print("The bot successfully enter the Job Card Number to the filter field:")
time.sleep(3)

Admin_apply_filter_btn = driver.find_element(By.XPATH, "//button[@id='getJobListBtn']")
print("The bot finds the Apply button path")
Admin_apply_filter_btn.click()
print("The Apply button has been successfully clicked by the bot:")
time.sleep(5)

Admin_assign_inspection_results = driver.find_element(By.XPATH,
                                                      "//li[contains(@class,'pn-ProductNav_LinkOne current-process')]//i[contains(@class,'fas fa-edit mx-1 primary-dark-font')]")
print("The bot finds the assign IR button successfully: ")
Admin_assign_inspection_results.click()
print("The assign IR button has been clicked by the bot:")
time.sleep(5)

Admin_inspection_results_dropdown = driver.find_element(By.XPATH,
                                                        "//ng-select[@id='Inspection Results1']//input[contains(@role,'combobox')]")
print("The bot finds the path of the IR dropdown:")
Admin_inspection_results_dropdown.click()
print("The IR dropdown click by the bot:")
time.sleep(2)

Admin_select_specific_inspection_technician = driver.find_element(By.XPATH,
                                                                  "//span[contains(text(),' بلال منصور (Supervisor)')]")

print("The bot finds the specific IR technician path successfully:")
driver.execute_script("arguments[0].scrollIntoView(true);", Admin_select_specific_inspection_technician)
Admin_select_specific_inspection_technician.click()
print("The specific IR technician has been selected by the bot:")
time.sleep(2)

Admin_save_ir_technician = driver.find_element(By.XPATH, "//button[normalize-space()='Yes']")
Admin_save_ir_technician.click()
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

# -------------------Filter the selected Job Card for IR--------------

Supervisor_filter_btn = driver.find_element(By.XPATH, "//button[@id='togglefilter']")
print("The Bot finds the Filter Path:")
Supervisor_filter_btn.click()
print("The filter button has been clicked by the Bot:")
time.sleep(3)

Supervisor_Job_filter_with_Job_Card_Number = driver.find_element(By.XPATH,
                                                                 "//input[@placeholder='Job Number, Customer Name or Plate Number']")
print("The system finds the filter field path successfully:")
Supervisor_Job_filter_with_Job_Card_Number.send_keys("AQ16122401")
print("The bot successfully enter the Job Card Number to the filter field:")
time.sleep(3)

Supervisor_apply_filter_btn = driver.find_element(By.XPATH, "//button[@id='getJobListBtn']")
print("The bot finds the Apply button path")
Supervisor_apply_filter_btn.click()
print("The Apply button has been successfully clicked by the bot:")
time.sleep(5)

dashboard_action_btn = driver.find_element(By.XPATH, "//div[@class='col-2 dropdown']//button[@id='dropdownMenuButton']")
print("The bot finds the action dropdown path:")
dashboard_action_btn.click()
print("The bot click on the action dropdown:")
time.sleep(3)

dashboard_edit_jobCard_btn = driver.find_element(By.XPATH, "//div[@class='dropdown-menu show']//i[@title='Edit']")
print("The bot finds the edit button path")
dashboard_edit_jobCard_btn.click()
print("The bot click on the edit button path")
time.sleep(3)

select_services_tab = driver.find_element(By.XPATH, "//span[@class='nav-text small-font primary-font']")
select_services_tab.click()
time.sleep(5)

# ---------------------------------------------Daily Checklist------------------------------------------------

daily_checkpoint_1 = driver.find_element(By.XPATH, "//tbody/tr[1]/td[2]/div[1]/label[1]/span[1]")
# Check if the element is visible on the page
is_displayed = driver.execute_script("return arguments[0].offsetParent !== null;", daily_checkpoint_1)
print(f"Is Element Visible? {is_displayed}")

# Get element dimensions
rect = daily_checkpoint_1.rect
print(f"Element dimensions: {rect['width']}x{rect['height']}")

# Check if the checkbox is already selected (checked)
checkbox_input_1 = driver.find_element(By.XPATH, "//tbody/tr[1]/td[2]/div[1]/label[1]/input")  # Adjust this if needed

if not checkbox_input_1.is_selected():  # Click only if it's not already checked
    print("Checkpoint 1 is NOT checked. Clicking to check it.")
    actions = ActionChains(driver)
    actions.move_to_element(daily_checkpoint_1).click().perform()
else:
    print("Checkpoint 1 is already checked. Skipping...")


time.sleep(3)

daily_checkpoint_2 = driver.find_element(By.XPATH, "//tbody/tr[2]/td[2]/div[1]/label[1]/span[1]")
is_displayed = driver.execute_script("return arguments[0].offsetParent !== null", daily_checkpoint_2)
print(f"Is Element Visible? {is_displayed}")

rect = daily_checkpoint_2.rect
print(f"Element dimensions: {rect['width']}x{rect['height']}")

checkbox_input_2 = driver.find_element(By.XPATH, "//tbody/tr[2]/td[2]/div[1]/label[1]/span[1]")

if not checkbox_input_2.is_selected():
    print("Checkpoint 2 is NOT checked. Clicking to check it.")
    actions = ActionChains(driver)
    actions.move_to_element(daily_checkpoint_2).click().perform()
else:
    print("Checkpoint 2 is already checked. Skipping...")

time.sleep(3)

# --------Scroll the checklist
scroll_element_checkpoint_after_2 = driver.find_element(By.XPATH, "//span[contains(text(),'الاطار الاحتياط')]")
print("Scroll to the element 'الاطار الاحتياط' ")
driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element_checkpoint_after_2)
time.sleep(3)
scroll_element_checkpoint_after_2.click()
print("The system scroll to the specific checkpoint:")
# ----------Successfully Scroll to the checkPoint
daily_checkpoint_3 = driver.find_element(By.XPATH, "//tbody/tr[3]/td[3]/div[1]/label[1]/span[1]")
is_displayed = driver.execute_script("return arguments[0].offsetParent !== null", daily_checkpoint_3)
print(f"Is Element Visible? {is_displayed}")

rect = daily_checkpoint_3.rect
print(f"Element dimensions: {rect['width']}x{rect['height']}")

checkbox_input_3 = driver.find_element(By.XPATH, "//tbody/tr[3]/td[3]/div[1]/label[1]/span[1]")

if not checkbox_input_3.is_selected():
    print("Checkpoint 3 is NOT checked. Clicking to check it.")
    actions = ActionChains(driver)
    actions.move_to_element(daily_checkpoint_3).click().perform()

time.sleep(3)

daily_checkpoint_4 = driver.find_element(By.XPATH, "//tbody/tr[4]/td[4]/div[1]/label[1]/span[1]")
is_displayed = driver.execute_script("return arguments[0].offsetParent !== null", daily_checkpoint_4)
print(f"Is Element Visible? {is_displayed}")

rect = daily_checkpoint_4.rect
print(f"Element dimensions: {rect['width']}x{rect['height']}")

checkbox_input_4 = driver.find_element(By.XPATH, "//tbody/tr[4]/td[4]/div[1]/label[1]/span[1]")
if not checkbox_input_4.is_selected():
    print("Checkpoint 3 is NOT checked. Clicking to check it.")
    actions = ActionChains(driver)
    actions.move_to_element(daily_checkpoint_4).click().perform()
else:
    print("Checkpoint 4 is already checked. Skipping...")

time.sleep(3)

# Need Maintenance
daily_checkpoint_5 = driver.find_element(By.XPATH, "//tbody/tr[5]/td[4]/div[1]/label[1]/span[1]")
is_displayed = driver.execute_script("return arguments[0].offsetParent !== null", daily_checkpoint_5)
print(f"Is Element Visible? {is_displayed}")

rect = daily_checkpoint_5.rect
print(f"Element dimensions: {rect['width']}x{rect['height']}")

checkbox_input_5 = driver.find_element(By.XPATH, "//tbody/tr[5]/td[4]/div[1]/label[1]/span[1]")
if not checkbox_input_5.is_selected():
    print("Checkpoint 5 is NOT checked. Clicking to check it.")
    actions = ActionChains(driver)
    actions.move_to_element(daily_checkpoint_5).click().perform()
else:
    print("Checkpoint 5 is already checked. Skipping...")

time.sleep(3)