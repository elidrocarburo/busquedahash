class TablaHash:
    def __init__(self):
        self.tamano = 11
        self.ranuras = [None] * self.tamano
        self.datos = [None] * self.tamano

    def agregar(self,clave,dato):
      valorHash = self.funcionHash(clave,len(self.ranuras))

      if self.ranuras[valorHash] == None:
        self.ranuras[valorHash] = clave
        self.datos[valorHash] = dato
      else:
        if self.ranuras[valorHash] == clave:
          self.datos[valorHash] = dato
        else:
          proximaRanura = self.rehash(valorHash,len(self.ranuras))
          while self.ranuras[proximaRanura] != None and \
                          self.ranuras[proximaRanura] != clave:
            proximaRanura = self.rehash(proximaRanura,len(self.ranuras))

          if self.ranuras[proximaRanura] == None:
            self.ranuras[proximaRanura]=clave
            self.datos[proximaRanura]=dato
          else:
            self.datos[proximaRanura] = dato

    def funcionHash(self,clave,tamano):
         return clave%tamano

    def rehash(self,hashViejo,tamano):
        return (hashViejo+1)%tamano

    def obtener(self,clave):
      ranuraInicio = self.funcionHash(clave,len(self.ranuras))

      dato = None
      parar = False
      encontrado = False
      posicion = ranuraInicio
      while self.ranuras[posicion] != None and  \
                           not encontrado and not parar:
         if self.ranuras[posicion] == clave:
           encontrado = True
           dato = self.datos[posicion]
         else:
           posicion=self.rehash(posicion,len(self.ranuras))
           if posicion == ranuraInicio:
               parar = True
      return dato

    def __getitem__(self,clave):
        return self.obtener(clave)

    def __setitem__(self,clave,dato):
        self.agregar(clave,dato)

H=TablaHash()
H[11] = "azul"
H[22] = "rojo"
H[33] = "verde"
H[44] = "amarillo"
H[55] = "negro"
H[66] = "blanco"
H[77] = "naranja"

H[66] = "gris"

print("Ranuras:", H.ranuras)
print("Datos:", H.datos)

print("Buscar clave 33:", H[33])
print("Buscar clave 66:", H[66])
print("Buscar clave 99:", H[99])
