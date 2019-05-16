'''
	# ricerca

	# Programmi di Laboratorio di Programmazione in Linguaggio "Python" (PY). Alunno: Bucchianico Enrico Ruggiero, 4^Finf.


	 - Programma "terzogradoforzabruta.py": Sia data l'equazione di terzo grado "x^3+4.5x^2+3.5x-3=0;"
		Uno studio preliminare ha permesso di stabilire che esiste una soluzione nell'intervallo [0.3, 0.75]. Utilizzo di un metodo a forza bruta per determinare tale soluzione.
'''
print("Terzo Grado\n\n")
print("Data l'equazione x^3+4.5x^2+3.5x-3=0;\n")
print("Calcolo della soluzione compresa nell'intervallo (0.3;0.75) mediante metodo a forza bruta\n\n\n\n")
x=0.3
xf=0.75
varx=0.0001
soglia=0.0001
c=1
print("x\n\n")
print("Valore iniziale=",x,"\n")
print("Valore finale=",xf,"\n")
print("Passo:",varx,"\n")
print("Valore soglia per lo zero=",soglia,"\n\n")
while x<xf:
	if abs(x**3.+4.5*x**2.+3.5*x-3.)<soglia:
		break
	x+=varx
	c+=1
print("Soluzione: x=",x,"\n")
print("Numero di passi=",c,"\n")