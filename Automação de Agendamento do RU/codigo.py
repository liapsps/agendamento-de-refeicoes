import pyautogui as pg
import time
from datetime import datetime, timedelta

# Configuração inicial
pg.PAUSE = 1  # Tempo de espera entre os comandos (em segundos)

# Função auxiliar para incrementar a data
def incrementar_data(data):
    """
    Incrementa a data em 1 dia.

    :param data: string - Data no formato "dd/mm/aaaa"
    :return: string - Data incrementada
    """
    formato = "%d/%m/%Y"
    data_formatada = datetime.strptime(data, formato) + timedelta(days=1)
    return data_formatada.strftime(formato)

# Função principal
def agendar_refeicoes_sigaa(usuario, senha, limite_dias, data_inicio):
    """
    Automatiza o agendamento de refeições no SIGAA.

    :param usuario: string - Usuário do SIGAA
    :param senha: string - Senha do SIGAA
    :param limite_dias: int - Número de dias a serem agendados
    :param data_inicio: string - Data de início no formato "dd/mm/aaaa"
    """
    # Passo 1: abrir o SIGAA
    pg.press("win")  # Abrir o menu iniciar
    pg.write("chrome")  # Digitar "chrome"
    pg.press("enter")  # Abrir o navegador
    pg.click(x=346, y=633)  # Clicar no perfil do Chrome

    # Acessar o site do SIGAA
    pg.write("https://si3.ufc.br/sigaa/verTelaLogin.do")
    pg.press("enter")
    time.sleep(2)  # Esperar o site carregar

    # Passo 2: fazer o login
    pg.click(x=647, y=387)  # Ajustar coordenadas do campo de login
    pg.write(usuario)
    pg.press("tab")  # Passar para o campo de senha
    pg.write(senha)
    pg.press("enter")  # Realizar login
    time.sleep(2)

    # Passo 3: abrir o agendamento do RU
    # 3.1 selecionar vínculo
    pg.click(x=685, y=361)
    time.sleep(2)

    # 3.2 acessar o portal do discente no menu principal
    pg.click(x=1020, y=229)
    time.sleep(3)

    # 3.3 selecionar restaurante universitário > agendar refeição
    pg.click(x=834, y=167)
    pg.click(x=846, y=190)
    time.sleep(2)

    # Passo 4 e 5: registrar almoço e janta
    data_atual = incrementar_data(data_inicio)  # Começar com o dia seguinte
    for dia in range(limite_dias):
        # Preencher campos para o almoço
        pg.click(x=601, y=229)  # Clicar no campo "Data do Agendamento"
        pg.write(data_atual)  # Escrever a data atual
        pg.press("tab")

        pg.press("enter")  # Clicar no campo "Tipo de Refeição"
        pg.press("a")  # Selecionar almoço
        pg.press("enter")
        pg.press("tab")

        pg.press("enter")  # Clicar no campo "Horário"
        pg.press("1")  # Selecionar o horário correto
        pg.press("enter")
        pg.press("tab")
        pg.press("enter")  # Cadastrar agendamento
        time.sleep(2)
        pg.press("tab")
        pg.press("enter")
        pg.press("tab")

        # Preencher campos para a janta
        pg.click(x=601, y=229)  # Clicar no campo "Data do Agendamento"
        pg.write(data_atual)  # Escrever a data atual
        pg.press("tab")

        pg.press("enter")  # Clicar no campo "Tipo de Refeição"
        pg.press("j")  # Selecionar janta
        pg.press("enter")
        pg.press("tab")

        pg.press("enter")  # Clicar no campo "Horário"
        pg.press("1")  # Selecionar o horário correto
        pg.press("enter")
        pg.press("tab")
        pg.press("enter")  # Cadastrar agendamento
        time.sleep(2)
        pg.press("tab")
        pg.press("enter")
        pg.press("tab")

        # Incrementar a data para o próximo dia
        data_atual = incrementar_data(data_atual)

    print(f"Agendamento concluído para 8 dias.")

    # Exemplo de uso
if __name__ == "__main__":
    # Definir variáveis necessárias
    usuario = "saddesteye"  # Substituir pelo usuário do SIGAA
    senha = "jna12354"  # Substituir pela senha do SIGAA
    limite_dias = 8  # Número de dias a serem agendados
    data_inicio = "22/01/2025"  # Data inicial no formato "dd/mm/aaaa"

    # Chamar a função principal
    agendar_refeicoes_sigaa(usuario, senha, limite_dias, data_inicio)

"""
# Exemplo de uso
if __name__ == "__main__":
    # Definir variáveis necessárias
    usuario = "seu_usuario"  # Substituir pelo usuário do SIGAA
    senha = "sua_senha"  # Substituir pela senha do SIGAA
    limite_dias = 8  # Número de dias a serem agendados
    data_inicio = "14/01/2025"  # Data inicial no formato "dd/mm/aaaa"

    # Chamar a função principal
    agendar_refeicoes_sigaa(usuario, senha, limite_dias, data_inicio)
    """
