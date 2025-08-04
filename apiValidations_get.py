import json

import requests

response=requests.get("http://216.10.245.166/Library/GetBook.php",params={"AuthorName":"Rahul Shetty"},)
# print(type(response.text))
# print(response.text)
# response_data=response.text
# list_res=json.loads(response_data)
# for res in list_res:
#     if res['book_name']=='Devops':
#          print(res["isbn"])
json_response=response.json()
print(type(json_response))
# print(json_response[0]['book_name'])
res_code=response.status_code
print(res_code)
assert res_code==200
print(response.headers)
print(response.cookies)
assert response.headers['Content-Type']=='application/json;charset=UTF-8'

#retrieve the book details with ISBN RGHCC
for actual_book in json_response:
    if actual_book['isbn']=="RSS575":
        print(actual_book)
        break
expected_book={"book_name": "Learn Appium Automation with Java",
        "isbn": "RSS575",
        "aisle": "228"
               }
assert actual_book==expected_book