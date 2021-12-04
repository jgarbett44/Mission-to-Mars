#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[5]:


slide_elem.find('div', class_='content_title')


# In[6]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[8]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[11]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[13]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[14]:


df.to_html()


# In[15]:


## The result is a slightly confusing-looking set of HTML code—it's a <table /> element with a lot of nested elements. 
## This means success. After adding this exact block of code to Robin's web app, 
## the data it's storing will be presented in an easy-to-read tabular format.


# In[16]:


browser.quit()


# D1 Challenge

# In[17]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[18]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[19]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[20]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[21]:


slide_elem.find('div', class_='content_title')


# In[22]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[23]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# In[24]:


### JPL Space Images Featured Image


# In[25]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[26]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[27]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[28]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[29]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[30]:


## Mars Facts


# In[31]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[32]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[33]:


df.to_html()


# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# Hemispheres

# In[34]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[35]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []
html = browser.html
img_soup = soup(html, 'html.parser')

items = img_soup.find_all('div', class_='item')

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for x in items:
    hemisphere = {}
    titles = x.find('h3').text
    link_ref = x.find('a', class_='itemLink product-item')['href']
    
    browser.visit(url + link_ref)
    
    image_html = browser.html
    image_soup = soup(image_html, 'html.parser')
    download = image_soup.find('div', class_='downloads')
    img_url = url + download.find('a')['href']
    
    #print(titles)
    
    hemisphere['img_url'] = img_url
    hemisphere['title'] = titles
    hemisphere_image_urls.append(hemisphere)
    browser.back()
   


# In[36]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[37]:


# 5. Quit the browser
browser.quit()


# In[ ]:





# In[ ]:




