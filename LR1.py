def razmer():
  fl=False
  while(fl==False):
    try:
      c=int(input('Введите количество стратегий I игрока: '))
      d=int(input('Введите количество стратегий II игрока: '))
      fl=True
    except ValueError:
      print('Неверный формат поданных на вход данных!') 
    if c==0 or d==0:
      fl=False
      print('Размеры матрицы не могут быть нулевыми!')
  return c,d 

def vvod():
  max_sl=0
  tablic=[]
  strat1=[]
  strat2=[]
  for i in range (0,a):
    strat1.append(input(str(i+1) + ' стратегия I игрока: '))
  for i in range(0,a):
    if max_sl<len(strat1[i]):
      max_sl=len(strat1[i])
  for i in range (0,b):
    strat2.append(input(str(i+1) + ' стратегия II игрока: '))
  for i in range (0,a):
    tablstr=[]
    for j in range (0,b):
      fl=False
      while(fl==False):
        try:
          win=[0,0]
          win[0]=int(input('Выйгрыши I игрока в ситуации (' + strat1[i] + ';' + strat2[j] +  '): '))
          win[1]=int(input('Выйгрыши II игрока в ситуации (' + strat1[i] + ';' + strat2[j] +  '): '))
          fl=True
        except ValueError:
          print('Неверный формат поданных на вход данных!') 
      tablstr.append(win)
    tablic.append(tablstr)

  qw=max_sl*2*' '
  print('Игровая матрица: ')
  print(max_sl*2*' ' + qw.join(strat2))
  for i in range(0,a):
    stroka=''
    for j in range(0,b):
      stroka=stroka + '(' + str(tablic[i][j][0]) + ',' + str(tablic[i][j][1]) + ')' + 2*max_sl*' '
    print(strat1[i] + max_sl*' ' + stroka)
  return strat1,strat2,tablic

def maxab():
  maxa={}
  maxb={}
  for i in range(0,b):
    maxb[stratI[0] + '*' + stratII[i]]=tabl[0][i][0]
    for j in range(0,a):
      keyss={}
      for key in maxb:
        keyss[key]=0
      for key in keyss:
        if (int(maxb[key]) == int(tabl[j][i][0])) and str(key).endswith(stratII[i]):
          maxb[stratI[j] + '*' + stratII[i]] = tabl[j][i][0]
        if (int(maxb[key]) < int(tabl[j][i][0])) and str(key).endswith(stratII[i]):
          maxb.pop(key)
          maxb[stratI[j] + '*' + stratII[i]] = tabl[j][i][0]

  for i in range(0,a):
    maxa[stratI[i] + '*' + stratII[0]]=tabl[i][0][1]
    for j in range(0,b):
      keyss={}
      for key in maxa:
        keyss[key]=0
      for key in keyss:
        if (int(maxa[key]) == int(tabl[i][j][1])) and str(key).startswith(stratI[i]):
          maxa[stratI[i] + '*' + stratII[j]] = tabl[i][j][1]
        if (int(maxa[key]) < int(tabl[i][j][1])) and str(key).startswith(stratI[i]):
          maxa.pop(key)
          maxa[stratI[i] + '*' + stratII[j]] = tabl[i][j][1]
  maxbb=str(maxb)
  maxaa=str(maxa)
  print('Максимумы для I игрока: ' + maxbb)
  print('Максимумы для II игрока: ' + maxaa)
  return maxa, maxb

def naash():
  nash={}
  for keya in max_a:
    for keyb in max_b:
      if keya==keyb:
        nash[keya]=[int(max_b[keya]),int(max_a[keyb])]
  nshh=str(nash)
  print('Равновесие по Нэшу: ' + nshh)
  return nash

def paretto():
  pareto={}
  max_sum=[int(tabl[0][0][0])+int(tabl[0][0][1]),stratI[0],stratII[0]]
  for i in range(0,a):
    for j in range(0,b):
      if max_sum[0]<int(tabl[i][j][0])+int(tabl[i][j][1]):
        max_sum=[int(tabl[i][j][0])+int(tabl[i][j][1]),stratI[i],stratII[j],i,j]
  pareto=[stratI[max_sum[3]] + '*' + stratII[max_sum[4]],tabl[max_sum[3]][max_sum[4]][0],tabl[max_sum[3]][max_sum[4]][1]]
  prtt=str(pareto)
  print('Оптимум по Парето: ' + prtt)
  return pareto

char=''
itog=[]
while char!='e':
  print('------------------------------------------------' + '\n' + 'r - ввод размера матрицы,' + '\n' + 'v - ввод матрицы решений' + '\n' + 'm - нахождение максимумов по строкам и столбцам' + '\n' + 'n - равновесие по Нэшу' + '\n' + 'p - оптимум по Парето' + '\n' + 'e - выход' + '\n' + '------------------------------------------------')
  char=input('Выберите действие: ')

  if char=='r':
    itog.clear()
    itog.append('r')
    a,b=razmer()

  if char=='v' and 'r' in itog:
    itog.append('v')
    stratI,stratII,tabl=vvod()
  if char=='v' and 'r' not in itog:
    print('Вы не ввели размерность матрицы!')

  if char=='m' and 'v' in itog:
    itog.append('m')
    max_a,max_b=maxab()
  if char=='m' and 'v' not in itog:
    print('Вы не ввели матрицу!')

  if char=='n' and 'm' in itog:
    itog.append('n')
    nsh=naash()
  if char=='n' and 'm' not in itog:
    print('Вы не нашли максимумы для игроков!')

  if char=='p' and 'v' in itog:
    itog.append('p')
    prt=paretto()
  if char=='p' and 'v' not in itog:
    print('Вы не ввели матрицу!')

  if char=='e':
    exit()
  
  if char!='r' and char!='v' and char!='m' and char!='n' and char!='p' and char!='e':
    print('Для данной буквы не задано действие! Попробуйте снова.')