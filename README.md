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

You can use anaconda to install Flask with 
    
    $ conda install flask

If you ever want to leave the virtual environment use the command (you shouldn't need to during the test). 

    $ source deactivate dev_test


## Current Application Structure






## The Test

You should be able to complete this challenge using only Flask, if you need/install other packages let us know.

