#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number = -number
    return number

def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    valeur = []
    for i in prefixes:
        valeur.append(i + suffixe)
    return valeur



def prime_integer_summation() -> int:
    somme = 0
    n=0
    nombre=2
    nombre_premier = []
    while n < 100:
        premier = True
        for j in range(2, nombre-1):
            if nombre/j == nombre//j:
                premier = False
        if premier != False:
            somme += nombre
            n+=1
        nombre+=1
    return somme


def factorial(number: int) -> int:
    for i in range(1, number):
        number *= i
    return number


def use_continue() -> None:
    for i in range(1,11):
        if i == 5:
            continue
        print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    l=[]
    return []


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
