# Burp Suite REST API

This script is utilised to communicate with the Burp Rest API. For these scripts to function, the Burp REST API must be enabled. Go to User Options->Misc->REST API to enable the API. The scripts will automatically use the address 127.0.0.1:1337 as their default address. Using command-line options, you can modify the location.  It does an active scan on a single host, a list of hosts in a file, or a range of hosts using the Burp REST API.

![](images\Rest_API.png)
![](images\Rest_API_Config.png)

# Usage :

Works with Python 3. This script Requires the Requests module. By default, the Burp REST API host is set to 127.0.0.1:1337 and the API is set to ''. If you specify a range, the tool will generate an IP range and run each address through a function that creates multiple URLs that attempts connections on multiple web ports. When providing URLs, the format should be http(s)://addr:port. If you don't provide URLs like this, that's okay, the tool will transform your URL to match that format.

In order to run this you woul require to install requirments:-

---

## pip install -r requirements.txt

Do an active scan
python3 main.py -u url of the burpsuite api -f filepath of the data.json

---

---

## python3 main.py -u http://127.0.0.1:1337/v0.1/scan -f /Users/mafiaguy/Desktop/data.json
