import serial

ser = serial.Serial('COM4', 9600)

while (True):
    # Читаем из порта данные
    response = ser.readline()
    # Декодируем ответ из байтов в строку с использованием UTF-8
    decoded_response = response.decode('utf-8')
    # Выводим данные в консоль
    print(decoded_response)