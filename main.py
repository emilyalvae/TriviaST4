BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
import random
import time
puntaje = 0
iniciar_trivia = True 
intentos = 0
print(RED+"Bienvenido a la Trivia sobre Stranger Things 4")
print("Pondremos a prueba que tan fan eres de la serie")
print("Comenzaras con", puntaje, "puntos"+RESET)
nombre = input(WHITE+"Dinos tu nombre: "+RESET)
print(CYAN+"\nHola", nombre, "responde las siguientes preguntas escribiendo la letra con la alternativa correcta y presiona Enter para enviar tu respuesta:\n"+RESET)
print("Iniciando...")
for numero_carga in range(5, 0, -1):
    print(numero_carga)
    time.sleep(1)
while iniciar_trivia == True: 
  intentos += 1
  puntaje = 0
  print(BLUE+"\nIntento número:"+RESET, intentos)
  print(WHITE+"\n1) ¿En que año transcurre la cuarta temporada?")
  print("a) 1989")
  print("b) 1986")
  print("c) 1985")
  print("d) 1988"+RESET)
  respuesta_1 = input(CYAN+"\nTu respuesta: "+RESET).lower()
  while respuesta_1 not in ("a", "b", "c", "d","z"):
    respuesta_1 = input(YELLOW+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET)
  if respuesta_1 == "a":
    puntaje -= random.randint(0, 5)
    print(RED+"Incorrecto!", nombre, ", en 1989 no transcurre la cuarta temporada"+RESET)
  elif respuesta_1 == "c":
    puntaje -= random.randint(0, 5)
    print(RED+"Incorrecto!", nombre, ", en 1985 no transcurre la cuarta temporada"+RESET)
  elif respuesta_1 == "d":
    puntaje -= random.randint(0, 5)
    print(RED+"Incorrecto!", nombre, ", en 1988 no transcurre la cuarta temporada"+RESET)
  elif respuesta_1 == "z":
    puntaje += 50
    print(RED+"Descrubiste el mensaje secreto"+RESET)
  else:
    puntaje += random.randint(1, 10)
    print(RED+"Es correcto!", nombre, "haz comenzado muy bien"+RESET)
  print(RED+"Puntaje actual:", puntaje, "puntos"+RESET)
  time.sleep(3)
  print(WHITE+"\n2)¿Como se llama la roca en la que se escondio Eddie?"+RESET)
  print("a) Roca Tubular")
  print("b) Roca Cadaver")
  print("c) Roca Calavera")
  print("d) Roca Amantes")
  respuesta_2 = input(CYAN+"\nTu respuesta: "+RESET).lower()
  while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input(YELLOW+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET)
  if respuesta_2 == "a":
    puntaje -= random.randint(0, 5)
    print(RED+"Incorrecto!", nombre, ", no se llamaba Roca Tubular"+RESET)
  elif respuesta_2 == "b":
    puntaje -= random.randint(0, 5)
    print(RED+"Incorrecto!", nombre, ", no se llamaba Roca Cadaver"+RESET)
  elif respuesta_2 == "d":
    puntaje -= random.randint(0, 5)
    print(RED+"Incorrecto!", nombre, ", no se llamaba Roca Amantes"+RESET)
  else:
    puntaje += random.randint(1, 10)
    print(RED+"Es correcto!", nombre, "Sigue así"+RESET)
  print(RED+"Puntaje actual:", puntaje, "puntos"+RESET)
  time.sleep(3)
  print(WHITE+"\n3) ¿Quien canta la cancion favorita de Max?"+RESET)
  print("a) Kate Bush")
  print("b) Monic Pardo")
  print("c) Madonna")
  print("d) Susy Diaz")
  respuesta_3 = input(CYAN+"\nTu respuesta: "+RESET).lower()
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input(YELLOW+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET)
  if respuesta_3 == "b":
    puntaje = puntaje / 2
    print(RED+"Incorrecto!", nombre, ", Monic Pardo no canta la cancion"+RESET)
  elif respuesta_3 == "c":
    puntaje = puntaje - 5
    print(RED+"Incorrecto!", nombre, ", Madonna no canta la cancion"+RESET)
  elif respuesta_3 == "d":
    puntaje = puntaje + 5
    print(RED+"Incorrecto!", nombre, ", Susy Diaz no canta la cancion, pero como tambien somos fan de Susy, sumaras puntos"+RESET)
  else:
    puntaje = puntaje * 2
    print(RED+"Es correcto!", nombre, "muy bien"+RESET)
  time.sleep(2)
  print(MAGENTA+"\nGracias", nombre, "por participar en la trivia, alcanzaste", puntaje, "puntos\n"+RESET)
  if puntaje < 10:
    print("Descuida, puedes mejorar tu puntaje con la")
  if puntaje >= 10:
    print("Gran puntaje, sigue ganando puntos con la")
  
  giros_ruleta = random.randint(2, 3)
  print(GREEN+"RULETA DE LA SUERTE")
  print("sumaras de 0 a 10 puntos extras"+RESET)
  time.sleep(1)
  print("Girarás la ruleta: ", giros_ruleta, "veces!")
  input("Presiona Enter para girar")
  giros_ruleta +=1 
  
  for numero_giro in range(1, giros_ruleta):
    print("\nGiro número: ", numero_giro)
    bonus = random.randint(0, 10) 
    print("Ganaste:", bonus, "puntos extra!")
    puntaje = puntaje + bonus
    input("Presiona Enter para continuar")  
  
  print(MAGENTA+"\nTu puntaje final es de: ", puntaje, "!"+RESET)
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si":
   print("\nEspero", nombre, "que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False