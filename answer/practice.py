import json
import requests

a = {"repairtype": 1, "repairman": "周大福",
        "repairmantel": "13802738933", "projectid": "107",
        "projectname": "水街市场", "repairaddress": "水街市场水产批发",
        "repairreason": "水管漏水2",
        "repairPicList": [{"name": "2.png", "size": 32446,
                           "pictureurl": "https://files.scn.weilian.cn/d/f549303366d39a534a100c065bfa189a"}]}
b = json.dumps(a)
print(a)
print(b)