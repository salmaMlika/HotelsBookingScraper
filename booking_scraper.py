from playwright.sync_api import sync_playwright 
import pandas as pd


def main():
    with sync_playwright() as p:
        checkin_date='2025-01-23'
        checkout_date='2025-01-24'
        page_url=f'https://www.booking.com/searchresults.en-gb.html?ss=Tunis%2C+Tunisia&efdco=1&label=en-tn-booking-desktop-vGrG91d5hgN1KyCoxw4VOwS652796016390%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9215224%3Ali%3Adec%3Adm&aid=2311236&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=-731701&dest_type=city&checkin={checkin_date}&checkout={checkout_date}&group_adults=2&no_rooms=1&group_children=0'
        browser=p.firefox.launch(headless=False)
        page=browser.new_page()
        page.goto(page_url,timeout=60000)

        hotels=page.locator('//div[@data-testid="property-card"]').all()
        print(f'there are{len(hotels)}hotels.')


        browser.close()


if __name__='__main__':  
   main()