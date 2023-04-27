from flask import Flask, render_template, request, jsonify
from flask_wtf.csrf import CSRFProtect, generate_csrf
from werkzeug.utils import secure_filename
import os
import csv
import threading
from instabot import Bot
import glob
import time, random
from instagrapi import Client




app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['UPLOAD_FOLDER'] = 'templates'
app.config['ALLOWED_EXTENSIONS'] = {'csv'}
csrf = CSRFProtect(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    csrf_token = generate_csrf()
    return render_template('index.html', csrf_token=csrf_token)

@app.route('/status')
def status():
    return f'Processing... {time.time()}'

@app.route('/start', methods=['POST'])
def start():
    username = request.form['username']
    password = request.form['password']
    message = request.form['message']

    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            usernames = [','.join(row) for row in reader]
        


        #instagrapi code
        print(username, password, usernames, message)
        client = Client()
        client.login(username=username, password=password)
        t = threading.Thread(target=send_insta, args=(usernames, message, client))
        t.start()


        # do something with the username and csv file
        if os.path.exists(file_path):
            os.remove(file_path)
        
        return render_template('index.html', message_sent='Sending Messages in Background')
        

    else:
        return jsonify({'result': 'error', 'message': 'Failed to send messages'})

def send_insta(usernames, message, client):
    

    for user in usernames:

        users = client.search_users(user)
        recipient = users[0]  # select the first user in the search results
        client.direct_send(message, user_ids=[recipient.pk])
        print("Sent to ", user)
        for i in range(20):
            time.sleep(random.randrange(10,15))
            print("processing ...")






def send_msg(username, password, usernames, message):
    try: 
        cookie_del = glob.glob("config/*cookie.json")
        os.remove(cookie_del[0])
    except Exception:
        None

    bot = Bot()
    bot.login(username=username, password=password, is_threaded = True)

    for user in usernames:
        bot.send_message(message, [user])
        print("Sent to ", user)
    
    bot.logout()


if __name__ == '__main__':
 
    app.run(debug=True)
