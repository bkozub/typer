# typer
My engineering work for graduate at the university.
## Getting Started
For start the project install virtual envormient via:
```
pip install virtualenv
```
Test your installation:
```
virtualenv --version
```
Create a virtual environment for a project:
```
cd my_project_folder
virtualenv my_project
```
Next activate virtual env using your activate binary file.
## Instalation
```
pip install -r requirments.txt

```
### Start Project
For starting project use
```
python manage.py runserver 0.0.0.0:8000
```
Dont forger about your database and migrations:
```
python manage.py makemigrations
python manage.py migrate
```

 
