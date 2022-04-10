import selenium
from selenium import webdriver
from pyshadow.main import Shadow
import time
from datetime import date
from webdriver_manager.chrome import ChromeDriverManager
import webdriver_manager.utils
from csv import writer
import pandas as pd
import numpy as np
from csv import writer

# Guardamos la fecha de la consulta
fecha = pd.to_datetime('today').normalize()

# Abrimos un driver de Chrome, utilizamos Install para que funcione en todos los PC independientemente de la versión que tenga
driver = webdriver.Chrome(ChromeDriverManager().install())

# Entramos en el plan 8h de Iberdrola
driver.get('https://www.iberdrola.es/luz/plan-elige-8-horas')
driver.implicitly_wait(5)

# Aceptamos las Cookies
cookies = driver.find_element_by_id('onetrust-accept-btn-handler')
cookies.click()

element = driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[3]/div[3]/p/span")
P2 = element.text
element = driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[3]/div[4]/p/span")

P1 = element.text
element = driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[3]/div[4]/p/span")
element = driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[4]/div[4]/p/span")

Te2 = element.text
element = driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[4]/div[3]/p/span")
Te1 = element.text
Te3 = np.nan

Plan8Horas_5kW = ["Plan 8 Horas", fecha, "< 5kW", Te1, Te2, Te3, P1, P2, (float(Te1.replace(",",".")) + float(Te2.replace(",",".")))/2, (float(P1.replace(",",".")) + float(P2.replace(",",".")))/2]
element = driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[2]/button[2]")
element.click()

P1 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[3]/div[4]/p/span").text
P2 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[3]/div[3]/p/span").text
Te2 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[4]/div[4]/p/span").text
Te1 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[4]/div[3]/p/span").text
Te3 =np.nan
Plan8Horas_10kW = ["Plan 8 Horas", fecha, "5 - 10kW", Te1, Te2, Te3, P1, P2, (float(Te1.replace(",",".")) + float(Te2.replace(",",".")))/2, (float(P1.replace(",",".")) + float(P2.replace(",",".")))/2]

element = driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[2]/button[3]")
element.click()

P1 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[3]/div[4]/p/span").text
P2 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[3]/div[3]/p/span").text
Te2 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[4]/div[4]/p/span").text
Te1 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[4]/div[3]/p/span").text
Te3 =np.nan
Plan8Horas_15kW = ["Plan 8 Horas", fecha, "10 - 15kW", Te1, Te2, Te3, P1, P2, (float(Te1.replace(",",".")) + float(Te2.replace(",",".")))/2, (float(P1.replace(",",".")) + float(P2.replace(",",".")))/2]

driver.get('https://www.iberdrola.es/luz/plan-noche')
driver.implicitly_wait(5)

P1 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[3]/div[4]/p/span").text
P2 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[3]/div[3]/p/span").text
Te2 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[4]/div[4]/p/span").text
Te1 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[4]/div[3]/p/span").text
Te3 =np.nan
PlanNoche_5kW = ["Plan Noche", fecha, "5kW", Te1, Te2, Te3, P1, P2, (float(Te1.replace(",",".")) + float(Te2.replace(",",".")))/2, (float(P1.replace(",",".")) + float(P2.replace(",",".")))/2]

element = driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[2]/button[2]")
element.click()

P1 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[3]/div[4]/p/span").text
P2 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[3]/div[3]/p/span").text
Te2 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[4]/div[4]/p/span").text
Te1 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[4]/div[3]/p/span").text
Te3 =np.nan
PlanNoche_10kW = ["Plan Noche", fecha, "5 - 10kW", Te1, Te2, Te3, P1, P2, (float(Te1.replace(",",".")) + float(Te2.replace(",",".")))/2, (float(P1.replace(",",".")) + float(P2.replace(",",".")))/2]

element = driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[2]/button[3]")
element.click()

P1 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[3]/div[4]/p/span").text
P2 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[3]/div[3]/p/span").text
Te2 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[4]/div[4]/p/span").text
Te1 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[4]/div[3]/p/span").text
Te3 =np.nan
PlanNoche_15kW = ["Plan Noche", fecha, "10 - 15kW", Te1, Te2, Te3, P1, P2, (float(Te1.replace(",",".")) + float(Te2.replace(",",".")))/2, (float(P1.replace(",",".")) + float(P2.replace(",",".")))/2]

driver.get("https://www.iberdrola.es/luz/plan-tres-periodos")

P2 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[3]/div[3]/p/span").text
P1 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[3]/div[4]/p/span").text
Te1 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[4]/div[5]/p/span").text
Te2 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[4]/div[4]/p/span").text
Te3 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[4]/div[3]/p/span").text
Plan3P_5kW = ["Plan 3 Periodos", fecha, "< 5kW", Te1, Te2, Te3, P1, P2, (float(Te1.replace(",",".")) + float(Te2.replace(",",".")) + float(Te3.replace(",",".")))/3, (float(P1.replace(",",".")) + float(P2.replace(",",".")))/2]

element = driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[2]/button[2]")
element.click()

P2 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[3]/div[3]/p/span").text
P1 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[3]/div[4]/p/span").text
Te1 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[4]/div[5]/p/span").text
Te2 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[4]/div[4]/p/span").text
Te3 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[4]/div[3]/p/span").text

Plan3P_10kW = ["Plan 3 Periodos", fecha, "5 - 10kW", Te1, Te2, Te3, P1, P2, (float(Te1.replace(",",".")) + float(Te2.replace(",",".")) + float(Te3.replace(",",".")))/3, (float(P1.replace(",",".")) + float(P2.replace(",",".")))/2]

element = driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[2]/button[3]")
element.click()

P2 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[3]/div[3]/p/span").text
P1 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[3]/div[4]/p/span").text
Te1 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[4]/div[5]/p/span").text
Te2 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[4]/div[4]/p/span").text
Te3 =driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/section[3]/div/div/div[2]/div[1]/div/article/div/div[4]/div[3]/p/span").text

Plan3P_15kW = ["Plan 3 Periodos", fecha, "10 - 15kW", Te1, Te2, Te3, P1, P2, (float(Te1.replace(",",".")) + float(Te2.replace(",",".")) + float(Te3.replace(",",".")))/3, (float(P1.replace(",",".")) + float(P2.replace(",",".")))/2]

with open("data.csv", 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(Plan8Horas_5kW)
        csv_writer.writerow(Plan3P_5kW)
        csv_writer.writerow(PlanNoche_5kW)
        csv_writer.writerow(Plan8Horas_10kW)
        csv_writer.writerow(Plan3P_10kW)
        csv_writer.writerow(PlanNoche_10kW)
        csv_writer.writerow(Plan8Horas_15kW)
        csv_writer.writerow(Plan3P_15kW)
        csv_writer.writerow(PlanNoche_15kW)
        write_obj.close()