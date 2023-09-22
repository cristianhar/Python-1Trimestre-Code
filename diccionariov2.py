d1={"Nombre":"Juan" , "Edad":23}
d2={"Ciudad": "Bello", "Genero": "Masculino"}
d3={"Salario":450000}
d4 = {}
for diccIter in (d1, d2, d3):
    d4.update(diccIter)#metodo update
print("La unión es", (d4))