from flask import render_template, flash, redirect, url_for

from app.main_app import mod
from app.spotify_api.spotify import spotify

## should contain a view that renders a form on the 'get'
## and renders the table with album information on the 'post' of the form 
