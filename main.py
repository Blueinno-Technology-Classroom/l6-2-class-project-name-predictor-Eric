import requests

name = input('What is your name?')


response = requests.get(f'https://api.agify.io?name={name}')
body = response.json()
age = body['age']

response = requests.get(f'https://api.genderize.io?name={name}')
body = response.json()
gender = body['gender']

response = requests.get(f'https://api.nationalize.io?name={name}')
body = response.json()
country = body['country'][0]['country_id']


print(f'You are probably a {age} years old {gender} from {country}')
