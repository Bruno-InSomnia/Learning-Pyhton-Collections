# usuarios_data_science = {15, 23, 43, 56}
# usuarios_machine_learning = {13, 23, 56, 42}
#
# # assistiram = usuarios_data_science.copy()
# # assistiram.extend(usuarios_machine_learning)
#
# # print(set(assistiram))
#
# print(usuarios_machine_learning | usuarios_data_science)

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"

meu_texto = meu_texto.lower()

print(len(meu_texto.split()))

print(set(meu_texto.split()))

print(len(set(meu_texto.split())))

def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower()) #devolve um dicionário com todas as letras e qtd. de aparições
    total_de_caracteres = sum(aparicoes.values()) #soma os valores de todas as letras (quantidade total de carct.)

    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
	#cria uma lista de tuplas com a letra(primeiro valor) + frequencia(segundo valor que foi devolvido por counter) e faz um for de ambos no dicionário.items(que pega ambos)
    proporcoes = Counter(dict(proporcoes))
	#cria um dicionário com a lista e tuplas de proporções e também utiliza um Counter, pois o counter leva em consideração já os valores, e não as chaves)
    mais_comuns = proporcoes.most_common(10) #chama a função de dictionary .most_common e passa o parametro 10 para sinalizar as 10 primeiras
    for caractere, proporcao in mais_comuns: #pede a impressão formatada dos dados em mais_comuns
        print("{} => {:.2f}%".format(caractere, proporcao * 100)) #formata os dados transformando em porcentagens
    analisa_frequencia_de_letras(texto1) #chama a função passando o parametro 'texto1'