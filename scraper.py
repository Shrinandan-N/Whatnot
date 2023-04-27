from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

#webdriver heroku code
import os
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1200,900")
#chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
#browser.set_window_size(1200, 900)

# options = Options()
# options.add_argument("start-maximized")
# browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# my_username = ""
# my_password = ""
usernames = [ 
    "kawaiipaperdream", 
    "kawaiigirlz.1", "lacasitadelasternuritas", "riversidekawaiishop", "katrinasdreamsshop", "holleyteatime", "polymernai", "luckyrainbowboutique", "divinegracehealing", "espa.cio120", "artemkemirov", 
    "rainbelyart", "kawaiicraftlady", "cosmical_doll", "tiffstudioco", "jeanadraws", 
    "kamiaristudio", "peque.store.pe", "oishi_toys", "mariahannxo", "vanillacookiestarshop", 
    "fairyheartsshop", "usagistore40", "tofucute", "poussinetpoupette", "latelier.de.cabich", 
    "kukistore.120", "opalandfern", "kanakodonnako", "psychobabyshop", "kozimocha", 
    "stuffy_puffs", "natgreenart", "____aristocrats____bd", "poyura.co", "tiny.treasures__", "lulidelacroix", "lolifairies", 
    "kutiecrafts", "resin.sweetshop", "runamishop", "mykawaiispace", "starlightsparklesart", "kawaiitherapy", "miffy_official", 
    "lunas_emporium", "kawaiienvy", "sweetmagicpaper", "vanyarushop", "korekawaiistore", "damxspa", "ponyo_corniocosmico", "kawaiiteeshop", 
    "thekawaiistory", "sh0ppeum", "candyhashi", "thebunbunshopofficial", "kawaiila_official", "thekawaiiconbini", "marofcreativity", "turtle.dove", 
    "kizspurr", "becca_vicious", "harajukuyume", "songes_illustrations", "shopcosmiclovely", "nicole.josephine", 
    "niji.usako.creations", "fairy.angelstore", "lacuchiwea", "10eestudio", 
    "crystal_creations_shop", "himashop___", "vazoonlinestore", "kpop_store__italia", 
    "otrio.stationery", "angelbunshop", "temps_dune_lolita", "designstudio_loliya",
    "teo_fun_art", "rebelyellsdesign", "kawaiies.collection", 
    "hiro.sep10ber", "bombo_maka.shop", "bluebearyco", "ubekeen", "kwaiishup_", "cautiivate",
    "macarons_and_stilettos", "catmeilingcreations", "kumacolv", "sanriotyler", "dollipop_sweet_shoppe",
    "anime.healing"]
#usernames = ["allison23liu"]
messages = ["Hi! We’re running marketing and outreach tests on behalf of our company. Please disregard this message and have a great day!"]

def auth(username, password):
    try:
        browser.get('https://instagram.com')
        print(browser.get_window_size())
        time.sleep(random.randrange(2,4))

        print("point 1: load website")

        #wait for page to load
        WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-label="Phone number, username, or email"]'))).click()
        #WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.NAME, "username"))).click()
        print("point 1.5")

        WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.NAME, "password")))

        input_username = browser.find_element(By.NAME, "username")
        input_password = browser.find_element(By.NAME, "password")

        print("point 2: found username & password entry location")

        input_username.send_keys(username)
        time.sleep(random.randrange(1,2))
        input_password.send_keys(password)
        time.sleep(random.randrange(1,2))
        input_password.send_keys(Keys.ENTER)
        time.sleep(random.randrange(1,2))

        print("point 3: successfully logged in")

    except Exception as err:
        print(err)
        browser.quit()

def send_message(users, messages):
    try:
        #open messages tab
        time.sleep(random.randrange(2,4))
        
        #ignore "Save login"
        WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,'//div[text()="Not Now"]'))).click()
        print("point 4: no to save login")

        #ignore "Turn on notifications"
        time.sleep(random.randrange(3,5))
        WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,'//button[text()="Not Now"]'))).click()
        print("point 5: no to enable notifications")

        #click on "Messages"
        time.sleep(random.randrange(3,5))
        WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/direct/inbox/']"))).click()
        print("point 6: navigate to message page")

        for user in users:
            time.sleep(random.randrange(3,5))

            if user == users[0]:
                #click on "Send message"
                WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Send Message"]'))).click()
            else:
                #click on writing icon
                WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[aria-label="New message"]'))).click()
            
            time.sleep(random.randrange(3,5))
            #search for user
            WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.NAME, "queryBox"))).send_keys(user)
            
            time.sleep(random.randrange(3,5))
            print("point 7: type in username")
            

            # try: 
            # #select user
            #     WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,'//circle'))).click()
            #     print("successfully selected user")
            # except:
            #     WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/button"))).click()
            #     print("Failed to send to", user)
            #     continue
            
            try:
                #click circle locate_with(By.TAG_NAME, "input").below({By.ID: "email"})
                WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[aria-label="Toggle selection"]'))).click()
                time.sleep(random.randrange(1,3))

                print("point 8: toggle selection")

                #click Next
                WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Next"]'))).click()
                time.sleep(random.randrange(1,3))
                print("point 9: clicks next")

                #send a random message in the text box
                typing = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//textarea')))
                print("passed 1")
                typing.send_keys(random.choice(messages) + Keys.ENTER)
                print("type + send message")

                # time.sleep(random.randrange(5, 7))
                # sending = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//textarea')))
                # sending.send_keys(Keys.ENTER)
                # time.sleep(random.randrange(10,15))
                # print("send message")

                print("Succesfully sent to " + user)

            except:
                print("Failed to send to " + user)
                continue

            #time.sleep(random.randrange(240,250))
            




    except Exception as err:
        print(err)
        browser.quit()

# auth(my_username, my_password)
# time.sleep(random.randrange(3,5))
# send_message(usernames, messages)
