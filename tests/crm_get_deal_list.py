# # список сделок
# import json
#
# import requests
# fields = {
#     'ID': None,
#     'TITLE': None,
#     'TYPE_ID': None,
#     'STAGE_ID': None,
#     'PROBABILITY': None,
#     'CURRENCY_ID': None,
#     'OPPORTUNITY': None,
#     'IS_MANUAL_OPPORTUNITY': None,
#     'TAX_VALUE': None,
#     'LEAD_ID': None,
#     'COMPANY_ID': None,
#     'CONTACT_ID': None,
#     'QUOTE_ID': None,
#     'BEGINDATE': None,
#     'CLOSEDATE': None,
#     'ASSIGNED_BY_ID': None,
#     'CREATED_BY_ID': None,
#     'MODIFY_BY_ID': None,
#     'DATE_CREATE': None,
#     'DATE_MODIFY': None,
#     'OPENED': None,
#     'CLOSED': None,
#     'COMMENTS': None,
#     'ADDITIONAL_INFO': None,
#     'LOCATION_ID': None,
#     'CATEGORY_ID': None,
#     'STAGE_SEMANTIC_ID': None,
#     'IS_NEW': None,
#     'IS_RECURRING': None,
#     'IS_RETURN_CUSTOMER': None,
#     'IS_REPEATED_APPROACH': None,
#     'SOURCE_ID': None,
#     'SOURCE_DESCRIPTION': None,
#     'ORIGINATOR_ID': None,
#     'ORIGIN_ID': None,
#     'MOVED_BY_ID': None,
#     'MOVED_TIME': None,
#     'LAST_ACTIVITY_TIME': None,
#     'UTM_SOURCE': None,
#     'UTM_MEDIUM': None,
#     'UTM_CAMPAIGN': None,
#     'UTM_CONTENT': None,
#     'UTM_TERM': None,
#     'PARENT_ID_145': None,
#     'PARENT_ID_146': None,
#     'PARENT_ID_154': None,
#     'PARENT_ID_176': None,
#     'PARENT_ID_182': None,
#     'PARENT_ID_1056': None,
#     'LAST_ACTIVITY_BY': None,
# }
# webhook_url = "https://crm.grandmed.ru/rest/27036/pnkrzq23s3h1r71c/"
# method = "crm.deal.list"
# _json = {
#     "filter": {"STAGE_ID": "C21:PREPARATION", "DATE_CREATE": "2025-01-21"},  # фильтр по стадии сделки
#     #"select": ["ID", "TITLE", "UF_CRM_1632131563786", "UF_CRM_1680855473", "DATE_CREATE"],  # обязательные поля
#     "order": {"DATE_CREATE": "ASC"},  # сортировка по дате создания
# }
# params = {
#     "start": 350,
# }
#
# HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}
# DATA = {
#     "FILTER": {"STAGE_ID": "C21:PREPARATION", "DATE_CREATE": "2021-01-21"},
#     "ORDER": {"DATE_CREATE": "ASC"},
# }
# response = requests.get(
#     f"{webhook_url}{method}",
#     headers={"Content-Type": "application/json", "Accept": "application/json"},
#     data=json.dumps(DATA),
# )
# response.raise_for_status()  # Проверка на HTTP ошибки (например, 404, 500)
# q = response.json()
#
# while True:
#     response = requests.get(f"{webhook_url}{method}", json=_json, params=params)
#
#     if response.status_code == 200:
#         deals = response.json().get("result", [])
#
#         _next = response.json().get("next")
#
#         print(_next)
#         params.update({"start": _next})
#
#         for deal in deals:
#             if all(fields.values()):
#                 break
#
#             for k, v in deal.items():
#                 if v is not None and fields[k] is None:
#                     fields[k] = v
#
#         if _next is None:
#             break
#
# print(fields)


import requests
import json
import datetime

# Замените на свои значения
webhook_url = "https://crmdp.grandmed.ru/rest/27036/pnkrzq23s3h1r71c/"
method = "crm.deal.list"

url = f"{webhook_url}{method}"

# Вычисляем дату за 6 месяцев до текущей
six_months_ago = datetime.datetime.now() - datetime.timedelta(days=1)  # Примерно 6 месяцев
date_string = six_months_ago.strftime("%Y-%m-%d")

# Формируем тело запроса
data = {
    "SELECT": [],
    "FILTER": {
        #"STAGE_ID": "C21:PREPARATION",
        "UF_CRM_1744898975": "123456",
    },
    "ORDER": {
        "TITLE": "ASC",
        "OPPORTUNITY": "ASC"
    },
    #"start": 150,
}

# Отправляем POST запрос
try:
    response = requests.post(
        url,
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        data=json.dumps(data),
    )
    response.raise_for_status()  # Проверка на HTTP ошибки (например, 404, 500)
    result = response.json()
    print(json.dumps(result, indent=4))  # Выводим результат в удобочитаемом формате

except requests.exceptions.RequestException as e:
    print(f"Произошла ошибка при выполнении запроса: {e}")
except json.JSONDecodeError:
    print("Ошибка декодирования JSON из ответа сервера.")
except Exception as e:
    print(f"Произошла неизвестная ошибка: {e}")
