def genetico(ciudades, pobtam, pcruza, pmuta, iteraciones ):
  poblacion = generapob(ciudades, pobtam)
  print imprimepob(poblacion)
  mejores = list()
  poblacion.sort()
  print "Poblacion ordenada"
  print imprimepob(poblacion)
  mejor = poblacion[0]
  mejores.append(mejor.copy())
  selec = selecciont(poblacion, pobtam)
  continua = True
  i = 1
  while continua and i < iteraciones:
    print i, ") comenzando iteracion"
    i+=1
    print imprimepob(selec)
    hijos = cruzarpob(selec, pcruza)
    selec.extend(hijos)
    mutarpop(selec, pmuta)
    selec = selecciont(selec, pobtam)
    selec.sort()
    mejores.append(selec[0].copy())
    if(len(mejores)>1):
      aux=list(mejores)
      aux.sort()
      n=aux.count(aux[0])
      if(len(mejores)>=10 and n>len(aux)/2):
        continua= False
  mejores.sort()
  print "Los mejores individuos en todas las iteraciones:"
  print imprimepob(mejores)
  return mejores[0]
  def guardaCoordenadas( optimo, rutaArchivo ):
  archivo   = open( rutaArchivo, "w" )
  contenido = ""
  for ciudad in optimo.getciudades():
    contenido += "%f %f\n" % (ciudad.getx(), ciudad.gety())
  archivo.write(contenido)
  archivo.close()

  def main():
  ciudades = parserCiudades("puntos-dj38.tsp")
  pobtam = 40
  pcruza = 0.9
  pmuta = 0.5
  iteraciones = 200
  optimo = genetico(ciudades, pobtam, pcruza, pmuta, iteraciones )
  print "Mejor solución encontrada:"
  print optimo, "-- Con un costo de", optimo.aptitud(), "unidades."
  guardaCoordenadas( optimo, "recorrido-optimo.data" )
if __name__ == "__main__":
  main()





