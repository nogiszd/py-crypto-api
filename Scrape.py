from bs4 import BeautifulSoup
import requests

class Scrape():
    def __init__(self, method, symbol, elements):
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
        }
        
        match method:
            case 1:
                res = requests.get("https://www.google.com/search?q=" + symbol.replace(" ", "+"), headers=headers).text
               
            case 2:
                res = requests.get("https://www.google.com/search?q=" + symbol[0] + "+to+" + symbol[1], headers=headers).text

        soup = BeautifulSoup(res, "html.parser")
        self.__summary = {}
                
        for el in elements["elements"]:
            tag = soup.select_one(el["from"])
            if tag != None:
                self.__summary[el["to"]] = "{:.2f}".format(float(tag["value"]))        

    def summary(self):
        return self.__summary