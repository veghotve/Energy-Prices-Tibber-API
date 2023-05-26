import requests
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
from config import sender_email, sender_password, TIBBER_TOKEN, recipient_email, recipient_email1

# Set up the API endpoint and authorization header
url = "https://api.tibber.com/v1-beta/gql"
headers = {
    "Authorization": f"Bearer {TIBBER_TOKEN}",
    "Content-Type": "application/json",
}

# Set up the GraphQL query to fetch energy prices
query = """
{
    viewer {
        homes {
            currentSubscription {
                priceInfo {
                    today {
                        total
                        startsAt
                    }
                    tomorrow {
                        total
                        startsAt
                    }
                }
            }
        }
    }
}
"""

# Set the initial values for the average prices
today_avg_price = None
tomorrow_avg_price = None

while tomorrow_avg_price is None:
    # Send the GraphQL query and parse the response
    response = requests.post(url, headers=headers, json={"query": query})

    if response.status_code != 200:
        print(f"Error: {response.content}")
    else:
        data = response.json()["data"]
        # Calculate the average price for today
        today_prices = data["viewer"]["homes"][0]["currentSubscription"]["priceInfo"]["today"]
        today_avg_price = sum(price["total"] for price in today_prices) / len(today_prices)
        
        # Calculate the average price for tomorrow if prices are available
        tomorrow_prices = data["viewer"]["homes"][0]["currentSubscription"]["priceInfo"]["tomorrow"]
        if tomorrow_prices:
            tomorrow_avg_price = sum(price["total"] for price in tomorrow_prices) / len(tomorrow_prices)
        else:
            print("Prices for tomorrow not available. Retrying in 1 minute...")
            time.sleep(60)  # Wait for 1 minute before retrying

# Create a Pandas DataFrame with the prices for today and tomorrow
today_prices_df = pd.DataFrame(today_prices)
today_prices_df["Date"] = pd.to_datetime(today_prices_df["startsAt"]).dt.strftime("%d.%m.%y %H:%M")
today_prices_df.drop("startsAt", axis=1, inplace=True)

tomorrow_prices_df = pd.DataFrame(tomorrow_prices)
tomorrow_prices_df["Date"] = pd.to_datetime(tomorrow_prices_df["startsAt"]).dt.strftime("%d.%m.%y %H:%M")
tomorrow_prices_df.drop("startsAt", axis=1, inplace=True)

# Create the email message with the average price and the prices for today and tomorrow
html = f"""
    <html>
        <body>
            <h2>Tibber Energy Prices</h2>
            <p>Average price for today ({today_prices_df.iloc[0]['Date'].split()[0]}): {today_avg_price:.2f} kr/kWh</p>
            <p>Average price for tomorrow ({tomorrow_prices_df.iloc[0]['Date'].split()[0]}): {tomorrow_avg_price:.2f} kr/kWh</p>
            <br>
            <table border="1">
                <thead>
                    <tr>
                        <th>Time</th>
                        <th>Today ({today_prices_df.iloc[0]['Date'].split()[0]})</th>
                        <th>Tomorrow ({tomorrow_prices_df.iloc[0]['Date'].split()[0]})</th>
                    </tr>
                </thead>
                <tbody>
"""

for i in range(len(today_prices_df)):
    html += f"""
        <tr>
            <td>{today_prices_df.iloc[i]['Date'].split()[1]}</td>
            <td>{today_prices_df.iloc[i]['total']:.2f} kr/kWh</td>
            <td>{tomorrow_prices_df.iloc[i]['total']:.2f} kr/kWh</td>
        </tr>
    """

html += """
                </tbody>
            </table>
        </body>
    </html>
"""

message = MIMEMultipart()
message["Subject"] = "Tibber Energy Prices"
message["From"] = sender_email
message["To"] = recipient_email
message.attach(MIMEText(html, "html"))

# Send the email using Gmail's SMTP server
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, [recipient_email, recipient_email1], message.as_string())
