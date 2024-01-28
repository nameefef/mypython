  from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import getpass

# Create a new Firefox WebDriver instance
browser = webdriver.Firefox()

# Visit the specified webpage
url = "<your url>"
browser.get(url)

# Function to check for the presence of reCAPTCHA
def is_recaptcha_present():
    try:
        recaptcha_element = browser.find_element(By.CLASS_NAME, 'g-recaptcha')
        return recaptcha_element.is_displayed()
    except:
        return False

# Function to check for the presence of an error message
def is_error_message_present():
    try:
        error_message_element = browser.find_element(By.XPATH, '//div[@class="o6cuMc"]')
        return error_message_element.is_displayed()
    except:
        return False

# Function to fill input fields
def fill_input_fields():
    input_fields = browser.find_elements(By.TAG_NAME, 'input')

    for input_field in input_fields:
        # Input data only if the input field is visible
        if input_field.is_displayed():
            field_name = input_field.get_attribute("name")
            if "email" in field_name.lower():
                input_value = input(f'请输入邮箱地址 ({field_name}): ')
            elif "phone" in field_name.lower():
                input_value = input(f'请输入手机号码 ({field_name}): ')
            elif "password" in field_name.lower():
                input_value = getpass.getpass(f'请输入密码 ({field_name}): ')
            elif "code" in field_name.lower() or "captcha" in field_name.lower():
                input_value = input(f'请输入验证码 ({field_name}): ')
            else:
                input_value = input(f'请输入值 ({field_name}): ')

            input_field.clear()  # Clear the input field in case it's pre-filled
            input_field.send_keys(input_value)

# Wait for up to 30 seconds for reCAPTCHA or error message to appear
wait = WebDriverWait(browser, 30)
if wait.until(is_recaptcha_present):
    print("Detected reCAPTCHA. The program will stop, and you need to handle the reCAPTCHA manually.")
    print("If you have completed the reCAPTCHA, you can resume the program.")

    # You can add any additional instructions or information for the user here

    # Keep the browser open until manually closed
    while True:
        pass  # This loop will run indefinitely until manually terminated

elif wait.until(is_error_message_present):
    print("Detected an error message. The program will stop, and you may want to handle this situation accordingly.")
    print("You can check the error message or take necessary actions.")

    # You can add any additional instructions or information for the user here

    # Keep the browser open until manually closed
    while True:
        pass  # This loop will run indefinitely until manually terminated

else:
    # Fill input fields
    fill_input_fields()

    # Locate and click the "Next" button (if applicable)
    next_button = browser.find_element(By.XPATH, '//div[@id="identifierNext"]')
    next_button.click()

# Continue with your regular program logic here
# ...

# The browser will remain open until you manually close the script.
