from playwright.sync_api import sync_playwright 
import pandas as pd


def main():
    with sync_playwright() as p:
        checkin_date='2025-04-23'
        checkout_date='2025-04-24'
        page_url=f'https://www.booking.com/searchresults.en-gb.html?ss=Tunis%2C+Tunisia&efdco=1&label=en-tn-booking-desktop-vGrG91d5hgN1KyCoxw4VOwS652796016390%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9215224%3Ali%3Adec%3Adm&aid=2311236&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=-731701&dest_type=city&checkin={checkin_date}&checkout={checkout_date}&group_adults=2&no_rooms=1&group_children=0'
        browser=p.firefox.launch(headless=False)
        page=browser.new_page()
        page.goto(page_url,timeout=600000)

        hotels=page.locator('//div[@data-testid="property-card"]').all()
        print(f'there are {len(hotels)} hotels.')
        hotels_list=[]
        for hotel in hotels :
          hotel_dict = {}
          hotel_dict['hotel'] = hotel.locator('//div[@data-testid="title"]').inner_text()
          hotel_dict['price'] = hotel.locator('//span[@data-testid="price-and-discounted-price"]').inner_text()
          hotel_dict['score'] = hotel.locator('//div[@data-testid="review-score"]/div[1]').inner_text()
          hotel_dict['avg review'] = hotel.locator('//div[@data-testid="review-score"]/div[2]/div[1]').inner_text()
          hotel_dict['reviews count'] = hotel.locator('//div[@data-testid="review-score"]/div[2]/div[2]').inner_text().split()[0]


          hotels_list.append(hotel_dict)
          df=pd.DataFrame(hotels_list)
          df.to_excel('hotels_list.xlsx',index=False)
          df.to_csv('hotels_list.csv',index=False)
        
        browser.close()


if __name__ == '__main__' :  
   main()