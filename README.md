# SUBSIDIES 
Web application for managing subsidies/subventions in my town hall (create, edit, delete, notifications, listing, etc).

### Deployment
Thing to keep in mind when deploying the application

##### Notify Application 
* The notify application has in his models the verb to 50 limit character, just change it to TextField instead of CharField 
* python manage.py makemigrations notify
* python manage.py migrate notify
* Or maybe I can override his model in mine project

##### When I load data from fixtures 
* python manage.py dumpdata myapp --indent=2 --output=myapp/fixtures/subsidies.json
* python manage.py dumpdata auth --indent=2 --output=myapp/fixtures/auth.json
* I can load users from auth model successfully
* But when I try to load subsidies.json: python .\manage.py loaddata subsidies.json it gives me a problem to fix it: 
* To solve it i go to myapp/models.py and I comment:
```
def send_email_created_updates => the whole function
and: post_save.connect(send_email_created_updates, sender=Subvencion)
```

##### Departments 
[EN] Sometimes when you click on the department for listing for that one and in the url appears None is because that one doesn't have 
slug and you have to go to the backend and select that department and save it so that his slug gets saved. After that do again the fixtures trick so every department has now slug. 
[ES] Si al darle sobre el departamento para listar por ese departamento y en la url pone None, es que
no tiene slug ese dep y por tanto vamos al backend y seleccionamos ese dep y lo guardamos para q se le guarde un
dep. Y luego de hacer eso volver a guardar las fixtures para que se guarde los slug de cada uno.

##### DATES 
[EN] In the input fecha inicho the holidays from array, you have to update them in accordance with your zone.
[ES] En el input fecha inicio los días festivos del array de js hay que ir actualizándolos está válido hasta diciembre de 2019.

##### BADGES RESPONSABLE (OLD VERSION I UPDATED IT)
If a new responsable is added, you have to give him a new color in index.html in badges like this and then in css:
```
{% elif responsable|split_value == 'F' %}fernando
.badge-fernando {
       background-color: #0c48b9;
       color: #fff;
}
```
