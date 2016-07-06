import sys
import xml.etree.ElementTree as ET
import urllib.request
from bs4 import BeautifulSoup

def main():
    args = sys.argv
    if len(args) > 2: sys.exit(0)
        
    url = args[1]    
    request_data = get_page_source(url)

    root = ET.fromstring(request_data)
    for child in root:
        print(child.tag, child.attrib)
        
def get_page_source(url):

    if is_url(url):               
        response = urllib.request.urlopen(url)
        response_data = response.read()
        return response_data
    else:
        return None
    
# TODO: this
def is_url(url):
    return True

if __name__ == '__main__':
    main()
# http://myanimelist.net/malappinfo.php?u=blankpanda&status=all&type=anime
