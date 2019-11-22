# launch at PROJ_DIR !!!


WORK_DIR="/home/box"
PROJ_DIR="$WORK_DIR/web"


sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

#sudo ln -sf $PROJ_DIR/etc/gunicorn.conf /etc/gunicorn.d/gunicorn.conf
#sudo /etc/init.d/gunicorn restart

#gunicorn -b 0.0.0.0:8080 web.hello:wsgi_application &
cd ./ask
gunicorn -b 0.0.0.0:8000 ask.wsgi:application
