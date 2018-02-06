
    Errors to fix:
        - Hacer ajax a los campos de añadir para que se añada la info directamente sin acutalizar
        y perder los datos del form.

        - Al editar si añadimos cualquier cosa (departamento, estado ...) el form vuelve a /new y se reiniciar el form.

        - Cuando hago click en el nombre de una subvención relacionarla con otras con el mismo nombre.

        - Añadir favicon.

        - Cuando a una subvención la creo con un departamento de la generalitat, lugeo al editarla aparecen los dos campos,
        tanto el del departamento de diuptación como el de generalitat.

        - Mejorar plantillas 404 y 505.

        - Enviar email cuando alguien añade, modifica, etc.


       - THINGS TO KEEP IN MIND WHEN I DEPLOY(or maybe I can override model in mine project):
        The notify application has in his models the verb to 50 limit character, just update it to 255 and then
        python manage.py makemigrations notify
        python manage.py migrate notify
