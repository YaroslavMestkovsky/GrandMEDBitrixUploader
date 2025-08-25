# регистрационный номер контракта
import requests

webhook_url = "https://crm.grandmed.ru/rest/27036/pnkrzq23s3h1r71c/"
method = "crm.contact.get"

# ID контакта
contact_id = 759  # из crm_deal_list.py
params = {
    "id": contact_id
}

response = requests.get(f"{webhook_url}{method}", params=params)

if response.status_code == 200:
    contact_info = response.json().get("result", {})
    reg_number = contact_info.get("UF_CRM_1744898975")
    if reg_number:
        print("Регистрационный номер:", reg_number)
    else:
        print("Регистрационный номер не найден.")
else:
    print("Ошибка при получении данных:", response.status_code, response.text)
