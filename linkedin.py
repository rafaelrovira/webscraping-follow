from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

#PRECISA INSTALAR O WEBDRIVER DO NAVEGADOR E O SELENIUM
#EU UTILIZEI O GOOGLE CHROME
#APÓS ISSO, VOCÊ PEGA O SITE PELO PROTOCOLO GET

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.linkedin.com')
time.sleep(2)

# LOG IN

#PROCURA AS LABELS DE LOGIN E SENHA PELO XPATH DO ELEMENTO
usuario = driver.find_element_by_xpath("//input[@name='session_key']")
senha = driver.find_element_by_xpath("//input[@name='session_password']")

#AQUI VOCÊ COLOCA SEU LOGIN E SENHA PQ ELE VAI SER ENVIADO PRA DENTRO DAS LABELS QUE ACHOU ANTERIORMENTE
usuario.send_keys('Seu login')
senha.send_keys('Sua senha')
time.sleep(2)

#CLICA NO BOTÃO DE LOGAR
submit = driver.find_element_by_xpath("//button[@type='submit']").click()

# ADICIONAR CONTATOS 

#ENTRA NA PÁGINA DE PESQUISA DE CONEXÕES
driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page=10")
time.sleep(2)

#ACHA OS BOTÕES
all_buttons = driver.find_elements_by_tag_name("button")
connect_buttons = [btn for btn in all_buttons if btn.text == "Conectar"]

#CLICA NOS BOTÕES PARA CONECTAR, OU FECHAR A ABA CASO SEJA PRIVADO O PERFIL
#ELE CLICA UTILIZANDO SCRIPT, POIS SE FOR POR PYTHON O SITE BLOQUEIA OS BOTÕES E DÁ ERRO

for btn in connect_buttons:
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(2)
    send = driver.find_element_by_xpath("//button[@aria-label='Enviar agora']")
    driver.execute_script("arguments[0].click();", send)
    close = driver.find_element_by_xpath("//button[@aria-label='Fechar']")
    driver.execute_script("arguments[0].click();", close)
    time.sleep(2)