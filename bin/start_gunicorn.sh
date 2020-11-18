#!bin/bash
source /home/www/code/blog_website/env/bin/activate
exec gunicorn -c "/home/www/code/blog_website/gunicorn_config.py" bulkashmak.wsgi
