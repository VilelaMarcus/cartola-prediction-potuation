import requests
import csv

# Fazendo requisição à API do Cartola
url = 'https://api.cartola.globo.com/partidas/3'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Nome do arquivo CSV
    csv_filename = 'resultados_partidas_rodada3.csv'

    # Abrindo arquivo CSV em modo de escrita
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')  # Use semicolon as the delimiter

        # Escrevendo o cabeçalho no CSV
        writer.writerow(['Time Casa', 'Time Visitante', 'Resultado'])

        # Iterando sobre cada partida
        for partida in data['partidas']:
            # Obtendo informações relevantes de cada partida
            time_casa = data['clubes'][str(partida['clube_casa_id'])]['nome']
            time_visitante = data['clubes'][str(partida['clube_visitante_id'])]['nome']
            placar_casa = partida['placar_oficial_mandante']
            placar_visitante = partida['placar_oficial_visitante']
            resultado = f"{placar_casa}-{placar_visitante}"

            # Escrevendo uma linha no CSV para cada partida
            writer.writerow([time_casa, time_visitante, resultado])

    print(f'Arquivo CSV criado com os resultados dos confrontos: {csv_filename}')
else:
    print(f'Erro ao acessar API do Cartola. Código de status: {response.status_code}')
