far = float(input('Enter temperature in Farenheit:'))
cel = float(input('Enter temperature in Celsius:'))

farConv = (cel - 32 * .5556)
celConv = (far * 1.8 + 32)

print('Value: {:.2f}'.format(celConv))
print('Value: {:.2f}'.format(farConv))


#far = cel