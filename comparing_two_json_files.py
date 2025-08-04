import json

with open(r'C:\Users\cprakash\PycharmProjects\restAPI_Project1\TestData\students.json') as f:
    data_1=json.load(f)

with open(r'C:\Users\cprakash\PycharmProjects\restAPI_Project1\TestData\students_1.json') as fi:
    data_2=json.load(fi)

if data_2==data_1:
    assert True
else:
    assert False