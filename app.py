from flask import Flask, render_template, request, jsonify
from flask_wtf.csrf import CSRFProtect, generate_csrf
from werkzeug.utils import secure_filename
import os
import csv
# from scraper import auth, send_message
# import threading
from instabot import Bot
import glob
# import signal
# from instascraper import send_dms
# import subprocess




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

@app.route('/start', methods=['POST'])
def start():
    username = request.form['username']
    password = request.form['password']

    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            usernames = [','.join(row) for row in reader]
        
        messages = "Hi! We’re running marketing and outreach tests on behalf of our company. Please disregard this message and have a great day!"

        #uncomment bellow code for selenium webdriver
        # auth(username, password)
        # time.sleep(random.randrange(3,5))
        # send_message(usernames, messages)

        #code for instabot
        # thread = threading.Thread(target=run_instabot, args=(username, password, ["allison23liu"], messages))
        # thread.start()
        # thread.join()
        send_msg(username, password, usernames, messages)


        # do something with the username and csv file
        if os.path.exists(file_path):
            os.remove(file_path)
        
        return render_template('index.html', message_sent='Sent all Messages')
        

    else:
        return jsonify({'result': 'error', 'message': 'Invalid file format'})

def send_msg(username, password, usernames, messages):
    try: 
        cookie_del = glob.glob("config/*cookie.json")
        os.remove(cookie_del[0])
    except Exception:
        None

    bot = Bot()
    bot.login(username=username, password=password, is_threaded = True)

    for user in usernames:
            
        bot.send_message(messages, [user])
        print("Sent to ", user)
    
    bot.logout()

# def run_instabot(username, password, usernames, messages):
#     print(username, password, str(usernames), messages)
#     subprocess.run(["python", "instascraper.py", "send_dms", username, password, str(usernames), str(messages)], check=True)

if __name__ == '__main__':
    # signal.signal(signal.SIGTERM, signal.SIG_IGN)
    # signal.signal(signal.SIGINT, signal.SIG_DFL)
    app.run(debug=True)
