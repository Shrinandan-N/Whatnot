from instabot import Bot
import os 
import glob
import time, random
import sys


def send_dms(username, password, usernames, messages):
    
    usernames = [x for x in usernames[1:-1].split(", ")]
    messages = [x for x in messages[1:-1].split(", ")]

    try: 
        cookie_del = glob.glob("config/*cookie.json")
        os.remove(cookie_del[0])
    except Exception:
        None

    bot = Bot()
    bot.login(username=username, password=password)

    for user in usernames:
            
        bot.send_message(messages, [user])
        print("Sent to ", user)
    
    bot.logout()

if __name__ == '__main__':
    username = sys.argv[2]
    password = sys.argv[3]
    usernames = sys.argv[4]
    messages = sys.argv[5]
    print(username, password, str(usernames), messages)

    send_dms(username, password, usernames, messages)




#send_msg("rychen2448", "goatboat10", ["allison23liu"], "Hi! We’re running marketing and outreach tests on behalf of our company. Please disregard this message and have a great day!")
# os.rmdir("config")

