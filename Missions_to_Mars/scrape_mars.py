
# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pymongo
import time
from webdriver_manager.chrome import ChromeDriverManager



def scrape():
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # Step 1: Scraping

    # To hold dictionary from scraping for import into Mongo after
    mars={}

    # NASA Mars News

    # URL of page to be scraped
    news_url = 'https://redplanetscience.com/'
    browser.visit(news_url)

    news_html = browser.html
    news_results = BeautifulSoup(news_html, 'html.parser')

    # Get values from html
    try:
        news_title = news_results.find('div', class_='content_title')
        news_title = news_title.text.strip()
        news_p = news_results.find('div', class_='article_teaser_body')
        news_p = news_p.text.strip()
    
        if (news_title and news_p):

            news_dict={'news_title': news_title, 'news_summary': news_p}

            mars.update(news_dict)
        
    except:
        scrape()

    # JPL Mars Space Featured Image

    # URL of page to be scraped
    image_url = 'https://spaceimages-mars.com/'
    browser.visit(image_url)

    image_html = browser.html
    image_results = BeautifulSoup(image_html, 'html.parser')

    # Get value from html

    featured_image_url = image_results.find('img', class_='headerimage')
    featured_image_url = image_url+featured_image_url['src']

    featured_image_dict={'featured_image': featured_image_url}

    mars.update(featured_image_dict)

    # Mars Facts

    import pandas as pd

    # URL of page to be scraped
    facts_url = 'https://galaxyfacts-mars.com/'

    # Scrape table from website
    fact_table = pd.read_html(facts_url)
    fact_table

    # Convert table to dataframe and clean it up
    facts_df=fact_table[1]
    facts_df=facts_df.rename(columns={0:"Fact", 1:"Value"})
    facts_df["Fact"]=facts_df["Fact"].str.replace(':', '')
    facts_df

    #convert dataframe to html table string
    facts_html=facts_df.to_html(index=False, header=False)
    facts_html.replace('\n', '')

    facts_dict={'mars_facts': facts_html}
    mars.update(facts_dict)

    # Mars Hemispheres

    # URL of page to be scraped
    hemis_url = 'https://marshemispheres.com/'
    browser.visit(hemis_url)

    hemis_html = browser.html
    hemis_results = BeautifulSoup(hemis_html, 'html.parser')

    # Get URL of pages to be scraped
    url_results = hemis_results.find_all('div', class_='item')

    url_list=[]

    for result in url_results:
    
        hemisphere=result.find('a')['href']
        url_list.append(hemisphere)

    # Loop through URLs to scrape and get list of dictionaries

    hemisphere_image_urls=[]

    for item in url_list:
        item_url=hemis_url+item
        browser.visit(item_url)
        item_html=browser.html
        item_results=BeautifulSoup(item_html, 'html.parser')
    
        # Get values to create dictionary
    
        parent1=item_results.find('div', class_='cover')
    
        h_title=parent1.find('h2','title')
        h_title=h_title.text.strip()
        h_title=h_title.rstrip('Enhanced')
        h_title=h_title.rstrip(' ')
    
        parent2 = item_results.find('div', class_='downloads')
        first_image=parent2.find('ul')
        h_image_item = first_image.find_all('li')[0]
        h_image = h_image_item.find('a')['href']
    
    
        # Create dictionary
    
        hemisphere_image_url={"title": h_title, "image_url": hemis_url + h_image}
        hemisphere_image_urls.append(hemisphere_image_url)
    


    mars.update({'hemispheres':hemisphere_image_urls})
    
    browser.quit()

    return mars


# # instructor says always do this to test!!!
if __name__ == "__main__":
    scrape_info = scrape()
    print(scrape_info)

# # Initialize PyMongo to work with MongoDBs
# conn = 'mongodb://localhost:27017'
# client = pymongo.MongoClient(conn)

# # Define database and collection
# db = client.mars_db
# collection = db.mars_info


# collection.insert_one(scrape_info)


