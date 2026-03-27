from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "emulator-5554"
options.platform_version = "16"
options.automation_name = "UiAutomator2"

options.adb_exec_timeout = 120000
options.new_command_timeout = 300

print("Starting session...")
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
print("Session started")

time.sleep(3)

try:
    driver.activate_app("com.android.settings")
except:
    driver.start_activity("com.android.settings", ".Settings")

time.sleep(3)

try:
    el = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().textContains("Network")'
    )
except NoSuchElementException:
    el = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true))'
        '.scrollIntoView(new UiSelector().textContains("Network"))'
    )

el.click()
time.sleep(3)

try:
    driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().textContains("Network")'
    ).click()
except NoSuchElementException:
    print("Already inside Network settings or no further option")

time.sleep(5)

driver.quit()
