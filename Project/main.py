
TIME1 = input('\nInforme o Time da CASA: ')
TIME2 = input('Informe o Time de FORA: ')

JOGOS_TIME1 = int(input(f'\nInforme a quantidade de Jogos Geral {TIME1}: '))
CASA_MARCOU_GERAL = int(input(f"Total de Gols Marcados por {TIME1}: "))
CASA_SOFREU_GERAL = int(input(f"Total de Gols Sofridos por {TIME1}: "))

JOGOS_TIME2 = int(input(f'\nInforme a quantidade de jogos Geral {TIME2}: '))
FORA_MARCOU_GERAL = int(input(f'Total de Gols Marcados por {TIME2}: '))
FORA_SOFREU_GERAL = int(input(f'Total de Gols Sofridos por {TIME2}: '))

JOGOS_CASA = int(input(f'\nInforme a quantidade de Jogos em CASA {TIME1}: '))
CASA_MARCOU = int(input(f"Quantidade de Gols {TIME1} Marcou em CASA: "))
CASA_SOFREU = int(input(f"Quantidade de Gols {TIME1} Sofreu em CASA: "))

JOGOS_FORA = int(input(f'\nInforme a quantidade de jogos FORA {TIME2}: '))
FORA_MARCOU = int(input(f'Quantidade de Gols {TIME2} Marcou FORA: '))
FORA_SOFREU = int(input(f'Quantidade de Gols {TIME2} Sofreu FORA: '))

Gols = int(input(f'\nGols +1.5 de {TIME1} em CASA: '))
Gols1 = int(input(f"Gols +2.5 de {TIME1} em CASA: "))
Ambas_CASA = int(input(f"Ambas Marcam {TIME1} em CASA: "))
CASA_GOLS_MARCADO = int(input(f"Nº de Jogos que {TIME1} Marcou em CASA: "))
CASA_GOLS_SOFRIDO = int(input(f"Nº de Jogos que {TIME1} Sofreu em CASA: "))
GOLS_MARCADOS_CASA = int(input(f'Gols Marcados {TIME1} Últimos 5 Jogos CASA: '))
GOLS_SOFRIDOS_CASA = int(input(f'Gols Sofridos {TIME1} Últimos 5 Jogos CASA: '))

Gols2 = int(input(f'\nGols +1.5 de {TIME2} FORA: '))
Gols3 = int(input(f'Gols +2.5 de {TIME2} FORA: '))
Ambas_FORA = int(input(f'Ambas Marcam {TIME2} FORA: '))
FORA_GOLS_MARCADO = int(input(f"Nº de Jogos que {TIME2} Marcou FORA: "))
FORA_GOLS_SOFRIDO = int(input(f"Nº de Jogos que {TIME2} Sofreu FORA: "))
GOLS_MARCADOS_FORA = int(input(f'Gols Marcados {TIME2} Últimos 5 Jogos FORA: '))
GOLS_SOFRIDOS_FORA = int(input(f'Sofridos {TIME2} Últimos 5 Jogos FORA: '))
