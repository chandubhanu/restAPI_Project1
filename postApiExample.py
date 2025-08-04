import json
import requests
import configparser

from payload import addBookPayload
from utilities.configurations import getConfig
from utilities.resources import Apiresources

##adding

url=getConfig()['API']['endpoint']+Apiresources.addBook
header={"Content-Type":"application/json"}
response=requests.post(url,json=addBookPayload("isbn","444"),
              headers=header,)
print(response.status_code)
print(response.json())
book_id=response['ID']
##deleting
url_1=getConfig()['API']['endpoint']+Apiresources.deleteBook
del_res=requests.post(url_1,json={"ID":"RS49269"})
print(del_res.json())