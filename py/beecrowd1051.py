salario = float(input())

aliquota_taxa_8 = 0.08
aliquota_taxa_18 = 0.18
aliquota_taxa_28 = 0.28

taxas = 0

if salario  > 2000:
    taxas += (salario - 2000) * aliquota_taxa_8 
    if salario > 3000:
        taxas += (salario - 3000) * aliquota_taxa_18
        if salario > 4500:
            taxas += (salario - 4500) * aliquota_taxa_28
else:
    taxas = "Isento"

if taxas != "Isento":
    print(f"{taxas:.2f}")
else:
    print(taxas)

