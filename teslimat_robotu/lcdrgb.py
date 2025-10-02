from RPLCD.i2c import CharLCD
import RPi.GPIO as GPIO
from time import sleep

# Kullanıcıdan onay al
onay = input("Bu kodu çalıştırmak istiyor musunuz? (Evet/Hayır): ")

if onay.lower() in ["evet", "e", "yes", "y"]:
    # LCD ekranın ayarları
    i2c_expander = 'PCF8574'
    lcd_address = 0x27  # I2C tarama sonucunda bulduğunuz adres
    lcd_columns = 16
    lcd_rows = 2

    # LCD'yi başlat
    lcd = CharLCD(i2c_expander, lcd_address, cols=lcd_columns, rows=lcd_rows)

    # GPIO ayarları
    GPIO.setmode(GPIO.BCM)

    # RGB LED pinleri
    RED_PIN = 13
    GREEN_PIN = 6
    BLUE_PIN = 5

    # Pinleri çıkış yap
    GPIO.setup(RED_PIN, GPIO.OUT)
    GPIO.setup(GREEN_PIN, GPIO.OUT)
    GPIO.setup(BLUE_PIN, GPIO.OUT)

    # PWM ayarları
    red_pwm = GPIO.PWM(RED_PIN, 100)
    green_pwm = GPIO.PWM(GREEN_PIN, 100)
    blue_pwm = GPIO.PWM(BLUE_PIN, 100)

    # PWM başlat
    red_pwm.start(0)
    green_pwm.start(0)
    blue_pwm.start(0)

    def set_color(r, g, b):
        """RGB LED'in rengini ayarla (0-100 arası)."""
        red_pwm.ChangeDutyCycle(r)
        green_pwm.ChangeDutyCycle(g)
        blue_pwm.ChangeDutyCycle(b)

    try:
        while True:
            command = input("Komut girin (1: alabilirsiniz, 2: teslimat sürecinde, 3: yanlış teslimat): ").strip()
            
            if command == "1":
                print("Alabilirsiniz")
                lcd.write_string("Alabilirsiniz!")
                set_color(0, 100, 0)  # Yeşil
                sleep(10)
                lcd.clear()

            elif command == "2":
                print("Teslimat sürecinde")
                lcd.write_string("Teslimat Sürecinde!")
                set_color(0, 0, 100)  # Mavi
                sleep(20)
                lcd.clear()

            elif command == "3":
                print("Yanlış teslimat")
                lcd.write_string("Yanlış Teslimat!")
                set_color(100, 0, 0)  # Kırmızı
                sleep(30)
                lcd.clear()

            else:
                print("Geçersiz komut. 1, 2 veya 3 girin.")

            set_color(0, 0, 0)  # LED'leri kapat

    except KeyboardInterrupt:
        pass

    # Temizlik
    red_pwm.stop()
    green_pwm.stop()
    blue_pwm.stop()
    GPIO.cleanup()
    lcd.clear()
    print("Kod başarıyla sonlandırıldı.")

else:
    print("Kod çalıştırılmadı.")
