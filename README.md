Django REST simple api  Example

This Django tutorial app was created for the purpose of demonstrating Django and Django Rest Framework. It shows the basics of writing a REST endpoint which allows uploading and retrieving pictures.

I also wrote a tutorial, though if you just want to try my code out, I suggest using using the Quick Start or the Docker Image below (todo).

Be aware that there are multiple branches, one for each chapter of the tutorial.

There is also a YouTube series about this tutorial: https://www.youtube.com/watch?v=hMiNTCIY7dw
Quick Start

Installation Steps if you want to try it out

git clone https://github.com/ChristianKreuzberger/django-rest-imageupload-example.git
cd django-rest-imageupload-example
mkdir uploaded_media # create a directory for the uploaded images
virtualenv -p python3.4 venv # Note: python3.5 should also work
source venv/bin/activate
pip install -r requirements.txt
cd django_rest_imageupload_backend
python manage.py migrate
python manage.py runserver # starts the server 

Requirements

    Python 3.4+
    Django 1.10
    Django Rest Framework 3.5
    Pillow

Please see requirements.txt for more information.
