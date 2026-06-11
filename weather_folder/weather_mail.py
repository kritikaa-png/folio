import requests
import smtplib
import os
from email.mime.text import MIMEText
# GitHub Secrets
API_KEY = os.environ["API_KEY"]
EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]

CITY = "Thiruvananthapuram"

# Get weather data
url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"

response = requests.get(url)
data = response.json()

temp = data["current"]["temp_c"]
condition = data["current"]["condition"]["text"]
humidity = data["current"]["humidity"]
wind = data["current"]["wind_kph"]
print(f"Temperature: {temp}°C")
print(f"Condition: {condition}")
print(f"Humidity: {humidity}%")
print(f"Wind Speed: {wind} kph")
if temp>35 or "rain" in condition.lower():
    html = f"""
    <html>
    <body>
        <h2>🌤 Daily Weather Report</h2>
        <p><b>City:</b> {CITY}</p>
        <p><b>Temperature:</b> {temp}°C</p>
        <p><b>Condition:</b> {condition}</p>
        <p><b>Humidity:</b> {humidity}%</p>
        <p><b>Wind Speed:</b> {wind} kph</p>
        <hr>
        <p>
            Alert triggered because:
            {"Temperature exceeded 35°C" if temp > 35 else "Rain detected"}
        </p>

        <p>Generated automatically using Python & GitHub Actions.</p>
    </body>
    </html>
    """

    msg = MIMEText(html, "html")
    msg["Subject"] = f"Weather Report - {CITY}"
    msg["From"] = EMAIL
    msg["To"] = EMAIL
# Send email
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.sendmail(
        EMAIL,
        EMAIL,
        msg.as_string()
)
    server.quit()
    print("Alert email sent successfully!")
else: 
    print("No alert triggered.")