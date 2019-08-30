import requests
import time

# BASE URL for API
url = 'https://www.virustotal.com/vtapi/v2/file/report'

# User API key and requested resource
params = {'apikey': '5495d7c47aafe9491e06136a47dc2dad29db87423ad5222b2e07760c4ba14aa4', 'resource': ''}

# Reading the file into a list
with open("sample.txt") as f:
    lineList = f.readlines()

# Used to check if any vendor had a result
detected = False;

# Iterate through resources
for i in lineList:
    url = 'https://www.virustotal.com/vtapi/v2/file/report'

    # Check if URL or Hash
    for j in i:
        if j == '.':
            url = 'https://www.virustotal.com/vtapi/v2/url/report'

    params['resource'] = i

    # Requests data from VirusTotal API
    response = requests.get(url, params=params)
    # Error code 204 indicates too many requests in a given time
    while (response.status_code == 204):
        time.sleep(10)
        response = requests.get(url, params=params)

    # response.json() gets response data in the form of a dictionary
    # The 'scans' key contains the data we want
    errorDetails = response.json()["scans"]

    # Prints requested URL or Hash after removing new lines
    print(i.strip("\n"))

    # Goes through each vendor to check if URL or Hash has been marked malicious
    # Prints first result
    for j in errorDetails:
        if (errorDetails[j]['detected'] is True):
            print(j + ": " + errorDetails[j]["result"])
            detected = True
            break;

    # If no vendor detects malicious activity
    if (detected is False):
        print("No Results")
    detected = False;
    print("\n")
