FROM ubuntu
WORKDIR /tadaa
COPY . .
SHELL ["/bin/bash", "-c"]
RUN apt update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade setuptools
RUN pip3 install -r requirements.txt --verbose --root-user-action=ignore
CMD ["bash", "-c", "tailwindcss -i ./tadaa/tailwind/input.css -o ./tadaa/static/tailwind.css && gunicorn --bind 0.0.0.0:5000 wsgi:app"]
EXPOSE 5000

