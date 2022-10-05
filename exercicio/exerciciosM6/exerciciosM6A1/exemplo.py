seconds = int(input())

convert = []

horas = seconds // 60
nãosei = seconds % 60
convert.append(horas)

minutos = nãosei // 60
nãosei = nãosei % 60
convert.append(minutos)

segundos = seconds // 60
convert.append(minutos)

print("{}:{}:{}".format(convert[0], convert[1], convert[2]))
