import argparse
import json
import time

import requests
from requests.structures import CaseInsensitiveDict

# Initialize parser
parser = argparse.ArgumentParser()
# Adding optional argument
parser.add_argument("-f", "--file_path", help = "File path of the data input")

# Adding optional argument
parser.add_argument("-u", "--base_url", help = "Base url")

# Read arguments from command line
args = parser.parse_args()
base_url=args.base_url
#URL to initiate scan on BurpSuite-------------------------------------

headers = CaseInsensitiveDict()

with open (args.file_path,"r") as f:
    data = json.dumps(json.load(f))
resp = requests.post(base_url, headers=headers, data=data)
print("Status Code:-",resp.status_code)
print("location of the scan result",resp.headers['location'])

#Getting Data from JSON Body--------------------------------------------
check_status = True
location= resp.headers["location"]
check_url = base_url+"/"+location
while check_status:
    resp = requests.get(check_url)
    respJson = resp.json()
    print(respJson)
    scanstatus = respJson["scan_status"]
    print(scanstatus)
    if scanstatus in ["succeeded","failed"]  :
        check_url = False
        break
    else:
        time.sleep(5)
issue_events = respJson['issue_events']
print("no of issue: "+str(len(issue_events)))
for issue in issue_events:
    print("Vulnerability Name:"+issue['issue']['name']+",""Severity:"+issue['issue']['severity']+",""Origin:"+issue['issue']['origin']+",""Path:"+issue['issue']['path']+",""Confidence:"+issue['issue']['confidence'])
print(json.dumps(respJson, indent = 1))
