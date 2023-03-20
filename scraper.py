from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

my_username = "yashwang23"
my_password = "testingwhatnot"
# usernames = [ 
#     "utileschic", "illustratorjake", "tuzineko", "dollipoppette", "kittenslittlewonders", "kawaiipaperdream", 
#     "kawaiigirlz.1", "lacasitadelasternuritas", "riversidekawaiishop", "katrinasdreamsshop", "holleyteatime", "polymernai", "luckyrainbowboutique", "divinegracehealing", "espa.cio120", "artemkemirov", 
#     "rainbelyart", "kawaiicraftlady", "cosmical_doll", "tiffstudioco", "jeanadraws", 
#     "kamiaristudio", "peque.store.pe", "oishi_toys", "mariahannxo", "vanillacookiestarshop", 
#     "fairyheartsshop", "usagistore40", "tofucute", "poussinetpoupette", "latelier.de.cabich", 
#     "kukistore.120", "opalandfern", "kanakodonnako", "psychobabyshop", "kozimocha", 
#     "stuffy_puffs", "natgreenart", "____aristocrats____bd", "poyura.co", "tiny.treasures__", "lulidelacroix", "lolifairies", 
#     "kutiecrafts", "resin.sweetshop", "runamishop", "mykawaiispace", "starlightsparklesart", "kawaiitherapy", "miffy_official", 
#     "lunas_emporium", "kawaiienvy", "sweetmagicpaper", "vanyarushop", "korekawaiistore", "damxspa", "ponyo_corniocosmico", "kawaiiteeshop", 
#     "thekawaiistory", "sh0ppeum", "candyhashi", "thebunbunshopofficial", "kawaiila_official", "thekawaiiconbini", "marofcreativity", "turtle.dove", 
#     "kizspurr", "becca_vicious", "harajukuyume", "songes_illustrations", "shopcosmiclovely", "nicole.josephine", 
#     "niji.usako.creations", "fairy.angelstore", "lacuchiwea", "10eestudio", 
#     "crystal_creations_shop", "himashop___", "vazoonlinestore", "kpop_store__italia", 
#     "otrio.stationery", "angelbunshop", "temps_dune_lolita", "designstudio_loliya",
#     "teo_fun_art", "rebelyellsdesign", "kawaiies.collection", 
#     "hiro.sep10ber", "bombo_maka.shop", "bluebearyco", "ubekeen", "kwaiishup_", "cautiivate",
#     "macarons_and_stilettos", "catmeilingcreations", "kumacolv", "sanriotyler", "dollipop_sweet_shoppe",
#     "anime.healing"]
usernames = ["utileschic", "illustratorjake", "tuzineko", "dollipoppette", "kittenslittlewonders", "kawaiipaperdream"]
messages = ["Hi! We’re running marketing and outreach tests on behalf of our company. Please disregard this message and have a great day!"]

#browser = webdriver.Chrome('chromedriver_mac_arm64')

def auth(username, password):
    try:
        browser.get('https://instagram.com')
        time.sleep(random.randrange(2,4))

        #wait for page to load
        # WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.NAME, "name")))
        # WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.NAME, "password")))

        input_username = browser.find_element("name", 'username')
        input_password = browser.find_element("name", 'password')

        input_username.send_keys(username)
        time.sleep(random.randrange(1,2))
        input_password.send_keys(password)
        time.sleep(random.randrange(1,2))
        input_password.send_keys(Keys.ENTER)
        time.sleep(random.randrange(1,2))
    except Exception as err:
        print(err)
        browser.quit()

def send_message(users, messages):
    try:
        #open messages tab
        time.sleep(random.randrange(2,4))
        WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/a/div"))).click()

        #browser.find_element("xpath", "/html/body/div[3]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/a/div").click()
        #browser.find_element("xpath", "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/a/div").click()
        time.sleep(random.randrange(3,5))
        #ignore notification
        #browser.find_element("xpath", "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
        WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]"))).click()

        for user in users:

            time.sleep(random.randrange(3,5))
            #click on send message
            WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[1]/div/div[3]/button"))).click()
            
            time.sleep(random.randrange(10,12))
            #search for user
            WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input"))).send_keys(user)

            #browser.find_element("xpath", "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input").send_keys(user)
            time.sleep(random.randrange(3,4))

            try: 
            #select user
                WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div/div[3]/div/button"))).click()
            except:
                WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/button"))).click()
                print("Failed tp send to", user)
                continue
                
            time.sleep(random.randrange(3,4))
            #click next
            WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button"))).click()
            time.sleep(random.randrange(3,4))
            #send a random message in the text box
            text_area = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")))
            text_area.send_keys(random.choice(messages))
            time.sleep(random.randrange(2,4))
            text_area.send_keys(Keys.ENTER)

            print("Succesfully sent to " + user)
            time.sleep(random.randrange(5,7))

            #time.sleep(random.randrange(240,250))
            




    except Exception as err:
        print(err)
        browser.quit()

# auth(my_username, my_password)
# time.sleep(random.randrange(3,5))
# send_message(usernames, messages)
