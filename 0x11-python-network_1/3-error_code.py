#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).

You have to manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code
You must use the packages urllib and sys
You are not allowed to import other packages than urllib and sys
You don’t need to check arguments passed to the script (number or type)
You must use the with statement
"""
if __name__ == "__main__":
    import urllib.error as error
    import urllib.request as request
    from sys import argv
    doc = request.Request(argv[1])
    try:
        with request.urlopen(doc) as docum:
            print(docum.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
