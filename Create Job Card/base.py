"""
Base class for JETT Automation project.
"""
import time
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config import TIMEOUTS

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class JettBase:
    def __init__(self):
        self.driver = None
        self.wait = None
        self.setup_driver()

    def setup_driver(self):
        """Initialize the WebDriver with proper settings."""
        try:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(TIMEOUTS["implicit_wait"])
            self.wait = WebDriverWait(self.driver, TIMEOUTS["explicit_wait"])
            logger.info("WebDriver initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize WebDriver: {str(e)}")
            raise

    def find_element(self, by, value, timeout=None):
        """Find an element with explicit wait."""
        try:
            wait_time = timeout or TIMEOUTS["explicit_wait"]
            element = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            logger.error(f"Element not found: {value}")
            raise
        except Exception as e:
            logger.error(f"Error finding element {value}: {str(e)}")
            raise

    def click_element(self, by, value, timeout=None):
        """Click an element with explicit wait."""
        try:
            element = self.find_element(by, value, timeout)
            element.click()
            logger.info(f"Clicked element: {value}")
        except Exception as e:
            logger.error(f"Failed to click element {value}: {str(e)}")
            raise

    def send_keys(self, by, value, text, timeout=None):
        """Send keys to an element with explicit wait."""
        try:
            element = self.find_element(by, value, timeout)
            element.clear()
            element.send_keys(text)
            logger.info(f"Sent keys to element: {value}")
        except Exception as e:
            logger.error(f"Failed to send keys to element {value}: {str(e)}")
            raise

    def wait_for_element_clickable(self, by, value, timeout=None):
        """Wait for an element to be clickable."""
        try:
            wait_time = timeout or TIMEOUTS["explicit_wait"]
            element = WebDriverWait(self.driver, wait_time).until(
                EC.element_to_be_clickable((by, value))
            )
            return element
        except TimeoutException:
            logger.error(f"Element not clickable: {value}")
            raise
        except Exception as e:
            logger.error(f"Error waiting for element {value}: {str(e)}")
            raise

    def scroll_to_element(self, element):
        """Scroll to an element using JavaScript."""
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            logger.info("Scrolled to element successfully")
        except Exception as e:
            logger.error(f"Failed to scroll to element: {str(e)}")
            raise

    def safe_sleep(self, seconds):
        """Safe sleep with logging."""
        logger.debug(f"Sleeping for {seconds} seconds")
        time.sleep(seconds)

    def quit(self):
        """Safely quit the WebDriver."""
        if self.driver:
            try:
                self.driver.quit()
                logger.info("WebDriver closed successfully")
            except Exception as e:
                logger.error(f"Error closing WebDriver: {str(e)}")
                raise 