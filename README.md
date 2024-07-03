# PyTest with Browserstack AppAutomate

PyTest Integration with BrowserStack.

![BrowserStack Logo](https://d98b8t1nnulk5.cloudfront.net/production/images/layout/logo-header.png?1469004780)
### Requirements

1. Python 3.6+ or Python 2.7+
    
    - For Windows, download latest python version from [here](https://www.python.org/downloads/windows/) and run the installer executable
    - For Mac and Linux, run `python --version` to see what python version is pre-installed. If you want a different version download from [here](https://www.python.org/downloads/)

### Install the dependencies

To install the dependencies, run the following command in project's base directory:

- For Python 3

    ```sh
    pip3 install -r requirements.txt
    ```

- For Python 2

    ```sh
    pip install -r requirements.txt
    ```

## Getting Started

Getting Started with Pytest-Appium tests in Python on BrowserStack couldn't be easier!

### Run your first test :

**1. Upload your Android or iOS App**

Upload your Android app (.apk or .aab file) or iOS app (.ipa file) to BrowserStack servers using our REST API. Here is an example cURL request :

```
curl -u "YOUR_USERNAME:YOUR_ACCESS_KEY" \
-X POST "https://api-cloud.browserstack.com/app-automate/upload" \
-F "file=@/path/to/apk/file"
```

Ensure that @ symbol is prepended to the file path in the above request. Please note the `app_url` value returned in the API response. We will use this to set the application under test while configuring the test later on.

**Note**: If you do not have an .apk or .ipa file and are looking to simply try App Automate, you can download and test using our [sample Android app](https://www.browserstack.com/app-automate/sample-apps/android/WikipediaSample.apk) or [sample iOS app](https://www.browserstack.com/app-automate/sample-apps/ios/BStackSampleApp.ipa).


**2. Configure and run your first single test**

Open `single.json` file in `android/run-single-test` folder for Android and `ios/run-single-test` folder for iOS:

- Replace `BROWSERSTACK_USERNAME` & `BROWSERSTACK_ACCESS_KEY` with your BrowserStack access credentials. Get your BrowserStack access credentials from [here](https://www.browserstack.com/accounts/settings)

- Replace `bs://<app-id>` with the URL obtained from app upload step

- Set the deviceName and platformVersion. You can refer our [Capability Generator](https://www.browserstack.com/app-automate/capabilities)

- Run the below command to execute a single Android test on BrowserStack AppAutomate:
    ```
    cd android
    paver run single
    ```

- Run the below command to execute a single iOS test on BrowserStack AppAutomate:
    ```
    cd ios
    paver run single
    ```

**3. Configure and run your parallel test**

- In order to run tests in parallel across different configurations, Open `parallel.json` file in `android/run-parallel-test` folder for Android and `ios/run-parallel-test` folder for iOS

- Replace `BROWSERSTACK_USERNAME` & `BROWSERSTACK_ACCESS_KEY` with your BrowserStack access credentials. Get your BrowserStack access credentials from [here](https://www.browserstack.com/accounts/settings)

- Replace `bs://<app-id>` wkth the URL obtained from app upload step

- Set the deviceName and platformVersion. You can refer our [Capability Generator](https://www.browserstack.com/app-automate/capabilities)
    
- Run the below command to execute parallel Android test on BrowserStack AppAutomate:
```
cd android
paver run parallel
```

- Run the below command to execute a parallel iOS test on BrowserStack AppAutomate:
```
cd ios
paver run parallel
```

- You can access the test execution results, and debugging information such as video recording, network logs on [App Automate dashboard](https://app-automate.browserstack.com/dashboard)

---

### **Use Local testing for apps that access resources hosted in development or testing environments :**

**1. Upload your Android or iOS App**

Upload your Android app (.apk or .aab file) or iOS app (.ipa file) that access resources hosted on your internal or test environments to BrowserStack servers using our REST API. Here is an example cURL request :

```
curl -u "YOUR_USERNAME:YOUR_ACCESS_KEY" \
-X POST "https://api-cloud.browserstack.com/app-automate/upload" \
-F "file=@/path/to/apk/file"
```

Ensure that @ symbol is prepended to the file path in the above request. Please note the `app_url` value returned in the API response. We will use this to set the application under test while configuring the test later on.

**Note**: If you do not have an .apk or .ipa file and are looking to simply try App Automate, you can download and test using our [sample Android Local app](https://www.browserstack.com/app-automate/sample-apps/android/LocalSample.apk) or [sample iOS Local app](https://www.browserstack.com/app-automate/sample-apps/ios/LocalSample.ipa).


**2. Configure and run your local test**

Open `local.json` file in `android/run-local-test` folder for Android and `ios/run-local-test` folder for iOS:


- Replace `BROWSERSTACK_USERNAME` & `BROWSERSTACK_ACCESS_KEY` with your BrowserStack access credentials. Get your BrowserStack access credentials from [here](https://www.browserstack.com/accounts/settings)

- Replace `bs://<app-id>` wkth the URL obtained from app upload step

- Set the deviceName and platformVersion. You can refer our [Capability Generator](https://www.browserstack.com/app-automate/capabilities)

- Ensure that `local` capability is set to `true`. The `conftest.py` contains the code snippet that automatically establishes Local Testing connection to BrowserStack servers using Python binding for BrowserStack Local. 

- Run the below command for Android: 
    ```
    cd android
    paver run local
    ```

- Run the below command for iOS: 
    ```
    cd ios
    paver run local
    ```

- You can access the test execution results, and debugging information such as video recording, network logs on [App Automate dashboard](https://app-automate.browserstack.com/dashboard)
