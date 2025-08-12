import requests
import  json
from detected_gender import DetectedGender

print('#1')
r = requests.get("https://randomuser.me/api/")
print(r.status_code)
print(r.text)



print('#2')
try :
    r = requests.get("https://randomuser.me/api/1")
    data = json.loads(r.text)


    if r.status_code==200:
        print(data['results'][0]['gender'])

except:
    print('not response')


    print('#3')
try :
    r = requests.get("https://randomuser.me/api/")
    data = json.loads(r.text)
    print(data['results'][0]['name']['title'])
except :
    print('not response')

print('#4')
detector = DetectedGender()
print(detector.get_gender())




