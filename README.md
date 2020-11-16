# FullyBooked

Fully Booked is a virtual bookshelf for storing completed/read books, along with their rating out of 5.

This program can be run locally, or through Python Anywhere.


To run the program locally, please download the zip file. Please make sure to have the installed tools and applications as specified in the requirements.txt file.

Run the program by navigating to the level of the manage.py file

    FullyBooked/fullybooked_project

using the terminal/bash console, run the server using

    python manage.py runserver
    
and clicking/navigating to localhost
    
    http://127.0.0.1:8000/

This will open the program, hosting it on the local server provided by Django.
To view the REST API interface for the JSON data, add "/books" to the end of the web address, such that it reads

    http://127.0.0.1:8000/books/   
   
This will allow new books to be added to the JSON data, which will then be viewable on the index page bookshelf.

Eventually, adding books to the shelf will be allowed through use of Django forms.

This web application is also hosted on Python Anywhere, at http://katehickey26.pythonanywhere.com/

The REST API interface to add new books can be accessed at
http://katehickey26.pythonanywhere.com/books/

Known issues:
When running the application, both locally and through Python Anywhere the style/css may not be visible without use of a  plugin which allows you to send cross-domain requests, such as the Moesif CORS extension for Google Chrome.
Be sure to turn this extension off once the application has been viewed.

 