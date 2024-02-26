"""
# Leitura do horário inicial
hora_inicio = int(input("Digite a hora de início: "))
minuto_inicio = int(input("Digite o minuto de início: "))
segundo_inicio = int(input("Digite o segundo de início: "))

# Leitura da duração em segundos
duracao_segundos = int(input("Digite a duração em segundos: "))

# Calculando o horário de término
hora_termino = hora_inicio
minuto_termino = minuto_inicio
segundo_termino = segundo_inicio + duracao_segundos

# Ajustando os segundos
minuto_termino += segundo_termino // 60
segundo_termino %= 60

# Ajustando os minutos
hora_termino += minuto_termino // 60
minuto_termino %= 60

# Ajustando as horas
hora_termino %= 24  # Se o resultado ultrapassar 24 horas, ajusta para o próximo dia

# Impressão do resultado
print(f"Horário de término: {hora_termino}:{minuto_termino}:{segundo_termino}")


"""

# Recebendo o horário de início (hora, minuto e segundo)
hora_inicio = int(input("Digite a hora de início (0-23): "))
minuto_inicio = int(input("Digite o minuto de início (0-59): "))
segundo_inicio = int(input("Digite o segundo de início (0-59): "))

# Recebendo a duração em segundos
duracao_segundos = int(input("Digite a duração em segundos: "))

# Calculando o novo horário de término
segundos_totais = hora_inicio * 3600 + minuto_inicio * 60 + segundo_inicio
segundos_finais = segundos_totais + duracao_segundos

hora_final = segundos_finais // 3600
minuto_final = (segundos_finais % 3600) // 60
segundo_final = segundos_finais % 60

# Exibindo o resultado
print(f"O novo horário de término é: {hora_final}:{minuto_final:02d}:{segundo_final:02d}")



