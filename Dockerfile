FROM python:3.6-alpine
COPY Pipfile* /
COPY service/ /service
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
CMD ["gunicorn", "wsgi", "-b 0.0.0.0:8000"]