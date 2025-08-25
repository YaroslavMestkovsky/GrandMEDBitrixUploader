import requests
webhook_url = "https://crmdp.grandmed.ru/rest/27036/pnkrzq23s3h1r71c/"

method = "crm.deal.add"


q = {
'Рег.номер': "UF_CRM_1744898975",
'Фамилия': "UF_CRM_64B7A1FD1D5BB",
'Имя': "UF_CRM_NAME",
'Отчество': "UF_CRM_64B7A1FEF374B",
'ДР': "UF_CRM_1671203152488",
'Телефон': "UF_CRM_66582450DADD8",
'Электронная почта': "UF_CRM_1744898823",
#'Дата создания': ,
}

# Поля сделки
fields = {
    "CATEGORY_ID": 63,
    "STATUS_ID": "NEW",
    "UF_CRM_64B7A1FD1D5BB": "Иванов", # Фамилия
    "UF_CRM_NAME": "Иван", # Имя
    "UF_CRM_64B7A1FEF374B": "Иванович", # Отчество
    "UF_CRM_66582450DADD8": "+79991234567", # Телефон
    "UF_CRM_1744898823": "ivanov@example.com", # Почта
    "UF_CRM_1744898975": "123456", # Рег. номер
    "UF_CRM_1669636928319": "Мужской", # Пол
    "UF_CRM_1671203152488": "1990-01-01" # Дата рождения
}

response = requests.post(f"{webhook_url}{method}", json={"fields": fields})

if response.status_code == 200:
    result = response.json()
    if "result" in result:
        print("Сделка успешно создана. ID сделки:", result["result"])
    else:
        print("Ошибка при создании сделки:", result.get("error", "Неизвестная ошибка"))
else:
    print("Ошибка при отправке запроса:", response.status_code, response.text)

# Выгрузка сделок.
# 1. У нас есть пациент из qMS с reg-номером.
# 2. Мы проверяем что такого рег-номера уже нет в битриксе.

# 3. Если такого пациента нет - ищем его по алгоритму. #todo его мы не знаем

# 4. Если мы нашли его - обновляем.
# 5. Если мы его не нашли - создаем.



