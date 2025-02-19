import requests
import csv
from datetime import datetime
import os

API_KEY = "OPENWEATHER_API_KEY"
CITY = "Seoul"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()
temp = data["main"]["temp"]
humidity = data["main"]["humidity"]
description = data["weather"][0]["description"]
timezone = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(temp, humidity, description, timezone)

csv_filename = "seoul_weather.csv"
header = ["timezone", "temp", "humidity", "description"]


file_exist = os.path.isfile(csv_filename)

# mode = "a" -> if not is file -> create
# if is file -> write
with open(csv_filename, "a", newline="") as file:
    writer = csv.writer(file)

    # 파일 존재 x -> header 가 없다
    if not file_exist:
        writer.writerow(header)

    writer.writerow([timezone, temp, humidity, description])

    print("csv 저장 완료")
