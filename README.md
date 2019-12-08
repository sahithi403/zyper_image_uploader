
# Zyper Image Uploader

1. Clone the project
2. Create a virtualenv and install requirements using `pip install -r reqs.txt`
3. Setup a postgres db. Please check DATABASES in settings.py for setting up the postgres connection accordingly
     1. createdb zyperdb
     2. createuser -d -l -P -r -s zyperuser
4. Run migrations
        `python manage.py migrate`    
5. Run the project
    python manage.py runserver
    You should see django server running at http://127.0.0.1:8000/

