#Price of RPA

import json


with open(r'C:\Users\cprakash\PycharmProjects\restAPI_Project1\TestData\students.json') as f:
    dict_1=json.load(f)
    list_courses=dict_1['courses']
    print(list_courses)
    for i in  list_courses:
        if i['title'] == "Cypress":
            print(i['price'])
            assert i['price']==40
            break