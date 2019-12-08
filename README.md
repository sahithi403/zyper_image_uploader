
# Zyper Image Uploader

1. Clone the project  
    git clone https://github.com/sahithi403/zyper_image_uploader.git
2. Create a virtualenv and install requirements using `pip install -r reqs.txt`
3. Setup a postgres db. Please check DATABASES in settings.py for setting up the postgres connection accordingly
     1. createdb zyperdb
     2. createuser -d -l -P -r -s zyperuser
4. Run migrations
        `python manage.py migrate`    
5. Run the project  
    python manage.py runserver  
    You should see django server running at http://127.0.0.1:8000/  
6. Install Redis on the platform. For Mac use brew.  
    brew install redis  
7. Start the redis-server and keep it running in the backgroud.  
    redis-server
8. Navigate to the project directory and start the celery worker with the following command.  
    cd image_uploader  
    celery -A image_uploader worker -l info  
    
9. API endpoint for image and thumbnail view and upload.  
    http://127.0.0.1:8000/images/  
    
10 Refer to docs/deployment_discussion.md for deployment and scalability notes.