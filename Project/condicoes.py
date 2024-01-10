import main

from calculos import MEDIA_CASA_MARCOU as AMBAS1
from calculos import MEDIA_CASA_SOFREU as AMBAS2
from calculos import MEDIA_FORA_MARCOU as AMBAS3
from calculos import MEDIA_FORA_SOFREU as AMBAS4

from calculos import MEDIA_CASA_GERAL as Casa1
from calculos import MEDIA_FORA_GERAL as Fora1
from calculos import SOMA_MEDIA_GERAL as Soma1

from calculos import MEDIA_CASA as Casa2
from calculos import MEDIA_FORA as Fora2
from calculos import SOMA_MEDIA as Soma2


def Gols15():
    if (Casa1 >= 2.50 and Soma1 >= 2.70 or Fora1 >= 2.50 and Soma1 >= 2.70
            and Casa2 >= 2.50 and Soma2 >= 2.70 or Fora2 >= 2.50 and Soma2 >= 2.70):
        print('\n Probabilidade de +1.5 Gols: ALTA')
    elif (2.00 <= Casa1 < 2.50 or 2.00 <= Fora1 < 2.50 or 2.40 <= Soma2 < 2.70
          and 2.00 <= Casa2 < 2.50 or 2.00 <= Fora2 < 2.50 or 2.40 <= Soma2 < 2.70):
        print('\nProbabilidade de +1.5 Gols: MÉDIA')
    elif (Casa1 < 2.00 and Soma1 < 2.00 or Fora1 < 2.00 and Soma1 < 2.00
          or Casa2 < 2.00 and Soma2 < 2.00 or Fora2 and Soma2 < 2.00):
        print('\nProbabilidade de +1.5 Gols: BAIXA')


def Gols25():
    if (Casa1 >= 3.50 and Soma1 >= 3.50 or Fora1 >= 3.50 and Soma1 >= 3.50
            or Casa2 >= 3.50 and Soma2 >= 3.50 or Fora2 >= 3.50 and Soma2 >= 3.50):
        print('\nProbabilidade de +2.5 Gols: ALTA')
    elif (2.80 <= Casa1 < 3.50 or 2.80 <= Fora1 < 3.50 or 3.00 <= Soma1 < 3.50
          and 2.80 <= Casa2 < 3.50 or 2.80 <= Fora2 < 3.50 or 3.00 <= Soma2 < 3.50):
        print('\nProbabilidade de +2.5 Gols: MÉDIA')
    elif (Casa1 < 2.80 and Soma1 < 2.80 or Fora1 < 2.80 and Soma1 < 2.80
          or Casa2 < 2.80 and Soma2 < 2.80 or Fora2 < 2.80 and Soma2 < 2.80):
        print(f'\nProbabilidade de +2.5 Gols: BAIXA')


def Ambas():
    if AMBAS1 >= 1.30 and AMBAS2 >= 1.30 and AMBAS3 >= 1.30 and AMBAS4 >= 1.30:
        print('\nProbabilidade de Ambos Marcarem: ALTA')
    elif 0.50 < AMBAS1 < 1.30 or 0.50 < AMBAS2 < 1.30 or 0.50 < AMBAS3 < 1.30 or 0.50 < AMBAS4 < 1.30:
        print('\nProbabilidade de Ambos Marcarem: MÉDIA')
    elif AMBAS1 <= 0.50 or AMBAS2 <= 0.50 or AMBAS3 <= 0.50 or AMBAS4 <= 0.50:
        print('\nProbabilidade de Ambos Marcarem: BAIXA')

