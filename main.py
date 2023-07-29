import requests

cep = input("Digite seu cep:")

cep = cep.replace("-","").replace(".","").replace(" ","").replace("  ","").replace("_","")

if len(cep) == 8:
    link = f'https://viacep.com.br/ws/{cep}/json/'
    requisicao = requests.get(link)
    dic_requisicao = requisicao.json()
    Logradouro = dic_requisicao['logradouro']
    Complemento = dic_requisicao['complemento']
    Bairro = dic_requisicao['bairro']
    Cidade = dic_requisicao['localidade']
    Estado = dic_requisicao['uf']
    print('='*50)
    print('Resultado da Busca: CEP :',cep)
    print('\nLogradouro:',Logradouro,
         '\nComplemento:',Complemento,
          '\nBairro:',Bairro,
          '\nCidade:',Cidade,
          '\nEstado":',Estado)
    print('='*50)
    if len(cep) == 0:
        print("Nenhum CEP informado")
else:
    print("CEP não encontrado")
