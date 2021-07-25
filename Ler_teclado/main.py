import serial # Importa a biblioteca para ler e escrever na serial
import keyboard # Importa a biblioteca para interagir com o teclado
from time import sleep # Importa a biblioteca para controle de interruções

arduino = serial.Serial('/dev/ttyUSB0', 9600) # Cria o objeto "arduino". Abre a serial. Parâmetros --> Porta, baud rate.
  
while True: # Loop infinito
    if keyboard.is_pressed('up'): # Se a seta para cima for pressionada
        print("Frente")
        arduino.write('0'.encode()) # Escreve na serial 0
    if keyboard.is_pressed("down"):
        print("Tras")
        arduino.write('2'.encode())
    if keyboard.is_pressed('left'):
        print("esquerda")
        arduino.write('4'.encode())  
    if keyboard.is_pressed ("right"):
        print("direita")
        arduino.write('8'.encode())
    if keyboard.is_pressed("a"):
        print("Pulso Esquerda")
        arduino.write('16'.encode())
    if keyboard.is_pressed("s"):
        print("Pulso Direita")
        arduino.write('32'.encode())
    if keyboard.is_pressed("space"):
        print("Parar")
        arduino.write('64'.encode())

    if keyboard.is_pressed("esc"):
        print("Fechando Serial")
        arduino.close() # Fecha a serial
        break # Termina o loop infinito

    sleep(0.1) # Atraso. Importante para não ler a mesma tecla mais de uma vez. 100 millis
    