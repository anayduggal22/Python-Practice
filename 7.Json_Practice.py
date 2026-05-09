import requests

r = requests.get("https://jsonplaceholder.typicode.com/users")

print(r.text)
user = r.json() #Dictionary Now

print(f"Number of users: {len(user)}")

for i in user:
    print(f"All user name {i['id']} -> {i['name']}")