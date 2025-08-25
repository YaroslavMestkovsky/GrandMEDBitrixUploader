# ID контакта из сделки
import requests

webhook_url = "https://crm.grandmed.ru/rest/27036/pnkrzq23s3h1r71c/"
method = "crm.deal.get"

# ID сделки
deal_id = 1000  # Не ясно, откуда брать
params = {
    "id": deal_id
}

response = requests.get(f"{webhook_url}{method}", params=params)

if response.status_code == 200:
    deal_info = response.json().get("result", {})
    contact_id = deal_info.get("CONTACT_ID")
    if contact_id:
        print("ID контакта:", contact_id)
    else:
        print("Контакт не найден.")
else:
    print("Ошибка при получении данных:", response.status_code, response.text)
