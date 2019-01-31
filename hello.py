from flask import Flask
app = Flask(__name__)
import RPi.GPIO as GPIO
import time


@app.route('/')
def hello_world():
    return 'Hello, World!<br><a href="/on">Allumer la led</a>'
@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello, %s !' % name
@app.route('/on')
def led_on():
    #Utilisation d'une norme de nommage pour les broches
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    #initialisation de la broche en mode "sortie"
    # Le nombre passé en paramètre correspond au numéro de GPIO et non au numéro de l
    GPIO.setup(14, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    #On indique à la pin GPIO 14 que l'on veut envoyer du courant sur celle-ci
    GPIO.output(14, GPIO.HIGH)
    GPIO.output(12, GPIO.HIGH)
    return '<a href="/off">Éteindre les leds </a>'
    GPIO.cleanup()
@app.route('/off')
def led_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(14, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    
    GPIO.output(14, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    return '<a href="/on"> allumer les leds </a>'
    GPIO.cleanup()
@app.route('/on/<name>')
def spec_on(name):
    #Utilisation d'une norme de nommage pour les broches
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    led = None
    if(name == 'led1'):
        led=14
    elif(name == 'led2'):
        led=12
    #initialisation de la broche en mode "sortie"
    # Le nombre passé en paramètre correspond au numéro de GPIO et non au numéro de l
    GPIO.setup(led, GPIO.OUT)
    #On indique à la pin GPIO 14 que l'on veut envoyer du courant sur celle-ci
    GPIO.output(led, GPIO.HIGH)
    return '<a href="/off">Éteindre les leds </a>'
    GPIO.cleanup()
@app.route('/off/<name>')
def spec_off(name):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    led = None
    if(name == 'led1'):
        led=14
    elif(name == 'led2'):
        led=12
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.LOW)
    return '<a href="/on"> allumer les leds </a>'
    GPIO.cleanup()
