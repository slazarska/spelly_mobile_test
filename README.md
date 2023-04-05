# Automated android tests for mobile application Spelly
<p align="center"><img src="https://github.com/slazarska/spelly_mobile_test/blob/main/resources/img/screen/spelly.png"/></p>

## Content:
- [Technology Stack](#technology-stack)
- [In a nutshell about the project](#in-a-nutshell-about-the-project)
- [Checks are implemented](#checks-are-implemented)
- Tests launch:
  - [Jenkins](#remote-launch-via-jenkins])
  - [Local](#computer-local-launch )
- Reporst:
  - [Allure](#test-reports-available-in-allure)
  - [BrowserStack](#browserstack)
  - [Telegram](#telegram)
- [Allure TestOps](#intergation-with-allure-testops)
- [Video](#test-run-video-example)

## Technology Stack:
<div>
<img src="https://github.com/slazarska/spelly_mobile_test/blob/main/resources/img/icons/python.png" title="Python" alt="Python" width="40" height="40"/>
<img src="https://github.com/slazarska/spelly_mobile_test/blob/main/resources/img/icons/pycharm.png" title="PyCharm" alt="PyCharm" width="40" height="40"/>
<img src="https://github.com/slazarska/spelly_mobile_test/blob/main/resources/img/icons/pytest.png" title="Pytest" alt="Pytest" width="40" height="40"/>
<img src="https://github.com/slazarska/spelly_mobile_test/blob/main/resources/img/icons/selene.png" title="Selene" alt="Selene" width="40" height="40"/>
<img src="https://github.com/slazarska/spelly_mobile_test/blob/main/resources/img/icons/android-studio.png" title="Android Studio" alt="Android Studio" width="40" height="40"/>
<img src="https://github.com/slazarska/spelly_mobile_test/blob/main/resources/img/icons/appium.png" title="Appium" alt="Appium" width="40" height="40"/>
<img src="https://github.com/slazarska/spelly_mobile_test/blob/main/resources/img/icons/browserstack.png" title="Browserstack" alt="Browserstack" width="40" height="40"/>
<img src="https://github.com/slazarska/spelly_mobile_test/blob/main/resources/img/icons/Jenkins.png" title="Jenkins" alt="Jenkins"/>
<img src="https://github.com/slazarska/spelly_mobile_test/blob/main/resources/img/icons/selenoid.png" title="Selenoid" alt="Selenoid" width="40" height="40"/>
<img src="https://github.com/slazarska/spelly_mobile_test/blob/main/resources/img/icons/Allure_Report.png" title="Allure Report" alt="Allure Report"/>
<img src="https://github.com/slazarska/spelly_mobile_test/blob/main/resources/img/icons/AllureTestOps.png" title="AllureTestOps" alt="AllureTestOps"/>
<img src="https://github.com/slazarska/spelly_mobile_test/blob/main/resources/img/icons/Jira.png" title="Jira" alt="Jira" width="40" height="40"/>
<img src="https://github.com/slazarska/spelly_mobile_test/blob/main/resources/img/icons/Telegram.png" title="Telegram" alt="Telegram"/>
</div>

## In a nutshell about the project
- [x] Patterns `Page Object` and `Application Manager`
- [x] Self-documenting code
- [x] Custom local launch using `Android Studio` or `Browserstack`
- [x] Remote launch using `Jenkins` and `Browserstack`
- [x] `Allure Reports` with attachments: logs, screenshots, videos
- [x] Integration with `Allure TestOps`
- [x] Integration with `Jira`
- [x] Notifications about test launch and test results via `Telegram`

## Checks are implemented:

- [X] - Opening spells page
- [X] - Check the name of spell
- [X] - Check the attributes on the spells page
- [X] - Adding the spell to the favorite spells list

## Remote launch via [Jenkins]()

To run tests from Jenkins:
1. Click the "Build Now" button.
<p><img src="" alt="Jenkins"/></p>

## Local launch 

To run locally:
1. Clone the repository
2. Install Poetry (`poetry install`)
3. Open the project in PyCharm, add Python Interpreter
4. Launch BrowserStack
   - Sign up and get credentials (username, access key), download apk from resources folder to get app id
5. Install Android Studio and Appium
   - Start Appium Server
   - Run device emulator with Virtual Device Manager in Android Studio
6. Create `env` files in the project folder according to the samples:
    - `config.browserstack.env` 
    - `config.local.env`
7. Run the tests in PyCharm or on the command line:
```bash
pytest . --alluredir allure-results/
```
8. Check launch status in BrowserStack

## Build parameters:

> In the `config.py` file, change the value of `EnvContext`:
> - `local` — run locally with device emulator
> - `browserstack` — run in BrowserStack

## Test reports available in Allure Report:

<img title="Allure" src=" ">

> When running locally, enter on the command line:
```bash
allure serve .\allure-results
```

#### How the tests look in Allure Report:

<p><img src="" alt="Allure"/></p>

<p><img src="" alt="Allure"/></p>

### <img title="BrowserStack" src=""> BrowserStack

<img src="" alt="BrowserStack"/>

### *Telegram notification configured:*

<img src="" alt="Telegram"/>

## Intergation with Allure TestOps:

<img src=" " alt="Allure TestOps"/>

## Added video into tests run. Test run video example:
![video]()
<br><br>

<p align="center">
  <img title="Video" src="">
</p>

Thanks :pray:<br/>
:green_heart: <a target="_blank" href="https://qa.guru">QA.GURU</a><br/>
:purple_heart: <a target="_blank" href="https://sites.google.com/view/qasisters/">QA Sisters</a><br/>