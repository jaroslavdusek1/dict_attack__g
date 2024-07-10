# dict_attack_ig

## Description
dict_attack_ig is a Python script designed to perform a dictionary attack on Instagram login. By using a provided wordlist and a username/email, the script iterates through possible passwords attempting to gain access to the specified Instagram account. If a successful login is detected, the script will print the successful password and terminate.

## Features
- Uses Selenium WebDriver to automate interactions with Instagram's login page.
- Supports dictionary attack using a custom wordlist.
- Adjustable screen positioning for better visibility during the attack process.
- Provides detailed output on each login attempt.

## Installation

### macOS and Linux
1. Clone the repository:

    ```sh
    git clone https://github.com/jaroslavdusek1/dict_attack_ig.git
    cd dict_attack_ig
    ```

2. Create and activate a virtual environment:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Download and install the latest version of ChromeDriver compatible with Chrome version 126:

    **For macOS:**

    ```sh
    wget https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.126/mac-arm64/chromedriver-mac-arm64.zipzip -O chromedriver.zip
    unzip chromedriver.zip
    sudo mv chromedriver-mac-arm64/chromedriver /usr/local/bin/
    ```

    **For Linux:**

    ```sh
    wget https://storage.googleapis.com/chrome-for-testing/126.0.6478.126/linux64/chromedriver-linux64.zip -O chromedriver.zip
    unzip chromedriver.zip
    sudo mv chromedriver-linux64/chromedriver /usr/local/bin/
    ```

5. Verify ChromeDriver installation:

    ```sh
    chromedriver --version
    ```

6. Ensure you have Google Chrome version 126 installed. If not, download and install it from [Chrome's official site](https://www.google.com/chrome/).

## Usage

To run the script, use the following command:

```sh
python3 run.py -w [wordlist_file] -u [username]
