# artem50years

First attempt on creation of simple crowdfunding web app for personal use

## Minimal setup:
- Set monobank API token and card id in app.py - [TOKEN](https://api.monobank.ua/) and CARD_ID vars
- Set random key in config.py/SECRET_KEY 
- Change text, links and everything you want to change in templates/index.html
- Install requirements with _pip install -r requirements.txt_
- Run with gunicorn --bind 0.0.0.0:5000 wsgi:app

## Additional setup:
- Read https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04
- Example of files for nginx and system service can found in _Other_ folder

## Main links used:
- https://www.twilio.com/blog/deploy-flask-python-app-aws
- https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04
- https://us-east-2.console.aws.amazon.com/ec2/v2/
- https://namecheap.com

## Keywords:
- flask
- ec2
- https
- nginx
- venv
- flex
- requirements.txt
- gunicorn
- certbot
