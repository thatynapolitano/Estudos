# Supondo que uma pessoa informa a sua idade em anos, meses e dias (exemplo 30 anos, 11 meses e  15 dias), qual sera a quantidade de dias vividos por essa pessoa. Para simplificar os calculos, assuma que todos os anos possuem 365 dias e todos os meses possuem 30 dias.

anos = int(input("Informe primeiramente a sua idade em anos: "))
meses = int(input("Informe quantos meses de idade voce tem alem dos anos: "))
dias = int(input("Informe quantos dias de idade voce tem alem dos anos e meses: "))

total = anos * 365 + meses * 30 + dias
print(f"Voce viveu {total} dias") 