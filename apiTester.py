import requests

payload = {'files' : [
                'https://drive.google.com/uc?export=download&id=1TCE2xpYm9DYDUZDyOmsmYvDq3yFnuJdo',
                'https://drive.google.com/uc?export=download&id=1h4Vzy9QkU6hBSMxTrt7WwEiVJWUApnDv',
                'https://drive.google.com/uc?export=download&id=1G4W_I9aBiFbEF0hBarm2ayeMKY11b-mt',
                ],
            'token' : "this is token"}
r = requests.get('http://localhost:5000/inputFiles', params=payload)
print(r.content)
