## Test 
print('''Sprawdznie rejestracji użytkownika o już istniejącycm loginie.
Scenariusz negatywny - oczekujemy błędu rejestracji\n''')

from selenium import webdriver
przegladarka = webdriver.Firefox()
import time

lista_pol = {'nazwa':['username'],
             'haslo': ['pass1'],
             'powtHaslo': ['pass2'],
             'imie': ['name'],
             'nazwisko': ['surname'],
             'kodGrupy': ['kodgrupy']}

lista_przypadkow_testowych = {'nazwa' : ["Łukasz30"],
                             'haslo' : ["Bolaa"],
                             'powtHaslo': ['Bolaa'],
                             'imie' : ["Łukasz"],
                             'nazwisko' : ["Bola"],
                             'kodGrupy' : ["wsbpsto2018"]}



Time = 0.0001

print("Dane wykorzystane w teście to: ")
przegladarka.get('http://kmg.hcm.pl/testowanie/register.html')
przegladarka.maximize_window()

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
przegladarka.save_screenshot('TST_02_2.png')
komunikat = przegladarka.find_element_by_id('registerCom')
tekstKomunikatu = komunikat.text
przegladarka.quit()
time.sleep(Time)
##komunikat 1: Rejestracja przebiegła pomyślnie. Kliknij, aby się zalogować!
##komunikat 2: Użytkownik o takim loginie już istnieje!

print ("\n")
print ("=== Podsumowanie ===")
if "JUŻ ISTNIEJE" in tekstKomunikatu:
    print("Test przebiegł pomyślnie!\n")
    print("Wyświetlony komunikat błędu to:\n" + tekstKomunikatu)
else:
    print("Test NIE przebiegł pomyślnie!\n")
    print("Wyświetlony komunikat to:\n" + tekstKomunikatu)
print("Screen z wyniekiem testu znajduje się w pliku TST_02_2.png")






