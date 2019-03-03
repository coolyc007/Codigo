import requests

resp = requests.get('https://api.data.gov.in/resource/918744fa-09b7-49c9-b19c-64c2d9ebb6b5?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&offset=0&limit=10')
if resp.status_code != 200:
    # Something went wrong!
    raise ApiError('GET /tasks {}'.format(resp.status_code))
for todo_item in resp.json():
    print('{} {}'.format(todo_item['id'],todo_item['summary']))