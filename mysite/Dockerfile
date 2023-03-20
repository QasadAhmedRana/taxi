FROM python:3.9
COPY . usr/scr/app
WORKDIR usr/scr/app
RUN pip install django django-environ django-crispy-forms

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
