
       - THINGS TO KEEP IN MIND WHEN I DEPLOY:

            1. Notify Application
                The notify application has in his models the verb to 50 limit character, just change it to TextField instead of CharField
                python manage.py makemigrations notify
                python manage.py migrate notify
                Or maybe I can override his model in mine project

            2. When I load data from fixtures:
                I can load users from auth model successfully.

                But when I try to load subsidies.json: python .\manage.py loaddata subsidies.json
                Will give me a problem:
                    Problem installing fixture 'C:\Users\AMOS\Dev\ayudas\subvenciones\myapp\fixtures\subsidies.json': 'NoneType' object has no attribute 'username'
                To solve it i go to myapp/models.py and I comment:
                    def send_email_created_updates => the whole function
                    and: post_save.connect(send_email_created_updates, sender=Subvencion)

            3. Si al darle sobre el departamento para listar por ese departamento y en la url pone None, es que
            no tiene slug ese dep y por tanto vamos al backend y seleccionamos ese dep y lo guardamos para q se le guarde un
            dep. Y luego de hacer eso volver a guardar las fixtures para que se guarde los slug de cada uno.

            4. En el input fecha inicio los días festivos del array de js hay que ir actualizándolos está válido hasta diciembre de 2019.



       - ERRORS TO FIX:
            1. Escribir un script q se ejecute cada 5 días y envie los datos de la bbdd a mi email para una mayor seguridad

            2. Pantallazo:
                - Añadir las subvenciones del excel
                - Hacer script para copia de seguridad de bbdd (tanto de phpmyadmin como de fixtures) y añadir exportar a excel desde el admin

            3. Al crear subvención se envía el email pero el link de la misma no es el que corresponde.
               Mirar en el proyecto de sharing_things lo de sites, sin ver como hacerlo.

            9. En relaciona con al crear y editar la subvención:
                - Que se filtre por mismo si la subvención que yo creo le pongo el dep aguas hídricas,
                pues que aparezcan esas subvenciones relacionadas con ese departamento
                - Pero si en generalitat tmb hay un dep q es aguas hídricas, que aparezcan tmb esas subvenciones
                q tengan ese dep de generalitat
            11. Quitar la columna de editar y cuando entremos en el detalle de la subvención pues que tengamos ahí
            dos botones: uno de editar y el otro para eliminarla si queremos
            12. Que la tabla ocupe lo q tenga q ocupar y ponerle overflow
            14. En detalles de la subv siempre saca que la ha creado el usuario logeado
            15. Otro choice Gobierno de España
