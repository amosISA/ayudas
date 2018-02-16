
    Errors to fix:
       - Escribir un script q se ejecute cada 5 días y envie los datos de la bbdd a mi email para una mayor seguridad

       - THINGS TO KEEP IN MIND WHEN I DEPLOY(or maybe I can override model in mine project):
        The notify application has in his models the verb to 50 limit character, just update it to 255 and then
        python manage.py makemigrations notify
        python manage.py migrate notify

        - Pantallazo:
            - 0.7 rem letra notificaciones, y el nombre tiene bold e italica
            - Ampliar width de la tabla del nombre de la subvención
            - Al email q solo llegue cuando crea la subvencion con enlace a la misma
            - Y en el front to.do, cuando crea, edita, q aparezca todoo en las notificaciones en el email solo cuando crea
            - Además en el front link a la subvención editada
            - En la tabla align-left a todos para q aparezcan a la izquierda
            - Añadir las subvenciones del excel
            - Hacer script para copia de seguridad de bbdd y añadir exportar a excel desde el admin
            - Los estados q aparecen a la izquierda q al hacer click q liste en la tabla solo las aprobadas
            (arreglar tema con slug y absolute_url, hacer un exclude en el form pero luego en el model con el signal q se cree auto)
            - En los responsables de la tabla hacer como etiquetas con un circulo alrededor: es decir, las iniciales como MV de maria vicenta
            , ese MV en un circulo rojo todos al lado del otro

        - En el form:
            - responsables sin overflow q se vean todos
            - se relaciona con: con height fijo y overflow pero con checkbox y no select multiple
            - quitar padding al boton
            - tamaño textarea de comentarios del mismo q el de desc
