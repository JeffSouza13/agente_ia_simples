while True:
    mensagem = input('Você: ')

    if 'agendar' in mensagem.lower():
        print('Agente: Claro! Para qual data e horário você gostaria de agendar?')
    elif 'cancelar' in mensagem.lower():
        print('Agente: Entendido. Qual é o número do seu agendamento para que eu possa cancelá-lo?')
    elif 'preço' in mensagem.lower():
        print('Agente: O preço do serviço é de R$100. Gostaria de agendar?')
    elif 'sair' in mensagem.lower():
        print('Agente: Até logo! Se precisar de mais alguma coisa, é só chamar.')
        break
    else:
        print('Agente: Desculpe, não entendi sua mensagem. Por favor, tente novamente.')