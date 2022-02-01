import requests
import os
class Unsplash:
    def __init__(self,search_term,per_page=20,quality="thumb"):
        self.search_term = search_term
        self.per_page = per_page
        self.page = 0
        self.quality = quality
        

    def set_url(self):
        #URL from which we have to extract data/photos.
        return f"https://unsplash.com/napi/search/photos?query={self.search_term}&xp=&per_page={self.per_page}&page={self.page}"

    def make_request(self):
        url = self.set_url()
        return requests.request("GET",url,)

    def get_data(self):
        self.data = self.make_request().json()

    def save_path(self,name):
        download_dir = "unsplash"
        if not os.path.exists(download_dir):
            os.mkdir(download_dir)
        return f"{os.path.join(os.path.realpath(os.getcwd()),download_dir,name)}.jpg"

    def download(self,url,name):
        filepath = self.save_path(name)
        with open(filepath,"wb") as f:
            f.write(requests.request("GET",url,).content)

    def Scrapper(self,pages):
        for page in range(0,pages+1):
            self.make_request()
            self.get_data()
            for item in self.data['results']:
                name = item['id']
                url = item['urls'][self.quality]
                self.download(url,name)
            self.pages += 1

if __name__ == "__main__":
    scrapper = Unsplash("cars")
    scrapper.Scrapper(1)