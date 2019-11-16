sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#gunicorn -c /home/box/web/etc/gunicorn.conf.py
#sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
gunicorn -b 0.0.0.0:8080 web.hello:wsgi_application
