# -*- coding: utf-8 -*-

#Variables Libreria

Libro = []
Autor = []
Fecha_De_Prestamo = []
Inventario_Libreria = [Libro, Autor, Fecha_De_Prestamo] #Lista para almacenar productos

#Variables Laboratorio

Medicamento = []
Fecha_De_Caducidad = []
Temperatura = []
Cantidad = []
Inventario_Laboratorio = [Medicamento, Fecha_De_Caducidad, Temperatura, Cantidad] #Lista para almacenar productos

#Historial Libreria

class Historial_Libreria:
   historial = [] # Lista para guardar los registros
        
   @classmethod
   def agregar_registro(cls, Libro, Autor, Fecha_De_Prestamo):
        cls.historial.append(f'{Libro} {Autor}: {Fecha_De_Prestamo}')  # Agregar los datos a la lista

#Historial Laboratorio

class Historial_Laboratorio:
   historial = [] # Lista para guardar los registros
        
   @classmethod
   def agregar_registro(cls, Medicamento, Fecha_De_Caducidad, Temperatura, Cantidad):
        cls.historial.append(f'{Medicamento} {Fecha_De_Caducidad} {Temperatura}: {Cantidad}')  # Agregar los datos a la list
         
#Interfaz principal

while True:
    
    print ("Bienvenido a la interfaz principal de la libreria municipal y el laboratorio nacional.\t") 
    print ("Por favor, dejenos saber a que interfaz desea ser remitido\t\t")
    print ("1. Libreria municipal\t")
    print ("2. Laboratorio nacional\t\t")
    print ("3. Salir del sistema\t")

    Opcion = input (">> ")

    # Salida del sistema
    if Opcion == "3":
        print("¡Gracias por usar el sistema!")
        break

#Interfaz de libreria
    while Opcion == "1":

        print ("Bienvenido nuevo organizador de libros, ¿Que necesitas hacer hoy?\t")
        print ("1. Agregar un nuevo libro")
        print ("2. Modificar su fecha de prestamo")
        print ("3. Revisar el catalogo de libros")
        print ("4. Volver a la interfaz principal")
        Libreria = input (">> ")

        if Libreria == "1":

            Nombre = input ("Por favor, ingresa el titulo del nuevo libro que quieras agregar: ")
            Libro.append(Nombre)
            Escritor = input ("Por favor, ingresa el nombre del escritor del nuevo libro que quieras agregar: ")
            Autor.append(Escritor)
            Prestamo = int(input ("Por favor, ingresa la fecha de prestamo del nuevo libro que quieras agregar: "))
            Fecha_De_Prestamo.append(Prestamo)
            Historial_Libreria.agregar_registro(Nombre, Escritor, Prestamo) #Guardar automaticamente en historial
            print("¡Felicidades! Acabas de agregar un nuevo libro a la libreria municipal")
            input("Presiona Enter para volver al menu.")

            continue

        elif Libreria == "2":

            Libro_Busqueda = input("Escribe el nombre del libro que desees modificar: ")
            if Libro_Busqueda in Libro:
                Titulo = Libro.index(Libro_Busqueda)

                # Guardar el registro viejo
                Registro_viejo = f"{Libro_Busqueda} {Libro[Titulo]}: {Fecha_De_Prestamo[Titulo]}"

            # Eliminar del historial si existe
                try:
                    Historial_Libreria.historial.remove(Registro_viejo)
                except ValueError:
                    pass  # Evitar error si no estaba en el historial

                # Pedir la nueva cantidad y actualizar
                Nueva_Fecha = int(input(f"Ingrese la nueva fecha para {Libro[Titulo]}: "))
                Fecha_De_Prestamo[Titulo] = Nueva_Fecha  # Actualizar cantidad
            
                # Guardar automáticamente en historial
                Historial_Libreria.agregar_registro(Libro_Busqueda, Libro[Titulo], Nueva_Fecha) 
                print("¡Fecha de prestamo actualizada con éxito!")
            else:
                print("El libro ingresado no existe en el inventario.")
            input("Presiona Enter para volver al menú.")

            continue

        elif Libreria == "3":

            print("Estos son tus libros actuales:")
            print("\n".join(Historial_Libreria.historial) if Historial_Libreria.historial else "No hay productos en el inventario aún.")
     
            input("Presiona Enter para volver al menú.")

            continue

        elif Libreria == "4":

            break

# Interfaz de Laboratorio
    while Opcion == "2":

        print ("Bienvenido nuevo cientifico, ¿Que necesitas hacer hoy?\t")
        print ("1. Agregar un nuevo Medicamento")
        print ("2. Modificar las temperaturas de los medicamentos")
        print ("3. Revisar el catalogo de medicamentos")
        print ("4. Volver a la interfaz principal")
        Laboratorio = input (">> ")

        if Laboratorio == "1":

            Llamado = input ("Por favor, ingresa el nombre del nuevo medicamento que quieras agregar: ")
            Medicamento.append(Llamado)
            Optimo = input ("Por favor, ingresa la temperatura optima del nuevo medicamento que quieras agregar: ")
            Temperatura.append(Optimo)
            Vencimiento = int(input ("Por favor, ingresa la fecha de vencimiento del nuevo medicamento que quieras agregar: "))
            Fecha_De_Caducidad.append(Vencimiento)
            Stock = input ("Por favor, ingresa la cantidad de unidades del nuevo medicamento que deseas agregar: ")
            Cantidad.append(Stock)
            Historial_Laboratorio.agregar_registro(Llamado, Optimo, Vencimiento, Stock) #Guardar automaticamente en historial
            print("¡Felicidades! Acabas de agregar un nuevo medicamento al laboratorio nacional")
            input("Presiona Enter para volver al menu.")

            continue

        elif Laboratorio == "2":

             Medicamento_Busqueda = input("Nombre del medicamento: ")
             if Medicamento_Busqueda in Medicamento:
                Lab = Medicamento.index(Medicamento_Busqueda)

                # Guardar el registro viejo
                Registro_viejo = f"{Medicamento_Busqueda} {Medicamento[Lab]}: {Temperatura[Lab]}"

                # Eliminar del historial si existe
                try:
                    Historial_Libreria.historial.remove(Registro_viejo)
                except ValueError:
                    pass  # Evitar error si no estaba en el historial

                # Pedir la nueva cantidad y actualizar

                Nueva_Temperatura = int(input("Nueva temperatura: "))
                Temperatura[Lab] = Nueva_Temperatura  

                if Nueva_Temperatura > 10:
                    print("¡Advertencia! Temperatura superior a 10°C, puede ser perjudicial.")
                elif Nueva_Temperatura < -12:
                    print("¡Advertencia! Temperatura inferior a -12°C, puede ser perjudicial.")

                print("¡Temperatura actualizada con éxito!")
             else:
                print("El medicamento no se encuentra en la base de datos.")
             input("Presiona Enter para continuar...")

             continue

        elif Laboratorio == "3":

            print("Estos son tus medicamentos actuales:")
            print("\n".join(Historial_Laboratorio.historial) if Historial_Laboratorio.historial else "No hay productos en el inventario aún.")
     
            input("Presiona Enter para volver al menú.")

            continue

        elif Laboratorio == "4":

            continue

        break
