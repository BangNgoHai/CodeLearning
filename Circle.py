from turtle import *

spirograph = Turtle()
spirograph.speed(10)
spirograph.pensize(1)
bgcolor('#131417')
spirograph.hideturtle()

def circulo(voces, angulo):
	for x in range(voces):
		spirograph.color('#FFAC12')
		spirograph.left(angulo)
		spirograph.circle(50)
		spirograph.forward(5)

circulo(20,18)#360/veces = angulo
done()