from django.shortcuts import render
from flickrapi import FlickrAPI
import urllib
from PIL import Image
from pprint import pprint

# Flickr api access key 
flickr=FlickrAPI('c6a2c45591d4973ff525042472446ca2', '202ffe6f387ce29b', cache=True)


FLICKR_PUBLIC = 'Your Flickr Key'
FLICKR_SECRET = 'Your Flickr Secret Key'

flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
extras='url_sq,url_t,url_s,url_q,url_m,url_n,url_z,url_c,url_l,url_o'
cats = flickr.photos.search(text='kitten', per_page=5, extras=extras)
photos = cats['photos']
pprint(photos)


keyword = 'siberian husky'

photos = flickr.walk(text=keyword,
                     tag_mode='all',
                     tags=keyword,
                     extras='url_c',
                     per_page=100,           # may be you can try different numbers..
                     sort='relevance')

urls = []
for i, photo in enumerate(photos):
    print (i)
    
    url = photo.get('url_c')
    urls.append(url)
    
    # get 50 urls
    if i > 50:
        break

print (urls)

# Download image from the url and save it to '00001.jpg'
urllib.urlretrieve(urls[1], '00001.jpg')

# Resize the image and overwrite it
image = Image.open('00001.jpg') 
image = image.resize((256, 256), Image.ANTIALIAS)
image.save('00001.jpg')