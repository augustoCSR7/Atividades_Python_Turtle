Celsius = float(input('Digite a temperatura em °C: '))
Fahrenheit = (Celsius*1.8) + 32
Kelvin = Celsius + 273
print('A temperatura de {:.1f}°C corresponde a: \n-{:.1f}°F \n-{:.1f}°K'.format(Celsius, Fahrenheit, Kelvin))