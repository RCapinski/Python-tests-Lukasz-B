## Test 1
print('''Stworzenie konta z różnym od siebie hasłem oraz powtórzeniem hasła.
Scenariusz negatywn - oczekujemy błedu rejestracji.\n''')

from selenium import webdriver
przegladarka = webdriver.Firefox()
import time

lista_pol = {'nazwa':['username'],
             'haslo': ['pass1'],
             'powtHaslo': ['pass2'],
             'imie': ['name'],
             'nazwisko': ['surname'],
             'kodGrupy': ['kodgrupy']}

lista_przypadkow_testowych = {'nazwa' : ["Łukasz32"],
                             'haslo' : ["aaaaa"],
                             'powtHaslo': ['bbbbb'],
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
przegladarka.save_screenshot('TST_02_11.png')
komunikat = przegladarka.find_element_by_id('registerCom')
tekstKomunikatu = komunikat.text
przegladarka.quit()
##komunikat 1: Rejestracja przebiegła pomyślnie. Kliknij, aby się zalogować!
##komunikat 2: Użytkownik o takim loginie już istnieje!

print ("\n")
print ("=== Podsumowanie ===")
if "RÓŻNIĄ SIĘ" in tekstKomunikatu:
    print("Test przebiegł pomyślnie!\n")
    print("Wyświetlony komunikat to:\n" + tekstKomunikatu)
elif "JUŻ ISTNIEJE" in tekstKomunikatu:
    print("Wpisz nazwę użytkowinka, która nie została jeszcze zarejestrowana!,\nMusi być ona nazwą niedozwoloną. ")
else:
    print("Test NIE przebiegł pomyślnie! BŁĄD!\n")
    print("Wyświetlony komunikat to:\n" + tekstKomunikatu)
print("Screen z wyniekiem testu znajduje się w pliku TST_02_11.png")






