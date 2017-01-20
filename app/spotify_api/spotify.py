import requests


class Spotify(object):

    """
    Artist name should be combined with '+'. For example, Elton John should
    be Elton+John.

    Cleaned data returns a list of dictionaries. Each dictionary will have the 
    following fields.
        
        {
            'artist': string,
            'image_url': string,
            'albumn_type': string,
            'us_available': boolean,
            'albumn_name': string

        }

    Usage:

    spotify = Spotify('Elton+John')
    if spotify.request_is_valid():
        data = spotify.cleaned_data()

    """

    BASE_URL = "https://api.spotify.com/v1/search?q={}&type={}"

    def __init__(self, artist):

        self.artist = artist
        self.search_type = 'album'
        self.request = requests.get(
            self.BASE_URL.format(self.artist, self.search_type)
        )
        self.request_valid = self.request_is_valid()

    def request_is_valid(self):
        if self.request.status_code >= 400:
            return False
        return True

    def data(self):
        if self.request_valid:
            return self.request.json()
        return 'Error: Invalid Request'

    def cleaned_data(self):
        if not self.request_valid:
            return 'Error: Invalid Request'
        
        data = self.request.json()['albums']
        albums = data['items']
        cleaned_data = []
        for album in albums:
            info = {
                'artist': album['artists'][0]['name'],
                'image_url': album['images'][2]['url'],
                'album_name': album['name'],
                'us_available': 'US' in album['available_markets'],
                'album_type': album['album_type']
            }
            cleaned_data.append(info)

        return cleaned_data


