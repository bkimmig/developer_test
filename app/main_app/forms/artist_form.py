from wtforms import Form, StringField


## should use flask forms to validate the input from the album view form.
## This is not totally necessary you are welcome 
## to just check this in your view function.

class ArtistForm(Form):

    artist = StringField('artist')

    def cleaned_data(self):
        artist = self.data['artist'].split(' ')
        artist = "+".join(artist).lower()
        return artist