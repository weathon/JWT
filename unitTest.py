import time
import json
import JWT
mark = "\033[92m✓\033[0m"

print("Testing For Normal Issueing 1")
jwt = json.dumps(JWT.issue(time.time()+10,"weathon"))
if JWT.getUserName(jwt) == "weathon":
    print(f'{mark} Passed!')

print("Testing For Normal Issueing 2")
jwt = json.dumps(JWT.issue(time.time()+15,"YWUE&*#RGYUTGXBIFGEFHNEUIF&*"*100))
if JWT.getUserName(jwt) == "YWUE&*#RGYUTGXBIFGEFHNEUIF&*"*100:
    print(f'{mark} Passed!')

print("Testing For Normal Issueing 3")
jwt = json.dumps(JWT.issue(time.time()+1,"Test"))
if JWT.getUserName(jwt) == "Test":
    print(f'{mark} Passed!')

print("Testing For Expired Issueing 1")
jwt = json.dumps(JWT.issue(time.time()-100,"weathon"))
try:
    JWT.getUserName(jwt)
    print("Failed!")
except JWT.ExpiredJWT: #err as not working 
    print(f'{mark} Passed!')

print("Testing For Expired Issueing 2")
jwt = json.dumps(JWT.issue(time.time()-50,"weathon"))
try:
    JWT.getUserName(jwt)
    print("Failed!")
except JWT.ExpiredJWT: #err as not working 
    print(f'{mark} Passed!')

print("Testing For Expired Issueing 3")
jwt = json.dumps(JWT.issue(time.time()-0,"weathon"))
try:
    JWT.getUserName(jwt)
    print("Failed!")
except JWT.ExpiredJWT: #err as not working 
    print(f'{mark} Passed!')



print("Testing For Forged JWT 1 - Changed signature")
jwt = JWT.issue(time.time()+100,"weathon")
jwt["signature"]+='1'
jwt = json.dumps(jwt)
try:
    JWT.getUserName(jwt)
    print("Failed!")
except JWT.ForgedJWT: #err as not working 
    print(f'{mark} Passed!')


print("Testing For Forged JWT 2 - Others signature")
jwt1 = JWT.issue(time.time()+100,"weathon")
jwt2 = JWT.issue(time.time()+100,"weathon")
jwt1["signature"] = jwt2["signature"]
jwt = json.dumps(jwt1)
try:
    JWT.getUserName(jwt)
    print("Failed!")
except JWT.ForgedJWT: #err as not working 
    print(f'{mark} Passed!')


print("Testing For Forged JWT 3 - Fake Key")
jwt = JWT.issue(time.time()+100,"weathon")
jwt = json.dumps(jwt)
JWT.key = "ifrne9c854n47n8cr4"
try:
    JWT.getUserName(jwt)
    print("Failed!")
except JWT.ForgedJWT: #err as not working 
    print(f'{mark} Passed!')


print("Testing For Forged JWT 4 - Fake secret")
jwt = JWT.issue(time.time()+100,"weathon")
jwt = json.dumps(jwt)
JWT.secret = "ceiouNX&#nt"
try:
    JWT.getUserName(jwt)
    print("Failed!")
except JWT.ForgedJWT: #err as not working 
    print(f'{mark} Passed!')

print("Testing For Forged JWT 5 - Time Changed Token")
jwt = JWT.issue(time.time(),"weathon")
jwt["exp_time"]=time.time()+5
jwt = json.dumps(jwt)
try:
    JWT.getUserName(jwt)
    print("Failed!")
except JWT.ForgedJWT: #err as not working 
    print(f'{mark} Passed!')
