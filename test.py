import requests
import random


usernames = open("data/usernames.txt", encoding="cp437").read().splitlines()
random.choice(usernames) 

url = 'https://spogentify.vercel.app/api/v1'

params = {
    'name': f'{usernames}',
    'email': f'uuid{random.randint(10000,1000000000)}@hotmail.com',
    'password': '2i13kDK.-$'
}

response = requests.get(url, params=params)

print(response.text)