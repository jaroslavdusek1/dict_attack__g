# dict_attack_ig

⚠️ DISCLAIMER ⚠️
This script is provided for educational purposes only. The author does not condone or promote illegal activities. Use this tool and at your own risk. Enjoy responsibly.

## description
dict_attack_ig is a .py script designed to perform a dictionary attack on Instagram login. By using a provided wordlist and a username/email, attempting to gain access to the specified Instagram accountm if a successful login is detected, the script will print the successful password and terminate

## features
- uses selenium webDriver to automate interactions with IG's login page
- supports dictionary attack using a custom wordlist.
- adjustable half page screen positioning for better visibility during the attack process
- provides detailed output on each login attempt success/faled

## installation

### macOS and Linux
1. clone the repo:

    ```sh
    git clone https://github.com/jaroslavdusek1/dict_attack_ig.git
    cd dict_attack_ig
    ```

2. create and activate a venv:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. download and install the latest version of ChromeDriver compatible with Chrome version 126:

    **for macOS:**

    ```sh
    wget https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.126/mac-arm64/chromedriver-mac-arm64.zipzip -O chromedriver.zip
    unzip chromedriver.zip
    sudo mv chromedriver-mac-arm64/chromedriver /usr/local/bin/
    ```

    **for Linux:**

    ```sh
    wget https://storage.googleapis.com/chrome-for-testing/126.0.6478.126/linux64/chromedriver-linux64.zip -O chromedriver.zip
    unzip chromedriver.zip
    sudo mv chromedriver-linux64/chromedriver /usr/local/bin/
    ```

5. verify chromeDriver and google Chrome versions:
    
    ///chrome driver///
    ```sh
    chromedriver --version
    ```

    ///chrome browser///
    **For macOS:**

    ```sh
    /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version
    ```

    **For Linux:**

    ```sh
    google-chrome --version
    ```

6. ensure you have google chrome version 126 installed. If not, follow these steps:

    **For Linux:**

    ```sh
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
    sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
    sudo apt update
    sudo apt install google-chrome-stable
    google-chrome --version
    ```

7. install google chrome:

    ```sh
    sudo apt install google-chrome-stable
    ```

8. verify the version of google chrome by running:

    ```sh
    google-chrome --version
    ```

## Usage

to run the script, use the following command:

```sh
python3 run.py -w [wordlist_file] -u [username]
```

Testing Environments
tested on macOS ARM-1 Ventura 13.6 and Kali Linux Purple with AMD, both setups play nice with:

Google Chrome: 126.0.6478.127
ChromeDriver: 126.0.6478.126
