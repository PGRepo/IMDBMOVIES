import request


headers = {}
headers['Authorization'] = 'Bearer '

r = request.get('http://127.0.0.1:8000/movie', headers=headers)

print(r.text)
