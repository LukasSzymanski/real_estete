from abc import ABC, abstractmethod
from communication import connect, get_soup
from work import find_date


class Region(ABC):

    def __init__(self, region_id, www, pages):
        self.region_id = region_id
        self.www = www
        self.pages = pages
        self.soups = []
        self.data = []

    def scrape(self):
        added, errors = 0, 0
        for page in self.pages:
            www = self.www + page
            res = connect(www)
            if not isinstance(res, Exception):
                self.soups.append(get_soup(res))
                added += 1
            else:
                errors += 1

        return {'ok': added, 'errors': errors}

    @abstractmethod
    def get_data(self):
        pass


class Ladek(Region):

    def get_data(self):
        """"""
        self.data.clear()
        for soup in self.soups:
            new = dict()
            adverts = soup.find("div", {"class": "doc-attachments"})
            for advert in adverts.find_all('li'):
                new['link'] = self.www + advert.find('a').get('href')
                text = advert.text
                new['text'] = text[:text.find('.pdf')]
                new['published'] = find_date(text)
                self.data.append(new)
        return {'Added': len(self.data), 'Error': None}


class Stronie(Region):

    def get_data(self):
        self.data.clear()
        for soup in self.soups:
            adverts = soup.find_all("tr", {"class": "odd"})
            for advert in adverts:
                new = dict()
                new['published'] = find_date(advert.find('td').text)
                description = advert.find('a')
                new['link'] = self.www + description.get('href')
                new['text'] = description.text
                self.data.append(new)
        return {'Added': len(self.data), 'Error': None}
