"""
1 - Exemplo de execução

total_venda = float(input("Digite o valor total da venda: R$ "))

total_com_desconto = total_venda * 0.9

valor_parcela = total_venda / 3

comissao_vista = total_com_desconto * 0.05

comissao_parcelada = total_venda * 0.05

print("\nResultados:")
print(f"Total a pagar com desconto de 10%: R$ {total_com_desconto:.2f}")
print(f"Valor de cada parcela em 3x sem juros: R$ {valor_parcela:.2f}")
print(f"Comissão do vendedor para venda á vista: R$ {comissao_vista:.2f}")
print(f"Comissão do vendedor para venda parcelada: R$ {comissao_parcelada:.2f}")


"""

# Entrada: valor total da venda
total_venda = float(input("Digite o valor total da venda: R$ "))

# Calculando o total a pagar com desconto de 10%
total_com_desconto = total_venda * 0.9

# Calculando o valor de cada parcela no parcelamento de 3x sem juros
valor_parcela = total_venda / 3

# Calculando a comissão do vendedor para venda à vista (5% sobre o valor com desconto)
comissao_vista = total_com_desconto * 0.05

# Calculando a comissão do vendedor para venda parcelada (5% sobre o valor total)
comissao_parcelada = total_venda * 0.05

print("\nResultados:")
print(f"Total a pagar com desconto de 10%: R$ {total_com_desconto:.2f}")
print(f"Valor de cada parcela em 3x sem juros: R$ {valor_parcela:.2f}")
print(f"Comissão do vendedor para venda à vista: R$ {comissao_vista:.2f}")
print(f"Comissão do vendedor para venda parcelada: R$ {comissao_parcelada:.2f}")
