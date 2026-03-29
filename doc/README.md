# Mobile QA Automation Lab

## Description
This is mobile test automation project using Appium and Python to automate Android applications. It includes a structured setup for driver configuration and test execution, with dynamic elemnt handling to support different Android versions.

## What the Project Does
the project automates Android applications via an emulator. The main test script (`test_settings.py`) opens the Android settings app, navigates to network related options, and interacts with them automatically. The framework handles variations in UI across Android versions and demonstartes key mobile QA automation practices like session management and resilient element loaction.

## How TO Run
1. Start teh Appium server at `https://127.0.0.1:4723`.
2. Launch your Android emulator and make sure it is fully booted.
3. Install project dependencies.

```bash
pip install -r requirements.txt

4. Run the test script:

```bash
python3 tests/test_settings.py

5. The script will open the Settings app, locate network options, and interact with them automatically.
Tools used
Python - main programming language
Appium - mobile automation framework
UiAutomator2 - Andriod driver for Android automation
Selenium WebDriver(Python) - for UI inetractions
Android Emulator - virtual device for testing
Project Structure
mobile-automation-appium/
│
├── tests/
│   └── test_settings.py      # Automates navigation in Android Settings
├── utils/
│   └── driver_setup.py       # Configures and initializes Appium driver
├── requirements.txt          # Project dependencies
├── README.md                 # Project overview and instructions
Notes
Designed for cross-version compatibility on Android emulators.
Includes dynamic elements handling to make automation resilient
Can be extended to automate other apps or more complex test scenerios
