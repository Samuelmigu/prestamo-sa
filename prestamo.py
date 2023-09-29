presupuesto = float(input("Cantidad de dinero: "))
anos = float(input("Los años deseados: "))
interes = 5/100
r = float(interes/12)
n = float(anos*12)
Pago_mensual = presupuesto*(r*(1+r)**n) / ((1+r)**n - 1)
print("El pago mensual sería: ", Pago_mensual, "€")

