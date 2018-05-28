## Test 
print('''Sprawdznie rejestracji użytkownika bez podania nazwy użytkownika.
Scenariusz negatywny - oczekujemy błedu rejestracji\n''')

from selenium import webdriver
przegladarka = webdriver.Firefox()
import time



lista_pol = {'nazwa':['username'],
             'haslo': ['pass1'],
             'powtHaslo': ['pass2'],
             'imie': ['name'],
             'nazwisko': ['surname'],
             'kodGrupy': ['kodgrupy']}

lista_przypadkow_testowych = {'nazwa' : [""],
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
przegladarka.save_screenshot('TST_02_3.png')
komunikat = przegladarka.find_element_by_id('registerCom')
tekstKomunikatu = komunikat.text
przegladarka.quit()
##komunikat 1: Rejestracja przebiegła pomyślnie. Kliknij, aby się zalogować!
##komunikat 2: Użytkownik o takim loginie już istnieje!

print ("\n")
print ("=== Podsumowanie ===")
if "NIE WYPEŁNIONO" in tekstKomunikatu:
    print("Test przebiegł pomyślnie!")
    print("Wyświetlony komunikat to:\n" + tekstKomunikatu)
else:
    print("Test NIE przebiegł pomyślnie!\n")
    print("Wyświetlony komunikat to:\n" + tekstKomunikatu)
print("Screen z wyniekiem testu znajduje się w pliku TST_02_3.png")






