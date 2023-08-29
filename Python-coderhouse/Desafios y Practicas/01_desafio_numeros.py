def calcular_promedio_equipo(ganados, empatados, perdidos):
  """
  Calcula el promedio final de un equipo de fútbol.

  Args:
    ganados: Número de partidos ganados.
    empatados: Número de partidos empatados.
    perdidos: Número de partidos perdidos.

  Returns:
    Promedio final del equipo.
  """

  puntos_totales = ganados * 3 + empatados * 1 + perdidos * 0
  promedio = puntos_totales / (ganados + empatados + perdidos)
  return promedio


def main():
  """
  Programa principal.
  """

  ganados = int(input("Ingrese el número de partidos ganados: "))
  empatados = int(input("Ingrese el número de partidos empatados: "))
  perdidos = int(input("Ingrese el número de partidos perdidos: "))

  promedio = calcular_promedio_equipo(ganados, empatados, perdidos)
  print("El promedio final del equipo es de:", promedio)


if __name__ == "__main__":
  main()
