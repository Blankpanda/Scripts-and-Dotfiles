
import requests
import urllib
import sys
import os

from bs4 import BeautifulSoup

def main():
    args = sys.argv

    if len(args) != 2:
        print("Invalid number of arguments")

    download_imgur_album(args[1])

def get_album_id(url):
    reverse_url = url[::-1]
    url_id =  reverse_url.split("/")[0]
    return url_id

def download_imgur_album(url):

    index = 0
    html_source = requests.get(str(url)).text
    soup = BeautifulSoup(html_source, "html.parser")
    matches = soup.find_all("a")

    # make sure the link in in grid form
    if not is_grid(url):
       url = url + '/layout/grid'
        
        
    for match in matches:
        if "//i.imgur.com" in match.get('href'): 
            scraped_url = match.get('href')
            id = get_album_id(url)

            if os.path.exists(id):
                file_type = '.' + get_file_type(url)

                print("downloading " + scraped_url + ".")
                urllib.request.urlretrieve("http:" + scraped_url, id + "/" + str(index) + file_type)
                    # print ("failed to download " + scraped_url)
            else:
                os.makedirs(str(id))
                file_type = "." + get_file_type(url)
                
                print("downloading " + scraped_url + ".")
                urllib.request.urlretrieve("http:" + scraped_url, id + "/" + str(index) + file_type)
                    # print ("failed to download " + scraped_url)
        index += 1

def is_grid(url):

    if '/layout/grid' in url:
        return True
    else:
        return False
        

# HACK HACK HACK 
def get_file_type(url):
    if ".png" in url:
        return "png"
    elif ".jpg" in url:
        return "jpg"
    elif ".gif" in url:
        return ".gif"
    else:
        return "jpg"

            
if __name__ == '__main__':
    main()
