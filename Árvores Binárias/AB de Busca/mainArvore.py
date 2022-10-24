from ArvoreBinariaBusca import ArvoreBinaria, No


arv = ArvoreBinaria('A')
arv.add('D')
arv.add('F')
arv.add('G')
arv.add('H')
arv.add('K')
arv.add('M')
arv.add('F')
print('Len: ', len(arv))
arv.preordem()
print()
print('\nBusca "H":', arv.busca('H'))
arv.removeNo('G')
arv.preordem()
print()
arv.removeNo('F')
arv.preordem()
print()
arv.removeNo('H')
arv.preordem()
print()
arv.removeNo('A')
arv.preordem()
print()
arv.removeNo('D')
arv.preordem()
print()
arv.removeNo('F')
arv.preordem()
print()
arv.removeNo('M')
arv.preordem()
print()
arv.removeNo('K')
arv.preordem()
print()
print('Len: ', len(arv))
print('RemoveRaiz():', arv.removeRaiz())


