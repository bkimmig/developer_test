# Developer Test


## Introduction

Hi - welcome to the developer test! This is a simple test to ensure you know some basics about web development and programming. We assume in this test that you have some experience using the command line. We don't expect you to be an expert on the syntax of the programming languages that are used in this test, but we think that your knowledge of how web applications work should be sufficient to get you through the test.  

Our main application is written in <a href='https://www.python.org/'> Python </a>, if you do not have it installed on your computer you should download the correct version for your operating system from <a href='https://www.continuum.io/downloads'> Anaconda </a> (please get Python 3.4 or higher). This test will use Python 3.4. If you are familiar with python you can skip to the test section and begin. For new people to Python the next few sections will aid in setup. 

This test will consist of a simple task to complete using the Python web framework <a href='http://flask.pocoo.org/'> Flask </a>. 

If you are using Anaconda's version of Python you can install this using the Anaconda installer. If you are using your own just keep your extra modules installed to Flask and the requests package. 

If you know about Python and how to set it up you can skip the Python/Virtual Environment Setup section.


## Python/Virtual Environment Setup (Anaconda)

Here is a basic tutorial for virtual environment with Anaconda if you would like to read more than what is written here https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/.

After downloading Anaconda, set up the environment from the command line using the following. We do not want any default packages with python, you should be able to complete this challenge using only Flask and requests, if you install other packages/dependencies let us know.

    $ conda create --no-deps --no-default-packages -n dev_test python=3.4 anaconda

You can then activate the virtual environment with

    $ source activate dev_test

You can use anaconda to install Flask with. 
    
    $ conda install flask

You should also install the requests package.

    $ conda install requests

If you ever want to leave the virtual environment use the command (you shouldn't need to during the test). 

    $ source deactivate dev_test

## Current Application Structure

Here we give you the basic framework for a Flask application. When you unzip the directory you will see folders in the following structure.

dev-test/
    app/
        main_app/
            views/
                home.py
            __init__.py
        static/
            css/
            js/
            vendor/
                bootstrap/
                    ...
                jquery/
                    ...
        templates/
            main_app/
                home.html
            base.html
            navbar.html
        spotify_api/
            spotify.py
        __init__.py
    config.py
    requirements.txt
    run.py
    README.md

The views for this application live in main_app directory. You should only need to add files in that directory and in the templates directory. If you decide to use JavaScript (write your own) for any reason you can put it into the static/js/ folder, or put it at the top of the html file.

You should take a look at the spotify_api/spotify.py. You will want to use this to get the data. Feel free to write your own if you feel more comfordable doing that.


### Running The Application

If you want to run the application type
    
    $ python run.py

in the dev-test directory. Then go to the url printed in the terminal in your browser. It should be http://127.0.0.1:3000/


## The Test

You should be able to complete this challenge using only Flask and the <a href='http://docs.python-requests.org/en/master/'> requests </a> module (you do not need to write the API request I have given you a class for this app/spotify/spotify_api.py), if you needed/installed other packages let us know, but you should not need to though.

In the most basic case, we want you to set up a view containing a form that allows a user to query Spotify for an artist's albums. After the query we would like you to display the results in a HTML table. The table should contain the following columns:

- artist name
- image
- albumn name
- albumn type
- U.S. available

Feel free to hardcode in the column names of the table. The results however should always be dymamically inserted.

We have provided a class to perform the Spotify query, spotify_api/spotify.py, you are welcome to use that but it is not required.

We have set up a couple of blank files for you to fill in. Feel free to add more if you need to.

- app/main_app/forms/artist_form.py
- app/main_app/views/album_view.py
- app/templates/main_app/artist_form.html
- app/templates/main_app/album_view.html


### Tips/Steps

Here are some tips/steps to help you, they are not the only way to do this just to provide guidance if needed. 


1. Create a view with html form that takes an artist name.
    - There should be a link to this page in the navbar.
    - View should have both post and get methods.

2. Form data
    - Create a flask form to handle the data.
    - The form should clean and validate that it. 

3. In the view request data from the Spotify API.

4. Display the artist data obtained from Spotify in an HTML table. Use the Flask templates to render the data in the HTML table.
