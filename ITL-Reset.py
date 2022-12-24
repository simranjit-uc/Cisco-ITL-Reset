import requests
from requests.auth import HTTPBasicAuth
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning

cti_User = '< User ID '
cti_Pass = '< User password >'

def Keypad(num):
    return "XML=%3CCiscoIPPhoneExecute%3E%3CExecuteItem%20URL%3D%22Key%3AKeyPad" + num + "%22%2F%3E%3C%2FCiscoIPPhoneExecute%3E"

def Softkey(key):
    return "XML=%3CCiscoIPPhoneExecute%3E%3CExecuteItem%20URL%3D%22Key%3ASoft" + key + "%22%2F%3E%3C%2FCiscoIPPhoneExecute%3E"

def Settings():
    return "XML=%3CCiscoIPPhoneExecute%3E%3CExecuteItem%20URL%3D%22Key%3ASettings%22%2F%3E%3C%2FCiscoIPPhoneExecute%3E"

def Applications():
    return "XML=%3CCiscoIPPhoneExecute%3E%3CExecuteItem%20URL%3D%22Key%3AApplications%22%2F%3E%3C%2FCiscoIPPhoneExecute%3E"



def Connect(phone, payload):
    disable_warnings(InsecureRequestWarning)
    url = "http://" + phone + "/CGI/Execute"
    headers = {'Content-Type': "application/x-www-form-urlencoded"}
    try:
        response = requests.request("POST", url, auth=HTTPBasicAuth(cti_User, cti_Pass), data=payload, headers=headers)
    except:
        print("Couldn't execute the code. Please re-run the code")



def reset_ITL(phone):
    Connect(phone, Applications())
    Connect(phone, Keypad('5'))
    Connect(phone, Keypad('4'))
    Connect(phone, Keypad('4'))
    Connect(phone, Keypad('4'))
    Connect(phone, Softkey('2'))


def user_Input():
    ip = input("Enter the IP Address : ")
    reset_ITL(ip)



user_Input()
