import itertools
import random
import string

from selenium import webdriver


class Framework:
    def __init__(self):
        try:
            self.web = webdriver.Firefox(executable_path="driver/geckodriver", log_path="geckodriver.log")
        except Exception as e:
            print("Erro:", e)

    def get_screenshot_one_by_one(self):
        try:
            template = string.ascii_lowercase + string.digits
            for x in itertools.product(template, repeat=8):
                template_path = x[1], x[2], x[3], x[4], x[5], x[6], x[7]
                template_path_formatado = str(template_path).replace(",", "").replace("'", "").replace("(", "").replace(
                    ")", "").replace(" ", "")

                self.web.get('https://prnt.sc/' + template_path_formatado)
                self.web.save_screenshot("imagens/" + template_path_formatado + ".png")
                print("screenshot tirada: ", template_path_formatado)
        except Exception as e:
            print("Erro:", e)


    def get_random_screenshot(self):
        while (True):
            try:
                template1 = string.ascii_lowercase + string.digits
                template2 = string.ascii_lowercase + string.digits
                template3 = string.ascii_lowercase + string.digits
                template4 = string.ascii_lowercase + string.digits
                template5 = string.ascii_lowercase + string.digits
                template6 = string.ascii_lowercase + string.digits
                template7 = string.ascii_lowercase + string.digits

                random_number_by_template1_length = random.randint(0, len(template1))
                random_number_by_template2_length = random.randint(0, len(template2))
                random_number_by_template3_length = random.randint(0, len(template3))
                random_number_by_template4_length = random.randint(0, len(template4))
                random_number_by_template5_length = random.randint(0, len(template5))
                random_number_by_template6_length = random.randint(0, len(template6))
                random_number_by_template7_length = random.randint(0, len(template7))
                template_path = template1[random_number_by_template1_length] + template2[
                    random_number_by_template2_length] + \
                                template3[random_number_by_template3_length] + template4[
                                    random_number_by_template4_length] + \
                                template5[random_number_by_template5_length] + template6[
                                    random_number_by_template6_length] + \
                                template7[random_number_by_template7_length]

                self.web.get('https://prnt.sc/' + template_path)
                self.web.save_screenshot("imagens/" + template_path + ".png")
                print("screenshot tirada: ", template_path)
            except Exception as e:
                print("Erro:", e)
