import requests

def InfoPerson(dni):
    url = "https://api.apis.net.pe/"
    headers = {
        'Authorization' : token,
        'Accept' : 'application/json'
    }
    app = requests.get(url+f'v2/reniec/dni?numero={dni}', headers=headers)
    return app
