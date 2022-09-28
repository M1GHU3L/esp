def on_received_number(receivedNumber):
    basic.show_number(randint(0, 10))
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global number
    number += 1
    basic.show_number(number)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global number
    number += -1
    basic.show_number(number)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    radio.send_number(number)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

number = 0
basic.show_icon(IconNames.HEART)

def on_forever():
    pass
basic.forever(on_forever)
