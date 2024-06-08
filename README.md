# s26302_ppy
Adam Harasimowicz
s26302
gr 18


Temat przykładowy - Kalkulator 
Kalkulator
Opis:
Twoim zadaniem jest stworzenie aplikacji konsolowej działającej jak kalkulator. Aplikacja
powinna umożliwić obliczanie bardziej złożonych wyrażeń poprzez przekazywanie wyniku
poprzedniego działania do następnego (np. 6+8 = 12 -> 12 / 4 = 3). Ponadto program
powinien przechowywać historię działań, do której użytkownik może mieć dostęp.
Wymagania:
1. Aplikacja powinna umożliwiać wykonywanie ciągu działań arytmetycznych.
2. Aplikacja powinna obsługiwać minimum dodawanie, odejmowanie, mnożenie,
dzielenie, potęgi, pierwiastki, procenty, silnię i operacje trygonometryczne (sin, cos,
tg, ctg).
3. Aplikacja powinna automatycznie wyświetlać historię ostatnich 5 operacji, z
możliwością cofania się do nich przy pomocy strzałek góra, dół.
4. Aplikacja powinna zapewniać interaktywny interfejs w konsoli.
5. Aplikacja powinna obsługiwać błędy, takie jak podanie nieprawidłowego znaku,
dzielenia przez 0 lub wpisaniu błędnego polecenia.
6. Użytkownik powinien otrzymywać odpowiednie komunikaty o błędach.

W projekcie zrealizowane zostały 4 klasy:

  Calculator - główna klasa odpowiadająca za wykonywanie operarcji, zarządzanie historią, oraz odpowiednie formatowanie napisu przekazanego przez użytkownika
    calculate - sprawdzenie wyrażenia, oblcizenie wyniku, wpis do historii
    factorial_finder - przygotowanie tekstu przekazanego przez użytkownika - obsługi znaku "!" jako silnia
    show_history - wyswietlenie operacji z historii
    select_from_history - wybór operacji z historii i wczytanie wartości x
    
  History - klasa zarządzająca historią obliczeń
    add - dodaje wyrażenie do historii
    get_last - zwaraca historię ostatnich wyrażeń
    
  ExpressionCalculator - klasa odpowiedzialna za oblcizanie wartości wyrażenia
    evaluate - metoda wykonująca obliczenia
    
  HandlerInput - klasa zarządzająca interakcją użytkownika z programem (tekst, nawigacja histori obliczeń)
    keyboard_action - obsluga naciśnięcia klawiszy
    clear_line - czyszczenie aktualnei wyświetlanej linii w konsoli 
    show_selected_history - wyswietla aktualne wybrane wyrażenie z historii
    run - główna pętla, nasłuchująca wejścia użytkownika


 Program pracuje w dwóch trybach - wybór historii lub prowadzenie obliczeń. Aby wyświetlić historię należy przekazać napis 'historia'

  W programie wprowadzono wartość - "x" która przyjmuje wartość ostatniego wyrażenia - lub wybranego z histori. Jest ona dostępna dla użytkownika w kolejnym działaniu poprzez podanie w przekazywanym ciagu wartości x, np
  2+2= 4  (wynik wyrażenia zostaje zapamiętany jako x=4)
  x*3 = 12 (4*3=12)

   
