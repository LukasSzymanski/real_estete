import bs4
import requests

SCRAPER_DATA = {'LD': {'www': 'http://www.bip.ug-ladekzdroj.dolnyslask.pl/',
                       'pages': ['dokument,iddok,4938,idmp,7,r,r', 'dokument,iddok,4940,idmp,7,r,r']
                       },
                'ST': {'www': 'http://bip.stronie.dolnyslask.pl/',
                       'pages': ['index,idmp,275,r,r', 'index,idmp,275,r,r,istr,2', 'index,idmp,275,r,r,istr,3']
                       },
                }


def connect(www):
    try:
        print(f'Connection to website:{www}')
        res = requests.get(www)
    except requests.RequestException as e:
        print(f'Problem with connection to website:{www}')
        return e
    if res.ok:
        return res
    else:
        message = f'Problem with connection to website:{www}, status {res.status_code}'
        print(message)
        return requests.RequestException('Status 404')


def get_soup(response, parser='html.parser'):
    try:
        soup = bs4.BeautifulSoup(response.text, parser)
    except Exception as e:
        print(e)
        return e
    return soup
