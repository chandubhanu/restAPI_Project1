import requests

from utilities.configurations import getConfig
from utilities.resources import Apiresources

utl=getConfig()['GITHUBAPI']['endpoint']+Apiresources.github
r=requests.get(utl,verify=False,auth=('sa','sa'))
print(r.status_code)
#Day2