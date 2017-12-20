the most important folder is /machinelearning 
the main files are machine_learning.py
views.py 
index.html
urls.py

you can pretty much ignore everything else for the time being
we can go over this tomororow more, set it up, I can explain a bit the structure (it is actually pretty poorly structured)


You have to install a virtualenv. and activate it.
Create virtualenv and do pip install -r 
1. Activate Virtual env
source activate

only have to do these once
2. ~/Django/python manage.py makemigrations
2. ~/Django/python manage.py migrate
2. ~/Django/python manage.py collectstatic

3. ~/Django/python manage.py runserver
4. GO to http://127.0.0.1:8000/

4. Downloaded template from https://templated.co/radius


can go to 

http://127.0.0.1:8000/api/hello-world/ - this accepts a file, parses it and gives the response.
http://127.0.0.1:8000/api/display-machine/
http://127.0.0.1:8000/api/machine-learning    - this uses "Wkhtml" to make a pdf file. It uses a command line process
