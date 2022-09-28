radio.onReceivedNumber(function (receivedNumber) {
    basic.showNumber(randint(0, 10))
})
input.onButtonPressed(Button.A, function () {
    number += 1
    basic.showNumber(number)
})
input.onButtonPressed(Button.B, function () {
    number += -1
    basic.showNumber(number)
})
input.onGesture(Gesture.Shake, function () {
    radio.sendNumber(number)
})
let number = 0
basic.showIcon(IconNames.Heart)
basic.forever(function () {
	
})
