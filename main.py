import time
import os


from prntframe.prntframework import Framework

# checa se a pasta imagens existe, se não existir ele cria a pasta e continua o script
if(os.path.exists('imagens') == False):
    os.mkdir('imagens')

# tela inicial do script
try:
    print("\n1 ... Tirar screenshot da página do aaaaaaa ao 9999999.\n")
    print("2 ... Tirar screenshot de uma página aleatória.\n")
    print("0 ... Sair\n")
    escolha = int(input("Escolha --> "))

    if(escolha == 1):
        prntframewk = Framework()
        print("Iniciando...")
        time.sleep(2)
        prntframewk.get_screenshot_one_by_one()
    elif(escolha == 2):
        prntframewk = Framework()
        print("Iniciando...")
        time.sleep(2)
        prntframewk.get_random_screenshot()
    elif(escolha == 0):
        print("Saindo...")
        exit()
    else:
        print("Escolha não reconhecida!")
except Exception as e:
    print("Erro: ", e)