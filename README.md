# PyTest with Browserstack AppAutomate

PyTest Integration with BrowserStack using SDK.

![BrowserStack Logo](https://d98b8t1nnulk5.cloudfront.net/production/images/layout/logo-header.png?1469004780)
### Requirements

* Python3

## Setup

* Clone the repo with `git clone -b sdk https://github.com/browserstack/pytest-appium-app-browserstack.git`
* It is recommended to use a virtual environment to install dependencies. To create a virtual environment:
  ```
  python3 -m venv env
  source env/bin/activate # on Mac
  env\Scripts\activate # on Windows
  ```
* Install dependencies `pip install -r requirements.txt`
* To run your automated tests using BrowserStack, you must provide a valid username and access key. This can be done either by providing your username and access key in the `browserstack.yml` configuration file, or by setting the `BROWSERSTACK_USERNAME` and `BROWSERSTACK_ACCESS_KEY` environment variables.

## Getting Started

Getting Started with Pytest-Appium tests in Python on BrowserStack couldn't be easier!

### Run your first test :

**1. Upload your Android or iOS App**

Specify your Android app (.apk or .aab file) or iOS app (.ipa file) in the `browserstack.yml` configuration file. Here is an example app config :

```
app: '/path/to/local/app.apk'
```

Set `app` to use the appliction under test for Appium sessions. Available options: app: `/path/to/local/app.apk` OR app: `bs://<app-id>` i.e App URL returned when uploading the app to BrowserStack manually. Visit https://www.browserstack.com/docs/app-automate/appium/set-up-tests/specify-app for more options

**Note**: If you do not have an .apk or .ipa file and are looking to simply try App Automate, you can download and test using our [sample Android app](https://www.browserstack.com/app-automate/sample-apps/android/WikipediaSample.apk) or [sample iOS app](https://www.browserstack.com/app-automate/sample-apps/ios/BStackSampleApp.ipa).


**2. Configure and run your first single test**

Open `browserstack.yml` file in `android` folder for Android and `ios` folder for iOS:

- Replace `YOUR_USERNAME` & `YOUR_ACCESS_KEY` in the `browserstack.yml` configuration file. Get your BrowserStack access credentials from [here](https://www.browserstack.com/accounts/settings)

- Replace `app: bs://<app-id>` with the URL obtained from app upload step or mention the path to your apk file.

- Run the below command to execute a Android test on BrowserStack AppAutomate:
    ```
    cd android
    browserstack-sdk pytest -s bstack_sample.py
    ```

- Run the below command to execute a iOS test on BrowserStack AppAutomate:
    ```
    cd ios
    browserstack-sdk pytest -s bstack_sample.py
    ```

- You can access the test execution results, and debugging information such as video recording, network logs on [App Automate dashboard](https://app-automate.browserstack.com/dashboard)

---

### **Use Local testing for apps that access resources hosted in development or testing environments :**

**1. Upload your Android or iOS App**

Specify your Android app (.apk or .aab file) or iOS app (.ipa file) in the `browserstack.yml` configuration file. Here is an example app config :

```
app: '/path/to/local/app.apk'
```

Set `app` to use the appliction under test for Appium sessions. Available options: app: `/path/to/local/app.apk` OR app: `bs://<app-id>` i.e App URL returned when uploading the app to BrowserStack manually. Visit https://www.browserstack.com/docs/app-automate/appium/set-up-tests/specify-app for more options

**Note**: If you do not have an .apk or .ipa file and are looking to simply try App Automate, you can download and test using our [sample Android app](https://www.browserstack.com/app-automate/sample-apps/android/WikipediaSample.apk) or [sample iOS app](https://www.browserstack.com/app-automate/sample-apps/ios/BStackSampleApp.ipa).


**2. Configure and run your local test**

Open `browserstack.yml` file in `android` folder for Android and `ios` folder for iOS:

- Replace `YOUR_USERNAME` & `YOUR_ACCESS_KEY` in the `browserstack.yml` configuration file. Get your BrowserStack access credentials from [here](https://www.browserstack.com/accounts/settings)

- Replace `app: bs://<app-id>` with the URL obtained from app upload step or mention the path to your apk file.

- Ensure that `browserstackLocal` capability is set to `true`. The `browserstack-sdk` contains the code snippet that automatically establishes Local Testing connection to BrowserStack servers using Python binding for BrowserStack Local. 

- Run the below command for Android: 
    ```
    cd android
    browserstack-sdk pytest -s bstack_sample_local.py
    ```

- Run the below command for iOS: 
    ```
    cd ios
    browserstack-sdk pytest -s bstack_sample_local.py
    ```

- You can access the test execution results, and debugging information such as video recording, network logs on [App Automate dashboard](https://app-automate.browserstack.com/dashboard)
