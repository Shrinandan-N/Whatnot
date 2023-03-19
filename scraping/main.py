import os
from dotenv import load_dotenv
from scraper import Scraper
import instaloader


def main():
    # load data
    load_dotenv()
    login_usr = os.environ["USERNAME"]
    login_pass = os.getenv('PASS')
    url = os.getenv("SHEET_URL")
    loader = instaloader.Instaloader()
    loader.login(login_usr, login_pass)
    phantom_sheet_url = url

    # run
    s = Scraper(phantom_sheet_url)
    profiles = s.get_profiles()
    potential_sellers = s.potential_sellers(loader, profiles)
    s.add(potential_sellers)


main()
