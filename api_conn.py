import requests
import codecs 
from bs4 import BeautifulSoup

base_url = 'http://api.genius.com'
# Go get your own token from the Genius API website ;)
token = ''
headers = {'Authorization': 'Bearer {}'.format(token)}

song_choices_en = {'Kanye West' : 'Jesus Walks', 'Eminem' : 'Lose Yourself', 'Snoop Dogg' : 'The Next Episode'}
song_choices_fr = {'Lomepal': 'Yeux Disent', 'Romeo Elvis' : 'ChanMax', 'Nekfeu' : 'On verra', 'IAM' : 'Demain C\'est Loin'}
#song_title = raw_input('Find song:')
#artist_name = raw_input('By artist:')

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

def get_lyrics(song_choices, name):
    search_url = base_url + '/search'

    for artist_name, song_title in song_choices.items():
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
            f = open('%s.txt' % name, 'a')
            full_lyrics = full_lyrics.encode('utf-8')
            f.write(full_lyrics)
        else:
            print(artist_name + ' - ' + song_title + ': Not found')

get_lyrics(song_choices_en, 'EN')
get_lyrics(song_choices_fr, 'FR')

