def create_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.platform_version = "16"
    options.automation_name = "UiAutomator2"
    options.adb_exec_timeout = 120000
    options.new_command_timeout = 300

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    return driver
