import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализируем браузер
driver = webdriver.Firefox()

# В отдельной переменной указываем сайт, который будем просматривать
url = "https://www.divan.ru/category/svet"

# Открываем веб-страницу
driver.get(url)

time.sleep(10)

# Находим все карточки cо светильниками с помощью названия класса
# Названия классов берём с кода сайта
lamps = driver.find_elements(By.CLASS_NAME, '_Ud0k')

# Выводим вакансии на экран
print(lamps)
# Создаём список, в который потом всё будет сохраняться
parsed_data = []
if not lamps:
       print("Нет найденных светильников")
# Перебираем коллекцию светильников
# Используем конструкцию try-except, чтобы "ловить" ошибки, как только они появляются
for lamp in lamps:
   try:
   # Находим элементы внутри карточек по значению
   # Находим названия светильника
       title = lamp.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
       print(f"Title: {title}")
   # Находим цены
       price = lamp.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU').text
       print(f"Price: {price}")
     # Находим ссылку с помощью атрибута 'href'
       link = lamp.find_element(By.CSS_SELECTOR, 'link[itemprop="url"]').get_attribute('href')
       print(f"Link: {link}")
   # Вставляем блок except на случай ошибки - в случае ошибки программа попытается продолжать
   except:
      print("произошла ошибка при парсинге: {e}")
      continue

# Вносим найденную информацию в список
   parsed_data.append([title, price, link])

# Закрываем подключение браузер
driver.quit()

# Прописываем открытие нового файла, задаём ему название и форматирование
# 'w' означает режим доступа, мы разрешаем вносить данные в таблицу
with open("svet.csv", 'w', newline='', encoding='utf-8') as file:
# Используем модуль csv и настраиваем запись данных в виде таблицы
# Создаём объект
    writer = csv.writer(file)
# Создаём первый ряд
    writer.writerow(['Название светильника', 'Цена', 'Ссылка на светильник'])
# Прописываем использование списка как источника для рядов таблицы
    writer.writerows(parsed_data)