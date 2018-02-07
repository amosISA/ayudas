
    Errors to fix:
        - Al editar si añadimos cualquier cosa (departamento, estado ...) el form vuelve a /new y se reiniciar el form (ajax).

        - Color estados con sass

       - THINGS TO KEEP IN MIND WHEN I DEPLOY(or maybe I can override model in mine project):
        The notify application has in his models the verb to 50 limit character, just update it to 255 and then
        python manage.py makemigrations notify
        python manage.py migrate notify
