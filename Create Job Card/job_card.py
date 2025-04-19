"""
Job Card creation functionality for JETT Automation project.
"""
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from base import JettBase
from config import SELECTORS, IMAGE_PATHS, MESSAGES

logger = logging.getLogger(__name__)

class JobCardCreator(JettBase):
    def __init__(self):
        super().__init__()
        self.actions = ActionChains(self.driver)

    def login(self, credentials):
        """Handle login process with password reset if needed."""
        try:
            self.driver.get(SELECTORS["login"]["url"])
            self.send_keys(By.NAME, "email", credentials["email"])
            self.send_keys(By.NAME, "password", credentials["old_password"])
            self.click_element(By.CLASS_NAME, "btn")
            self.safe_sleep(5)

            # Check for password reset
            try:
                reset_button = self.find_element(By.XPATH, SELECTORS["login"]["reset_password"])
                if reset_button.is_displayed():
                    logger.info(MESSAGES["password_expired"])
                    self.handle_password_reset(credentials["new_password"])
            except:
                logger.info(MESSAGES["login_success"])

        except Exception as e:
            logger.error(f"Login failed: {str(e)}")
            raise

    def handle_password_reset(self, new_password):
        """Handle password reset process."""
        try:
            self.send_keys(By.XPATH, SELECTORS["login"]["password"], new_password)
            self.safe_sleep(5)
            self.send_keys(By.XPATH, SELECTORS["login"]["confirm_password"], new_password)
            self.click_element(By.XPATH, SELECTORS["login"]["reset_password"])
            self.safe_sleep(5)
            logger.info(MESSAGES["password_reset"])
        except Exception as e:
            logger.error(f"Password reset failed: {str(e)}")
            raise

    def select_branch(self):
        """Select the Aqaba branch."""
        try:
            self.click_element(By.XPATH, SELECTORS["branch"]["dropdown"])
            self.safe_sleep(5)
            self.click_element(By.XPATH, SELECTORS["branch"]["aqaba"])
            logger.info("Selected Aqaba branch")
        except Exception as e:
            logger.error(f"Failed to select branch: {str(e)}")
            raise

    def create_job_card(self, plate_number):
        """Create a new job card with the given plate number."""
        try:
            # Click create job button
            self.click_element(By.XPATH, SELECTORS["job_card"]["create"])
            self.safe_sleep(12)

            # Enter plate number
            self.send_keys(By.XPATH, SELECTORS["job_card"]["plate_number"], plate_number)
            self.safe_sleep(5)

            # Search for plate number
            self.click_element(By.XPATH, SELECTORS["job_card"]["search"])
            self.safe_sleep(5)

            # Select driver
            self.select_driver()

            # Upload images
            self.upload_vehicle_images()

            # Add driver concerns
            self.add_driver_concerns()

            # Complete entry stage checklist
            self.complete_entry_checklist()

            # Submit job card
            self.submit_job_card()

        except Exception as e:
            logger.error(f"Failed to create job card: {str(e)}")
            raise

    def select_driver(self):
        """Select a driver from the dropdown."""
        try:
            driver_dropdown = self.find_element(By.XPATH, "//div[@class='ng-select-container']//input[@role='combobox']")
            self.scroll_to_element(driver_dropdown)
            driver_dropdown.click()
            self.safe_sleep(2)

            specific_driver = self.find_element(By.XPATH, "//span[contains(text(),'محمود هاشم محمود البيك')]")
            specific_driver.click()
            logger.info("Selected driver from dropdown")
        except Exception as e:
            logger.error(f"Failed to select driver: {str(e)}")
            raise

    def upload_vehicle_images(self):
        """Upload all required vehicle images."""
        try:
            # Upload mileage image
            self.upload_image("fileInput", IMAGE_PATHS["mileage"])
            
            # Upload vehicle photos
            self.upload_image("fileInput5", IMAGE_PATHS["front"])
            self.upload_image("fileInput6", IMAGE_PATHS["rear"])
            self.upload_image("Right", IMAGE_PATHS["right"])
            self.upload_image("Left", IMAGE_PATHS["left"])
            self.upload_image("Interior", IMAGE_PATHS["interior"])
            self.upload_image("Dashboard", IMAGE_PATHS["dashboard"])
            
            logger.info("All vehicle images uploaded successfully")
        except Exception as e:
            logger.error(f"Failed to upload images: {str(e)}")
            raise

    def upload_image(self, element_id, image_path):
        """Upload a single image."""
        try:
            element = self.find_element(By.ID, element_id)
            element.send_keys(image_path)
            self.safe_sleep(5)
            logger.info(f"Uploaded image: {image_path}")
        except Exception as e:
            logger.error(f"Failed to upload image {image_path}: {str(e)}")
            raise

    def add_driver_concerns(self):
        """Add driver concerns of different types."""
        try:
            # Add mechanical concern
            self.add_concern("Mechanical", "This is the Mechanical Concern.")
            
            # Add electrical concern
            self.add_concern("Electrical", "This is the Electrical Concern.")
            
            # Add body repair concern
            self.add_concern("Body Repair", "This is the Body Repair Concern.")
            
            logger.info("Added all driver concerns")
        except Exception as e:
            logger.error(f"Failed to add driver concerns: {str(e)}")
            raise

    def add_concern(self, concern_type, concern_text):
        """Add a single driver concern."""
        try:
            # Click add concern button
            self.click_element(By.XPATH, "//button[normalize-space()='Add Driver Concern']")
            self.safe_sleep(5)

            # Select concern type
            self.click_element(By.XPATH, f"//span[normalize-space()='{concern_type}']")
            self.safe_sleep(2)

            # Enter concern text
            self.send_keys(By.XPATH, "//textarea[@placeholder='You can write customer concern here...']", concern_text)
            self.safe_sleep(3)

            # Save concern
            self.click_element(By.XPATH, "//button[normalize-space()='Save & Add']")
            self.safe_sleep(3)

            logger.info(f"Added {concern_type} concern")
        except Exception as e:
            logger.error(f"Failed to add {concern_type} concern: {str(e)}")
            raise

    def complete_entry_checklist(self):
        """Complete the entry stage checklist."""
        try:
            # Click through all checkpoints
            for i in range(1, 11):
                self.handle_checkpoint(i)
            
            logger.info("Completed entry checklist")
        except Exception as e:
            logger.error(f"Failed to complete entry checklist: {str(e)}")
            raise

    def handle_checkpoint(self, checkpoint_number):
        """Handle a single checkpoint in the entry checklist."""
        try:
            xpath = f'//tbody/tr[{checkpoint_number}]/td[3]/div[1]/label[1]/span[1]'
            element = self.find_element(By.XPATH, xpath)
            
            if element.is_displayed():
                self.actions.move_to_element(element).click().perform()
                logger.info(f"Completed checkpoint {checkpoint_number}")
            
            self.safe_sleep(5)
        except Exception as e:
            logger.error(f"Failed to handle checkpoint {checkpoint_number}: {str(e)}")
            raise

    def submit_job_card(self):
        """Submit the completed job card."""
        try:
            self.click_element(By.XPATH, "//button[@type='submit']")
            self.safe_sleep(10)
            logger.info("Job card submitted successfully")
        except Exception as e:
            logger.error(f"Failed to submit job card: {str(e)}")
            raise 