import re

def extrair_informacoes_anuncio(publicacao): #buscando e separando as informações 
    informacoes = {}
   
    if re.search(r'vend', publicacao, re.IGNORECASE):
        informacoes['Modalidade'] = 'Venda'
    elif re.search(r'alug', publicacao, re.IGNORECASE):
        informacoes['Modalidade'] = 'Aluguel'
    else:
        informacoes['Modalidade'] = 'nao informado'

    # Tipo
    tipo_match = re.search(r'casa|apartamento', publicacao, re.IGNORECASE)
    if tipo_match:
        informacoes['Tipo'] = tipo_match.group(0).capitalize()
    else:
        informacoes['Tipo'] = "nao informado"

    # Endereço
    endereco_find = re.findall(r'(?:Rua|Avenida)[^\d]*\d+', publicacao)
    if len(endereco_find) > 0:
        informacoes['Endereco'] = endereco_find[0]
    else:
        informacoes['Endereco'] = "nao informado"
    

    # CEP
    cep_match = re.search(r'\d{5}-\d{3}\b', publicacao)
    if cep_match:
        informacoes['CEP'] = cep_match.group(0)
    else:
        informacoes['CEP'] = "nao informado" 

    # Área
    area_match = re.search(r'\d+\s*(metros quadrados|m2)', publicacao, re.IGNORECASE)
    if area_match:
        informacoes['Area'] = area_match.group(0).split()[0]
    else:
        informacoes['Area'] = "nao informado"    

    # Valor
    valor_find = re.findall(r'(?:R\$\s?)\d+(?:[\.\,]?\d+)+|\d+(?:[\.\,]?\d+)+ reais', publicacao)

    if len(valor_find) > 0:
        informacoes['Valor'] = valor_find[0].replace('R$', '').replace('reais', '').strip()
    else:
        informacoes['Valor'] = "nao informado"
    
    # Telefone(s)
    telefone_match = re.findall(r'\d{4,5}-\d{4}', publicacao)
    if telefone_match:
        if len(telefone_match) > 1:
            informacoes['Telefones'] = ', '.join(telefone_match)
        else:
            informacoes['Telefone'] = telefone_match[0]
            
    else:
        informacoes['Telefone'] = "nao informado"

    # Responsável, ARRUMA NE
    responsavel_find = re.findall(r'([A-Z]\w*\s?(?:[A-Z]\w*\s?){0,2})', publicacao)
    if len(responsavel_find) > 0:
        informacoes['Responsavel'] = responsavel_find[-1]
    else:
        informacoes['Responsavel'] = "nao informado"

    return informacoes


#publicacao = ("Apartamento disponivel para aluguel na Avenida Sao Carlos, numero 542, CEP 13560-010. 140 metros quadrados, confortavel e espacoso. Falar no numero 99245-1777 com Jose Galdino.")
#publicacao = ("Vendo um apartamento na Rua Alameda dos Crisantemos, 175, CEP 13566-550, proximo ao Bar do Toco, boa localizacao, arejado e com jardim secreto. Valor da venda a combinar. Falar com Rosane Minghim, no numero 99321-9746.")
#publicacao = ("Apartamento para aluguel na Rua Jacinto Favoretto, 739, bairro Jardim Lutfalla, 87 m2. Valor: R$1.100,00 mensais. Necessário fiador morador de São Carlos. Contato: 99913-4532 ou 9231-8888. Geraldo Garcia Novaes.")
#publicacao = ("Oportunidade unica. Vendo uma casa na Rua Episcopal, 45, super espacosa, 200 metros quadrados. O valor a vista eh 126.000,00 reais. Aceito permuta de terreno em Ribeirao Preto-SP. Telefone para contato e 9971-1056. Ricardo Campelo.")
#publicacao = ("Tenho um apartamento para vender na Avenida Getulio Vargas, n. 387, na Vila Irene. O apartamento possui 132 metros quadrados, vazado, poente, 3 quartos, 2 banheiros, 1 cozinha e ar condicionado. Estou pedindo 200000,00 reais. Por favor, falar no numero 81234-9823 com Francisco Louzada.")
#publicacao = ("Quero alugar uma casa completa, mobiliada, na Avenida Doutor Carlos Botelho, 1245, 13560-250, no Centro, proximo a padaria Guanabara. Valor e demais detalhes devem ser consultados no telefone 2124-2546 com Fernando Osorio.")
#publicacao = ("Eu nao gostaria, mas estou endividado e preciso vender uma casa na Avenida Francisco Pereira Lopes, n. 7, no Cidade Jardim. A casa possui churrasqueira, piscina, 230 m2, 4 quartos, 1 suite, 3 vagas para carros, 1 sala e 1 quarto de servico. Tem um fusca velho guardado nos fundos, mas precisa quitar 20 parcelas vencidas do IPVA. O valor para venda eh 56234234 reais, mas faco desconto se quiser ficar com a minha sogra que soh sabe reclamar. Contato: 0000-0000. Falar com Illiarde Ubijara, tambem conhecido como jacare.")
#publicacao = ("9876-5432. Vendo casa na Avenida da vida 13. 12345-678. 2.357,00 reais, 42 m2. Tem de ligar para o J J e perguntar mais detalhes.")
#publicacao = ("Casa de 42 m2 para venda na Avenida da vida 13. 9876-5432 12345-678 por 2.357 reais. Tem de ligar para o J J J e perguntar mais detalhes.")
#publicacao = ("12345-678 Avenida da vida 13, 42 m2 de casa para vender. 2357 reais. 9876-5432 09876-5432. Fale com J J.")
#publicacao = ("9876-5432. Aluguel de apartamento na Rua da Lua 42, 12345-678. R$2.357,00, 13 metros quadrados. J J.")
#publicacao = ("Alugo apartamento de 13 metros quadrados na Rua da Lua 42 9876-5432 12345-678 por R$2.357. Fale com J J J.")
#publicacao = ("Rua da Lua 42 12345-678, 13 metros quadrados, apartamento para alugar. R$2357. Ligue dja! 9876-5432 ou 09876-5432. J J J.")


for a, b in extrair_informacoes_anuncio(input()).items():
    print(f'{a}: {b}')