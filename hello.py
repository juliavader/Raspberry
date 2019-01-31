from flask import Flask
app = Flask(__name__)
import time
from flask import render_template 
from led import Led

led1 = Led(14)
led2 = Led(12)

@app.route('/')
def hello_world():
    return render_template('base.html')
@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello, %s !' % name

@app.route('/led/')
@app.route('/led/<state>')
@app.route('/led/<state>/<name>')
def led(state=None, name=None):
    led = None
    
    if(name == 'led1'):
        led=led1
    elif(name == 'led2'):
        led=led2
    else:
        name=None

    if(state == 'on'):
        if(name):
            led.allumer()
        else:
            led1.allumer()
            led2.allumer()
    elif(state == 'off'):
        if(name):
            led.eteindre()
        else:
            led1.eteindre()
            led2.eteindre()
    return render_template('hello.html',on=state,led1=led1.statut, led2=led2.statut)

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
