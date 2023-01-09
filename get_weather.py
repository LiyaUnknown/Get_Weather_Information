from requests_html import HTMLSession
from bs4 import BeautifulSoup

class Weather_Information() : 
    def __init__(self) :
        self.loc = None
        self.week = None
        self.url = None
    def get_weather(self) : 
        if self.loc != None : 
            if self.week != None : 
                self.url = f'https://www.google.com/search?q=how+is+the+weather+in+{self.loc}+on{self.week}&oq=how+is+the+weather+in+{loc}&aqs=chrome.1.69i59l2j69i57j0i512j0i22i30l6.8272j0j7&sourceid=chrome&ie=UTF-8'
            else : 
                self.url = f'https://www.google.com/search?q=how+is+the+weather+in+{self.loc}&oq=how+is+the+weather+in+{loc}&aqs=chrome.1.69i59l2j69i57j0i512j0i22i30l6.8272j0j7&sourceid=chrome&ie=UTF-8'
        else : 
            if self.week != None : 
                self.url = f'https://www.google.com/search?q=how+is+the+weather&oq=how+is+the+weather+on+{self.week}&aqs=chrome.1.69i59l2j69i57j0i512j0i22i30l6.8272j0j7&sourceid=chrome&ie=UTF-8'
            else : 
                self.url = f'https://www.google.com/search?q=how+is+the+weather&oq=how+is+the+weather&aqs=chrome.1.69i59l2j69i57j0i512j0i22i30l6.8272j0j7&sourceid=chrome&ie=UTF-8'
        try : 
            print("Starting .")
            session = HTMLSession()
            response = session.get(self.url)
            soup = BeautifulSoup(response.content, 'html.parser')
            weather = soup.find('span', {'class' : "wob_t q8U8x"}).text + '°C'
            country = soup.find('div', {'class' : "wob_loc q8U8x"}).text
            more = soup.find('div', {'class' : "wtsRwe"}).text
            more = more.replace(' ' , "")
            more = more.replace('%' , "% \n ,")
            more = more.replace(':' , " : ")
            more = more.replace('km/h' , "kilometer per hour ,")
            img = soup.find('span', {'id' : "wob_dc"}).text
            print("Done")
            return [weather , country , img , more]
        except : 
            Weather_Information().get_weather()
    def set_loc(self , location = "united states") : 
        self.loc = location
    def set_week(self , week = "monday") : 
        self.week = week
    
