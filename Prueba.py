def registro (nombre,direccion,Dias,cargasFamiliares,adicionalPorCarga,MontoAbonado,TotalFinalAbonado):
    varNombre = input("ingrese su nombre y apellido")
    nombre.append(varNombre)
    varDireccion = input("ingrese su direccion")
    direccion.append(varDireccion)
    VarDias = int(input("ingrese los dias trabajados el ultimo mes"))
    Dias.append(VarDias)
    MontoAbonado = VarDias * 10000
    VarCargasFamiliares = int(input("ingrese cantidad de cargas familiares"))
    cargasFamiliares.append(VarCargasFamiliares)
    if VarCargasFamiliares == 3 or VarCargasFamiliares>3:
        adicionalPorCarga = MontoAbonado * 0.25 
        TotalFinalAbonado = MontoAbonado * 0.25 + MontoAbonado
def listar(nombre,direccion,Dias,cargasFamiliares,adicionalPorCarga,MontoAbonado,TotalFinalAbonado):
    for i in range (len(nombre)):
        print ("Trabajador:\t\t Direccion:\tMontoAbonado:\tNumeroCargas:\tAdicionalCargas:\tTotal:}")
        print(f"{nombre,{i}}\t{direccion,{i}}\t{MontoAbonado,{i}}\t{cargasFamiliares,{i}}\t{adicionalPorCarga,{i}}\t{TotalFinalAbonado,{i}}")
def despacho(Norte,Sur,Centro):
    VarNorte = int(input("¿desea su despacho en la zona norte? si(S/N)no"))
    if VarNorte == ("N"):
     VarSur = int(input("¿desea su despacho en la zona sur? si(S/N)no"))
    if VarSur == ("N"):
     VarCentro = int(input("¿desea su despacho en la zona centro? si(S/N)no"))