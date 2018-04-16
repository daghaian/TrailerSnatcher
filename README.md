# TrailerSnatcher
A standalone python script for grabbing high definition trailers for all movies in a given directory. The script will pull the best quality available and
store the trailer with the proper naming convention for Plex so that trailers will appear for all movies in your library. Note you will likely need to perform a refresh metadata
after the initial run.

## Requirements
Python 2.7 w/ the following libraries

1. Requests (https://pypi.org/project/requests/)
2. Youtube_dl (https://pypi.org/project/youtube_dl/)


## Environment Setup
Just place the main script in whatever location you currently store your movies. The script will recursively iterate through each of the subfolders adding the best
quality trailer available for the movie using the YouTube video API.


## Running the Script
I suggest adding a cronjob to run the script every [X] minutes/hours depending on your needs.
