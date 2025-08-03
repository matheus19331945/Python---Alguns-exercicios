medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
dam = medida / 10
dm = medida * 10
print(f'A media de {medida}m corresponde a: \n'
      f' {cm:.0f}cm \n'
      f' {mm:.0f}mm \n'
      f' {dam:.0f}dam \n'
      f' {dm:.0f}dm \n')

# Com cores
print(f'A media de {medida}m corresponde a: \n'
      f' \033[33m{cm:.0f}cm \033[m \n'
      f' \033[32m{mm:.0f}mm \033[m \n'
      f' \033[35m{dam:.0f}dam \033[m \n'
      f' \033[37m{dm:.0f}dm \033[m \n')