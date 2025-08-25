# информация о конкретном контракте
import json

import requests

URL = "https://crm.grandmed.ru/rest/27036/pnkrzq23s3h1r71c/crm.contact.list"
HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}
SELECT = []
FILTER = {"@ID": [176636, 42341351251]}
ORDER = {"DATE_CREATE": "ASC"}

DATA = {'FILTER': {'@ID': [176636]}}
resp = requests.post(
    url=URL,
    headers=HEADERS,
    data=json.dumps(DATA),
)
print(resp.json())
#
#
# response = requests.get(f"{webhook_url}{method}", params=params)
#
# if response.status_code == 200:
#     contact_info = response.json().get("result", {})
#     print(contact_info)
# else:
#     print("Ошибка при получении данных:", response.status_code, response.text)
