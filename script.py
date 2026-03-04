import requests
from datetime import datetime
from zoneinfo import ZoneInfo  
url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=21.01&current_weather=true"

response = requests.get(url)
data = response.json()

temp = data["current_weather"]["temperature"]

# Get current time in Warsaw (CET/CEST automatically handled)
warsaw_time = datetime.now(ZoneInfo("Europe/Warsaw")).strftime("%Y-%m-%d %H:%M:%S")

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Weather Dashboard</title>
</head>
<body>
    <h1>Weather in Warsaw</h1>
    <p>Temperature: {temp}°C</p>
    <p>Last updated: {warsaw_time} (CET/CEST)</p>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("HTML file generated successfully with Warsaw local time.")
