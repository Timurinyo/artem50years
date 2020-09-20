from flask import Flask, render_template, url_for, redirect
import monobank
import locale
import time
import datetime

locale.setlocale(locale.LC_ALL, '')

token = 'uR-j44ioFTArzlrFd6JJXyLAZH7vIUf4kEG-H4xmjSMM'
white_card_id = 'gsSGMNasjjQR_2BDIVOv3g'

FIRST_TIME = True

UPLOAD_FOLDER = 'static/uploads'

BALANCE = 0
PEOPLE_DONATED = 0
START_DONATION_DATE = datetime.datetime(2020, 9, 13)
LAST_REQUEST_TIME = 0

app = Flask(__name__)
app.config.from_pyfile('config.py')


mono = monobank.Client(token)

def find_card(card_id, user_info):
    for card in user_info['accounts']:
        if card['id'] == card_id:
            return card

def get_account_balance(card_id):
    try:
        user_info = mono.get_client_info()
        card = find_card(card_id, user_info)
        balance = card['balance']
        balance = round(balance / 100 )
    except:
        balance = 0
    return balance

def get_people_donated(card_id, since, to=datetime.datetime.now()):
    try:
        statements = mono.get_statements(card_id, since, to)
        peoples_donated = 0
        for statement in statements:
            if statement['amount'] > 0:
                peoples_donated += 1
    except:
        peoples_donated = 0
    return peoples_donated

@app.route("/")
def home():
    global FIRST_TIME
    global LAST_REQUEST_TIME
    global BALANCE
    global PEOPLE_DONATED

    current_time = int(time.time())
    time_difference = current_time - LAST_REQUEST_TIME
    print(time_difference)
    if time_difference > 61 or FIRST_TIME:
        gethered = get_account_balance(white_card_id)
        BALANCE = gethered

        people_supported = get_people_donated(white_card_id, START_DONATION_DATE)
        PEOPLE_DONATED = people_supported

        LAST_REQUEST_TIME = int(time.time())
    else:
        gethered = BALANCE
        people_supported = PEOPLE_DONATED
    
    time_until_birthday = datetime.datetime(2020, 9, 29) - datetime.datetime.now()
    days_until_birthday = time_until_birthday.days

    progress_bar_style_width = f"style=width:{(gethered / 300000)*100}%"

    FIRST_TIME = False
    return render_template("index.html", gathered="{0:n}".format(gethered).replace(',', ' '), people_supported=people_supported, days_until_birthday=days_until_birthday, progress_bar_style_width=progress_bar_style_width)

@app.route("/support")
def support():
    return redirect('https://send.monobank.ua/ADwpCQ3D64')

if __name__ == "__main__":
    app.run(debug=True)



