import json

courses='{"name": "Bhanu Prakash","languages": ["java","python"]}'
#loads method parse json string and it returns dictionary

dict_courses=json.loads(courses)
print(type(dict_courses))
list_languages=dict_courses['languages'][0]
print(list_languages)