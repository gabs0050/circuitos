from machine import Pin, time_pulse_us
import time




PINO_TRIG = 25
PINO_ECHO = 27


PINO_LED_VERMELHO = 35
PINO_LED_VERDE = 26


sensor_trig = Pin(PINO_TRIG, Pin.OUT)
sensor_echo = Pin(PINO_ECHO, Pin.IN)
led_vermelho = Pin(PINO_LED_VERMELHO, Pin.OUT)
led_verde = Pin(PINO_LED_VERDE, Pin.OUT)


def obter_distancia():
    """Mede a distância de um objeto usando o sensor ultrassônico."""
  
    sensor_trig.value(0)
    time.sleep_us(2)

  
    sensor_trig.value(1)
    time.sleep_us(10)
    sensor_trig.value(0)

  
    duracao_pulso = time_pulse_us(sensor_echo, 1, 30000)


    if duracao_pulso > 0:
      
        distancia = (duracao_pulso / 2) * 0.0343
        return distancia
    else:
      
        return -1


contador_deteccoes = 0

while True:
    distancia_medida = obter_distancia()
    
   
    if distancia_medida != -1:
        print("Distância medida:", round(distancia_medida, 2), "cm") 

        if distancia_medida <= 5:
          
            led_vermelho.value(1)
          
            time.sleep(0.5) 
            
          
            contador_deteccoes += 1
            print("Objeto detectado! Contagem:", contador_deteccoes)
    
            led_vermelho.value(0)

        
            if contador_deteccoes >= 10:
                print("Todos os 10 objetos detectados! Acendendo LED verde...")
                led_verde.value(1)
                
             
                time.sleep(10)
                
             
                led_verde.value(0)
                contador_deteccoes = 0
        else:
         
            led_vermelho.value(0)

  
    time.sleep(0.3)
