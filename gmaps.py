import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service("C:\drivers\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service)
# Maximize the window
driver.maximize_window()
# URL
driver.get('https://www.google.co.id/maps/@-7.7628208,113.2165054,15z')
print(driver.title)
time.sleep(2)


#Search Lokasi
def searchLoc():
    location = driver.find_element(By.CLASS_NAME, 'tactile-searchbox-input')
    location.send_keys('Malang')

    time.sleep(2)

    firstLoc = driver.find_element(By.CLASS_NAME, 'ZHeE1b-icon')
    firstLoc.click()


searchLoc()
time.sleep(3)


#Set Route
def setRoute():
    route = driver.find_element(By.XPATH, '//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/button')
    route.click()


setRoute()
time.sleep(5)


#Durasi & Jarak
def durasiJarak():
    #Hitung durasi perjalanan
    durasiKota = driver.find_element(By.XPATH, '//*[@id="section-directions-trip-0"]/div/div[1]/div[1]/div[1]')
    print("Durasi perjalanan ke Kota Malang: ", durasiKota.text)
    #Hitung jarak perjalanan
    jarakKota = driver.find_element(By.XPATH, '//*[@id="section-directions-trip-0"]/div/div[1]/div[1]/div[2]')
    print("Jarak perjalanan ke Kota Malang: ", jarakKota.text)

    #tutup rute
    kemb = driver.find_element(By.XPATH, '//*[@id="omnibox-directions"]/div/div[2]/div/button')
    kemb.click()


durasiJarak()
time.sleep(3)


#Search Di Sekitar
def sekitar():
    icon = driver.find_element(By.XPATH, '//*[@id="pane"]/div/div[1]/div/div/div[4]/div[3]/button')
    icon.click()
    cariLokasi = driver.find_element(By.XPATH, '//*[@id="searchboxinput"]')
    cariLokasi.send_keys('Universitas Brawijaya')
    telusuri = driver.find_element(By.XPATH, '//*[@id="searchbox-searchbutton"]')
    telusuri.click()


sekitar()
time.sleep(3)


#Durasi & Jarak UB
def durasijarakUB():
    # Set rute
    rute = driver.find_element(By.XPATH, '//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div/div[2]/div[2]/div[2]/div[2]/button')
    rute.click()
    time.sleep(3)
    #Hitung durasi perjalanan
    durasiUB = driver.find_element(By.XPATH, '//*[@id="section-directions-trip-0"]/div/div[1]/div[1]/div[1]')
    print("Durasi perjalanan ke Universitas Brawijaya: ", durasiUB.text)
    jarakUB = driver.find_element(By.XPATH, '//*[@id="section-directions-trip-0"]/div/div[1]/div[1]/div[2]')
    print("Durasi perjalanan ke Universitas Brawijaya: ", jarakUB.text)


durasijarakUB()
driver.close()