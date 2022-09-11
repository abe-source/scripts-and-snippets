import requests

url = 'https://target.com.com/img/logo.png'
r = requests.get(url, allow_redirects=True)
open('logo.png', 'wb').write(r.content)