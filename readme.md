# BurpSuite API
This is a script used to interact with the Burp Rest API. You must enable the Burp API for these scripts to work. To enable the API, go to User Options -> Misc -> REST API. The default address is 127.0.0.1:1337, and the scripts will default to that address. You can change the location with commandline options. You can choose to require an API key; the scripts will work either way. 
Uses the Burp API to do an active scan on a single host, a file listing hosts, or a range of hosts.

Usage
Works with Python 3. This script Requires the Requests module. By default, the Burp API host is set to 127.0.0.1:1337 and the API is set to ''. If you specify a range, the tool will generate an IP range and run each address through a function that creates multiple URLs that attempts connections on multiple web ports. When providing URLs, the format should be http(s)://addr:port. If you don't provide URLs like this, that's okay, the tool will transform your URL to match that format. 

Inorder to run this you woul require to install requirments:-
------------
pip install -r requirements.txt
------------
Do an active scan
python3 main.py -u url of the burpsuite api -f filepath of the data.json
------------ 
--------
python3 main.py -u http://127.0.0.1:1337/v0.1/scan -f /Users/mafiaguy/Desktop/data.json
--------
