# Google Drive Backup Script

This Python script allows you to back up a local folder to your Google Drive.

## Prerequisites

* **Python:** Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
* **Google Account:** You'll need a Google account with access to Google Drive.
* **Google Cloud Project:**  You need to create a Google Cloud Project and enable the Google Drive API.
* **OAuth 2.0 Credentials:** You need to set up OAuth 2.0 credentials to allow the script to access your Google Drive.
* **Required Libraries:** Install the necessary Python libraries using `pip`:
   ```bash
   pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

## Setup

* **Create a Google Cloud Project:**
    * Go to the [Google Cloud Console](https://console.cloud.google.com/).
    * Create a new project with a descriptive name (e.g., "Desktop-Backup-Project").

* **Enable the Google Drive API:**
    * In the Google Cloud Console, go to **APIs & Services > Library**.
    * Search for "Google Drive API" and click **Enable**.

* **Set Up OAuth 2.0 Credentials:**
    * In the Google Cloud Console, go to **APIs & Services > Credentials**.
    * Click **Create Credentials > OAuth client ID**.
    * Select **Desktop app** as the application type.
    * Download the `credentials.json` file. This file contains your client ID and secret.

* **Place `credentials.json`:**
    * Place the downloaded `credentials.json` file in the **same directory** as this script (`backup_script.py`).

## Usage

* **Update Script:**
    * Open `backup_script.py` in a text editor.
    * Replace `'D:\x'` with the **actual path** to the local folder you want to back up.
    * Replace `''` with the **ID** of the Google Drive folder where you want to store your backups. You can find the folder ID in the URL of the folder in your browser.

* **Run the Script:**
    * Open a terminal or command prompt.
    * Navigate to the directory where you saved `backup_script.py`.
    * Run the script using the command `python backup_script.py`.

* **Authorize Access:**
    * The first time you run the script, it will open a browser window asking you to authorize the script to access your Google Drive.
    * Sign in with your Google account and grant the requested permissions.

* **Backup Process:**
    * Once authorized, the script will start backing up the files from your local folder to your Google Drive.
    * The script will create a `token.json` file to store your refresh token, so you don't have to re-authorize every time.

## Important Notes

* **Keep `credentials.json` and `token.json` safe:** These files contain sensitive information. Treat them like passwords.
* **Error Handling:** The script does not include extensive error handling. You might want to add `try-except` blocks to handle potential errors (network issues, file access problems, etc.).
* **Large Files:** For very large files, consider using the resumable upload feature of the Google Drive API to handle interruptions.
* **Incremental Backups:** To save space and time, you could modify the script to perform incremental backups, where only files that have changed since the last backup are uploaded.
* **Scheduling:** You can use the Windows Task Scheduler or a similar tool to automate the execution of this script on a regular schedule.

* 
