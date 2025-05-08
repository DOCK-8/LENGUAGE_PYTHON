import requests

def InfoPerson(dni):
    url = "https://api.apis.net.pe/"
    token = "Bearer apis-token-14861.03jtwiQ87KeztWfVytRc0O3QxrmB7R0P"
    headers = {
        'Authorization' : token,
        'Accept' : 'application/json'
    }
    app = requests.get(url+f'v2/reniec/dni?numero={dni}', headers=headers)
    return app
