primeira_entrada = input().split()

x1 = float(primeira_entrada[0])
y1 = float(primeira_entrada[1])

segunda_entrada = input().split()

x2 = float(segunda_entrada[0])
y2 = float(segunda_entrada[1])

a = ((x2 - x1) ** (2) + (y2 - y1) ** (2)) ** (1/2)

print('{:.4f}'.format(a))
