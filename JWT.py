import hmac
import hashlib
import base64
import json


key = "uweDW^TDT#DH#FJ" # FOR DEMO ONLY! MUST BE DIFFERENT FOR PRODUCTION!
secret  = "UIHWE&^X^&*$&#YHIOEJFIOEUF&*RYUH" # FOR DEMO ONLY! MUST BE DIFFERENT FOR PRODUCTION!

def issue(exp_time, username):
    body = {"username": username, "exp_time": exp_time}
    msg=username+"=="+str(exp_time)+secret
    # https://stackoverflow.com/questions/7585435/best-way-to-convert-string-to-bytes-in-python-3
    signature = hmac.new(key.encode('utf-8'), msg = msg.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()
    body["signature"] = signature
    return body
print(issue(1000,"test"))