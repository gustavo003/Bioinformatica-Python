from functions import *

def infos(sequencia):
    print("\n\n")
    assert valida(sequencia)
    frec = frequencia(sequencia)

    print("Digite o que deseja analisar: \n\n")
    c = input("1 - Quantidade de cada nucleotideo\n2 - Porcentagem de cada nucleotídeo\n"
    "3 - Sequencia reverse (DNA Complementar)\n4 - Transcrição(mRNA)\n5 - A tradução literal da sequência:" 
    "\n6 - As proteínas possíveis existentes\n7 - Verificar as cadeiras de nucleotídeos que estão presentes"
    "\n8 - Fazer pareamento de sequências\n 0 para sair\n")
    while(c!="0"):
        if(c=="1"):
            print("\n\nQuantidade de cada nucleotídeo: \n\n", frec)
        if(c=="2"):
            print("\n\nPorcentagem de cada: \n\n", porcentagem(sequencia, frec))
        if(c=="3"):
            print("\n\nA sequencia reversa é: \n\n", reverse(sequencia))
        if(c=="4"):
            print("\n\nA transcrição (mRNA) da sequencia é: \n\n", mRNA(sequencia))
        if(c=="5"):
            print("\n\nA tradução literal da sequencia é: \n\n", traducao(sequencia, 0))
        if(c=="6"):
            poss = all_possible_proteinas(sequencia)
            print("\n\nAs possiveis proteinas para a sequência são \n\n",poss)
        if(c=="7"):
            x=input("\n\nDigite a cadeia de nucleotideos que deseja verificar se estão presentes, 0 para sair\n")
            if(valida(x)):
                m = find_all_occurrences_re( sequencia, x)
                if(m): 
                    print("Local de ocorrencias(índices): ",m)
                    print(str(len(m))+" Ocorrencias\n")
        if (c=="8"):
            x=input("\nDigite sequências que gostaria de fazer o alinhamento, 0 para sair\n")
            x = x.strip()
            if(valida(x)):
                needleman_wunsch(sequencia, x)
        c = input("\n1 - Quantidade de cada nucleotideo\n2 - Porcentagem de cada nucleotídeo\n"
    "3 - Sequencia reverse (DNA Complementar)\n4 - Transcrição(mRNA)\n5 - A tradução literal da sequência:" 
    "\n6 - As proteínas possíveis existentes\n7 - Verificar as cadeiras de nucleotídeos que estão presentes\n"
    "8 - Fazer pareamento de sequências\n 0 para sair\n")
