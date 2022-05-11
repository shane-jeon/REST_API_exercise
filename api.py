import requests
import json

response = requests.get(
    'http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

# # receive response num
# print(response)

# # gets all data 
# print(response.json())

# # index for key
# print(response.json()['items'])

# to iterate through data, consume API
for question in response.json()['items']:
    # print(question)
    if question['answer_count'] == 0:
        print(question['title'])
        print(question['link'])
    else:
        print("skipped")
    print()