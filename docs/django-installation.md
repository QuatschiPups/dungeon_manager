

# Django installieren

``` cmd
pip install Django
```

``` cmd
django-admin startproject dungeon_manager src
```

``` cmd
python src/manage.py startapp accounts src/apps/accounts
python src/manage.py startapp users src/apps/users
```


``` cmd
python src/manage.py makemigrations
```
``` cmd
python src/manage.py migrate
```