# algcodetest
Example of a web app where users can stablish relationships with another users and see them in a chart.

I choosed Django framework because I use Python for automating the regressions tests that we run in our daily tasks.
Python includes Sqlite database that is enough for this code test, so no need to install MySQL or any other database.
Django also includes a small HTTP server for development purposes, so no need to install Apache either.

**Steps for deployment:**
  
  **1.** Install Python 3.X: 'https://www.python.org/downloads/'  
  **2.** Repository download: 'git clone https://github.com/alejandrosanchezortiz/algcodetest.git'  
  **3.** Access repository folder: 'cd algcodetest'  
  **4.** Install Django framework: 'pip install -r requirements.txt'    
      * It will install Django 2.2.4  
  **5.** Database Initialization: 'python .\manage.py migrate'  
  **6.** Create an admin user: 'python .\manage.py createsuperuser'  
      * That is only for accesing django administration  
  **7.** Launch webserver: 'python.\manage.py runserver 8000'    
      * If it fails, try another port like 8080  
  **8.** Test in a browser: http://127.0.0.1:8000    
      * In the main page we can see some help about the web app functionality.  
  
**Admin:**  
  We can access Django adminsitration here: http://127.0.0.1:8000/admin with the login/password created 
  with the command 'python .\manage.py createsuperuser'  
  Django administration panel allow us to create new users and stablish relationships between them, I used that to test the database model before creating the final user web pages. 
  
  
**Notes:**  
  You can notice that the GoJS library used for the chart is an evaluation version, I tested other free Javascript libraries like Chart.JS   but I did not find a chart that suits better the connection between the users.
