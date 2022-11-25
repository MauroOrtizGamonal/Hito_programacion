class AplicacionVenum:#Creo una clase llamada AplicacionVenum
    print('')#Espacio simplemente por cuestiones estéticas
    print('¡Bienvenido a la página web Venum!')#Dentro de la clase hago un print para darle la bienvenida al cliente
    print('Para ayudarle tiene que rellenar los siguientes datos-> ')#Dentro de la clase hago otro print para informar al cliente sobre lo que tiene que hacer a continuación
    print('')#Espacio simplemente por cuestiones estéticas

class TiendaVenum(AplicacionVenum):#Creo otra clase llamada TiendaVenum y hago una herencia muy simple metiendola dentro de la clase padre AplicacionVenum
        def __init__(self) -> None:#Utilizo el __init__ para asignar variables, también el self para que funcioné correctamente
            self.nombreyapellidos=input('Introduzca su nombre y apellidos: ')#Asigno el self.nombreyapellidos para pedir con un input el nombre y los apellidos del cliente
            self.telefono=input('Introduzca su número de teléfono: ')#Asigno el self.telefono para pedir con un input el número de teléfono del cliente
            self.correo=input('Introduzca su correo electrónico: ')#Asigno el self.correo para pedir con un input el correo electrónico del cliente
            self.contraseña=input('Introduzca su contraseña: ')#Asigno el self.contraseña para pedir con un input la contraseña del cliente
            self.nif=input('Introduzca su NIF: ')#Asigno el self.nif para pedir con un input el NIF del cliente
            self.direccion=input('Introduzca su dirección: ')#Asigno el self.direccion para pedir con un input la dirección del cliente
            self.codigopostal=input('Introduzca su código postal: ')#Asigno el self.codigopostal para pedir con un input el código postal del cliente
            print('')#Espacio simplemente por cuestiones estéticas
            print('Cargando.................................................... ')#Cuestiones estéticas
            print('')#Espacio simplemente por cuestiones estéticas
            
        def confirmarRegistro(self):#Creo una función llamada confirmarRegistro para poder realizar la confirmación de registro del cliente
            print(f'Tus datos se han guardado correctamente {self.nombreyapellidos} con NIF {self.nif}')#Hago un print con plantilla para dirigirme al cliente y confirmarle que sus datos se han guardado correctamente
            print(f'Enhorabuena {self.nombreyapellidos}, ya está registrado en nuestra página web!')#Hago otro print con plantilla para dirigirme al cliente y confirmarle que se ha registrado correctamente

        def comprarProducto(self):#Creo una función llamada confirmarRegistro para poder realizar la confirmación de registro del cliente
            print('Introduzca los siguientes datos para realizar la compra: ')#Hago un print para que el cliente sepa lo que debe hacer para realizar la compra
            productos=['guantes', 'vendas', 'saco', 'bucal','cuerda','shorts','zapatillas']#Creo una lista con los productos que se van a vender en mi tienda
            precios=[45, 12, 100, 15, 30, 60, 50]#Creo otra lista con los precios correspondientes de cada producto
            listafinal=[]#Creo otra lista llamada listafinal para almacenar el precio
            while True:#Hago un while true
                digito=input('''
                A. Introducir producto al carrito 
                B. Mostrar precio total
                C. Finalizar compra
                Introduzca ''').capitalize()#Asigno la variable digito con un input para que el cliente pueda realizar la compra del producto e informarse sobre él, finalmente he utilizado el método capitalize para evitar fallos
                print('')#Espacio simplemente por cuestiones estéticas
                print('Cargando.................................................... ')#Cuestiones estéticas
                print('')#Espacio simplemente por cuestiones estéticas
                
                if  digito== 'A':#Si el digito es A
                    print(productos)#Imprime productos
                    nombre=input('Introduzca el producto que desea: ').lower()#Asigno la variable nombre con un input para que el cliente pueda introducir el producto que quiera, finalmente he utilizado el método lower para evitar fallos
                    if nombre not in productos:#Si nombre no está en productos
                        print('El producto no está disponible')#Imprime el producto no está disponible
                    else:#En otro caso
                        almacen=productos.index(nombre)#Asigno la variable almacen a productos con el método index para organizar los nombres de los productos
                        precio=precios[almacen]#Asigno la variable precio a precios de almacen
                        print(f'El precio del producto que has seleccionado es {precio}€')#Hago un print con plantilla para que el cliente pueda ver l precio del producto seleccionado
                        listafinal.append(precio)#Asigno la lista final al método append para que me adjunte el precio

                elif digito=='B':#En caso de que el digito fuera B
                    precioTotal=sum(listafinal)#Asigno la variable precioTotal a la suma de la lista final para calcular el precio total
                    print(f'El precio total es {precioTotal}€')#Hago un print con plantilla para informar al cliente del precio total
                    
                elif digito=='C':#En caso de que el digito fuera C

                    precioTotal=sum(listafinal)#Asigno la variable precioTotal a la suma lista final de nuevo
                    print('''Si vives en España, Italia, Francia, Colombia, Chile, Rusia, Reino Unido, Croacia o Australia,
el IVA implementado se aplicará en función del país, si tu país no está en la lista el IVA será de un 23% ''')#Imprimo lo siguiente para informar al cliente del IVA de cada país
                    pais=input('Introduzca su país: ').lower()#Asigno la variable pais a un input para que el cliente introduzca su país
                    if pais=='España':#Si el pais es España
                        print('El iva es del 21%')#Imprime el IVA es del 21%
                        precioTotalIva=precioTotal*1.21#Asigno la variable precioTotalIva a precioTotal multiplicado por el correspondiente IVA
                        print(f'El precio total en España es {precioTotalIva}€')#Hago un print con plantilla para mostrar el precio total con IVA en España
                    elif pais=='Italia':#Si el pais es Italia
                        print('El iva es del 22%')#Imprime el IVA es del 22%
                        precioTotalIva=precioTotal*1.22#Asigno la variable precioTotalIva a precioTotal multiplicado por el correspondiente IVA
                        print(f'El precio total en Italia es {precioTotalIva}€')#Hago un print con plantilla para mostrar el precio total con IVA en Italia
                    elif pais=='Francia':#Si el pais es Francia
                        print('El iva es del 20%')#Imprime el IVA es del 20%
                        precioTotalIva=precioTotal*1.20#Asigno la variable precioTotalIva a precioTotal multiplicado por el correspondiente IVA
                        print(f'El precio total en Francia es {precioTotalIva}€')#Hago un print con plantilla para mostrar el precio total con IVA en Francia
                    elif pais=='Colombia':#Si el pais es Colombia
                        print('El iva es del 16%')#Imprime el IVA es del 16%
                        precioTotalIva=precioTotal*1.16#Asigno la variable precioTotalIva a precioTotal multiplicado por el correspondiente IVA
                        print(f'El precio total en Colombia es {precioTotalIva}€')#Hago un print con plantilla para mostrar el precio total con IVA en Colombia
                    elif pais=='Chile':#Si el pais es Chile
                        print('El iva es del 19%')#Imprime el IVA es del 19%
                        precioTotalIva=precioTotal*1.19#Asigno la variable precioTotalIva a precioTotal multiplicado por el correspondiente IVA
                        print(f'El precio total en Chile es {precioTotalIva}€')#Hago un print con plantilla para mostrar el precio total con IVA en Chile
                    elif pais=='Rusia':#Si el pais es Rusia
                        print('El iva es del 18%')#Imprime el IVA es del 18%
                        precioTotalIva=precioTotal*1.18#Asigno la variable precioTotalIva a precioTotal multiplicado por el correspondiente IVA
                        print(f'El precio total en Rusia es {precioTotalIva}€')#Hago un print con plantilla para mostrar el precio total con IVA en Rusia
                    elif pais=='Reino Unido':#Si el pais es Reino Unido
                        print('El iva es del 20%')#Imprime el IVA es del 20%
                        precioTotalIva=precioTotal*1.20#Asigno la variable precioTotalIva a precioTotal multiplicado por el correspondiente IVA
                        print(f'El precio total en Reino Unido es {precioTotalIva}€')#Hago un print con plantilla para mostrar el precio total con IVA en Reino Unido
                    elif pais=='Croacia':#Si el pais es Croacia
                        print('El iva es del 25%')#Imprime el IVA es del 25%
                        precioTotalIva=precioTotal*1.25#Asigno la variable precioTotalIva a precioTotal multiplicado por el correspondiente IVA
                        print(f'El precio total en Croacia es {precioTotalIva}€')#Hago un print con plantilla para mostrar el precio total con IVA en Croacia
                    elif pais=='Australia':#Si el pais es Australia
                        print('El iva es del 10%')#Imprime el IVA es del 10%
                        precioTotalIva=precioTotal*1.10#Asigno la variable precioTotalIva a precioTotal multiplicado por el correspondiente IVA
                        print(f'El precio total en Australia es {precioTotalIva}€')#Hago un print con plantilla para mostrar el precio total con IVA en Australia
                            
                    else:#En otro caso
                        print('El iva es del 24%')#Imprime el IVA es del 24%
                        precioTotalIva=precioTotal*1.24#Asigno la variable precioTotalIva a precioTotal*1.24 para calcular el precio con el IVA
                        print(f'El precio total en tu país es {precioTotalIva}€')#Hago un print con plantilla para mostrar el precio total con IVA del país

                    print('')#Espacio simplemente por cuestiones estéticas
                    print('Cargando.................................................... ')#Cuestiones estéticas
                    print('')#Espacio simplemente por cuestiones estéticas
                    print(f'Su compra ha sido realizada con éxito y su precio es {precioTotalIva}€')#Hago un print con plantilla para confirmarle al cliente el precio con IVA de su país y que su compra se ha realizado con éxito
                    print(f'Se ha enviado un pdf de la factura al correo registrado {self.correo}')#Hago un print con plantilla para enviarle al cliente un pdf de la factura al correo con el que se ha registrado 
                    print(f'El seguimiento de su pedido lo podrá realizar en el correo {self.correo} o en el teléfono {self.telefono}')#Hago un print con plantilla para informar al cliente de que el seguimiento de su pedido lo podrá realizar por el correo y teléfonos registrados
                    print('')#Espacio simplemente por cuestiones estéticas
                    print(f'¡Gracias por confiar en nosotros {self.nombreyapellidos}, esperamos que le gusten nuestros productos!')#Hago otro print con plantilla para dirigirme al cliente y confirmarle que sus datos se han guardado correctamente
                    print('')#Espacio simplemente por cuestiones estéticas  
                    break#Es la sentencia que me permite parar el bucle

cliente1=TiendaVenum()#Asigno una variable llamada cliente1 a TindaVenum, de esta manera luego podré asignar la variable y meterle las funciones confirmarRegistro y comprarProducto, y funcionará correctamente
cliente1.confirmarRegistro()#Le asigno a la variable cliente1 la función confirmarRegistro para que se ejecute el registro del cliente
cliente1.comprarProducto()#Le asigno a la variable cliente1 la función comprarProducto para que se ejecute la compra