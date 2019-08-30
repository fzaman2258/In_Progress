import requests
import time
import operator

# BASE URL for the API
url = 'https://www.virustotal.com/vtapi/v2/file/report'

# Contains User API Key and Hash that needs to be analyzed
params = {'apikey': '5495d7c47aafe9491e06136a47dc2dad29db87423ad5222b2e07760c4ba14aa4', 'resource': ''}

# Dictionary to hold all vendor hits
count = {'key': 0}

# Reading the file into a list
with open("hashes.txt") as f:
    lineList = f.readlines()

# Iterating through the provided hashes from file
for i in lineList:
    # Putting current hash in params dictionary
    params['resource'] = i
    # Using requests library and url and params to get results from VirusTotal API
    response = requests.get(url, params=params)
    # Error 204 indicates too many requests in a given period of time
    while (response.status_code == 204):
        time.sleep(10)
        response = requests.get(url, params=params)

    # response.json() gets the library form of the response
    # The 'scans' key holds the data that we are interested in
    errorDetails = response.json()["scans"]

    # For each vendor if the current has is detected then the number
    # of hits for that vendor is incremented by one
    for i in errorDetails:
        if (errorDetails[i]['detected'] is True):
            count[i] = count.get(i, 0) + 1

# Sorts vendor data by number of hits
sorted_d = sorted(count.items(), key=operator.itemgetter(1))

for i in lineList:
    params['resource'] = i
    response = requests.get(url, params=params)
    while (response.status_code == 204):
        time.sleep(10)
        response = requests.get(url, params=params)

    errorDetails = response.json()["scans"]
    counter = -1;  # Counter starting from vendor with most hits
    hasHit = False;  # Checks case where no vendors have hits
    checked = 0;

    print("HASH: " + i.strip("\n"))

    # Checks if McAfee has a result
    try:
        if (errorDetails['McAfee']['detected'] is True):
            print("McAfee Result: " + errorDetails["McAfee"]["result"])
            checked += 1;
        else:
            print("McAfee: No Results")
    except:
        print("McAfee unable to process hash")

    # Checks if PaloAlto has a result
    try:
        if (errorDetails['Paloalto']['detected'] is True):
            print("PaloAlto Result: " + errorDetails["Paloalto"]["result"])
            checked += 1;
        else:
            print("PaloAlto: No Results")
    except:
        print("Palo Alto unable to process hash")

    # If either McAfee or PaloAlto has no result
    if (checked != 2):
        # While we havent gone through every vendor
        while (sorted_d[counter][0] != 'key'):
            main_string = sorted_d[counter][0]
            # Check to see if vendor has a result
            try:
                if (errorDetails[main_string]['detected'] is True):
                    print(main_string + " Result: " + errorDetails[main_string]["result"])
                    hasHit = True
                    break;
                else:
                    counter -= 1;  # Next vendor with largest number of hits
            except:
                counter -= 1;

        # If no results from any vendor
        if (not hasHit):
            print("No Results")

    print("-------------------------------\n")
