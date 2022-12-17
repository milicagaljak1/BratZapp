# BratZapp
Instalirati python

Instalirati pip

Instalirati virtuelno okruzenje
----------------------------------------
Linux: python3 -m venv venv

Windows: 
- sudo apt-get update
- sudo apt-get upgrade
- sudo apt install python-pip
- sudo apt install python3.10-venv
- python3 -m venv venv


Pravljenje baze podataka
----------------------------------------
1. korak: Uraditi komandu python manage.py migrate
Napomena: pre pravljenja baze aktivirati virtuelno okruzenje (pise ispod kako)!

Pokretanje Web aplikacije
-------------------------------------------------------
1. korak: Pozicionirate se u folder aplikacije

2. korak: Aktivirate virtuelno okruzenje
Linux : source venv/bin/activate
Windows:venv\Scripts\activate.bat ( ako ne radi, probati bez ekstenzije bat!)

3. korak: Zvanicno pokretanje servera
Linux & Windows: python manage.py runserver

Backend ce biti pokrenut na linku http://127.0.0.1:8000 koji samo iskopirate u browser

Napomene
--------------------------------------------
Za bilo koje promene u bazi podataka OBAVEZNO odraditi sledece dve komande
1. python manage.py makemigrations imeaplikacije
2. python manage.py migrate
