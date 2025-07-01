# 🚗 Kalkulator Wpływu Kół na Moc Pojazdu

## 📋 Opis

⚠️ **UWAGA: Skrypt eksperymentalny napisany na szybko - wyniki mogą być nieprecyzyjne!**

Prosty kalkulator do wstępnej analizy wpływu zmiany parametrów kół na moc i charakterystyki pojazdu. Program oblicza jak zmiana rozmiaru, masy i szerokości opon może wpływać na moment bezwładności, opory toczenia oraz dostępną moc na kołach.

**🚨 Używaj tylko jako wstępne oszacowanie - nie polegaj na wynikach przy ważnych decyzjach!**

## ⚡ Funkcjonalności

- **Analiza momentu bezwładności** - oblicza wpływ na przyspieszanie pojazdu
- **Ocena oporów toczenia** - uwzględnia masę i powierzchnię kontaktu
- **Wpływ na prędkość maksymalną** - analiza zmiany promienia koła
- **Szczegółowy raport** - procentowe zmiany wszystkich parametrów
- **Rekomendacje** - praktyczne wskazówki dotyczące wyboru kół
- **Intuicyjny interfejs** - prosty w użyciu interfejs tekstowy

## 🔧 Wymagania

- Python 3.6 lub nowszy
- Biblioteka `math` (standardowa w Pythonie)

## 📦 Instalacja

1. Sklonuj repozytorium:
```bash
git clone https://github.com/[twoja-nazwa]/kalkulator-kol-moc.git
cd kalkulator-kol-moc
```

2. Uruchom kalkulator:
```bash
python kalkulator_kol.py
```

## 🚀 Użycie

### Przykład użycia

```
============================================================
    KALKULATOR WPŁYWU ZMIANY KÓŁ NA MOC POJAZDU
============================================================

📊 WPROWADŹ DANE:
Moc na kołach [kW]: 200

🔧 KOŁO PIERWOTNE:
Średnica koła [mm]: 700
Szerokość opony [mm]: 225
Masa koła [kg]: 30

🔧 KOŁO NOWE:
Średnica koła [mm]: 750
Szerokość opony [mm]: 245
Masa koła [kg]: 33
```

### Interpretacja wyników

Kalkulator przedstawia wyniki w kilku sekcjach:

- **📏 Parametry** - porównanie specyfikacji kół
- **📈 Zmiany parametrów** - procentowe różnice
- **🚗 Wpływ na charakterystyki** - przyspieszanie i prędkość maksymalna
- **⚡ Wpływ na moc** - ostateczny wynik analizy
- **🔍 Analiza szczegółowa** - rozkład wpływu poszczególnych czynników
- **💡 Rekomendacje** - praktyczne wskazówki

## 📊 Przykładowe wyniki

```
⚡ WPŁYW NA MOC:
   Moc początkowa: 200.0 kW
   Moc po zmianie: 182.0 kW
   Zmiana mocy: -18.0 kW (-9.0%)

🔍 ANALIZA SZCZEGÓŁOWA:
   Wpływ momentu bezwładności: -8.0%
   Wpływ oporów toczenia: -3.0%
   Wpływ zmiany promienia: +2.0%
   Łączny wpływ: -9.0%
```

## 🧮 Metodologia obliczeń

### Moment bezwładności
```
I = 0.5 × m × r²
```
Gdzie:
- `I` - moment bezwładności [kg⋅m²]
- `m` - masa koła [kg]
- `r` - promień koła [m]

### Opory toczenia
Uwzględnia:
- Masę koła
- Powierzchnię kontaktu (szerokość × √średnica)
- Współczynniki empiryczne

### Wpływ na moc
Program analizuje:
- **Moment bezwładności** - wpływ na przyspieszanie (30% wagi)
- **Opory toczenia** - wpływ na zużycie energii (20% wagi)
- **Promień koła** - wpływ na prędkość maksymalną (30% wagi)

## 🎯 Zastosowania

⚠️ **Tylko do eksperymentów i nauki - nie do zastosowań profesjonalnych!**

- **Eksperymenty hobbystyczne** - wstępne oszacowanie wpływu kół
- **Nauka i edukacja** - zrozumienie podstawowych zasad fizyki pojazdu
- **Porównania względne** - analiza różnic między wariantami kół
- **Punkt startowy** - podstawa do dalszych, dokładniejszych analiz

**🚨 NIE używaj do:**
- Profesjonalnego tuningu
- Decyzji zakupowych o dużej wartości
- Projektowania komercyjnego
- Zastosowań wymagających precyzji

## 📚 Teoretyczne podstawy

Program bazuje na fundamentalnych prawach fizyki:

1. **Druga zasada dynamiki dla ruchu obrotowego**: `M = I × α`
2. **Kinematyka ruchu obrotowego**: `v = ω × r`
3. **Energia kinetyczna obrotowa**: `E = ½ × I × ω²`
4. **Opory toczenia**: zależne od masy i powierzchni kontaktu

## ⚠️ Ważne ostrzeżenia

**🚨 UWAGA: Ten skrypt został napisany szybko i nie był dokładnie sprawdzony!**

- **Wyniki mogą być błędne** - używaj tylko jako wstępne oszacowanie
- **Nie polegaj na obliczeniach** przy podejmowaniu ważnych decyzji
- **Przetestuj samodzielnie** przed wykorzystaniem w praktyce
- **To narzędzie eksperymentalne** - nie do zastosowań profesjonalnych

## 📝 Ograniczenia techniczne

- Model zakłada równomierny rozkład masy w kole
- Opory toczenia są oszacowane na podstawie modelu uproszczonego
- Nie uwzględnia wpływu aerodynamiki
- Wyniki są szacunkowe i mogą różnić się od rzeczywistych pomiarów
- Współczynniki empiryczne mogą być nieprecyzyjne
- Brak walidacji z rzeczywistymi testami

## 🤝 Wkład w projekt

Zapraszamy do współpracy! Możesz:

1. **Zgłaszać błędy** - otwórz issue z opisem problemu
2. **Proponować ulepszenia** - podziel się pomysłami
3. **Dodawać funkcjonalności** - prześlij pull request
4. **Poprawiać dokumentację** - każda pomoc jest cenna

### Jak dodać funkcjonalność

1. Stwórz fork repozytorium
2. Utwórz branch na nową funkcjonalność: `git checkout -b nowa-funkcjonalnost`
3. Wprowadź zmiany i przetestuj
4. Zatwierdź zmiany: `git commit -m "Dodano nową funkcjonalność"`
5. Wypchnij zmiany: `git push origin nowa-funkcjonalnost`
6. Otwórz Pull Request

## 📄 Licencja

Ten projekt jest udostępniony na licencji MIT. Zobacz plik `LICENSE` dla szczegółów.

```
MIT License

Copyright (c) 2025 Kalkulator Kół

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

## 👨‍💻 Autor

Stworzony z ❤️ dla społeczności motoryzacyjnej

## 🔗 Przydatne linki

- [Dokumentacja Python](https://docs.python.org/3/)
- [Podstawy mechaniki pojazdu](https://en.wikipedia.org/wiki/Vehicle_dynamics)
- [Moment bezwładności](https://pl.wikipedia.org/wiki/Moment_bezw%C5%82adno%C5%9Bci)

## 📈 Status projektu

![Python](https://img.shields.io/badge/Python-3.6+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Experimental-orange)
![Warning](https://img.shields.io/badge/⚠️-Not_Validated-red)

---

**⭐ Jeśli ten projekt Ci pomógł, zostaw gwiazdkę na GitHubie!**
