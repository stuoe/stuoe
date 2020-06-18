import requests

a = requests.post('http://127.0.0.1:31/api/register',data={'register_email':'snbckcode@gmail.com','register_password':'123d1'})
print(a.text)