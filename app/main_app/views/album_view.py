from flask import request, render_template, flash, redirect, url_for

from app.main_app import mod
from app.spotify_api.spotify import Spotify
from app.main_app.forms.artist_form import ArtistForm

## should contain a view that renders a form on the 'get'
## and renders the table with album information on the 'post' of the form 

@mod.route('/album', methods=['GET', 'POST'])
def album_view():
    """
    Return a greeting on the main page.
    """
    if request.method == 'GET':
        return render_template('main_app/artist_view.html')

    form = ArtistForm(request.form)
    if form.validate():
        artist = form.cleaned_data()
    else:
        flash('Form data invalid.', 'warning')
        return render_template('main_app/artist_view.html')
    
    spotify = Spotify(artist)
    if spotify.request_is_valid():
        data = spotify.cleaned_data()
    else:
        flash('Invalid Spotify artist. Bad request.', 'warning')
        return render_template('main_app/artist_view.html')

    
    return render_template('main_app/album_view.html', data=data)

