from bs4 import BeautifulSoup
import urllib.request

base_url = "https://travel.state.gov"
index_url_stub = "/content/travel/en/traveladvisories/traveladvisories.html?tsg-rwd-content-page-parsysxxx_list_start="
tmp_downloads = []
page_contents = []
collected_urls = []
data = []
def main():

    for i in range(0,200,25): # step by 25
        local_filename = download_html(base_url+index_url_stub+str(i))
        tmp_downloads.append(local_filename)
        page_contents.append(read_tmp_file(local_filename))
    
    # read each page, collect urls
    for page in page_contents:
        soup = BeautifulSoup(page,'html.parser')
        for link in soup.find_all('a'):
            local_filename = download_html(base_url + link.get('href'))
            info_page = read_tmp_file(local_filename) # country                        
            child_soup = BeautifulSoup(info_page,'html.parser')
                
            alert_label = child_soup.find("div",class_="tsg-rwd-emergency-alertheader-title").text
            tmp = alert_label.split("–",2)
            print(tmp)
            raw_risks = child_soup.find_all("span",class_="showThreat")
            risks = []

            for children in raw_risks:
                risks.append(str(children['data-tooltip']).split(":")[0])                        
#            data.append(CountryData(tmp[0],tmp[1].strip()[6:7],risks)) # all titles have the same style
    
                
    return 0

def download_html(url):
    local_filename, headers = urllib.request.urlretrieve(url)
    #print("Downloaded "+ url + " saving to " + local_filename)
    return local_filename

def read_tmp_file(filename):
    contents = str()
    try:
        f = open(filename,'r')
        print("Reading " + filename)
        contents = f.read()
    except IOError:
        print("could not read file " + filename)
    finally:
        f.close()
        return contents

# data model
class CountryData:
    items = {}
    def __init__(self,country_name,country_threat_level,reasons_list):
        items['country_name'] = country
        items['country_threat_level'] = country_thread_level
        items['reasons_list'] = reasons_list

    def get_country_name(self):
        return items['country_name']
    
    def get_country_threat_level(self):
        return items['country_threat_level']

    def get_reasons_list(self):
        return items['risks_list']
        
if __name__ == '__main__':
    main()

