# algcodetest
Example of a web app where users can stablish realtionships with another users and see them in a chart

I choosed Django framework because I use Python for automating the regressions tests that we run in our daily tasks.
Python includes Sqlite database that is enough for this code test, so no need to install MySQL or any other database.
Django also includes a small HTTP server for development purposes, so no need to install Apache either.

Steps for deployment:
  
  1. Install Python 3.X https://www.python.org/downloads/
  3. Within a folder: git clone https://github.com/alejandrosanchezortiz/algcodetest.git
  4. cd algcodetest
  4. python .\manage.py migrate
  5. python .\manage.py createsuperuser
  6. python.\manage.py runserver 8080
  7. http://127.0.0.1:8080
