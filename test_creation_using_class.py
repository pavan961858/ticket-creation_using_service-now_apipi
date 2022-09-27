import requests
import json
class Tour:
    api_url="https://dev107069.service-now.com/api/now/table/incident"
    headers={"accept": "application/json","content-type": "application/json"}
    plan={"description": "permission",
    "short_description": "i want to go to paris"}
    def __init__(self,identity,passcode):
        self.identity=identity
        self.passcode=passcode
    def arrangement(self):
        visit=requests.post(self.api_url,auth=(self.identity,self.passcode),
        headers=self.headers,data=json.dumps(plan))
        print(visit.json())
happy=Tour("admin","cn20*DHkvVR/")
happy.arrangement()