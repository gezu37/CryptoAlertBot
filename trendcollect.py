from fake_useragent import UserAgent
import requests
import json

agent = UserAgent()
rez = []
rez1 = []


def collect_data():
    response = requests.get(
        url='https://api.coinmarketcap.com/data-api/v3/cryptocurrency/spotlight?dataType=2&limit=5&rankRange=0&timeframe=24h',
        headers={'user-agent': f'{agent.random}'})

    data = response.json()

    for i in data["data"]["gainerList"]:
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
    with open('result_g.json', 'w') as file:
        json.dump(rez, file, indent=4, ensure_ascii=False)

    for i in data["data"]["loserList"]:
        name = i['name']
        change = i['priceChange']['priceChange24h']
        slug = i['slug']
        rez1.append(
            {
                'name': name,
                'priceChange24h': change,
                'slug': slug
            }
        )
    with open('result_l.json', 'w') as file:
        json.dump(rez1, file, indent=4, ensure_ascii=False)