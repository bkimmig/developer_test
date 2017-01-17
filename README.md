# Developer Test


## Introduction

Hi - welcome to the developer test! This is a simple test to ensure you know some basics about web development and programming. We assume in this test that you have some experience using the command line. We don't expect you to be an expert on the syntax of the programming languages that are used in this test, but we think that your knowledge of how web applications work should be sufficient to get you through the test.  

Our main application is written in <a href='https://www.python.org/'> Python </a>, if you do not have it installed on your computer you should download the correct version for your operating system from <a href='https://www.continuum.io/downloads'> Anaconda </a> (please get Python 3.4 or higher). This test will use Python 3.4. If you are familiar with python you can skip to the test section and begin. For new people to Python the next few sections will aid in setup. 

This test will consist of a simple task to complete using the Python web framework <a href='http://flask.pocoo.org/'> Flask </a>. 

You can install this using the Anaconda installer, or pip. If you know how to do this you can skip the Virtual Environment Setup. Otherwise I would recommend creating a virtual environment for each application you build.


## Virtual Environment Setup (Anaconda)

Here is a basic tutorial for virtual environment with Anaconda if you would like to read more than what is written here https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/.

After downloading Anaconda, set up the environment from the command line using the following. We do not want any default packages with python, you should be able to complete this challenge using only Flask, if you need/install other packages let us know.

    $ conda create --no-deps --no-default-packages -n dev_test python=3.4 anaconda

You can then activate the virtual environment with

    $ source activate dev_test

You can use anaconda to install Flask with. The application will also rely on the json package so install that as well. 
    
    $ conda install flask

    $ conda install json

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
        __init__.py
    config.py
    requirements.txt
    run.py
    README.md

The views for this application live in main_app. You should only need to add files in that directory and in the templates directory. If you decide to use JavaScript (write your own) for any reason you can put it into the static/js/ folder (you shouldn't need to), or put it at the top of the html file.

### Running The Application

If you want to run the application type
    
    $ python run.py

in the dev-test directory. Then go to the url printed in the terminal in your browser. It should be http://127.0.0.1:3000/



## The Test

You should be able to complete this challenge using only Flask and the <a href='http://docs.python-requests.org/en/master/'> requests </a> module (you do not need to write the API request I have given you a class for this), if you needed/installed other packages let us know, but you should not need to.

The challenge here is fairly simple, and is comprised of a few simple steps.

1. Create a form that takes an artist name.
2. Clean the form data
3. Request data from the Spotify API
4. Display the artist data obtained from Spotify in an HTML table


We want you to create a view that renders an HTML table with the data we have provided you.


https://shkspr.mobi/blog/2016/05/easy-apis-without-authentication/

