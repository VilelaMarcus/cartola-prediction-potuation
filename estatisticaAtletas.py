import pandas as pd
import requests

# Faz a requisição para a API do Cartola
url = 'https://api.cartola.globo.com/atletas/mercado'
response = requests.get(url)

# Verifica se a requisição foi bem sucedida
if response.status_code == 200:
    data = response.json()

    # Lista para armazenar os dados dos jogadores
    players_data = []

    # Scouts disponíveis
    scouts_list = [
        'FF', 'G', 'CA', 'DS', 'FC', 'FD', 'FS', 'I', 'SG', 'DE', 'DP',
        'GS', 'PC', 'CV', 'FT', 'A', 'PS', 'V', 'PP'
    ]

    # Dicionário de clubes (para mapear ID do clube para nome do clube)
    clubes_dict = {club['id']: club['nome'] for club in data['clubes'].values()}

    # Itera sobre os jogadores na resposta da API
    for player in data['atletas']:
        player_id = player['atleta_id']
        nome = player['apelido']
        posicao_id = player['posicao_id']
        pontos = player['pontos_num']

        # Processa os scouts (caso haja)
        player_scouts = {scout: player['scout'].get(scout, 0) for scout in scouts_list}

        # Obtém mais informações do jogador
        clube_id = player['clube_id']
        clube_nome = clubes_dict.get(clube_id, 'Desconhecido')  # Obtém o nome do clube

        status_id = player['status_id']
        preco = player['preco_num']
        jogos_num = player['jogos_num']
        rodada_id = player['rodada_id']
        media_num = player['media_num']
        variacao_num = player['variacao_num']

        # Cria um dicionário com os dados do jogador
        player_info = {
            'ID': player_id,
            'Nome': nome,
            'Posição': posicao_id,
            'Pontos': pontos,
            'Preço': preco,
            'Jogos': jogos_num,
            'Rodada': rodada_id,
            'Média': media_num,
            'Variação': variacao_num,
            'Clube': clube_nome,  # Adiciona o nome do clube
            'Status_ID': status_id,
            **player_scouts  # Inclui os scouts como colunas individuais
        }

        players_data.append(player_info)

    # Cria um DataFrame com os dados dos jogadores
    df = pd.DataFrame(players_data)

    # Escreve os dados em um arquivo Excel
    df.to_excel('stats-rodada-3.xlsx', index=False)

    print("Dados exportados para dados_cartola.xlsx com sucesso!")

else:
    print("Erro ao acessar a API do Cartola.")
