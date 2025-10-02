from flask import Flask
import RPi.GPIO as GPIO

# GPIO ayarları
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Motor pinleri
Motor1A = 23
Motor1B = 24
Motor1E = 25

Motor2A = 17
Motor2B = 27
Motor2E = 22

# Pinleri çıkış yap
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)

GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)
GPIO.setup(Motor2E, GPIO.OUT)

# Flask uygulaması
app = Flask(__name__)

@app.route('/')
def home():
    return "Motor Kontrol Ana Sayfası"

@app.route('/forward', methods=['POST'])
def forward():
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)

    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    GPIO.output(Motor2E, GPIO.HIGH)
    return "Moving Forward"

@app.route('/backward', methods=['POST'])
def backward():
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)

    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)
    return "Moving Backward"

@app.route('/left', methods=['POST'])
def left():
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)

    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)
    return "Turning Left"

@app.route('/right', methods=['POST'])
def right():
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)

    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    GPIO.output(Motor2E, GPIO.HIGH)
    return "Turning Right"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
