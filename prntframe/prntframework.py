import itertools
import random
import string

from selenium import webdriver


class Framework:
    # Início da classe
    def __init__(self):
        try:
            self.web = webdriver.Firefox(executable_path="driver/geckodriver", log_path="geckodriver.log")
        except Exception as e:
            print("Erro:", e)

    # tira screenshots de todos os URis um por um.
    def get_screenshot_one_by_one(self):
        try:
            template = string.ascii_letters + string.digits
            for x in itertools.product(template, repeat=20):  
                              
                # Parte 1
                template_path = x[1]
                template_path_formatado = str(template_path).replace(",", "").replace("'", "").replace("(", "").replace(
                    ")", "").replace(" ", "")

                # Parte 2
                self.web.get('https://prnt.sc/' + template_path_formatado)
                self.web.save_screenshot("imagens/" + template_path_formatado + ".png")
                print("screenshot tirada: ", template_path_formatado)
                
                template_path = x[1], x[2]
                template_path_formatado = str(template_path).replace(",", "").replace("'", "").replace("(", "").replace(
                    ")", "").replace(" ", "")

                # Parte 3
                self.web.get('https://prnt.sc/' + template_path_formatado)
                self.web.save_screenshot("imagens/" + template_path_formatado + ".png")
                print("screenshot tirada: ", template_path_formatado)
                
                # Parte 4
                template_path = x[1], x[2], x[3]
                template_path_formatado = str(template_path).replace(",", "").replace("'", "").replace("(", "").replace(
                    ")", "").replace(" ", "")

                self.web.get('https://prnt.sc/' + template_path_formatado)
                self.web.save_screenshot("imagens/" + template_path_formatado + ".png")
                print("screenshot tirada: ", template_path_formatado)
                
                # Parte 5
                template_path = x[1], x[2], x[3], x[4]
                template_path_formatado = str(template_path).replace(",", "").replace("'", "").replace("(", "").replace(
                    ")", "").replace(" ", "")

                self.web.get('https://prnt.sc/' + template_path_formatado)
                self.web.save_screenshot("imagens/" + template_path_formatado + ".png")
                print("screenshot tirada: ", template_path_formatado)
                
                # Parte 6
                template_path = x[1], x[2], x[3], x[4], x[5]
                template_path_formatado = str(template_path).replace(",", "").replace("'", "").replace("(", "").replace(
                    ")", "").replace(" ", "")

                self.web.get('https://prnt.sc/' + template_path_formatado)
                self.web.save_screenshot("imagens/" + template_path_formatado + ".png")
                print("screenshot tirada: ", template_path_formatado)
                
                # Parte 7
                template_path = x[1], x[2], x[3], x[4], x[5], x[6]
                template_path_formatado = str(template_path).replace(",", "").replace("'", "").replace("(", "").replace(
                    ")", "").replace(" ", "")

                self.web.get('https://prnt.sc/' + template_path_formatado)
                self.web.save_screenshot("imagens/" + template_path_formatado + ".png")
                print("screenshot tirada: ", template_path_formatado)
                
                # Parte 8
                template_path = x[1], x[2], x[3], x[4], x[5], x[6], x[7]
                template_path_formatado = str(template_path).replace(",", "").replace("'", "").replace("(", "").replace(
                    ")", "").replace(" ", "")

                self.web.get('https://prnt.sc/' + template_path_formatado)
                self.web.save_screenshot("imagens/" + template_path_formatado + ".png")
                print("screenshot tirada: ", template_path_formatado)
                
                # Parte 9
                template_path = x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]
                template_path_formatado = str(template_path).replace(",", "").replace("'", "").replace("(", "").replace(
                    ")", "").replace(" ", "")

                self.web.get('https://prnt.sc/' + template_path_formatado)
                self.web.save_screenshot("imagens/" + template_path_formatado + ".png")
                print("screenshot tirada: ", template_path_formatado)
                
                # Parte 10
                template_path = x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9]
                template_path_formatado = str(template_path).replace(",", "").replace("'", "").replace("(", "").replace(
                    ")", "").replace(" ", "")

                self.web.get('https://prnt.sc/' + template_path_formatado)
                self.web.save_screenshot("imagens/" + template_path_formatado + ".png")
                print("screenshot tirada: ", template_path_formatado)
                
                # Parte 11
                template_path = x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10]
                template_path_formatado = str(template_path).replace(",", "").replace("'", "").replace("(", "").replace(
                    ")", "").replace(" ", "")

                self.web.get('https://prnt.sc/' + template_path_formatado)
                self.web.save_screenshot("imagens/" + template_path_formatado + ".png")
                print("screenshot tirada: ", template_path_formatado)
                
                # Parte 12
                template_path = x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11]
                template_path_formatado = str(template_path).replace(",", "").replace("'", "").replace("(", "").replace(
                    ")", "").replace(" ", "")

                self.web.get('https://prnt.sc/' + template_path_formatado)
                self.web.save_screenshot("imagens/" + template_path_formatado + ".png")
                print("screenshot tirada: ", template_path_formatado)
                
                # Parte 13
                template_path = x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12]
                template_path_formatado = str(template_path).replace(",", "").replace("'", "").replace("(", "").replace(
                    ")", "").replace(" ", "")

                self.web.get('https://prnt.sc/' + template_path_formatado)
                self.web.save_screenshot("imagens/" + template_path_formatado + ".png")
                print("screenshot tirada: ", template_path_formatado)
                
                # Parte 14
                template_path = x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13]
                template_path_formatado = str(template_path).replace(",", "").replace("'", "").replace("(", "").replace(
                    ")", "").replace(" ", "")

                self.web.get('https://prnt.sc/' + template_path_formatado)
                self.web.save_screenshot("imagens/" + template_path_formatado + ".png")
                print("screenshot tirada: ", template_path_formatado)
                
                # Parte 15
                template_path = x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14]
                template_path_formatado = str(template_path).replace(",", "").replace("'", "").replace("(", "").replace(
                    ")", "").replace(" ", "")

                self.web.get('https://prnt.sc/' + template_path_formatado)
                self.web.save_screenshot("imagens/" + template_path_formatado + ".png")
                print("screenshot tirada: ", template_path_formatado)
                
                # Parte 16
                template_path = x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14], x[15]
                template_path_formatado = str(template_path).replace(",", "").replace("'", "").replace("(", "").replace(
                    ")", "").replace(" ", "")

                self.web.get('https://prnt.sc/' + template_path_formatado)
                self.web.save_screenshot("imagens/" + template_path_formatado + ".png")
                print("screenshot tirada: ", template_path_formatado)
                
                # Parte 17
                template_path = x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14], x[15], x[16]
                template_path_formatado = str(template_path).replace(",", "").replace("'", "").replace("(", "").replace(
                    ")", "").replace(" ", "")

                self.web.get('https://prnt.sc/' + template_path_formatado)
                self.web.save_screenshot("imagens/" + template_path_formatado + ".png")
                print("screenshot tirada: ", template_path_formatado)
                
                # Parte 18
                template_path = x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14], x[15], x[16], x[17]
                template_path_formatado = str(template_path).replace(",", "").replace("'", "").replace("(", "").replace(
                    ")", "").replace(" ", "")

                self.web.get('https://prnt.sc/' + template_path_formatado)
                self.web.save_screenshot("imagens/" + template_path_formatado + ".png")
                print("screenshot tirada: ", template_path_formatado)
                
                # Parte 19
                template_path = x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14], x[15], x[16], x[17], x[18]
                template_path_formatado = str(template_path).replace(",", "").replace("'", "").replace("(", "").replace(
                    ")", "").replace(" ", "")

                self.web.get('https://prnt.sc/' + template_path_formatado)
                self.web.save_screenshot("imagens/" + template_path_formatado + ".png")
                print("screenshot tirada: ", template_path_formatado)
                
                # Última Parte
                template_path = x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14], x[15], x[16], x[17], x[18], x[19]
                template_path_formatado = str(template_path).replace(",", "").replace("'", "").replace("(", "").replace(
                    ")", "").replace(" ", "")

                self.web.get('https://prnt.sc/' + template_path_formatado)
                self.web.save_screenshot("imagens/" + template_path_formatado + ".png")
                print("screenshot tirada: ", template_path_formatado)
        except Exception as e:
            print("Erro:", e)

    # tira screenshots aleatórias de todos os URis (pode haver repetições).
    def get_random_screenshot(self):
        while (True):
            try:
                template1 = string.ascii_letters + string.digits
                template2 = string.ascii_letters + string.digits
                template3 = string.ascii_letters + string.digits
                template4 = string.ascii_letters + string.digits
                template5 = string.ascii_letters + string.digits
                template6 = string.ascii_letters + string.digits
                template7 = string.ascii_letters + string.digits
                template8 = string.ascii_letters + string.digits
                template9 = string.ascii_letters + string.digits
                template10 = string.ascii_letters + string.digits
                template11 = string.ascii_letters + string.digits
                template12 = string.ascii_letters + string.digits
                template13 = string.ascii_letters + string.digits
                template14 = string.ascii_letters + string.digits
                template15 = string.ascii_letters + string.digits
                template16 = string.ascii_letters + string.digits
                template17 = string.ascii_letters + string.digits
                template18 = string.ascii_letters + string.digits
                template19 = string.ascii_letters + string.digits
                template20 = string.ascii_letters + string.digits

                random_number_by_template1_length = random.randint(0, len(template1))
                random_number_by_template2_length = random.randint(0, len(template2))
                random_number_by_template3_length = random.randint(0, len(template3))
                random_number_by_template4_length = random.randint(0, len(template4))
                random_number_by_template5_length = random.randint(0, len(template5))
                random_number_by_template6_length = random.randint(0, len(template6))
                random_number_by_template7_length = random.randint(0, len(template7))
                random_number_by_template8_length = random.randint(0, len(template8))
                random_number_by_template9_length = random.randint(0, len(template9))
                random_number_by_template10_length = random.randint(0, len(template10))
                random_number_by_template11_length = random.randint(0, len(template11))
                random_number_by_template12_length = random.randint(0, len(template12))
                random_number_by_template13_length = random.randint(0, len(template13))
                random_number_by_template14_length = random.randint(0, len(template14))
                random_number_by_template15_length = random.randint(0, len(template15))
                random_number_by_template16_length = random.randint(0, len(template16))
                random_number_by_template17_length = random.randint(0, len(template17))
                random_number_by_template18_length = random.randint(0, len(template18))
                random_number_by_template19_length = random.randint(0, len(template19))
                random_number_by_template20_length = random.randint(0, len(template20))
                
                while True:                    
                    etapa = random.randint(1, 19)
                    if(etapa == 1):
                        template_path1 = template1[random_number_by_template1_length]

                        self.web.get('https://prnt.sc/' + template_path1)
                        self.web.save_screenshot("imagens/" + template_path1 + ".png")
                        print("screenshot tirada: ", template_path1)    
                    elif(etapa == 2):
                        template_path2 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length]

                        self.web.get('https://prnt.sc/' + template_path2)
                        self.web.save_screenshot("imagens/" + template_path2 + ".png")
                        print("screenshot tirada: ", template_path2)  
                    elif(etapa == 3):
                        template_path3 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + template3[random_number_by_template3_length]

                        self.web.get('https://prnt.sc/' + template_path3)
                        self.web.save_screenshot("imagens/" + template_path3 + ".png")
                        print("screenshot tirada: ", template_path3)  
                    elif(etapa == 4):
                        template_path4 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + template3[random_number_by_template3_length] + template4[random_number_by_template4_length]

                        self.web.get('https://prnt.sc/' + template_path4)
                        self.web.save_screenshot("imagens/" + template_path4 + ".png")
                        print("screenshot tirada: ", template_path4)  
                    elif(etapa == 5):
                        template_path5 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + template3[random_number_by_template3_length] + template4[random_number_by_template4_length] + template5[random_number_by_template5_length]

                        self.web.get('https://prnt.sc/' + template_path5)
                        self.web.save_screenshot("imagens/" + template_path5 + ".png")
                        print("screenshot tirada: ", template_path5)
                        
                    elif(etapa == 6):
                        template_path6 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + template3[random_number_by_template3_length] + template4[random_number_by_template4_length] + template5[random_number_by_template5_length] + template6[random_number_by_template6_length]

                        self.web.get('https://prnt.sc/' + template_path6)
                        self.web.save_screenshot("imagens/" + template_path6 + ".png")
                        print("screenshot tirada: ", template_path6)
                        
                    elif(etapa == 7):
                        template_path7 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + template3[random_number_by_template3_length] + template4[random_number_by_template4_length] + template5[random_number_by_template5_length] + template6[random_number_by_template6_length] + template7[random_number_by_template7_length]

                        self.web.get('https://prnt.sc/' + template_path7)
                        self.web.save_screenshot("imagens/" + template_path7 + ".png")
                        print("screenshot tirada: ", template_path7)
                        
                    elif(etapa == 8):
                        template_path8 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + template3[random_number_by_template3_length] + template4[random_number_by_template4_length] + template5[random_number_by_template5_length] + template6[random_number_by_template6_length] + template7[random_number_by_template7_length] + template8[random_number_by_template8_length]

                        self.web.get('https://prnt.sc/' + template_path8)
                        self.web.save_screenshot("imagens/" + template_path8 + ".png")
                        print("screenshot tirada: ", template_path8)
                        
                    elif(etapa == 9):
                        template_path9 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + template3[random_number_by_template3_length] + template4[random_number_by_template4_length] + template5[random_number_by_template5_length] + template6[random_number_by_template6_length] + template7[random_number_by_template7_length] + template8[random_number_by_template8_length] + template9[random_number_by_template9_length]

                        self.web.get('https://prnt.sc/' + template_path9)
                        self.web.save_screenshot("imagens/" + template_path9 + ".png")
                        print("screenshot tirada: ", template_path9)
                        
                    elif(etapa == 10):
                        template_path10 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + template3[random_number_by_template3_length] + template4[random_number_by_template4_length] + template5[random_number_by_template5_length] + template6[random_number_by_template6_length] + template7[random_number_by_template7_length] + template8[random_number_by_template8_length] + template9[random_number_by_template9_length] + template10[random_number_by_template10_length]

                        self.web.get('https://prnt.sc/' + template_path10)
                        self.web.save_screenshot("imagens/" + template_path10 + ".png")
                        print("screenshot tirada: ", template_path10)
                        
                    elif(etapa == 11):
                        template_path11 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + template3[random_number_by_template3_length] + template4[random_number_by_template4_length] + template5[random_number_by_template5_length] + template6[random_number_by_template6_length] + template7[random_number_by_template7_length] + template8[random_number_by_template8_length] + template9[random_number_by_template9_length] + template10[random_number_by_template10_length] + template11[random_number_by_template11_length]

                        self.web.get('https://prnt.sc/' + template_path11)
                        self.web.save_screenshot("imagens/" + template_path11 + ".png")
                        print("screenshot tirada: ", template_path11)
                        
                    elif(etapa == 12):
                        template_path12 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + template3[random_number_by_template3_length] + template4[random_number_by_template4_length] + template5[random_number_by_template5_length] + template6[random_number_by_template6_length] + template7[random_number_by_template7_length] + template8[random_number_by_template8_length] + template9[random_number_by_template9_length] + template10[random_number_by_template10_length] + template11[random_number_by_template11_length] + template12[random_number_by_template12_length]

                        self.web.get('https://prnt.sc/' + template_path12)
                        self.web.save_screenshot("imagens/" + template_path12 + ".png")
                        print("screenshot tirada: ", template_path12)
                        
                    elif(etapa == 13):
                        template_path13 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + template3[random_number_by_template3_length] + template4[random_number_by_template4_length] + template5[random_number_by_template5_length] + template6[random_number_by_template6_length] + template7[random_number_by_template7_length] + template8[random_number_by_template8_length] + template9[random_number_by_template9_length] + template10[random_number_by_template10_length] + template11[random_number_by_template11_length] + template12[random_number_by_template12_length] + template13[random_number_by_template13_length]

                        self.web.get('https://prnt.sc/' + template_path13)
                        self.web.save_screenshot("imagens/" + template_path13 + ".png")
                        print("screenshot tirada: ", template_path13)
                        
                    elif(etapa == 14):
                        template_path14 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + template3[random_number_by_template3_length] + template4[random_number_by_template4_length] + template5[random_number_by_template5_length] + template6[random_number_by_template6_length] + template7[random_number_by_template7_length] + template8[random_number_by_template8_length] + template9[random_number_by_template9_length] + template10[random_number_by_template10_length] + template11[random_number_by_template11_length] + template12[random_number_by_template12_length] + template13[random_number_by_template13_length] + template14[random_number_by_template14_length]

                        self.web.get('https://prnt.sc/' + template_path14)
                        self.web.save_screenshot("imagens/" + template_path14 + ".png")
                        print("screenshot tirada: ", template_path14)
                        
                    elif(etapa == 15):
                        template_path15 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + template3[random_number_by_template3_length] + template4[random_number_by_template4_length] + template5[random_number_by_template5_length] + template6[random_number_by_template6_length] + template7[random_number_by_template7_length] + template8[random_number_by_template8_length] + template9[random_number_by_template9_length] + template10[random_number_by_template10_length] + template11[random_number_by_template11_length] + template12[random_number_by_template12_length] + template13[random_number_by_template13_length] + template14[random_number_by_template14_length] + template15[random_number_by_template15_length]

                        self.web.get('https://prnt.sc/' + template_path15)
                        self.web.save_screenshot("imagens/" + template_path15 + ".png")
                        print("screenshot tirada: ", template_path15)
                        
                    elif(etapa == 16):
                        template_path16 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + template3[random_number_by_template3_length] + template4[random_number_by_template4_length] + template5[random_number_by_template5_length] + template6[random_number_by_template6_length] + template7[random_number_by_template7_length] + template8[random_number_by_template8_length] + template9[random_number_by_template9_length] + template10[random_number_by_template10_length] + template11[random_number_by_template11_length] + template12[random_number_by_template12_length] + template13[random_number_by_template13_length] + template14[random_number_by_template14_length] + template15[random_number_by_template15_length] + template16[random_number_by_template16_length]

                        self.web.get('https://prnt.sc/' + template_path16)
                        self.web.save_screenshot("imagens/" + template_path16 + ".png")
                        print("screenshot tirada: ", template_path16)
                        
                    elif(etapa == 17):
                        template_path17 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + template3[random_number_by_template3_length] + template4[random_number_by_template4_length] + template5[random_number_by_template5_length] + template6[random_number_by_template6_length] + template7[random_number_by_template7_length] + template8[random_number_by_template8_length] + template9[random_number_by_template9_length] + template10[random_number_by_template10_length] + template11[random_number_by_template11_length] + template12[random_number_by_template12_length] + template13[random_number_by_template13_length] + template14[random_number_by_template14_length] + template15[random_number_by_template15_length] + template16[random_number_by_template16_length] + template17[random_number_by_template17_length]

                        self.web.get('https://prnt.sc/' + template_path17)
                        self.web.save_screenshot("imagens/" + template_path17 + ".png")
                        print("screenshot tirada: ", template_path17)
                        
                    elif(etapa == 18):
                        template_path18 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + template3[random_number_by_template3_length] + template4[random_number_by_template4_length] + template5[random_number_by_template5_length] + template6[random_number_by_template6_length] + template7[random_number_by_template7_length] + template8[random_number_by_template8_length] + template9[random_number_by_template9_length] + template10[random_number_by_template10_length] + template11[random_number_by_template11_length] + template12[random_number_by_template12_length] + template13[random_number_by_template13_length] + template14[random_number_by_template14_length] + template15[random_number_by_template15_length] + template16[random_number_by_template16_length] + template17[random_number_by_template17_length] + template18[random_number_by_template18_length]

                        self.web.get('https://prnt.sc/' + template_path18)
                        self.web.save_screenshot("imagens/" + template_path18 + ".png")
                        print("screenshot tirada: ", template_path18)
                        
                    elif(etapa == 19):
                        template_path19 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + template3[random_number_by_template3_length] + template4[random_number_by_template4_length] + template5[random_number_by_template5_length] + template6[random_number_by_template6_length] + template7[random_number_by_template7_length] + template8[random_number_by_template8_length] + template9[random_number_by_template9_length] + template10[random_number_by_template10_length] + template11[random_number_by_template11_length] + template12[random_number_by_template12_length] + template13[random_number_by_template13_length] + template14[random_number_by_template14_length] + template15[random_number_by_template15_length] + template16[random_number_by_template16_length] + template17[random_number_by_template17_length] + template18[random_number_by_template18_length] + template19[random_number_by_template19_length]

                        self.web.get('https://prnt.sc/' + template_path19)
                        self.web.save_screenshot("imagens/" + template_path19 + ".png")
                        print("screenshot tirada: ", template_path19)
                        
                    elif(etapa == 20):
                        template_path20 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + template3[random_number_by_template3_length] + template4[random_number_by_template4_length] + template5[random_number_by_template5_length] + template6[random_number_by_template6_length] + template7[random_number_by_template7_length] + template8[random_number_by_template8_length] + template9[random_number_by_template9_length] + template10[random_number_by_template10_length] + template11[random_number_by_template11_length] + template12[random_number_by_template12_length] + template13[random_number_by_template13_length] + template14[random_number_by_template14_length] + template15[random_number_by_template15_length] + template16[random_number_by_template16_length] + template17[random_number_by_template17_length] + template18[random_number_by_template18_length] + template19[random_number_by_template19_length]  + template20[random_number_by_template20_length]

                        self.web.get('https://prnt.sc/' + template_path20)
                        self.web.save_screenshot("imagens/" + template_path20 + ".png")
                        print("screenshot tirada: ", template_path20)
                    else:
                        pass
            except Exception as e:
                print("Erro:", e)
