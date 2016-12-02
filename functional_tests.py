from selenium import webdriver

browser = webdriver.Firefox()

# Edyta dowiedziala sie o nowej, wspanialej aplikacji w postaci listy rzeczy do zrobienia
# Pstanowila wiec przejsc na glowna strone tej aplikacji
browser.get('http://localhost:8000')
# zwrocila uwage, ze tytul strony i naglowek zawieraja slowo Listy
assert 'Listy' in browser.title
# Od razu zostaje zachecona, aby wspisac rzecz do zrobienia

# W polu tekstowym wpisala "Kupic pawie piora " (hobby Edyty
# polega na tworzeniu ozdobnych przynet

# Po nacisnieciu klawisza Enter strona zostala uaktualniona i wyslietla
# "1: Kupic pawie piora" jako element listy rzeczy do zrobienia

# Na stronie nadal znajduje sie pole tekstowe zachecajace do podania kolejnego zadania
# Edyta wpisala "Uzyc pawich pior do zrobienia przyjety" (Edyta jest niezwykle skrupulatna)

# Strona zostala ponownie uaktualniona i teraz wyswietla dwa elementy na liscie rzeczy do zrobienia

# Edyta byla ciekawa czy witryna zapamieta jej liste. Zwrocila uwage na wygenerowany dla niej
# unikatowy adrs URL, obok ktorego znajduje sie pewnien tekst z wyjasnieniem

# Przechodzi pod podany adres URL i widzi wyswietlona swoja liste rzeczy do zrobienia

# Usatysfakcjonowania kladzie sie spac

browser.quit