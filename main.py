import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

url = "https://www.divan.ru/category/svet"

driver.get(url)

time.sleep(3)

lamps = driver.find_elements(By.CLASS_NAME, '_Ud0k yxmWx U4KZV')

# Выводим карточки светильников на экран
print(lamps)
# Создаём список, в который потом всё будет сохраняться
parsed_data = []

# Перебираем карточки светильников
# Используем конструкцию try-except, чтобы "ловить" ошибки, как только они появляются
for lamp in lamps:
    try:
   # Находим элементы внутри карточек по значению
   # Находим названия светильников
        name = lamp.find_element(By.CSS_SELECTOR, 'span.lsooF').text
     # Находим цену
        price = lamp.find_element(By.CSS_SELECTOR, 'span.pY3d2').text

     # Находим ссылку с помощью атрибута 'href'
        link = lamp.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
   # Вставляем блок except на случай ошибки - в случае ошибки программа попытается продолжать
    except:
        print("Произошла ошибка при парсинге")
        continue

# Вносим найденную информацию в список
        parsed_data.append([name, price, link])

# Закрываем подключение браузера
driver.quit()

# Прописываем открытие нового файла, задаём ему название и форматирование
with open("lamps.csv", 'w',newline='', encoding='utf-8') as file:
    # Используем модуль csv и настраиваем запись данных в виде таблицы
    # Создаём объект
    writer = csv.writer(file)
# Создаём первый ряд
    writer.writerow(['Название светильника', ' Цена светильника', ' Ссылка на карточку'])

# Прописываем использование списка как источника для рядов таблицы
    writer.writerows(parsed_data)