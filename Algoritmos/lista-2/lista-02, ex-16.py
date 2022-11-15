mgkg = 2.50
mckg = 1.80
qtdmo = float(input('digite os quilos de morango desejados: '))
qtdma = float(input('digite os quilos de maçã desejados: '))

if qtdmo > 5:
    mgkg = 2.20
if qtdma > 5:
    mckg = 1.50

vt = (mgkg * qtdmo) + (mckg * qtdma)

if (qtdmo + qtdma) > 8 or vt > 25.00:
    desconto = (vt * 10) / 100
    vt = vt - desconto
    print('o valor com a porcentagem foi de: %.2f' % vt, 'R$')
else:
    print('o valor com a porcentagem foi de: %.2f' % vt, 'R$')