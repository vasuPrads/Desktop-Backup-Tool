import os
import shutil
import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaFileUpload  # Add this import

# Google Drive API setup (replace with your own credentials)
SCOPES = ['https://www.googleapis.com/auth/drive']
creds = None

# ... (Code to handle OAuth2 authentication - see step 4) ...

def backup_files(source_folder, destination_folder_id):
    """
    Backs up files from the source folder to the specified Google Drive folder.

    Args:
        source_folder: The path to the local folder you want to back up.
        destination_folder_id: The ID of the Google Drive folder to store backups.
    """
    service = build('drive', 'v3', credentials=creds)

    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)

            # Create a file metadata object
            file_metadata = {
                'name': filename,
                'parents': [destination_folder_id]  # Set the destination folder
            }
            media = MediaFileUpload(file_path)

            # Upload the file
            file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            print(f'File ID: {file.get("id")} ({filename})')

if __name__ == '__main__':
    source_folder = 'D:\x'  # Replace with your source folder
    destination_folder_id = ''  # Replace with your Drive folder ID

    # OAuth2 authentication flow
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    backup_files(source_folder, destination_folder_id)