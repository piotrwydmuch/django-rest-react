### Edycja i aktualizacja bazy danych
Note that every time you make changes to the models.py file, we will need to make migrations.
"three-step guide" to making model changes:
    Change your models (in models.py).
    Run `python manage.py makemigrations` to create migrations for those changes
    Run `python manage.py migrate` to apply those changes to the database.
https://docs.djangoproject.com/en/4.2/intro/tutorial02/#activating-models


### DOSTEPY
Admin panel:
  admin
  dupa123


### Dodawanie nowej aplikacji do projektu
## (Pozwala np na to aby dzialaly różne połączenia pomiędzy aplikacją a widokami itp)
To include the app in our project, we need to add a reference to its configuration class in the INSTALLED_APPS setting. The PollsConfig class is in the polls/apps.py file, so its dotted path is 'polls.apps.PollsConfig'. Edit the mysite/settings.py file and add that dotted path to the INSTALLED_APPS setting. It’ll look like this:

```
INSTALLED_APPS = [
    ...
    "nowa.apps.NowaConfig",
    ...
## ewentualnie tak:
    ...
    "polls.apps.PollsConfig",
    ...
]
```