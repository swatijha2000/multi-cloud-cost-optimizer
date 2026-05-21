import requests

def check_aws():
    try:
        res = requests.get("http://13.207.43.209:5000/")
        return res.status_code == 200
    except:
        return False

def check_azure():
    try:
        res = requests.get("http://20.193.251.136:5000/")
        return res.status_code == 200
    except:
        return False