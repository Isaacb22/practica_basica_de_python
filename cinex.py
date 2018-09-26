import getpass
limite_validacion_veinte = 0
porcentaje_de_clientes_vip = 20
salas = []
nombre_de_sala = ""
limite_sala = 0
nro_sala = 0 

def registro_de_administrador():
	nombre_de_usuario = input("\nIngrese su nombre de usuario: ")
	contrasena = getpass.getpass('\nIngrese su contrasena: ')
	while True:
		if nombre_de_usuario != 'isaacb22' or contrasena != '1234':
			print ('\nInicio de sesion fallido. Intente otra vez')
			nombre_de_usuario = input("\nIngrese su nombre de usuario: ")
			contrasena = getpass.getpass('\nIngrese su contrasena: ')
		else:
			print ("\nInicio de sesion exitoso")
			control_de_salas()
			break


def mostrar_salas():
	print("\n\n\t\t\t\t\t\t\t\tSeleccione una sala: \n")

	for i,n in enumerate(salas):
		print("{}) {}\n".format(i+1, n[0]))



def eleccion_cliente():

	while True:
		try:
			mostrar_salas()
			entrar_sala = input("A cual sala quiere entrar? ")
			
			if entrar_sala not in salas:
				print ("\nTiene que elegir la sala a la que quiere entrar")
			else:
				print("\nUsted a elegido entrar a la " + entrar_sala)
			elegir_cliente = int(input('\nQue tipo de cliente quiere ser? \n\n\t\t\t1)VIP  \t\t\t\t\t\t2)NORMAL : '))
			
			for i in range(len(salas)):
				
				if entrar_sala in salas[i] and elegir_cliente == 1:
					if validacion_de_porcentaje(salas[i][3]) == False:
						print ("\n\nLimite de asientos VIP excedido\n")
						
					else:
						salas[i][1] += 1
						
				if entrar_sala in salas[i] and elegir_cliente == 2:
					salas[i][2] += 1
					
		except ValueError:
			print ('\nCaracter invalido, solo se permiten numeros')
		
		
	
	




def validacion_de_porcentaje(limite):
	
	porcentaje_total = int(limite) * int(porcentaje_de_clientes_vip) / 100
	
	for i in range(len(salas)):
	
		if salas[i][1] + 1 > int(porcentaje_total):
			return 	False
		else:
			return True
		


def menu():
	
	print ("\n\n\t\t\t\t\t\t\t  Bienvenido al cine VERGATARIO")
	print (" =============================================================================================================================================")
	print (" |||  1)Control de salas   |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||    2)Control de clientes  |||")
	print (" |||=======================|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||===========================|||")
	print (" |||	  3)Resultados     |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||    4)Salir del programa   |||")
	print (" =============================================================================================================================================")
	selecciona_una_opcion = input("\nSeleccione una opcion: ")
	
	if selecciona_una_opcion == '1':
		print ("\nTu has elegido la opcion Control de salas")
		registro_de_administrador()
	if selecciona_una_opcion != '2' or limite_sala == 0 or nro_sala == 0:
		print ("\n\n\t\t\t\tAun no puede entrar en esta opcion, espere que el administrador llene la opcion 1")
	else:
		print ("\nTu has elegido la opcion Contro de clientes")
		eleccion_cliente()
	
	
	
def control_de_salas():
	while True:
		try:
			nro_sala = int(input("\n\nIngrese el numero de salas: "))
			break	
	
		except ValueError:
			print ('\nCaracter invalido, solo se permiten numeros')
	
	
	for i in range(1,int(nro_sala)+1):
		

		while True:
			try:
				limite_sala = int(input("\nIngrese el limite para la sala {}: ".format(i)))
				nombre_de_sala = "sala {}".format(i)
				salas.append([nombre_de_sala,0,0,limite_sala])

				break
			

			except ValueError:
				print ('\nCaracter invalido, solo se permiten numeros')

		
	print ("\n\t\t\t\t\t     Has validado la opcion Control de salas exitosamente")
	
		
	
		
		

		
	
	


while True:
	menu()