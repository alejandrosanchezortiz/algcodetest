# algcodetest
Example of a web app where users can stablish realtionships with another users and see them in a chart

I choosed Django framework because I use Python for automating the regressions tests that we run in our daily tasks.
Python includes Sqlite database that is enough for this code test, so no need to install MySQL or any other database.
Django also includes a small HTTP server for development purposes, so no need to install Apache.

Steps for deployment:
  1. git clone https://github.com/alejandrosanchezortiz/algcodetest.git
  2. cd algcodetest
  3. python .\manage.py migrate
  4 .python .\manage.py createsuperuser
  4. python.\manage.py runserver 8080
  5. http://127.0.0.1:8080
