import hmac
import hashlib
import base64
import json
import time

key = "uweDW^TDT#DH#FJ" # FOR DEMO ONLY! MUST BE DIFFERENT FOR PRODUCTION!
secret  = "UIHWE&^X^&*$&#YHIOEJFIOEUF&*RYUH" # FOR DEMO ONLY! MUST BE DIFFERENT FOR PRODUCTION!

def issue(exp_time, username):
    JWT = {"username": username, "exp_time": exp_time}
    msg=username+"=="+str(exp_time)+secret
    # https://stackoverflow.com/questions/7585435/best-way-to-convert-string-to-bytes-in-python-3
    signature = hmac.new(key.encode('utf-8'), msg = msg.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()
    JWT["signature"] = signature
    return JWT



def getUserName(JWT: str): #validate vs verify vs check
    """
    Check if the JWT is valid and if yes return the username. 
    If the JWT is expired, exception ExpiredJWT will be raised.
    If the JWT is forged, exception ForgedJWT will be raised
    """
    JWT = json.loads(JWT)
    if time.time()>JWT["exp_time"]:
        raise Exception("ExpiredJWT")
    msg=JWT["username"]+"=="+JWT["exp_time"]+secret
    signature = hmac.new(key.encode('utf-8'), msg = msg.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()
    if signature != JWT["signature"]:
        raise Exception("ForgedJWT")
    return JWT["username"]
    