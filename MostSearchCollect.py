from fake_useragent import UserAgent
import requests
import json

agent = UserAgent()
rez = []


def collect_data_search():
    response = requests.get(
        url='https://api.coinmarketcap.com/data-api/v3/topsearch/rank',
        headers={'user-agent': f'{agent.random}'})

    data = response.json()

    for i in data["data"]["cryptoTopSearchRanks"]:
        name = i['name']
        change = i['priceChange']['priceChange24h']
        slug = i['slug']
        rez.append(
            {
                'name': name,
                'priceChange24h': change,
                'slug': slug
            }
        )
    with open('result_a.json', 'w') as file:
        json.dump(rez, file, indent=4, ensure_ascii=False)
