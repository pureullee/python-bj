import requests


url = "https://discord.com/api/webhooks/1107662458006540400/dGEKTqoVc5JS-twAP_uLuHAllUzHO-8JWVJPHa6sdgPiiETVTQ6lVD4RszHN-OH56Ve5"
headers = {
    'Content-Type' : 'application/json',
}
data = {
  "content": "메시지"
}
r = requests.post(url, json=data, headers=headers)
print(r.status_code)