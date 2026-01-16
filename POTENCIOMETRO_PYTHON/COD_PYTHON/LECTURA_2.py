# pip install pygame en cmd si fuera nesecario
import serial
import time
import pygame

arduino = serial.Serial('COM1', 9600)  # Reemplaza 'COM1' con el puerto correcto
time.sleep(2)  # Espera a que la conexión se establezca 2 milisegundos

def main():
    pygame.init() # Inicializa Pygame
    screen = pygame.display.set_mode((600, 400)) # Crea una ventana
    pygame.display.set_caption("Lectura del Potenciómetro y movimiento de nave horizontal") # Título de la ventana
    
    color_fondo = (255, 255, 255) # Color de fondo
    color_texto = (0, 0, 0) # Color del texto
    
    mi_font=pygame.font.SysFont("monospace", 20) # Fuente para el texto
    minave=pygame.image.load("nave.jpg").convert() # Carga la imagen de la nave
    
    screen.fill(color_fondo) # Rellena el fondo
    while True:
         valor=arduino.readline().strip()  # Lee una línea del Arduino
         mivalor=valor.decode('utf-8')  # Decodifica el valor leído
         screen.blit(mi_font.render("Lectura Potenciómetro: "+str(mivalor), 1, color_texto), (215, 15)) # Muestra el valor en pantalla
         screen.blit(minave, (int(mivalor), 200)) # Mueve la nave horizontalmente según el valor leído
         pygame.display.flip() # Actualiza la pantalla
         screen.fill(color_fondo) # Rellena el fondo de nuevo para borrar la pantalla
         for event in pygame.event.get(): # Maneja eventos
             if event.type == pygame.QUIT: # Si se cierra la ventana
                 sys.exit() # Sale del programa
            
if __name__ == "__main__":
    main()   
arduino.close()  # Cierra la conexión cuando se termine (aunque en este caso nunca se llega aquí) 