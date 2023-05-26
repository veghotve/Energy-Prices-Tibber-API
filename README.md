# Energy Prices Tibber API

This script fetches energy prices from the Tibber API and sends an email containing the average prices for today and tomorrow, as well as a table with detailed prices for each hour. The script uses Python and requires a few dependencies to be installed.

## Installation

To use this script, you need to have the following installed:

- Python (version 3.6 or higher)
- The `requests` library
- The `smtplib` library
- The `pandas` library

You can install these dependencies using `pip`. Open your terminal or command prompt and run the following command:

```
pip install requests smtplib pandas
```

## Usage

1. Clone the repository to your local machine or download the script file.

2. Open the script file in a text editor.

3. Provide your API credentials and email details:

   - Replace `TIBBER_TOKEN` with your Tibber API token.
   - Replace `sender_email` with your Gmail email address.
   - Replace `sender_password` with your Gmail password or an [app password](https://support.google.com/accounts/answer/185833?hl=en) if you have two-factor authentication enabled.
   - Replace `recipient_email` with the email address where you want to receive the energy price notification.
   - (Optional) Add additional recipient email addresses in the `recipient_email1` variable.

4. Save the changes to the script file.

5. Open a terminal or command prompt and navigate to the directory where the script is located.

6. Run the script by executing the following command:

   ```
   python script_name.py
   ```

   Replace `script_name.py` with the actual name of the script file.

7. The script will fetch the energy prices and send an email containing the average prices for today and tomorrow, as well as a table with detailed prices for each hour.

8. You will receive the email at the specified recipient email address(es).

Note: Make sure to keep your API token and email credentials secure and avoid committing them to a public repository.

## Additional Information

For more information about the Tibber API and how to obtain an API token, refer to the [Tibber API documentation](https://developer.tibber.com/docs/overview).

If you encounter any issues or have questions, feel free to contact the script author: veghotve.

Happy monitoring of energy prices with Tibber API!
