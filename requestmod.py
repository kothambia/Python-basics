# import requests
import requests 
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r = requests.get(url)
# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"):
  print(heading.text)

# # r = requests.get(url="https://discord.com")
# # print(r.text)


# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": "aryan",
#     "body": "bhakkam",
#     "userId": 69
# }

# headers = {
#     "Content-Type": "application/json; charset=UTF-8"
# }

# r = requests.post(url, headers=headers, json=data)

# print(r.status_code)   # should be 201
# print(r.json())        # print response data
