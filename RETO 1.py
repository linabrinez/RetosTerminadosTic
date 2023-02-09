
codigo=int(input())#se pide codigo de tipo entero 
nombreProducto=input()#se pide nombre de prodto tipo string
cantidadProducto=float(input())#se pide cant de product de tipo flotante
ValorUnitario=float(input())#se pide valor unitario de tipo flotante
totalSINIVA=cantidadProducto*ValorUnitario# se hace operacion para saber el valor subtotal comprado 
TOTALCONIVA=(((ValorUnitario*0.19)+(ValorUnitario))*(cantidadProducto))#operacion para saber el total con iva incluido
#se realizan las impresiones a mostrar al usuario cod,product,subtotal,total.
print(codigo) 
print(nombreProducto)
print(totalSINIVA)
print(TOTALCONIVA)

