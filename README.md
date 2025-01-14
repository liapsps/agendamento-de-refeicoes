# Automação de Agendamento dp RU pelo SIGAA

Esse projeto tem como objetivo automatizar o processo de agendamento de refeições no Restaurante Universitário (RU) através do SIGAA (Sistema Integrado de Gestão de Atividades Acadêmicas). Utilizando a biblioteca `pyautogui`, o programa simula ações de teclado e mouse para realizar o agendamento de forma eficiente e rápida.

---

## Funcionalidades

- Realiza login automático no SIGAA.
- Navega pelo sistema até a página de agendamento de refeições do RU.
- Agenda automaticamente refeições de almoço e jantar para um número determinado de dias.
- Incrementa a data para garantir que os agendamentos sejam realizados apenas a partir do próximo dia.

---

## Pré-requisitos

- **Python 3.6 ou superior**
- Bibliotecas Python:
  - `pyautogui`
  - `datetime`

Para instalar o `pyautogui`, utilize o comando:
```bash
pip install pyautogui
```

---

## Configuração

### Antes de Executar o Código

1. **Coordenadas de Tela**: 
   As coordenadas (`x, y`) usadas no código foram baseadas em uma configuração específica de tela. Para ajustar ao seu computador, você pode usar a ferramenta `pyautogui.position()` para capturar as coordenadas corretas dos elementos na tela.

   Exemplo para capturar coordenadas:
   ```python
   import pyautogui as pg
   print(pg.position())
   ```

2. **Dados de Login**:
   Substitua as variáveis `usuario` e `senha` pelos seus dados do SIGAA:
   ```python
   usuario = "seu_usuario"
   senha = "sua_senha"
   ```

3. **Data Inicial**:
   Informe a data inicial no formato `dd/mm/aaaa`, garantindo que seja a data de hoje ou futura:
   ```python
   data_inicio = "14/01/2025"
   ```

4. **Limite de Dias**:
   Configure o número de dias para agendar refeições:
   ```python
   limite_dias = 8
   ```

---

## Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/automacao-agendamento-ru.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd automacao-agendamento-ru
   ```

3. Execute o script:
   ```bash
   python script.py
   ```

---

## Fluxo do Programa

1. **Abrir o Navegador**: Abre o navegador Chrome e acessa a página de login do SIGAA.
2. **Login**: Preenche automaticamente o usuário e a senha para realizar o login.
3. **Navegação**: Acessa o portal do discente e a página de agendamento de refeições do RU.
4. **Agendamento**: Preenche os campos necessários (data, tipo de refeição e horário) e confirma o agendamento.
5. **Iteração**: Repete o processo para os dias subsequentes até atingir o limite especificado.

---

## Personalização

Caso você precise ajustar algo, como coordenadas ou horários, edite os seguintes trechos do código:

- **Coordenadas**: Substitua as coordenadas `pg.click(x, y)` por valores adaptados à sua tela.
- **Horário das Refeições**: Ajuste os valores selecionados para o campo de horário (ex.: `pg.press("1")`).

---

## Observação

Este script é um exemplo de automação simples e pode não se adaptar a todas as situações. Certifique-se de usá-lo de forma responsável e dentro das políticas de uso do SIGAA.

---

## Contato

Caso tenha dúvidas ou sugestões, entre em contato:

- **E-mail**: lialilinbox@gmail.com
- **GitHub**: https://github.com/liapsps/
