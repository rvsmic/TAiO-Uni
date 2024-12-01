# Projekt z Teorii Algorytmów i Obliczalności
*Theory of Algorithms and Computability project*

## Wymagania projektu

Program zawiera:
- ✅ Wyliczanie rozmiaru grafu
- ✅ Metrykę w zbiorze wszystkich grafów
- ✅ Wyliczanie maksymalnego cyklu w grafie
- ✅ Wyliczanie liczby maksymalnych cykli

Sprawozdanie zawiera:
- ✅ Opisy/definicje powyższych pojęć z uzasadnieniami/dowodami. Opisy mogą być przygotowane na podstawie literatury (wówczas należy przytoczyć źródło i podać krótkie uzasadnienie) lub opracowane autorsko (wówczas wskazane jest krótkie uzasadnienie przyjętej definicji)
- ✅ Opisy algorytmów implementacji pojęć z uzasadnieniem złożoności obliczeniowej. W przypadku wykładniczej złożoności algorytmu dokładnego należy opracować algorytm aproksymujący o złożoności wielomianowej
- ✅ Wyniki testów obliczeniowych z charakterystykami czasowymi ("czas" obliczeń w zależności od rozmiaru zadania).
- ✅ Krótki opis techniczny programu z dokładną instrukcją kompilacji i uruchomienia programu
- ✅ Wnioski

## Dane wejściowe
Pliki tekstowe zawierające opisy grafów (jednego lub więcej) oddzielone pustą linią. Pierwszy wiersz pliku zawiera liczbę grafów zapisanych w pliku. Od drugiego wiersza zapisane są opisy grafów:
- Pierwszy wiersz opisu zawiera liczbę wierzchołków, ta informacja jest zapisana w jednym wierszu pliku
- Następne wiersze pliku zawierają wiersze macierzy sąsiedztwa z elementami oddzielonymi spacją
- Po macierzy sąsiedztwa w kolejnych wierszach pliku mogą być zapisane dodatkowe dane

W macierzy sąsiedztwa zapisane są liczby krawędzi między wierzchołkami (dla grafów to będzie 0 lub 1). Dla grafów nieskierowanych macierz sąsiedztwa będzie symetryczna względem głównej przekątnej. Informację o rodzaju grafu można np. dodatkowo zapisać bezpośrednio po macierzy sąsiedztwa.
