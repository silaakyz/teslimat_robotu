import RPi.GPIO as GPIO
import time
import cv2

# Pin tanımları
TRIG_PIN = 21
ECHO_PIN = 20
BUZZER_PIN = 16

# Mesafe eşiği
THRESHOLD_DISTANCE_CM = 10

def get_distance():
    GPIO.output(TRIG_PIN, False)
    time.sleep(0.1)
    
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = (pulse_duration * 34300) / 2
    return distance

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)

    # Kamera başlat
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Kamera açma hatası!")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Kare alınamadı!")
                break

            cv2.imshow('Webcam', frame)

            # Mesafe ölç
            distance = get_distance()
            print(f"Distance: {distance:.2f} cm")

            if distance <= THRESHOLD_DISTANCE_CM:
                GPIO.output(BUZZER_PIN, True)
            else:
                GPIO.output(BUZZER_PIN, False)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            time.sleep(0.1)

    except KeyboardInterrupt:
        pass

    GPIO.cleanup()
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
