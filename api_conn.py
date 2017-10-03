'''
Python 3
'''


import requests
from bs4 import BeautifulSoup

base_url = 'http://api.genius.com'
headers = {'Authorization': 'Bearer 5gjDjwFArLPqHFYwuUeCqLbDwbM6Jp972-z8_u-rpYdAyQGuqX-D7Uajxx0l2W6U'}

song_title = input('Find song:')
artist_name = input('By artist:')

def lyrics_from_song_api_path(song_api_path):
    song_url = base_url + song_api_path
    response = requests.get(song_url, headers=headers)
    json = response.json()
    path = json['response']['song']['path']

    # Regular HTML scraping
    page_url = 'http://genius.com' + path
    page = requests.get(page_url)
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics = html.find(class_='lyrics').get_text()
    return lyrics

if __name__ == '__main__':
    search_url = base_url + '/search'
    data = {'q': song_title}
    response = requests.get(search_url, params=data, headers=headers)
    song_info = None
    json = response.json()

    for hit in json['response']['hits']:
        if hit['result']['primary_artist']['name'] == artist_name:
            song_info = hit
    if song_info:
        song_api_path = song_info['result']['api_path']
        print(song_info['result']['full_title'])
        print(lyrics_from_song_api_path(song_api_path))
        full_lyrics = lyrics_from_song_api_path(song_api_path)
        f = open('text.txt', 'a')
        f.write(full_lyrics)

    else:
        print(artist_name + ' - ' + song_title + ': Not found')
