from index import *

sequencia = input("Digite a sequência de nucleotídeos:")
if(valida(sequencia)):
    frec = frequencia(sequencia)
    print("Quantidade de cada nucleotídeo: ", frequencia(sequencia))
    print("Porcentagem de cada: ", porcentagem(sequencia, frec))
    print("A sequencia reversa é: ", reverse(sequencia))
    print("A transcrição (mRNA) da sequencia é: ", mRNA(sequencia))
    print("A tradução literal da sequencia é: ", traducao(sequencia, 0))
    print("As possiveis proteinas para a sequência é ", all_possible_proteinas(sequencia))

    c=input("Digite as cadeias de nucleotideos que deseja verificar se estão presentes, 0 para sair")
    while(c!="0"):
        x = find_all_occurrences_re( sequencia, c)
        if(x): 
            print("Local de ocorrencias: ",x)
            print(str(len(x))+" Ocorrencias")
        c=input("Digite as cadeias de nucleotideos que deseja verificar se estão presentes, 0 para sair")

