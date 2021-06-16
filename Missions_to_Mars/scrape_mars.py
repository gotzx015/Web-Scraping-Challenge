# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def scrape():
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # Choose url that we are scraping data from
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Find all titles that are div and class content_title
    titles = soup.find_all('div', attrs={"class":"content_title"})
    # Store most recent article title
    news_title = titles[0].text
    # Find all text associated with article titles
    text = soup.find_all('div', attrs={"class":"article_teaser_body"})
    # Store most recent article text
    news_p = text[0].text


    # Choose url that we are scraping data from
    url = 'https://spaceimages-mars.com'
    browser.visit(url)
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Find url of featured image
    links = soup.find_all('img')
    link = links[1]['src']
    featured_image_url = 'https://spaceimages-mars.com/' + link


    # Choose url that we are scraping data from
    url = 'https://galaxyfacts-mars.com'
    browser.visit(url)
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Find all table facts for Mars and Earth
    mars = soup.find_all('span', attrs={"class":"orange"})
    earth = soup.find_all('span', attrs={"class":"purple"})
    # Create dataframe to store planet data
    row_labels = ["Diameter", "Mass", "Moons", "Distance from Sun", "Length of Year", "Temperature"]
    mars_facts = []
    earth_facts = []
    for x in range(3,9):
        mars_facts.append(mars[x].text)
    for x in range(2,8):
        earth_facts.append(earth[x].text)
    dict = {
        "": row_labels,
        "Mars": mars_facts,
        "Earth": earth_facts,
    }
    df = pd.DataFrame(dict)
    df.at[5, "Earth"] = "-88 to 58°C"
    df = df.set_index("")
    # Create html code from dataframe
    html_table = df.to_html(classes='table table-striped', justify="left")


    #hemisphere_image_urls = [
    #{"title": "Valles Marineris Hemisphere", "img_url": "https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg"},
    #{"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/images/full.jpg"},
    #{"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg"},
    #{"title": "Syrtis Major Hemisphere", "img_url": "https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg"},
    #]

    valles_image = "https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg"
    cerberus_image = "https://marshemispheres.com/images/full.jpg"
    schia_image = "https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg"
    syrtis_image = "https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg"

    listings = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "html_table": html_table,
        "valles_image": valles_image,
        "cerberus_image": cerberus_image,
        "schia_image": schia_image,
        "syrtis_image": syrtis_image,
    }

    # Quit the browser
    browser.quit()

    return listings