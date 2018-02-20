
    Errors to fix:
       - Escribir un script q se ejecute cada 5 días y envie los datos de la bbdd a mi email para una mayor seguridad

       - THINGS TO KEEP IN MIND WHEN I DEPLOY(or maybe I can override model in mine project):
        The notify application has in his models the verb to 50 limit character, just change it to TextField instead of CharField
        python manage.py makemigrations notify
        python manage.py migrate notify

        - Pantallazo:
            - 0.7 rem letra notificaciones, y el nombre tiene bold e italica
            - Ampliar width de la tabla del nombre de la subvención
            - Al email q solo llegue cuando crea la subvencion con enlace a la misma
            - Y en el front to.do, cuando crea, edita, q aparezca todoo en las notificaciones en el email solo cuando crea
            - Además en el front link a la subvención editada
            - Añadir las subvenciones del excel
            - Hacer script para copia de seguridad de bbdd y añadir exportar a excel desde el admin


        - En el form:
            - se relaciona con: con height fijo y overflow pero con checkbox y no select multiple


        - ahora como he hecho q al dar click sobre el estado liste todas las subv de ese estado, pues cambiarle el color al anchor

        - Detalles cada subv:
            - jc quiere q sea el mismo diseño q al crear las subv
            - y quiere cambiar las urls de slug por id