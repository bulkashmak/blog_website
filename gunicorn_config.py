command = '/home/www/code/blog_website/env/bin/gunicorn'
pythonpath = '/home/www/code/blog_website'
bind = '127.0.0.1:8001'
workers = 5
user = 'www'
limit_request_fields = 32000
limit_request_fields_size = 0
raw_env = 'DJANGO_SETTIGS_MODULE=bulkashmak.settings'
