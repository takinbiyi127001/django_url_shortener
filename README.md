=====
Demo Url Shortener
=====

Url shorteners work by transforming any long URL into a shorter, more readable link. When a user clicks
the shortened version, they’re automatically forwarded to the destination URL.

NOTE: - I intentionally left the custom user model in the application, which the official Django documentation
highly recommends because changes can be made to the built-in User model at some point in the project life. 
- The Url shortener is a demo app and is not ready for production. 


Quick start
-----------

1. Extract the zip file and navigate to the project directory/folder
Run
$ cd django_url_shortner

2. To build the Docker image from the Dockerfile, execute the command below.The period, ., indicating the Dockerfile is
located in the current directory.This command will result in a long stream of output code on the command line 
and Create a custom image
Run
$ docker build .

3. Initialize the database for the very first time, migrate database and startup the development server at http://0.0.0.0:8000/.
This command will result in another long stream of output code on the command line.
Run
$ docker-compose up

4. Visit http://127.0.0.1:8000/ to shorten a URL.
   
5. Visit http://127.0.0.1:8000/list to list existing set of original, corresponding url and how many times the short url has been used.
   
6. To run test, open a new terminal
Run
$ docker-compose exec web python manage.py test

7. The final step is to Stop the currently running container with Control+c and additionally type
Run
$ docker-compose down


Please if you have any issue running the application, please contact me via email akintobiakinbiyi@gmail.com