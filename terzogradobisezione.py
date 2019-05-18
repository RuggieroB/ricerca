
'''
	
	
	# ricerca

	# Programmi di Laboratorio di Programmazione in Linguaggio "Python" (PY). Alunno: Bucchianico Enrico Ruggiero, 4^Finf.


	 - Programma "terzogradoforzabisezione.py": Sia data l'equazione di terzo grado "x^3+4.5x^2+3.5x-3=0;"
		Uno studio preliminare ha permesso di stabilire che esiste una soluzione nell'intervallo [0.3; 0.75]. Utilizzare un metodo a bisezione per trovare tale soluzione.

'''

print("Terzo Grado\n\n")
print("Data l'equazione x^3+4.5x^2+3.5x-3=0;\n")
print("Calcolo della soluzione compresa nell'intervallo (0.3; 0.75) mediante metodo a forza bruta\n\n\n\n")
xi=0.3
xf=0.75
soglia=0.0001
c=1
print("x\n\n")
print("Valore iniziale=",xi,"\n")
print("Valore finale=",xf,"\n")
print("Valore soglia per lo zero=",soglia,"\n\n")
while xi<xf:
	x=(xi+xf)/2
	v=x**3+4.5*x**2+3.5*x-3
	vxi=xi**3+4.5*xi**2+3.5*xi-3
	vxf=xf**3+4.5*xf**2+3.5*xf-3
	if abs(v)<soglia:
		break
	elif v*vxi>0:
		xi=x
	else:
		xf=x
	c+=1
print("Soluzione: x=",x,"\n")
print("Numero di passi=",c,"\n")