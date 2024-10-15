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

driver.find_element(By.XPATH, "//a[normalize-space()='+Create Job']").click()

print("The Create Job Card button has been pressed by the Admin user:")
time.sleep(12)

driver.find_element(By.XPATH,
                    "/html[1]/body[1]/app-root[1]/app-full-layout[1]/div[1]/main[1]/div[1]/div[1]/div[1]/app-create-job[1]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[1]/app-inspection[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys(
    "58-2760")

time.sleep(5)

driver.find_element(By.XPATH, "//i[@class='fas fa-search pt-1']").click()
print("The Entered Plate Number's data has been fetched:")
time.sleep(5)

driver.execute_script("window.scrollBy(0, 5000);")
time.sleep(2)

# ------------------------Select the specific driver from the driver dropdown-------------------------

# Simple Implimentation

driver.find_element(By.XPATH, "//div[@class='ng-select-container']//input[@role='combobox']").click()
time.sleep(2)

print("The Drivers Name Dropdown has been opened:")

# driver_list = driver.find_elements(By.XPATH,
#                                    "/html[1]/body[1]/app-root[1]/app-full-layout[1]/div/main[1]/div[1]/div[1]/div[1]/app-create-job[1]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[1]/app-inspection[1]/form[1]/div[2]/div[2]/div[1]/ng-select[1]/ng-dropdown-panel[1]/div[1]/div[2]/div/span")
#
# print("The system shows the all drivers name that are available in the dropdown list:")

select_specific_driver = driver.find_element(By.XPATH, "//span[contains(text(),'محمود هاشم محمود البيك')]")
select_specific_driver.click()
print("The Drivers has been selected from the driver's dropdown:")

time.sleep(3)



# for select_driver in driver_list:
#     if select_driver.text == "نايف حسن عبد القادر الزوغة":
#         print(f"Selected driver: {select_driver.text}")
#         select_driver.click()
#         break


# select_specific_driver = driver.find_element(By.XPATH, "//span[contains(text(),'محمود هاشم محمود البيك')]")
# select_specific_driver.click()
# print("The Drivers has been selected from the driver's dropdown:")


# WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//div[@class='ng-select-container']//input[@role='combobox']"))
# ).click()
#
# # Locate all the dropdown options
# driver_list = driver.find_elements(By.XPATH,
#                                    "/html[1]/body[1]/app-root[1]/app-full-layout[1]/div[1]/main[1]/div[1]/div[1]/div[1]/app-create-job[1]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[1]/app-inspection[1]/form[1]/div[2]/div[2]/div[1]/ng-select[1]/ng-dropdown-panel[1]/div[1]/div[2]/div/span")
#
# print("All the drivers in the driver's dropdown are visible to the user:")
#
# # Iterate through the options and select the one with the specified text
# for select_driver in driver_list:
#     # Extract the driver's name from each option element
#     driver_name = select_driver.text.strip()
#
#     print(f"Checking driver: {driver_name}")
#     if driver_name == "محمد حسن ابراهيم حسين":  # Replace with the exact name in Arabic
#         print(f"Selected driver: {driver_name}")
#         select_driver.click()
#         break
# else:
#     print("Driver not found in the list")


# for select_driver in driver_list:
#     # Extract the driver's name from each option element
#     driver_name = select_driver.text.strip()
#
#     print(f"Checking driver: {driver_name}")
#     if driver_name == "محمد حسن ابراهيم حسين":  # Replace with the exact name in Arabic
#         print(f"Selected driver: {driver_name}")
#         select_driver.click()
#         break


# if driver_list:
#     # Select a random driver from the list
#     random_driver = random.choice(driver_list)
#
#     # Get the name of the randomly selected driver (for debugging)
#     driver_name = random_driver.text.strip()
#     print(f"Randomly selected driver: {driver_name}")
#
#     # Click on the randomly selected driver
#     random_driver.click()
#
#     print(f"Selected driver: {driver_name}")
# else:
#     print("No drivers found in the list.")


# Function to get the current index from a file or start at 0 if it's the first run
# def get_current_index(file_path):
#     if os.path.exists(file_path):
#         with open(file_path, 'r') as file:
#             return int(file.read())
#     return 0
#
#
# def save_current_index(file_path, index):
#     with open(file_path, 'w') as file:
#         file.write(str(index))
#
#
# # Path to store the index across script runs
# index_file_path = 'driver_index.txt'
#
# # Get the current index (which driver to select next)
# driver_index = get_current_index(index_file_path)
#
# # Click the dropdown to reveal the driver list
# driver.find_element(By.XPATH, "//div[@class='ng-select-container']//input[@role='combobox']").click()
# time.sleep(2)
#
# # Find all driver options in the dropdown list
# driver_list = driver.find_elements(By.XPATH,
#                                    "/html[1]/body[1]/app-root[1]/app-full-layout[1]/div[1]/main[1]/div[1]/div[1]/div[1]/app-create-job[1]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[1]/app-inspection[1]/form[1]/div[2]/div[2]/div[1]/ng-select[1]/ng-dropdown-panel[1]/div[1]/div[2]/div/span")
#
# # Ensure there are drivers in the list
# if driver_list:
#
#     if driver_index >= len(driver_list):
#         driver_index = 0
#
#         # Select the driver at the current index
#     selected_driver = driver_list[driver_index]
#     driver_name = selected_driver.text.strip()
#     print(f"Selecting driver at index {driver_index}: {driver_name}")
#
#     selected_driver.click()
#
#     # Increment the index for the next run
#     driver_index += 1
#
#     save_current_index(index_file_path, driver_index)
#
#     print(f"Selected driver: {driver_name}")
# else:
#     print("No drivers found in the list.")
#
# time.sleep(3)

driver.execute_script("window.scrollBy(0, 5000);")
time.sleep(2)

# ---------------------------------Add Image Markers-----------------------------------------------
# -------------------------Add the fuel Information while creating Job Card------------------------

# Click on the "75%" button
driver.find_element(By.XPATH, "//span[normalize-space()='75%']").click()
time.sleep(2)

upload_mileage_img = driver.find_element(By.ID, "fileInput")
# upload_icon.click()
print("The Image Icon is Successfully clicked by the Bot:")
time.sleep(3)

# Specify the file path (use raw string for Windows path)
mileage_image_path = r"D:\Abdullah's Desktop Data\Busses\down2.jpg"
print("The Bot finds the Image path Successfully:")
time.sleep(5)


# Send the file path to the <input type="file"> element
upload_mileage_img.send_keys(mileage_image_path)
print("The image has been successfully uploaded.")
time.sleep(5)


# # Upload the mileage image
# upload_mileage_img = driver.find_element(By.XPATH, "//i[@class='fas fa-2x fa-camera upload-btn camera-icon']")
# upload_mileage_img.click()
# print("The Image Icon is Successfully clicked by the Bot:")
# time.sleep(3)
#
# # Fix the file path by using double backslashes or a raw string (r"...")
# mileage_image_path = r"D:\Abdullah's Desktop Data\Busses\down2.jpg"
# print("The Bot finds the Image path Successfully:")
# time.sleep(5)
# driver.execute_script("arguments[0].style.display = 'block';", upload_mileage_img)
# upload_mileage_img.send_keys(mileage_image_path)
# time.sleep(5)

# Click to check the mileage history
check_mileage = driver.find_element(By.XPATH, "//i[contains(@title,'Mileage History')]")
check_mileage.click()

# Wait for the top mileage element to be visible and retrieve the value
top_mileage_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//td[normalize-space()='50000']"))

)
print("Top Mileage has been checked:")
top_mileage_value = int(top_mileage_element.text.strip())

# Close the mileage history pop-up (wait for the close button to be clickable)
close_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@type,'button')]//span[contains(@aria-hidden,'true')][normalize-space()='×']"))
)
close_button.click()

# Calculate new mileage and input it
new_mileage_value = top_mileage_value + 1000
mileage_input_field = driver.find_element(By.XPATH, "//input[contains(@name,'engine_capacity')]")
print("The Mileage has been incremented by 1000 km:")
mileage_input_field.clear()  # Clear the field before entering a new value
mileage_input_field.send_keys(str(new_mileage_value))
print("The mileage has been entered to the mileage field:")

# Wait for the text-center row to ensure the action is successful
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='row text-center px-2']"))
)

time.sleep(5)

driver.execute_script("window.scrollBy(0, 5000);")
time.sleep(2)


# driver.find_element(By.XPATH, "//span[normalize-space()='75%']").click()
# time.sleep(2)
#
# upload_mileage_img = driver.find_element(By.XPATH, "//i[contains(@title,'upload')]")
# mileage_image_path = "D:\Abdullah's Desktop Data\Busses\down2.jpg"
# upload_mileage_img.send_keys(mileage_image_path)
# time.sleep(5)
#
# check_mileage = driver.find_element(By.XPATH, "//i[contains(@title,'Mileage History')]")
# check_mileage.click()
#
# top_mileage_element = driver.find_element(By.XPATH, "//td[normalize-space()='5000']")
# top_mileage_value = int(top_mileage_element.text.strip())
#
# close_button = driver.find_element(By.XPATH,
#                                    "//button[contains(@type,'button')]//span[contains(@aria-hidden,'true')][normalize-space()='×']")
# new_mileage_value = top_mileage_value + 1000
# mileage_input_field = driver.find_element(By.XPATH, "//input[contains(@name,'engine_capacity')]")
# mileage_input_field.clear()  # Clear the field before entering a new value
# mileage_input_field.send_keys(str(new_mileage_value))
# driver.find_element(By.XPATH, "//div[@class='row text-center px-2']")
#
# time.sleep(5)

# ------------------------------------------Upload Additional Photos--------------------------------------

vehicle_front_img = driver.find_element(By.ID, "fileInput5")
print("Front Image Icon successfully clicked by the bot:")
time.sleep(3)
front_image_path = r"D:\Abdullah's Desktop Data\Busses\down3.jpg"
print("The bot find the path of the front image:")
vehicle_front_img.send_keys(front_image_path)
print("The front image has been successfully uploaded:")
time.sleep(5)

vehicle_rear_img = driver.find_element(By.ID, "fileInput6")
print("Rear Image Icon successfully clicked by the bot:")
time.sleep(3)
rear_image_path = r"D:\Abdullah's Desktop Data\Busses\down2.jpg"
print("The bot find the rear image:")
vehicle_rear_img.send_keys(rear_image_path)
print("The Rear image has been successfully uploaded:")
time.sleep(5)

vehicle_right_img = driver.find_element(By.ID, "Right")
print("Right Image Icon successfully clicked by the bot:")
time.sleep(3)
right_image_path = r"D:\Abdullah's Desktop Data\Busses\down3.jpg"
print("The bot find the rear image:")
vehicle_right_img.send_keys(right_image_path)
print("The Right image has been successfully uploaded:")
time.sleep(5)

vehicle_left_img = driver.find_element(By.ID, "Left")
print("Left Image Icon successfully clicked by the bot:")
time.sleep(3)
left_image_path = r"D:\Abdullah's Desktop Data\Busses\down2.jpg"
print("The bot find the Left Image path:")
vehicle_left_img.send_keys(left_image_path)
print("The Left image has been successfully uploaded:")
time.sleep(5)

vehicle_interior_img = driver.find_element(By.ID, "Interior")
print("Interior Image Icon successfully clicked by the bot:")
time.sleep(3)
interior_image_path = r"D:\Abdullah's Desktop Data\Busses\down3.jpg"
print("The bot finds the Interior image path:")
vehicle_interior_img.send_keys(interior_image_path)
print("The Interior image has been successfully Uploaded:")
time.sleep(5)

vehicle_dashboard_img = driver.find_element(By.ID, "Dashboard")
print("Dashboard Image Icon successfully clicked by the bot:")
time.sleep(3)
dashboard_image_path = r"D:\Abdullah's Desktop Data\Busses\down2.jpg"
print("The bot finds the dashboard image path:")
vehicle_dashboard_img.send_keys(dashboard_image_path)
print("The Dashboard image has been successfully Uploaded:")
time.sleep(5)

driver.execute_script("window.scrollBy(0, 5000);")
time.sleep(2)

# ------------------------Add Driver's Concerns---------------------------------

add_concern_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Add Driver Concern']")
print("The Clicks on the Mechanical Concern:")
add_concern_btn.click()
print("The Mechanical Concern has been added:")
time.sleep(3)

driver_mechanical_concern = driver.find_element(By.XPATH, "//textarea[@placeholder='You can write customer concern here...']")
driver_mechanical_concern.send_keys("This is the Mechanical Concern:")
time.sleep(3)

save_mech_concern = driver.find_element(By.XPATH, "//button[normalize-space()='Save & Add']")
save_mech_concern.click()
time.sleep(3)

electrical_task_type = driver.find_element(By.XPATH, "//div[contains(@class,'modal-body1 rtl')]//div[2]//label[1]")
electrical_task_type.click()
time.sleep(2)

driver_electrical_concern = driver.find_element(By.XPATH, "//textarea[@placeholder='You can write customer concern here...']")
driver_electrical_concern.send_keys("This is the Electrical Concern:")
time.sleep(3)

save_electrical_concern = driver.find_element(By.XPATH, "//button[normalize-space()='Save & Add']")
save_electrical_concern.click()

br_task_type = driver.find_element(By.XPATH, "//span[@class='form-check-sign Concern Toggle dark-font active-text']")
br_task_type.click()
time.sleep(2)

br_driver_concern = driver.find_element(By.XPATH, "//textarea[@placeholder='You can write customer concern here...']")
br_driver_concern.send_keys("This is the Body Repair Concern:")
time.sleep(3)

save_br_concern = driver.find_element(By.XPATH, "//button[normalize-space()='Save & Add']")
save_br_concern.click()

time.sleep(4)

# -------------------------------Entry Stage Checklist----------------------------------------

try:
    # Check if 'Need Maintenance' status is visible
    need_maintenance_status = driver.find_element(By.XPATH, "//span[normalize-space()='Need Maintenance']")
    if need_maintenance_status.is_displayed():
        print("The Checkpoint Status is 'Need Maintenance'.")

        # Find the note input field
        note_input = driver.find_element(By.XPATH, "//input[@placeholder='Note']")
        note_input.clear()  # Clear the input field before adding a note
        add_note = "The Note is mandatory for the Need Maintenance Checkpoint"
        note_input.send_keys(add_note)
        print(f"Added note: {add_note}")

        # List of checkpoint IDs (adjust if necessary)
        checkpoint_ids = [
            "تفقد زجاج الباص كامل2",
            "طاسات عجال+الاطارات2",
            "الهندام2",
            "تاكوجراف1",
            "الاضوية3",
            "المرايا2",
            "DVD2",
            "العدة اليدوية2",
            "الشاشات3",
            "ميكرفون2"
        ]

        # Iterate over the checkpoint IDs and click each one
        for i, checkpoint_id in enumerate(checkpoint_ids, start=1):
            try:
                checkpoint = driver.find_element(By.ID, checkpoint_id)
                checkpoint.click()
                print(f"Checkpoint {i} clicked: {checkpoint_id}")
            except NoSuchElementException:
                print(f"Checkpoint {i} not found: {checkpoint_id}. Moving to the next one.")

    else:
        print("Invalid Status of the Checkpoint: Not 'Need Maintenance'.")

except NoSuchElementException as e:
    print(f"Error: {str(e)} - 'Need Maintenance' status not found on the page.")

time.sleep(5)

# try:
#     need_maintenance_status = driver.find_element(By.XPATH, "//span[normalize-space()='Need Maintenance']")
#     if need_maintenance_status.is_displayed():
#         print("The Checkpoint Status is Need Maintenance: ")
#
#         note_input = driver.find_element(By.XPATH, "//input[@placeholder='Note']")
#         note_input.clear()
#         add_note = "The Note is mandatory for the Need Maintenance Checkpoint"
#         note_input.send_keys(add_note)
#
#         first_entry_checkpoint = driver.find_element(By.ID, "تفقد زجاج الباص كامل2")
#         first_entry_checkpoint.click()
#
#         second_entry_checkpoint = driver.find_element(By.ID, "طاسات عجال+الاطارات2")
#         second_entry_checkpoint.click()
#
#         third_entry_checkpoint = driver.find_element(By.ID, "الهندام2")
#         third_entry_checkpoint.click()
#
#         fourth_entry_checkpoint = driver.find_element(By.ID, "تاكوجراف1")
#         fourth_entry_checkpoint.click()
#
#         fifth_entry_checkpoint = driver.find_element(By.ID, "الاضوية3")
#         fifth_entry_checkpoint.click()
#
#         sixth_entry_checkpoint = driver.find_element(By.ID, "المرايا2")
#         sixth_entry_checkpoint.click()
#
#         seventh_entry_checkpoint = driver.find_element(By.ID, "DVD2")
#         seventh_entry_checkpoint.click()
#
#         eight_entry_checkpoint = driver.find_element(By.ID, "العدة اليدوية2")
#         eight_entry_checkpoint.click()
#
#         ninth_entry_checkpoint = driver.find_element(By.ID, "الشاشات3")
#         ninth_entry_checkpoint.click()
#
#         tenth_entry_checkpoint = driver.find_element(By.ID, "ميكرفون2")
#         tenth_entry_checkpoint.click()
#
#     else:
#         print("Invalid Status of the Chckpoint.")

driver.quit()
