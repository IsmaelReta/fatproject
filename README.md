Non-Profit project for "Fundación Córdoba Fibrosis Quística"
An institution that helps people with Cystic fibrosis.

This repository contains back-end only, for front-end reach [our front-end repository](https://github.com/maximomazzuchin/frontendFQ)

Steps to run this project:

1 - git pull <<https://github.com/IsmaelReta/fatproject>>

2 - python -m venv <<folder_for_venv>>

If the venv is located in the same directory as django_fqc you must name it fat_project_venv in order to be ignored in commits

Also note this project was created using Python 3.10.6

3 - pip install -r requirements.txt

4 - python django_fqc/manage.py check

5 - python django_fqc/manage.py runserver