FROM python:3.10-slim
WORKDIR /tadaa
COPY . .
SHELL ["/bin/bash", "-c"]
RUN apt update
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt  --verbose

CMD ["bash", "-c", "tailwindcss -i ./tadaa/tailwind/input.css -o ./tadaa/static/tailwind.css && gunicorn --bind 0.0.0.0:5000 wsgi:app"]
EXPOSE 5000


