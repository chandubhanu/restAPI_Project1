import json

#************* Parse content present in Json File*************

with open(r'C:\Users\cprakash\PycharmProjects\restAPI_Project1\TestData\students.json') as f:
    data=json.load(f)#dictionary
    dict_1=data['dashboard']
    print(dict_1['website'])
    list_courses=data['courses'][1]
    dict_2=list_courses['title']
    print(dict_2)