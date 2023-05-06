from Universidad import Universidad
u = Universidad("UTPL", 50, 12)
print(u)
u.establecer_nombre("Espe")
print(u)


from Carrera import Carrera
c = Carrera("Carrera en ciencias", "Sistemas y datos", 80)
print(c)
print(c.obtener_alumnos())


