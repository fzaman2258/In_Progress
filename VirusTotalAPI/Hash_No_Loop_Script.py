import requests
import time
import operator

# BASE URL for the API
url = 'https://www.virustotal.com/vtapi/v2/file/report'

# Dictionary that Contains User API Key and Hash that needs to be analyzed
params = {'apikey': '5495d7c47aafe9491e06136a47dc2dad29db87423ad5222b2e07760c4ba14aa4', 'resource': ''}

# Opens the file and reads all the lines(hashes) into a list
with open("hashes.txt") as f:
    lineList = f.readlines()

# Iterates through each hash
for i in lineList:

    # Replaces resource in params dictionary with current Hash
    params['resource'] = i

    # Sends Query using url and params
    response = requests.get(url, params=params)

    # Code 204 means too many requests in a given amount of time
    while (response.status_code == 204):
        time.sleep(10)
        response = requests.get(url, params=params)

    # response.json() gets the dictonary form of the data and the 'scans' key contains the data that we want
    errorDetails = response.json()["scans"]

    # Prints current Hash after removing any newlines
    print("HASH: " + i.strip("\n"))

    # Checks if McAfee has a result
    try:
        if (errorDetails['McAfee']['detected'] is True):
            print("McAfee Result: " + errorDetails["McAfee"]["result"])
        else:
            print("McAfee: No Results")
    except:
        print("McAfee unable to process hash")

    # Checks if PaloAlto has a result
    try:
        if (errorDetails['Paloalto']['detected'] is True):
            print("PaloAlto Result: " + errorDetails["Paloalto"]["result"])
        else:
            print("PaloAlto: No Results")
    except:
        print("Palo Alto unable to process hash")

    print("-------------------------------\n")
