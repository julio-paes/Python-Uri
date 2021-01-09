
linha = input().split()
peca_a = int(linha[0])
quant_peca_a = int(linha[1])
valor_peca_a = float(linha[2])

linha2 = input().split()
peca_b = int(linha2[0])
quant_peca_b = int(linha2[1])
valor_peca_b = float(linha2[2])

total_compra = valor_peca_a * quant_peca_a + valor_peca_b * quant_peca_b

print("VALOR A PAGAR: R$ {:.2f}".format(total_compra))
