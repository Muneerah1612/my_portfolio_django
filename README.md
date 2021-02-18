# my_portfolio

my_portfolio is a web application done with django which shows projects I have done, A contact page and a homepage.

# Getting Started

- activate virtual environment
- install Django
- create a Django project with the command 'django-admin startproject projectname'
- create a Django app with the command 'python3 manage.py startapp appname'
- register the new app in the project directory settings.py file
- setup database using PostgreSQL
- install psycopg2
- run migration
- create the homepage view
- activate the view
- create a model
- activate the model
- register model in admin site to enable interaction (admin. site. register(model class) in admin.py)
-add model objects in admin site (optional)
-create templates directory in the Django app
-create another directory in the templates directory, add an index.html file to the subdirectory
-replace the HttpResponse() in views.py with render(),to display the index.html content which has the response data now
-display data from the database (create a variable that houses the modelclass. objects, add the variable as a key: pair value to the render() )
-add bootstrap to the templates and tweak
