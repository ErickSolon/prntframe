import itertools
import random
import string

from selenium import webdriver


class Framework:
    # Início da classe
    def __init__(self):
        try:
            self.web = webdriver.Firefox(
                executable_path="driver/geckodriver", log_path="geckodriver.log")
        except Exception as e:
            print("Erro:", e)

    # tira screenshots de todos os URis um por um.
    def get_screenshot_one_by_one(self):
        try:
            template = string.ascii_letters + string.digits + "_-"
            for x in itertools.product(template, repeat=12):
                # Parte 12
                template_path = x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11]
                template_path_formatado = str(template_path).replace(",", "").replace("'", "").replace("(", "").replace(
                    ")", "").replace(" ", "")

                self.web.get('https://prnt.sc/' + template_path_formatado)
                self.web.save_screenshot(
                    "imagens/" + template_path_formatado + ".png")
                print("screenshot tirada: ", template_path_formatado)
        except Exception as e:
            print("Erro:", e)

    # tira screenshots aleatórias de todos os URis (pode haver repetições).
    def get_random_screenshot(self):
        while (True):
            try:
                template1 = string.ascii_letters + string.digits + "_-"
                template2 = string.ascii_letters + string.digits + "_-"
                template3 = string.ascii_letters + string.digits + "_-"
                template4 = string.ascii_letters + string.digits + "_-"
                template5 = string.ascii_letters + string.digits + "_-"
                template6 = string.ascii_letters + string.digits + "_-"
                template7 = string.ascii_letters + string.digits + "_-"
                template8 = string.ascii_letters + string.digits + "_-"
                template9 = string.ascii_letters + string.digits + "_-"
                template10 = string.ascii_letters + string.digits + "_-"
                template11 = string.ascii_letters + string.digits + "_-"
                template12 = string.ascii_letters + string.digits + "_-"

                random_number_by_template1_length = random.randint(
                    0, len(template1))
                random_number_by_template2_length = random.randint(
                    0, len(template2))
                random_number_by_template3_length = random.randint(
                    0, len(template3))
                random_number_by_template4_length = random.randint(
                    0, len(template4))
                random_number_by_template5_length = random.randint(
                    0, len(template5))
                random_number_by_template6_length = random.randint(
                    0, len(template6))
                random_number_by_template7_length = random.randint(
                    0, len(template7))
                random_number_by_template8_length = random.randint(
                    0, len(template8))
                random_number_by_template9_length = random.randint(
                    0, len(template9))
                random_number_by_template10_length = random.randint(
                    0, len(template10))
                random_number_by_template11_length = random.randint(
                    0, len(template11))
                random_number_by_template12_length = random.randint(
                    0, len(template12))

            
                etapa = random.randint(1, 12)
                
                if (etapa == 1):
                    template_path1 = template1[random_number_by_template1_length]

                    self.web.get(f'https://prnt.sc/{template_path1}')
                    self.web.save_screenshot(
                        "imagens/" + template_path1 + ".png")
                    print("screenshot tirada: ", template_path1)
                elif (etapa == 2):
                    template_path2 = template1[random_number_by_template1_length] + \
                        template2[random_number_by_template2_length]

                    self.web.get(f'https://prnt.sc/{template_path2}')
                    self.web.save_screenshot(
                        "imagens/" + template_path2 + ".png")
                    print("screenshot tirada: ", template_path2)
                elif (etapa == 3):
                    template_path3 = template1[random_number_by_template1_length] + \
                        template2[random_number_by_template2_length] + \
                        template3[random_number_by_template3_length]

                    self.web.get(f'https://prnt.sc/{template_path3}')
                    self.web.save_screenshot(
                        "imagens/" + template_path3 + ".png")
                    print("screenshot tirada: ", template_path3)
                elif (etapa == 4):
                    template_path4 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + \
                        template3[random_number_by_template3_length] + \
                        template4[random_number_by_template4_length]

                    self.web.get(f'https://prnt.sc/{template_path4}')
                    self.web.save_screenshot(
                        "imagens/" + template_path4 + ".png")
                    print("screenshot tirada: ", template_path4)
                elif (etapa == 5):
                    template_path5 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + \
                        template3[random_number_by_template3_length] + \
                        template4[random_number_by_template4_length] + \
                        template5[random_number_by_template5_length]

                    self.web.get(f'https://prnt.sc/{template_path5}')
                    self.web.save_screenshot(
                        "imagens/" + template_path5 + ".png")
                    print("screenshot tirada: ", template_path5)

                elif (etapa == 6):
                    template_path6 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + template3[random_number_by_template3_length] + \
                        template4[random_number_by_template4_length] + \
                        template5[random_number_by_template5_length] + \
                        template6[random_number_by_template6_length]

                    self.web.get(f'https://prnt.sc/{template_path6}')
                    self.web.save_screenshot(
                        "imagens/" + template_path6 + ".png")
                    print("screenshot tirada: ", template_path6)

                elif (etapa == 7):
                    template_path7 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + template3[random_number_by_template3_length] + \
                        template4[random_number_by_template4_length] + template5[random_number_by_template5_length] + \
                        template6[random_number_by_template6_length] + \
                        template7[random_number_by_template7_length]

                    self.web.get(f'https://prnt.sc/{template_path7}')
                    self.web.save_screenshot(
                        "imagens/" + template_path7 + ".png")
                    print("screenshot tirada: ", template_path7)

                elif (etapa == 8):
                    template_path8 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + template3[random_number_by_template3_length] + template4[random_number_by_template4_length] + \
                        template5[random_number_by_template5_length] + template6[random_number_by_template6_length] + \
                        template7[random_number_by_template7_length] + \
                        template8[random_number_by_template8_length]

                    self.web.get(f'https://prnt.sc/{template_path8}')
                    self.web.save_screenshot(
                        "imagens/" + template_path8 + ".png")
                    print("screenshot tirada: ", template_path8)

                elif (etapa == 9):
                    template_path9 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + template3[random_number_by_template3_length] + template4[random_number_by_template4_length] + \
                        template5[random_number_by_template5_length] + template6[random_number_by_template6_length] + \
                        template7[random_number_by_template7_length] + \
                        template8[random_number_by_template8_length] + \
                        template9[random_number_by_template9_length]

                    self.web.get(f'https://prnt.sc/{template_path9}')
                    self.web.save_screenshot(
                        "imagens/" + template_path9 + ".png")
                    print("screenshot tirada: ", template_path9)

                elif (etapa == 10):
                    template_path10 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + template3[random_number_by_template3_length] + template4[random_number_by_template4_length] + template5[random_number_by_template5_length] + \
                        template6[random_number_by_template6_length] + template7[random_number_by_template7_length] + \
                        template8[random_number_by_template8_length] + \
                        template9[random_number_by_template9_length] + \
                        template10[random_number_by_template10_length]

                    self.web.get(f'https://prnt.sc/{template_path10}')
                    self.web.save_screenshot(
                        "imagens/" + template_path10 + ".png")
                    print("screenshot tirada: ", template_path10)

                elif (etapa == 11):
                    template_path11 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + template3[random_number_by_template3_length] + template4[random_number_by_template4_length] + template5[random_number_by_template5_length] + \
                        template6[random_number_by_template6_length] + template7[random_number_by_template7_length] + template8[random_number_by_template8_length] + \
                        template9[random_number_by_template9_length] + \
                        template10[random_number_by_template10_length] + \
                        template11[random_number_by_template11_length]

                    self.web.get(f'https://prnt.sc/{template_path11}')
                    self.web.save_screenshot(
                        "imagens/" + template_path11 + ".png")
                    print("screenshot tirada: ", template_path11)

                elif (etapa == 12):
                    template_path12 = template1[random_number_by_template1_length] + template2[random_number_by_template2_length] + template3[random_number_by_template3_length] + template4[random_number_by_template4_length] + template5[random_number_by_template5_length] + template6[random_number_by_template6_length] + \
                        template7[random_number_by_template7_length] + template8[random_number_by_template8_length] + template9[random_number_by_template9_length] + \
                        template10[random_number_by_template10_length] + \
                        template11[random_number_by_template11_length] + \
                        template12[random_number_by_template12_length]

                    self.web.get(f'https://prnt.sc/{template_path12}')
                    self.web.save_screenshot(
                        "imagens/" + template_path12 + ".png")
                    print("screenshot tirada: ", template_path12)
                else:
                    pass
            except Exception as e:
                print("Erro:", e)
