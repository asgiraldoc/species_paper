# Abrimos el archivo en modo lectura
with open("nombre_del_archivo.txt", "r") as archivo:
  # Leemos cada línea del archivo
  for linea in archivo:
    # Buscamos el primer patrón de caracteres
    inicio = linea.find("patron1")
    # Si encontramos el patrón
    if inicio != -1:
      # Buscamos el segundo patrón de caracteres
      fin = linea.find("patron2", inicio + len("patron1"))
      # Si encontramos el segundo patrón
      if fin != -1:
        # Extraemos el texto que está entre los dos patrones
        texto = linea[inicio + len("patron1"):fin]
        # Podemos hacer algo con el texto aquí, como imprimirlo
        print(texto)
