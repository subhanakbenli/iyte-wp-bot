from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import calendar
from random import uniform
# Chrome seçeneklerini yapılandır
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Tarayıcıyı tam ekran başlat

# ChromeDriver servis yolu (gerekirse belirtin)
service = Service()  # Eğer chromedriver sistem PATH'inde ise, parametre gerekmez

# WebDriver'ı başlat
driver = webdriver.Chrome(service=service, options=chrome_options)

# İYTE yemek menüsü sayfasını aç
def get_menu(date_to_select):
    driver.get("https://yks.iyte.edu.tr/LoginYemekMenu.aspx")
    
    wait = WebDriverWait(driver, 10)
    date_input= wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="selectedMenuDate"]')))
    date_input.clear()
    date_input.send_keys(date_to_select)
    id_list =[ "GridView1", "GridViewVej", "GridViewVegan", "GridViewGltensiz"]
    total_data = []
    for id in id_list:
        menu = wait.until(EC.presence_of_element_located((By.ID,  id)))
        menu_data=[]
        for row in menu.find_elements(By.TAG_NAME, 'tr'):
            row_data =[]
            for cell in row.find_elements(By.TAG_NAME, 'td'):
                row_data.append(cell.text)
            menu_data.append(row_data)
        total_data.append([id,menu_data])


    return total_data


year = 2025
month = 5
days_in_month = calendar.monthrange(year, month)[1]
data_list = []

for day in range(1, days_in_month + 1):
    date_to_select = f"{day:02d}.{month:02d}.{year}"
    data = get_menu(date_to_select)
    data_list.append([f"{year}-{month:02d}-{day:02d}",data])
    time.sleep(0.5)  # Her tarih için 1 saniye bekle
    # Eğer çok uzun beklemeler istiyorsan time.sleep(3) gibi ekle
with open(f"{year}-{month:02}.txt", "w", encoding="utf-8") as f:
    f.write(str(data_list))

driver.quit()
