import math
import numpy
from fractions import Fraction

print("""Programm zur Berechnung der Hesse-Form aus drei Punkte im Raum.
Trenne beim Eingeben die einzelnen Koordinaten mit einem / voneinander. (Bsp.: -2/3/-1)
Drücke Strg+C um das Programm zu beenden.\n""")

def input_vektor(type_str):
    raw_vektor = input(type_str)
    if len(raw_vektor.split("/")) == 3:
        return [int(x) for x in raw_vektor.split("/")]
    else:
        print("Deine Eingabe ist nicht korrekt...")
        input_vektor(type_str)
    
A = input_vektor("Aufpunkt A: ")
B = input_vektor("Richtungspunkt B: ")
C = input_vektor("Richtungspunkt C: ")

def skalarprodukt(u, v):
    produkt = u*v
    final_product = 0
    for x in produkt:
        final_product = final_product+x
    return final_product

ab = numpy.array([
    B[0] - A[0],
    B[1] - A[1],
    B[2] - A[2]
])

ac = numpy.array([
    C[0] - A[0],
    C[1] - A[1],
    C[2] - A[2]
])

n = numpy.cross(ab, ac)

n0 = skalarprodukt(n, A)

betrag = math.sqrt(n[0]**2+n[1]**2+n[2]**2)
betrag_str = f"\u221A{n[0]**2+n[1]**2+n[2]**2}"

print(f"""+-------------------------------------------------------------------------+
| Ebenentabelle
+---------------+---------------------------------------------------------+""")
print(f"| Vektor AB:    | {ab}")
print(f"| Vektor AC:    | {ac}")
print(f"| Vektor n:     | {n}")
print(f"| ~Länge von n: | {betrag}")
print(f"| Normalenform: | ({n[0]})x1 + ({n[1]})x2 + ({n[2]})x3 + ({n0*(-1)}) = 0")

if n0*(-1) > 0:
    print(f"| Hesse-Form:   | (-{n[0]}/{betrag_str})x1 - ({n[1]}/{betrag_str})x2 - ({n[2]}/{betrag_str})x3 + ({n0})")
else:
    print(f"| Hesse-Form:   | ({n[0]}/{betrag_str})x1 + ({n[1]}/{betrag_str})x2 + ({n[2]}/{betrag_str})x3 + ({n0*(-1)})")

print(f"+---------------+---------------------------------------------------------+")

"""
try:
    if n0/betrag >= 0: 
        print(f"Hesse-Form: ({n[0]/betrag})x1 + ({n[1]/betrag})x2 + ({n[2]/betrag})x3 + ({n0/betrag*(-1)})")
        print(f"Hesse-Form: ({Fraction(n[0]/betrag)})x1 + ({Fraction(n[1]/betrag)})x2 + ({Fraction(n[2]/betrag)})x3 + ({Fraction(n0/betrag*(-1))})")
    else:
        print(f"Hesse-Form: ({n[0]/betrag*(-1)})x1 + ({n[1]/betrag*(-1)})x2 + ({n[2]/betrag*(-1)})x3 + ({n0/betrag})")
        print(f"Hesse-Form: ({Fraction(n[0]/betrag*(-1))})x1 + ({Fraction(n[1]/betrag*(-1))})x2 + ({Fraction(n[2]/betrag*(-1))})x3 + ({Fraction(n0/betrag)})")
except:
    pass
"""
input("Enter drücken um zu beenden...")