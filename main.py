import time

from prntframe.prntframework import Framework

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