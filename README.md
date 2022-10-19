# Django_JS_Chat

My practice project in Django and HTML (with some JS)

Features:
1) Basic web-chat;
2) Multiple room usage (in work);
3) Check other users in chat room (in work); 
4) Minimalistic design; 
5) Personal user info (in work);

~~ Requirements: 
1) In requirements.txt file (Docker install everything automatically);
2) Create file "keys.py" in root project directory with parameters: 
- DJANGO_KEY (put your own pre-made Django token in it)
3) Create file ".env" in root project directory with parameters:
- DJANGO_PORT=*port number*
- DOCKER_EXPOSE_PORT=*port number*
- DJANGO_ALLOWED_HOSTS=*host list* (f.e. "127.0.0.1")
4) properly installed docker on your machine.~~

~~
For starting server use command in project root directory:
*docker-compose up*
After properly started cluster of three containers (Django, Redis and Celery) you can access project web-interface on localhost address with standard port 8000 (127.0.0.1:8000).
~~

Made for final practice exercise in chapter "Django and backend" for SkillFactory

Superuser:
~~login: 
password:~~ (don't need anymore)

Just create superuser by yourself after first migration.


For education purpose only. Workability is not guarantee.

If you'll have suggestions or encounter errors in project, do not hesitate to contact me, please.

Made by IvanDamNation (a.k.a. IDN) GNU General Public License v3, 2022
