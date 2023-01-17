#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.

The email must be sent in the variable email
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to error check arguments passed to the script (number or type)
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    payloads = {'email': argv[2]}
    doc = requests.post(argv[1], data=payloads)
    print(doc.text)
