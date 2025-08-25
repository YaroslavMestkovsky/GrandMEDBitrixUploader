# информация о конкретной сделке (вроде не нужно)
import requests

webhook_url = "https://crm.grandmed.ru/rest/27036/pnkrzq23s3h1r71c/"
method = "crm.deal.get"

# ID сделки
deal_id = 295543  # Не ясно, откуда брать

params = {
    "id": deal_id
}

response = requests.get(f"{webhook_url}{method}", params=params)

if response.status_code == 200:
    deal_info = response.json().get("result", {})
    print(deal_info)
else:
    print("Ошибка при получении данных:", response.status_code, response.text)
