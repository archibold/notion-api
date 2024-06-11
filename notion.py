import requests


class Notion:
    def __init__(self, api_key):
        self.page = 'https://api.notion.com/v1'
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json',
            'Notion-Version': '2022-06-28'
        }

    def databases(self):
        data = {
            "filter": {
                "value": "database",
                "property": "object"
            }
        }
        r = requests.post(f'{self.page}/search', json=data, headers=self.headers)
        # print(r.status_code)
        # print(r.text)

