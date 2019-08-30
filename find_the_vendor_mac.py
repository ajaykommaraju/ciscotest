import re
import requests
import datetime
import json
def macaddress(address):
    mac_address=str(address)
    full_url = 'https://api.macaddress.io/v1?apiKey=at_APyi89BT2MT71pFE27I5lFNRs2tFC&output=json&search='+mac_address
    result = requests.get(full_url)
    if result.status_code == 200:
        data = result.json()
        Vdetails=data['vendorDetails']
        CompanyName=Vdetails['companyName']
        print("The company name who owns this MAC Address is:", CompanyName)
macaddress(input("please enter the mac address you want to search:"))