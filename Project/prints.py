import main
import calculos

from condicoes import Gols15, Gols25, Ambas

from calculos import Porc15Casa, Porc15Fora
from calculos import Porc25Casa, Porc25Fora
from calculos import PorcAmbCasa, PorcAmbFora
from calculos import PorcCasaMar, PorcForaMar
from calculos import PorcCasaSof, PorcForaSof

# TIMES que irão se enfrentar
print("\n---------------------------------------------------------------")
print(f"|                    {main.TIME1} x {main.TIME2}       ")
print("---------------------------------------------------------------")

print(f"|       MANDANTE                 "
      f"|       VISITANTE            |"
      
      f"\n|                                |                            |")

# Gols +1.5
print(f"|       Gols +1.5                |       "
      f"Gols +1.5            |"
      f"\n|       {main.Gols}/5 Jogos ({Porc15Casa}%)          |       "
      f"{main.Gols2}/5 Jogos ({Porc15Fora}%)      |")

print(f"|-------------------------------------------------------------|\n"
      f"|       Gols +2.5                "
      f"|       Gols +2.5            |")

# Gols +2.5
print(f"|       {main.Gols1}/5 Jogos ({Porc25Casa}%)          |       "
      f"{main.Gols3}/5 Jogos ({Porc25Fora}%)      |")

print(f"|-------------------------------------------------------------|\n"
      f"|       Ambas Marcam             "
      f"|       Ambas Marcam         |")

# Ambas equipes Marcam
print(f"|       {main.Ambas_CASA}/5 Jogos ({PorcAmbCasa}%)          |       "
      f"{main.Ambas_FORA}/5 Jogos ({PorcAmbFora}%)      |")

print(f"|-------------------------------------------------------------|\n"
      f"|       CASA Marcou              "
      f"|       FORA Marcou          |")

# Casa Marcou Gol / Fora Marcou Gol
print(f"|       {main.CASA_GOLS_MARCADO}/5 Jogos ({PorcCasaMar}%)          |       "
      f"{main.FORA_GOLS_MARCADO}/5 Jogos ({PorcForaMar}%)      |")

print(f"|-------------------------------------------------------------|\n"
      f"|       CASA Sofreu              "
      f"|       FORA Sofreu          |")

# Casa Sofreu Gol / Fora Sofreu Gol
print(f"|       {main.CASA_GOLS_SOFRIDO}/5 Jogos ({PorcCasaSof}%)          |       "
      f"{main.FORA_GOLS_SOFRIDO}/5 Jogos ({PorcForaSof}%)      |")

print(f"|-------------------------------------------------------------|\n"
      f"|       Média Marcado CASA       "
      f"|       Média Marcado FORA   |")

# Média de Gols Marcados CASA / Média de Gols Marcados FORA (Últimos 5 jogos)
print(f"|       {main.GOLS_MARCADOS_CASA / 5:.2f} ({main.GOLS_MARCADOS_CASA} Gols)            |       "
      f"{main.GOLS_MARCADOS_FORA / 5:.2f} ({main.GOLS_MARCADOS_FORA} Gols)        |")

print(f"|-------------------------------------------------------------|\n"
      f"|       Média Sofrido CASA       "
      f"|       Média Sofrido FORA   |")

# Média de Gols Sofridos CASA / Média de Gols Sofridos FORA (Últimos 5 jogos)
print(f"|       {main.GOLS_SOFRIDOS_CASA / 5:.2f} ({main.GOLS_SOFRIDOS_CASA} Gols)            |       "
      f"{main.GOLS_SOFRIDOS_FORA / 5:.2f} ({main.GOLS_SOFRIDOS_FORA} Gols)        |")

print(f"|-------------------------------------------------------------|\n"
      f"|       Média GERAL              "
      f"|       Média CASA + FORA    |")

# Média Geral / Média Casa + Fora
print(f"|       {calculos.MEDIA_CASA_GERAL:.2f} + {calculos.MEDIA_FORA_GERAL:.2f}              "
      f"|       {calculos.MEDIA_CASA:.2f} + {calculos.MEDIA_FORA:.2f}          |\n"
      f"|       Média = {calculos.SOMA_MEDIA_GERAL:.2f}             "
      f"|       Média = {calculos.SOMA_MEDIA:.2f}         |")

# Média Total Geral / Média Total Casa + Fora
print(f"|                          "
      f" Média Geral                       |\n"
      f"|                             "
      f" {(calculos.SOMA_MEDIA_GERAL + calculos.SOMA_MEDIA) / 2:.2f}"
      f"                           |")

print(f"|-------------------------------------------------------------|\n"
      f"|       MANDANTE                 "
      f"|       VISITANTE            |"
      f"\n|                                |                            |\n"
      f"|       GERAL                    "
      f"|       GERAL                |")

# Média Geral Gols Marcados Casa / Média Geral Gols Marcados Fora
# Média Geral Gols Sofridos Casa / Média Geral Gols Sofridos Fora
print(f"|       {calculos.MEDIA_GERAL_GOLS_MARCADOS_CASA:.2f}                     |       "
      f"{calculos.MEDIA_GERAL_GOLS_MARCADOS_FORA:.2f}                 |"
      f"\n|       {calculos.MEDIA_GERAL_GOLS_SOFRIDOS_CASA:.2f}                     |       "
      f"{calculos.MEDIA_GERAL_GOLS_SOFRIDOS_FORA:.2f}                 |")

print(f"|                                |                            |\n"
      f"|       CASA                     "
      f"|       FORA                 |")

# Média Casa Marcou / Média Fora Marcou
# Média Casa Sofreu / Média Fora Sofreu
print(f"|       {calculos.MEDIA_CASA_MARCOU:.2f}                     |       "
      f"{calculos.MEDIA_FORA_MARCOU:.2f}                 |"
      f"\n|       {calculos.MEDIA_CASA_SOFREU:.2f}                     |       "
      f"{calculos.MEDIA_FORA_SOFREU:.2f}                 |")

print(f"---------------------------------------------------------------")

# Condição: Gol +1.5 (Alta, Média e Baixa Probabilidade)
Gols15()
# Condição: Gol +2.5 (Alta, Média e Baixa Probabilidade)
Gols25()
# Condição: Ambas Marcam (Alta, Média e Baixa Probabilidade)
Ambas()
