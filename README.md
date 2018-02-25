
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



       - ERRORS TO FIX:
            1. Escribir un script q se ejecute cada 5 días y envie los datos de la bbdd a mi email para una mayor seguridad

            2. Pantallazo:
                - Añadir las subvenciones del excel
                - Hacer script para copia de seguridad de bbdd (tanto de phpmyadmin como de fixtures) y añadir exportar a excel desde el admin

            3. Al crear subvención se envía el email pero el link de la misma no es el que corresponde.
               Mirar en el proyecto de sharing_things lo de sites, sin ver como hacerlo.

            4. Detalles cada subv:
                - JC quiere q sea el mismo diseño q al crear las subv
                - y quiere cambiar las urls de slug por id

            5. Nuevas reglas JC:
                - Nuevo campo (select):
                    - Colectivo de uno a muchos
                        - Ayuntamiento (por defecto)
                        - Mancomunidad
                        - Asociaciones
                        - Particulares
                        - Ayuntamientos y mancomunidades

            6. Pulsar sobre dep y listar con ajax
            7. Pulsar sobre nombre y listar ajax tmb
            8. En la columna dep poner dynamic color y background pero da error de jquery pq es hex y no rgb
            9. En relaciona con al crear y editar la subvención:
                - Que se filtre por mismo si la subvención que yo creo le pongo el dep aguas hídricas,
                pues que aparezcan esas subvenciones relacionadas con ese departamento
            10. En la columna fin no ordena bien
            11. Quitar la columna de editar y cuando entremos en el detalle de la subvención pues que tengamos ahí
            dos botones: uno de editar y el otro para eliminarla si queremos
            12. Que la tabla ocupe lo q tenga q ocupar y ponerle overflow
            13. En la fecha fin al crear subsidies: poner una opción dentro del ui de jquery calendar q sea:
                + 30 días hábiles
                + 25 días hábiles
                + 15 días hábiles
                *** Aun falta añadir los días festivos nacionales, intentar coger de alguna api pero no he encontrado,
                de manera que hay que ir actualizándolo
            14. En detalles de la subv siempre saca que la ha creado el usuario logeado
