#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = Options()
chrome_options.add_argument("--headless")

service = Service('/usr/bin/chromedriver')
service.start()

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://ru.investing.com/economic-calendar/")
time.sleep(5)

current_time = time.strftime("%H:%M", time.localtime())
print(f"Current time: {current_time}")

news = []
for row in driver.find_elements(By.XPATH, '//tr[contains(@class, "js-event-item")]'):
    time_el = row.find_element(By.CSS_SELECTOR, ".time.js-time")
    if f"через" in time_el.get_attribute("title"):
        continue  # skip news that will be released later than 15 minutes
    if "bull3" not in row.get_attribute("innerHTML"):
        continue  # skip news without the 'bull3' indicator
    
    release_time = time_el.text
    news.append(f"{release_time} - Выход новостей")

# clear existing content in the file
open('/home/ordanax/.config/polybar/scripts/news.txt', 'w').close()

# write news to file
with open('/home/ordanax/.config/polybar/scripts/news.txt', 'a') as file:
    file.write("\n".join(news) + "\n")

driver.quit()




file_path = "/home/ordanax/.config/polybar/scripts/news.txt"
time_diff = datetime.timedelta(minutes=30)

# Читаем содержимое файла
with open(file_path, "r") as f:
    lines = f.readlines()

# Перебираем строки и удаляем те, время которых прошло более 30 минут
new_lines = []
for line in lines:
    # Разбиваем строку на время и текст
    if " - " not in line:
        continue
    time_str, text = line.split(" - ", maxsplit=1)
    # Преобразуем строку времени в объект datetime.time()
    time = datetime.datetime.strptime(time_str, "%H:%M").time()
    # Вычисляем разницу между текущим временем и временем из строки
    now = datetime.datetime.now().time()
    time_diff = datetime.datetime.combine(datetime.date.today(), now) - datetime.datetime.combine(datetime.date.today(), time)
    # Если разница больше 30 минут, то не добавляем строку в новый список
    if time_diff.total_seconds() <= 30*60:
        new_lines.append(line)

# Записываем обновленный список строк в файл
with open(file_path, "w") as f:
    f.writelines(new_lines)