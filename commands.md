<!-- Packages -->

django
python-dotenv
djangorestframework
pytest
pytest-django

<!-- command -->

django-admin startproject drfcommerce

./manage.py runserver

./manage.py makemigrations

./manage.py migrate

from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())

./manage.py spectacular --file schema.yml

<!-- pytest -->

pytest -h # prints option _and_ condfig file settings

pip install coverage

coverage run -m pytest # used to create a test result

# pip install pytest-cov 

coverage html

<!-- 
Add schema.yml to the .gitignore file
htmlcov 
 -->