# импортируем используемые модули
import pygame
import usb.core
import usb.util

# инициализируем модуль pygame (usb.core и usb.util инициализации не требуют)
pygame.init()


def send(move):
    '''
    Получает направление движения в качестве аргумента
    Настраивается на конкретное устройство
    Отправляет на нему данные
    '''
    # необходимо заменить "0x1234" и "0x5678" на идентификаторы поставщика (т.е. ноута) и продукта (Arduino)
    device = usb.core.find(idVendor=0x1234, idProduct=0x5678)

    # проверка, а подкючены ли вообще устройство
    if device is None:
        print("Device not found")
    else:

        # поставим активную конфигурацию. Без аргументов, первая же
	    # конфигурация будет активной
        device.set_configuration()

        # просто строка
        endpoint = device[0][(0, 0)][0]

        # Записываем данные на устройство
        data = move
        bytes_written = device.write(endpoint.bEndpointAddress, data)
        print("Bytes written:", bytes_written)

        


# здесь будет код 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# основное тело кода

# наш "флаг"
running = True
while running:

    # сюда записываем текущее направление движения: 0 - никуда; w - вверх; s - вниз
    move = 0

    # проверка на произошедшие события
    for event in pygame.event.get():

        # если мы мышкой закрыли всплывшее окно программа прекратится
        if event.type == pygame.QUIT:
            running = False
        
        # если мы нажали esc программа прекратится
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                running = False

    # в этом словаре хранются текущие значения всех клавиш клавиатуры
    keys = pygame.key.get_pressed()

    # обращаемся к значениям словаря, хранящимся по соответствующему ключу
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        move = 'w'
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        move = 's'

    # передаём текущее направление движения в функцию, которая отправит значение на Arduino
    send(move)

    # проверка, что всё работает
    print(move)

    