import requests

# for class CBV 
BASE_URL='http://127.0.0.1:8000/'
END_URL='Json_CBV/'
# resp=requests.get(BASE_URL+END_URL)
# resp=requests.post(BASE_URL+END_URL)
# resp=requests.put(BASE_URL+END_URL)
# resp=requests.patch(BASE_URL+END_URL)
resp=requests.delete(BASE_URL+END_URL)
print(resp.json())
print(resp.status_code)

# for employee methods
'''
BASE_URL='http://127.0.0.1:8000/'
END_URL='Json_CBV'
resp=requests.get(BASE_URL+END_URL)
print(resp.json())
print(resp.status_code)

data=resp.json()
print("Data from django application ")
print("*"*30)
print("Employee number      ",data['eno'])
print("Employee name        ",data['ename'])
print("Employee salary      ",data['esal'])
print("Employee address     ",data['eaddr'])
'''