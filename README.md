# Random Quote Email Sender

## Overview

The Random Quote Email Sender is a Python script designed to bring a touch of inspiration to your inbox by sending a daily random quote via email. It leverages the power of Python, the `smtplib` library for email sending, and a CSV file containing a curated list of quotes.

## Prerequisites

Before diving into the world of daily inspiration, ensure that your environment is set up properly:

- **Python Installation:** The script requires Python, preferably version 3.x. If you don't have Python installed, you can download it from the [official Python website](https://www.python.org/downloads/).

- **CSV File with Quotes:** The heart of the project lies in a CSV file named `quotes.csv`, which should contain a list of quotes, each on a separate line under the "Quote" column.

- **SMTP Server Access:** To send emails, you need access to an SMTP server. For simplicity, the script is configured to work with Gmail. Ensure that you have your sender email address and an application-specific password ready.

## Setup

Let's get everything up and running:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/random-quote-email-sender.git
    cd random-quote-email-sender
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Now that you're set up, it's time to experience daily inspiration. Run the script with the following command:

```bash
python script.py sender_email app_password receiver_email
```

Replace sender_email, app_password, and receiver_email with your actual email details.

### Example

To illustrate, here's an example command:
```
python script.py your_email@gmail.com your_app_password recipient@example.com
```

## Features

#### Email Validation
The script ensures that both the sender's and receiver's email addresses are valid before attempting to send the email. This helps prevent errors and ensures a smooth experience.

#### Random Quote Selection
With over 1665 quotes at its disposal, the script randomly selects a quote from the CSV file for each email, providing a fresh and unique message every time.

#### Seamless Email Sending
The script utilizes the smtplib library to handle email sending seamlessly. It connects to the SMTP server, logs in using the provided credentials, and dispatches the chosen random quote to the recipient.

## Additional Notes

#### Security Considerations: 
If you're using Gmail, consider enabling "Less secure app access" for the sender's email account. Additionally, generating an application-specific password is recommended for enhanced security.

## License

This project is licensed under the MIT License.