from google.colab import drive
drive.mount('/content/drive')


v1,vv2 = 256,240
mcm= minimo_comun_multiplo(v1,v2)
print(f"El minimo comun multiplo de {v1} y {v2} es {mcm}")