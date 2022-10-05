m=float(input("donner la masse"))
po=float(input("donner la masse volumique de mercure"))
H=float(input("donner la valeur de la hauteur"))
l=float(input("donner la longeur"))
L=float(input("donner la largeur"))
S=float(input("donner la valeur de la surface"))
v=m/po
print("le volume versé de mercure est:",v,"m3")
vt=(v-(L*l*H))/3
print("le volume dans chaque tube est:",vt,"m3")
h=vt/S
print("la hauteur de mercure est:",h,"m")