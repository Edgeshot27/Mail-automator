# Gmail Automation Project

This project is designed to interact with Gmail using the Gmail API. It includes functionalities to:
1. Fetch up to 100,000 emails (from Inbox or Spam).
2. Move emails out of the Spam folder programmatically.
3. Send personalized emails.
4. Auto-reply to specific emails (e.g., emails containing "hello").
5. Maintain a database of replied emails to avoid duplicate replies.

---

## Project Structure

Here's the structure of the files included in this project:

- **`main.py`**: Handles authentication with the Gmail API using `credentials.json`.
- **`fetch.py`**: Fetches emails from the Inbox.
- **`sending.py`**: Sends emails with customization.
- **`fetch_spam.py`**: Fetches emails from Spam and moves them to the Inbox.
- **`auto_reply.py`**: Automatically replies to unread emails based on content.

---

## Setup Instructions

### Step 1: Enable the Gmail API
To interact with Gmail, you'll need to enable the Gmail API for your account and generate the `credentials.json` file.

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Navigate to **APIs & Services** > **Library**.
4. Search for "Gmail API" and enable it.
5. Go to **APIs & Services** > **Credentials**.
6. Click **Create Credentials** > **OAuth Client ID** and follow these steps:
   - Configure the consent screen – select "External" (if applicable) and fill out the required details.
   - Under "Application type," select **Desktop app**.
7. Download the `credentials.json` file and save it in the root directory of your project.

---

### Step 2: Install Dependencies

This project requires Python 3.10 or above. Install the required libraries using `pip`.

Run the following command:
```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

---

### Step 3: Authenticate with Gmail

The first time you run the project, you'll need to authenticate with your Gmail account. The application will prompt you to log in via a browser and grant permissions.

It will store your access and refresh tokens in a `token.json` file so you don't need to log in again for future script executions.

---

## How to Run the Project

Below are the features and instructions to run each part of the project.

### 1. Fetch Emails (Inbox)

To fetch up to 100,000 emails from your Inbox:
```bash
python fetch.py
```

### 2. Fetch and Move Emails from Spam to Inbox

To fetch emails from the Spam folder and move them to the Inbox:
```bash
python fetch_spam.py
```

### 3. Send Emails

To send personalized emails:
```bash
python sending.py
```

You can specify the recipient, subject, and body of the email in the script.

### 4. Auto-Reply to Emails

To auto-reply to unread emails containing specific keywords (like "hello"):
```bash
python auto_reply.py
```

The script keeps track of replied emails to avoid sending multiple replies to the same sender by storing a record in a local file (`replied_emails.pickle`).

---

## Key Points

1. **Authentication**: The `main.py` file handles authentication with the Gmail API. This script generates `token.json` after the initial login, which is used for subsequent API requests.
2. **Error Handling**: If there are API failures (errors in email fetching or sending), the system gracefully handles and logs those errors.

---

## Step 4: API Quotas

Your Gmail account has the following default quotas when using the Gmail API:
- **Daily sending limit**: 500 emails/day (for standard Gmail accounts).
- **API requests limit**: 250,000 requests/day.

Ensure your project stays within these limits.

---

## Future Enhancements

Consider adding the following improvements:
- A GUI or CLI menu system to select tasks dynamically.
- Advanced filters (e.g., only fetching unread emails or emails with specific labels).
- Support for archiving, deleting, or labeling emails programmatically.

---

Let me know if you need further adjustments or have additional requirements! 😊