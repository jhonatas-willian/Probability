import main

MEDIA_CASA_GERAL = float(f'{(main.CASA_MARCOU_GERAL + main.CASA_SOFREU_GERAL) / main.JOGOS_TIME1}')
MEDIA_FORA_GERAL = float(f'{(main.FORA_MARCOU_GERAL + main.FORA_SOFREU_GERAL) / main.JOGOS_TIME2}')
SOMA_MEDIA_GERAL = float(f'{(MEDIA_CASA_GERAL + MEDIA_FORA_GERAL) / 2}')

MEDIA_CASA = float(f'{(main.CASA_MARCOU + main.CASA_SOFREU) / main.JOGOS_CASA}')
MEDIA_FORA = float(f'{(main.FORA_MARCOU + main.FORA_SOFREU) / main.JOGOS_FORA}')
SOMA_MEDIA = float(f'{(MEDIA_CASA + MEDIA_FORA) / 2}')

MEDIA_GERAL_GOLS_MARCADOS_CASA = float(f'{main.CASA_MARCOU_GERAL / main.JOGOS_TIME1}')
MEDIA_GERAL_GOLS_SOFRIDOS_CASA = float(f'{main.CASA_SOFREU_GERAL / main.JOGOS_TIME1}')

MEDIA_GERAL_GOLS_MARCADOS_FORA = float(f'{main.FORA_MARCOU_GERAL / main.JOGOS_TIME2}')
MEDIA_GERAL_GOLS_SOFRIDOS_FORA = float(f'{main.FORA_SOFREU_GERAL / main.JOGOS_TIME2}')

MEDIA_CASA_MARCOU = float(f'{main.CASA_MARCOU / main.JOGOS_CASA}')
MEDIA_CASA_SOFREU = float(f'{main.CASA_SOFREU / main.JOGOS_CASA}')

MEDIA_FORA_MARCOU = float(f'{main.FORA_MARCOU / main.JOGOS_FORA}')
MEDIA_FORA_SOFREU = float(f'{main.FORA_SOFREU / main.JOGOS_FORA}')


# PORCENTAGEM

# Jogos +1.5 Gols
Porc15Casa = main.Gols * 20
Porc15Fora = main.Gols2 * 20

# Jogos +2.5 Gols
Porc25Casa = main.Gols1 * 20
Porc25Fora = main.Gols3 * 20

# Ambas Marcam
PorcAmbCasa = main.Ambas_CASA * 20
PorcAmbFora = main.Ambas_FORA * 20

# Casa Marcou / Fora Sofreu
PorcCasaMar = main.CASA_GOLS_MARCADO * 20
PorcForaMar = main.FORA_GOLS_MARCADO * 20

# Casa Sofreu / Fora Sofreu
PorcCasaSof = main.CASA_GOLS_SOFRIDO * 20
PorcForaSof = main.FORA_GOLS_SOFRIDO * 20
