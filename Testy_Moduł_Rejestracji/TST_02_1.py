## Test 
print('''Stworzenie konta używając poprawnych danych.
Scenariusz POZYTYWNY - oczekujemy komunikatu poprawnej rejestracji.\n''')

from selenium import webdriver
przegladarka = webdriver.Firefox()
import time
import datetime
a = datetime.date.isoformat(datetime.date.today())+time.strftime("%H%M%S")  

lista_pol = {'nazwa':['username'],
             'haslo': ['pass1'],
             'powtHaslo': ['pass2'],
             'imie': ['name'],
             'nazwisko': ['surname'],
             'kodGrupy': ['kodgrupy']}

lista_przypadkow_testowych = {'nazwa' : ["Łukasz"+a],
                             'haslo' : ["Bolaa"],
                             'powtHaslo': ['Bolaa'],
                             'imie' : ["Łukasz"],
                             'nazwisko' : ["Bola"],
                             'kodGrupy' : ["wsbpsto2018"]}

przegladarka.get('http://kmg.hcm.pl/testowanie/register.html')

Time = 0.00001

przegladarka.maximize_window()
time.sleep(Time)
print("Dane wykorzystane w teście to: ")
for pola in lista_pol:
    nazwa = przegladarka.find_element_by_id(lista_pol[pola][0])
    nazwa.click()
    time.sleep(Time)
    for fraza in lista_przypadkow_testowych[pola]:
        nazwa.send_keys(lista_przypadkow_testowych[pola][0])
        time.sleep(Time)
    print( pola + ": " + fraza)
rejestruj = przegladarka.find_element_by_id("register")
rejestruj.click()
time.sleep(1)
przegladarka.save_screenshot('TST_02_1.png')
komunikat = przegladarka.find_element_by_id('registerCom')
tekstKomunikatu = komunikat.text

##komunikat 1: Rejestracja przebiegła pomyślnie. Kliknij, aby się zalogować!
##komunikat 2: Użytkownik o takim loginie już istnieje!

print ("\n")
print ("=== Podsumowanie ===")
if "REJESTRACJA PRZEBIEGŁA POMYŚLNIE" in tekstKomunikatu:
    print("Test przebiegł pomyślnie!")
    print("Wyświetlony komunikat to:\n" + tekstKomunikatu)
else:
    print("Test NIE przebiegł pomyślnie!\n")
    print("Wyświetlony komunikat błędu to:\n" + tekstKomunikatu)
print("Screen z wyniekiem testu znajduje się w pliku TST_02_1.png")

time.sleep(1)
powrótDoLogowania = przegladarka.find_element_by_xpath("//A[@href='index.html'][text()='Kliknij, aby się zalogować!']")
powrótDoLogowania.click()
time.sleep(1)
if przegladarka.find_element_by_xpath("//INPUT[@id='login']"):
    time.sleep(1)
    print("Przycisk powrotu do logowania również działa.")
    print("Test przebiegł pomyślnie!")
else:
    print("Przycisk zalogowanie po rejestracji nie działa.")
    print("Test NIE przebiegł pomyślnie!\n")

przegladarka.quit()
