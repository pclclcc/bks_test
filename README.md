# Mobly + Snippet UiAutomator
## Description
This test is to verify login cathay homepage.
It used snippet-uiautomator and mobly to build the test.
-  mobly: https://github.com/google/mobly
-  snippet-uiautomator: https://github.com/google/snippet-uiautomator

## Requirements
-   Android 8.0+ (SDK 26+)
-   adb (1.0.40+ recommended)
-   Python3.11+

## Installation
```shell
sudo pip3 install snippet-uiautomator
```
```shell
sudo pip3 install mobly
```

## Compatibility
Mobly requires python 3.11 or newer.
Mobly tests could run on the following platforms:
-   Ubuntu 14.04+
-   MacOS 10.6+
-   Windows 7+

## Command
Navigate to the root directory.
```shell
python3 test1.py -c sample_config.yml
```
Invoking specific test case:
```shell
python3 test1.py -c sample_config.yml --test_case test_open_bidv
```
Multiple Test Beds and Default Test Parameters:
```shell
python3 test1.py -c sample_config.yml --test_bed SampleTestBed
```