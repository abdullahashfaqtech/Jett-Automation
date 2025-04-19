"""
Configuration settings for the JETT Automation project.
"""

# URLs
BASE_URL = "https://jett.autohub.jo/auth/login"

# Credentials
ADMIN_CREDENTIALS = {
    "email": "admin@jett.com",
    "old_password": "P@$$w0rd@autohub",
    "new_password": "123123"
}

SUPERVISOR_CREDENTIALS = {
    "email": "supervisor@autohub.jo",
    "old_password": "123123",
    "new_password": "123456"
}

# XPath Selectors
SELECTORS = {
    "login": {
        "email": "//input[@name='email']",
        "password": "//input[@name='password']",
        "submit": "//button[@class='btn']",
        "reset_password": "//button[@type='submit']",
        "confirm_password": "//input[@name='confirm_password']"
    },
    "branch": {
        "dropdown": "//div[@class='ng-select-container ng-has-value']//span[@class='ng-arrow-wrapper']",
        "aqaba": "/html[1]/body[1]/app-root[1]/app-full-layout[1]/div[1]/nav[1]/div[1]/div[3]/div[1]/ng-select[1]/ng-dropdown-panel[1]/div[1]/div[2]/div[3]/span[1]"
    },
    "job_card": {
        "create": "//a[normalize-space()='+Create Job']",
        "plate_number": "/html[1]/body[1]/app-root[1]/app-full-layout[1]/div[1]/main[1]/div[1]/div[1]/div[1]/app-create-job[1]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[1]/app-inspection[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]",
        "search": "//i[@class='fas fa-search pt-1']"
    }
}

# File Paths
IMAGE_PATHS = {
    "mileage": r"D:\Abdullah's Desktop Data\Busses\down2.jpg",
    "front": r"D:\Abdullah's Desktop Data\Busses\down3.jpg",
    "rear": r"D:\Abdullah's Desktop Data\Busses\down2.jpg",
    "right": r"D:\Abdullah's Desktop Data\Busses\down3.jpg",
    "left": r"D:\Abdullah's Desktop Data\Busses\down2.jpg",
    "interior": r"D:\Abdullah's Desktop Data\Busses\down3.jpg",
    "dashboard": r"D:\Abdullah's Desktop Data\Busses\down2.jpg"
}

# Timeouts
TIMEOUTS = {
    "implicit_wait": 10,
    "explicit_wait": 10,
    "page_load": 30
}

# Messages
MESSAGES = {
    "login_success": "Successfully logged in",
    "password_reset": "Password has been successfully reset",
    "password_expired": "Password has expired. Resetting password...",
    "login_error": "Error during login process"
} 