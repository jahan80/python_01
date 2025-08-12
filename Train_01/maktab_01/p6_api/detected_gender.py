import requests

class DetectedGender:
    def get_gender(self):
        r = requests.get("https://randomuser.me/api/")
        if r.status_code == 200:
            return r.json()['results'][0]['gender']
        return None