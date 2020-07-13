Requirements:
	Python 3.7.4
	Django==3.0.8
	django-postgres-copy==2.4.2
	psycopg2==2.8.5

Data is stored in ./order/management/data

Follow the follwing stpes to run the App

update the Postgresql details in settings.py file 

1. Navigate to the root directory where manage.py fie is present through terminal
2. Use 'python manage.py migrate' to create tables in database
3. Use 'python manage.py add_data' to populate the database from csv files
4. Use 'python manage.py runserver' to run the server and access it through localhost


P.S. orders.csv was modified to include an amount column
 