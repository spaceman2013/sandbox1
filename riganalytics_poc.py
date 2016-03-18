import requests

class DirectAccess(object):

    api_key = ''
    url = ''
    params = ''
    headers = {}
    session = None

    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.url = base_url
        self.headers = {
            'X-API-KEY': self.api_key
        }
        self.session = requests.session()
        self.session.headers.update(self.headers)

    def get_dataset(self, dataset, params):
        url = self.url + dataset
        r = self.session.get(url, params=params)
        return r.content


api_key = '2697829ad5da5d0bc6d8cbb57f58ea8f'
url = 'http://preprod-api.drillinginfo.com/v1/direct-access/'
params = {
    'format': 'xml',
    'page': 1,
    'pagesize': 100000,
   }
dataset = 'rig-jobs'


da = DirectAccess(api_key=api_key, base_url=url)

rigs = da.get_dataset(dataset, params)

with open('riganalytics.xml', 'w+') as f:
    f.write(rigs)
