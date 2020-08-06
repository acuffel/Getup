# Getup For Animals 
Get Up For Animals is a Django application. The aim of this web application 
is to collect donation for Associations.

This V1 can allow users to do : 

 - The Associations can create an account
 - The Donors can look for an association filter by country, by city or 
by name and give them a donation.


## Packages

* Django : Python framework to build web app and manage the tests
* PostgreSQL : Database management system
* Coverage : To check the test coverage

## How to setup the project 
* Clone the repository 
* Install virtual environment

        pip3 install virtualenv
        virutalenv venv
        source venv/bin/activate
* Install requirements

        pip3 install -r requirements.txt
    

* Run the project in Development
    
    - Run the program in local
    
            ./manage.py runserver
            
    - Launch tests 

            ./manage.py test tests
            
    - Check coverage 
            
            coverage report
            