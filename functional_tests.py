from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicity_wait(3)
        
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edyta dowiedziala sie o nowej, wspanialej aplikacji w postaci listy rzeczy do zrobienia
        # Postanowila wiec przejsc na glowna strone tej aplikacji
        self.browser.get('http://localhost:8000')

        # zwrocila uwage, ze tytul strony i naglowek zawieraja slowo Listy
        self.assertIn('Listy', self.browser.title)
        self.fail('Zakonczenie testu!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')

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

