# scratchy 
Django Channels + React.js webapp template

Hi! This is a web-app template build with Django-Channels and React.js!
All the settings and configs are included, ideally it's a plug-n-play template

A few quick tips:

  -Below are commands needed to operate the dev-server
  
    # [start|shutdown] redis
    sudo service redis-server [start|stop]
    # start django-channels
    python3 manage.py runworker channels # recommended
    -or-
    python3 manage.py runserver 
  
  -Add a config.py file before running server/worker. config.py should contain a 50 char secret_key
  charset=[abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)]
  
  -Redis-server MUST BE installed in order for the channel_layers to work!
  
Enjoy!

David Ham
7/4/2018
  
