from time import sleep as slp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

loginMail = "arquivoseestudos@gmail.com"
loginPass = "Senha@2023"
url = "https://frontend-lacrei-pessoa-usuaria.vercel.app/"

browser.get(url)

slp(5)

selectCMail = browser.find_element("xpath",'//*[@id="email"]')
selectCMail.click()
selectCMail.send_keys(loginMail)

selectCPass = browser.find_element("xpath",'//*[@id="password"]')
selectCPass.click()
selectCPass.send_keys(loginPass)

EnterLogin = browser.find_element("xpath",'//*[@id="__next"]/div/section/div/form/div[3]/div[1]/button')
EnterLogin.click()

slp(5)

textoElement = browser.find_element("xpath",'//*[@id="__next"]/div/section/div/h2[1]').text
msg = "Boas-vindas à Lacrei Saúde, continue o seu cadastro"

if msg == textoElement:
    print("#### Teste PASS! #####")
