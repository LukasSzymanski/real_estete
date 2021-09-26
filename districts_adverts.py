from abc import ABC, abstractmethod
from communication import connect, get_soup


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
