#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kalkulator wpływu zmiany parametrów kół na moc pojazdu
Autor: Asystent AI
"""

import math

def oblicz_moment_bezwladnosci(masa_kg, promien_m):
    """
    Oblicza moment bezwładności koła (zakładając równomierny rozkład masy)
    I = 0.5 * m * r^2
    """
    return 0.5 * masa_kg * (promien_m ** 2)

def oblicz_objetosc_opony(srednica_mm, szerokosc_mm):
    """
    Szacuje objętość opony (uproszczony model)
    """
    promien_m = srednica_mm / 2000  # konwersja mm na m
    szerokosc_m = szerokosc_mm / 1000  # konwersja mm na m
    # Przybliżona objętość jako torus
    objetosc = 2 * math.pi**2 * promien_m * (szerokosc_m/2)**2
    return objetosc

def oblicz_opory_toczenia(masa_kg, srednica_mm, szerokosc_mm):
    """
    Szacuje względne opory toczenia
    """
    # Współczynnik oparty na masie i powierzchni kontaktu
    powierzchnia_kontaktu = szerokosc_mm * math.sqrt(srednica_mm)
    return masa_kg * powierzchnia_kontaktu / 100000  # normalizacja

def kalkulator_mocy_kol():
    print("=" * 60)
    print("    KALKULATOR WPŁYWU ZMIANY KÓŁ NA MOC POJAZDU")
    print("=" * 60)
    
    try:
        # Wprowadzenie danych
        print("\n📊 WPROWADŹ DANE:")
        moc_poczatkowa = float(input("Moc na kołach [kW]: "))
        
        print("\n🔧 KOŁO PIERWOTNE:")
        srednica_1 = float(input("Średnica koła [mm]: "))
        szerokosc_1 = float(input("Szerokość opony [mm]: "))
        masa_1 = float(input("Masa koła [kg]: "))
        
        print("\n🔧 KOŁO NOWE:")
        srednica_2 = float(input("Średnica koła [mm]: "))
        szerokosc_2 = float(input("Szerokość opony [mm]: "))
        masa_2 = float(input("Masa koła [kg]: "))
        
        # Obliczenia podstawowe
        promien_1 = srednica_1 / 2000  # konwersja mm na m
        promien_2 = srednica_2 / 2000
        
        moment_1 = oblicz_moment_bezwladnosci(masa_1, promien_1)
        moment_2 = oblicz_moment_bezwladnosci(masa_2, promien_2)
        
        opory_1 = oblicz_opory_toczenia(masa_1, srednica_1, szerokosc_1)
        opory_2 = oblicz_opory_toczenia(masa_2, srednica_2, szerokosc_2)
        
        # Stosunki zmian
        stosunek_momentow = moment_2 / moment_1
        stosunek_promieni = promien_2 / promien_1
        stosunek_mas = masa_2 / masa_1
        stosunek_oporow = opory_2 / opory_1
        
        # Wyniki
        print("\n" + "=" * 60)
        print("                    WYNIKI ANALIZY")
        print("=" * 60)
        
        print(f"\n📏 PARAMETRY POCZĄTKOWE:")
        print(f"   Koło: ⌀{srednica_1:.0f}mm × {szerokosc_1:.0f}mm, {masa_1:.1f}kg")
        print(f"   Moment bezwładności: {moment_1:.4f} kg⋅m²")
        print(f"   Względne opory: {opory_1:.2f}")
        
        print(f"\n📏 PARAMETRY NOWE:")
        print(f"   Koło: ⌀{srednica_2:.0f}mm × {szerokosc_2:.0f}mm, {masa_2:.1f}kg")
        print(f"   Moment bezwładności: {moment_2:.4f} kg⋅m²")
        print(f"   Względne opory: {opory_2:.2f}")
        
        print(f"\n📈 ZMIANY PARAMETRÓW:")
        print(f"   Moment bezwładności: {(stosunek_momentow-1)*100:+.1f}%")
        print(f"   Promień koła: {(stosunek_promieni-1)*100:+.1f}%")
        print(f"   Masa koła: {(stosunek_mas-1)*100:+.1f}%")
        print(f"   Opory toczenia: {(stosunek_oporow-1)*100:+.1f}%")
        
        # Analiza wpływu na charakterystyki
        zmiana_przyspieszenia = (1/stosunek_momentow - 1) * 100
        zmiana_predkosci = (stosunek_promieni - 1) * 100
        
        print(f"\n🚗 WPŁYW NA CHARAKTERYSTYKI POJAZDU:")
        print(f"   Przyspieszanie: {zmiana_przyspieszenia:+.1f}%")
        print(f"   Prędkość maksymalna: {zmiana_predkosci:+.1f}%")
        
        # Szacowanie wpływu na moc
        # Współczynniki wpływu (można dostosować na podstawie doświadczenia)
        wsp_moment = max(0.85, 1 - (stosunek_momentow - 1) * 0.3)  # większy moment = mniejsza efektywność
        wsp_opory = max(0.90, 1 - (stosunek_oporow - 1) * 0.2)    # większe opory = mniejsza efektywność
        wsp_predkosc = min(1.05, 1 + (stosunek_promieni - 1) * 0.3)  # większy promień = lepsza prędkość
        
        wspolczynnik_calkowity = wsp_moment * wsp_opory * wsp_predkosc
        moc_nowa = moc_poczatkowa * wspolczynnik_calkowity
        zmiana_mocy = moc_nowa - moc_poczatkowa
        zmiana_procentowa = (moc_nowa / moc_poczatkowa - 1) * 100
        
        print(f"\n⚡ WPŁYW NA MOC:")
        print(f"   Moc początkowa: {moc_poczatkowa:.1f} kW")
        print(f"   Moc po zmianie: {moc_nowa:.1f} kW")
        print(f"   Zmiana mocy: {zmiana_mocy:+.1f} kW ({zmiana_procentowa:+.1f}%)")
        
        # Szczegółowy rozkład wpływu
        print(f"\n🔍 ANALIZA SZCZEGÓŁOWA:")
        print(f"   Wpływ momentu bezwładności: {(wsp_moment-1)*100:+.1f}%")
        print(f"   Wpływ oporów toczenia: {(wsp_opory-1)*100:+.1f}%")
        print(f"   Wpływ zmiany promienia: {(wsp_predkosc-1)*100:+.1f}%")
        print(f"   Łączny wpływ: {(wspolczynnik_calkowity-1)*100:+.1f}%")
        
        # Podsumowanie i rekomendacje
        print(f"\n" + "=" * 60)
        print("                      PODSUMOWANIE")
        print("=" * 60)
        
        if zmiana_mocy > 0:
            print(f"✅ POZYTYWNY WPŁYW: Nowe koła zwiększą moc o {abs(zmiana_mocy):.1f} kW")
        else:
            print(f"❌ NEGATYWNY WPŁYW: Nowe koła zmniejszą moc o {abs(zmiana_mocy):.1f} kW")
        
        print(f"\n💡 GŁÓWNE CZYNNIKI:")
        if stosunek_momentow > 1.1:
            print("   ⚠️  Znacznie większy moment bezwładności - gorsze przyspieszanie")
        if stosunek_oporow > 1.1:
            print("   ⚠️  Większe opory toczenia - większe zużycie energii")
        if stosunek_promieni > 1.05:
            print("   ✅ Większy promień - lepsza prędkość maksymalna")
        if stosunek_mas > 1.1:
            print("   ⚠️  Znacznie większa masa - gorsze przyspieszanie")
        
        print(f"\n📋 REKOMENDACJE:")
        if abs(zmiana_procentowa) < 2:
            print("   ℹ️  Zmiana parametrów ma minimalny wpływ na moc")
        elif zmiana_procentowa < -5:
            print("   ⚠️  Rozważ lżejsze koła lub mniejszy rozmiar")
        elif zmiana_procentowa > 5:
            print("   ✅ Zmiana korzystna dla charakterystyk pojazdu")
        
        print("=" * 60)
        
    except ValueError:
        print("❌ Błąd: Wprowadź poprawne wartości liczbowe!")
    except ZeroDivisionError:
        print("❌ Błąd: Wartości nie mogą być zerowe!")
    except Exception as e:
        print(f"❌ Wystąpił błąd: {e}")

def main():
    """Główna funkcja programu"""
    while True:
        kalkulator_mocy_kol()
        
        print(f"\nCzy chcesz wykonać kolejne obliczenie? (t/n): ", end="")
        if input().lower() not in ['t', 'tak', 'y', 'yes']:
            break
    
    print("\nDziękujemy za skorzystanie z kalkulatora! 👋")

if __name__ == "__main__":
    main()