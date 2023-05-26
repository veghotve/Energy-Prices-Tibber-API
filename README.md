Energy Prices Tibber API Script
This script retrieves energy prices from the Tibber API and sends an email with the average prices for today and tomorrow, along with a table containing the prices for each hour.

Prerequisites
Before running the script, make sure you have the following installed:

Python 3.x
The following Python packages: requests, smtplib, pandas
Installation
To use this script, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/veghotve/Energy-Prices-Tibber-API.git
Install the required Python packages:

Copy code
pip install requests smtplib pandas
Set up the configuration file:

Create a file named config.py in the root directory.
Add the following lines to config.py:
python
Copy code
sender_email = "your_email@gmail.com"  # Replace with your email address
sender_password = "your_email_password"  # Replace with your email password
TIBBER_TOKEN = "your_tibber_api_token"  # Replace with your Tibber API token
recipient_email = "recipient_email@gmail.com"  # Replace with the recipient's email address
recipient_email1 = "recipient_email1@gmail.com"  # Add additional recipient email addresses if needed
Run the script:

Copy code
python energy_prices_script.py
Description
The script performs the following steps:

Imports the necessary modules and libraries:

requests: for making API requests
smtplib: for sending emails
time: for adding delays
email.mime.text and email.mime.multipart: for composing email messages
pandas: for creating and manipulating data frames
Sets up the API endpoint, authorization header, and GraphQL query for fetching energy prices from the Tibber API.

Initializes the average price variables.

Executes a loop to fetch the average prices for today and tomorrow:

Sends a GraphQL query to the Tibber API.
Parses the response and calculates the average price for today.
Calculates the average price for tomorrow if available. If not, waits for 1 minute before retrying.
Creates data frames for today's and tomorrow's prices using the Pandas library.

Generates an HTML email message with the average prices and the hourly prices for today and tomorrow.

Sets up the email message with the sender, recipient, subject, and HTML content.

Sends the email using Gmail's SMTP server.

Note: Make sure to replace the placeholder values in the config.py file with your actual email, API token, and recipient email addresses.

That's it! You can now run the script to retrieve energy prices from the Tibber API and receive an email with the price information.