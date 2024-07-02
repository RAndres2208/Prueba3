##CONSTRUYE
MontoAbonado = []
TotalFinalAbonado = []
nombre = []
direccion = []
abonado = []
cargasFamiliares = []
adicionalPorCarga = []
TotalFinalGifcard = []
Centro = []
Sur = []
Norte = []
import Prueba as Prueba
while(True):
 print("FUNCIONALIDADES")
 print("1. Registrar Gifcard")
 print("2. Listar Gifcard registradas")
 print("3. Definir sector de despacho")
 print("4. Salir del programa")
 opcion = int(input("ingrese la opcion que quiera utilizar. (1-4)"))
 if opcion == 1:
  Prueba.registro(nombre,direccion,abonado,cargasFamiliares,adicionalPorCarga,MontoAbonado,TotalFinalAbonado)
 if opcion == 2 :
  Prueba.listar(nombre,direccion,abonado,cargasFamiliares,adicionalPorCarga,MontoAbonado,TotalFinalAbonado)