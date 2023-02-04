import requests

API_KEY = 'yourAPIkey'

def get_data(place, days):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
    data = requests.get(url).json()
    data = data['list']
    data = data[:8 * days]
    return data

if __name__ == '__main__':
    print(get_data('kaohsiung', 2))