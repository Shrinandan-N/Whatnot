import os
from dotenv import load_dotenv
import instaloader
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
import gspread
from seller import Seller


class Scraper:
    loader = None
    follower_threshold = 10000
    RANGE = 'C2:C501'

    def __init__(self, phantom_sheet_url):
        self.scope = ['https://spreadsheets.google.com/feeds',
                      'https://www.googleapis.com/auth/drive']
        load_dotenv()
        file_path = os.environ["JSON_FILE_PATH"]
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(
            file_path, self.scope)
        self.client = gspread.authorize(self.creds)
        self.account_rd = phantom_sheet_url
        self.service = build('sheets', 'v4', credentials=self.creds)

    def get_followers(self, loader, username):
        profile = instaloader.Profile.from_username(
            loader.context, username)
        return profile.followers

    def get_profiles(self):
        profile_url_range = self.RANGE
        result = self.service.spreadsheets().values().get(
            spreadsheetId=self.account_rd, range=profile_url_range).execute()
        urls = result.get('values', [])
        usernames = self.remove_duplicates(urls)
        return usernames

    def remove_duplicates(self, urls):
        usernames = []
        for url in urls:
            if url not in usernames:
                usernames.append(url)
        return usernames

    def potential_sellers(self, loader, usernames):
        p_sellers = []
        for user in usernames:
            username = user[0]
            follow_count = self.get_followers(loader, username)
            seller = Seller(username, follow_count)
            if (follow_count >= self.follower_threshold):
                p_sellers.append([seller.username, seller.follow_count])

        return p_sellers

    def add(self, profiles):
        spreadsheet = self.client.open_by_key(self.account_rd)
        sheet = spreadsheet.worksheet(
            "Potential Sellers")
        sheet.append_rows(profiles)
