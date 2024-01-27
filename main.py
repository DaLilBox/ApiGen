
 ███▄ ▄███▓ ▄▄▄      ▓█████▄ ▓█████     ▄▄▄▄ ▓██   ██▓   ▓█████▄  ▄▄▄       ██▓     ██▓ ██▓     ▄▄▄▄    ▒█████  ▒██   ██▒
▓██▒▀█▀ ██▒▒████▄    ▒██▀ ██▌▓█   ▀    ▓█████▄▒██  ██▒   ▒██▀ ██▌▒████▄    ▓██▒    ▓██▒▓██▒    ▓█████▄ ▒██▒  ██▒▒▒ █ █ ▒░
▓██    ▓██░▒██  ▀█▄  ░██   █▌▒███      ▒██▒ ▄██▒██ ██░   ░██   █▌▒██  ▀█▄  ▒██░    ▒██▒▒██░    ▒██▒ ▄██▒██░  ██▒░░  █   ░
▒██    ▒██ ░██▄▄▄▄██ ░▓█▄   ▌▒▓█  ▄    ▒██░█▀  ░ ▐██▓░   ░▓█▄   ▌░██▄▄▄▄██ ▒██░    ░██░▒██░    ▒██░█▀  ▒██   ██░ ░ █ █ ▒ 
▒██▒   ░██▒ ▓█   ▓██▒░▒████▓ ░▒████▒   ░▓█  ▀█▓░ ██▒▓░   ░▒████▓  ▓█   ▓██▒░██████▒░██░░██████▒░▓█  ▀█▓░ ████▓▒░▒██▒ ▒██▒
░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒▒▓  ▒ ░░ ▒░ ░   ░▒▓███▀▒ ██▒▒▒     ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒░▓  ░░▓  ░ ▒░▓  ░░▒▓███▀▒░ ▒░▒░▒░ ▒▒ ░ ░▓ ░
░  ░      ░  ▒   ▒▒ ░ ░ ▒  ▒  ░ ░  ░   ▒░▒   ░▓██ ░▒░     ░ ▒  ▒   ▒   ▒▒ ░░ ░ ▒  ░ ▒ ░░ ░ ▒  ░▒░▒   ░   ░ ▒ ▒░ ░░   ░▒ ░
░      ░     ░   ▒    ░ ░  ░    ░       ░    ░▒ ▒ ░░      ░ ░  ░   ░   ▒     ░ ░    ▒ ░  ░ ░    ░    ░ ░ ░ ░ ▒   ░    ░  
       ░         ░  ░   ░       ░  ░    ░     ░ ░           ░          ░  ░    ░  ░ ░      ░  ░ ░          ░ ░   ░    ░  
                      ░                      ░░ ░         ░                                          ░                   



from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

def generator():
    global value
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("--disable-gpu")
    options.add_experimental_option(
        "prefs", {
            "profile.managed_default_content_settings.images": 2,
        }
    )
    driver = webdriver.Chrome(options=options)
    driver.get("*") # *: entrer le lien du site
    input_element = driver.find_element(By.XPATH, "//input[@readonly and contains(@value, '*')]")  # *: entrer la valeur cherchée
    if input_element:
        value = input_element.get_attribute('value')
        print("Checking",value)
        driver.quit()

def checker(str):
    global code
    url = "*" + str + "**" # *: entrer début du lien de l'api **: entrer fin du lien de l'api
    response = requests.get(url)
    code = response.status_code

    if code == 200:
        print(str,"is valid")
        
    else:
        print(value,"is invalid")

while True:
    generator()
    checker(value)
    if code == 200:
        break
