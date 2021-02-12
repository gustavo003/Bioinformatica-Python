def read_fasta(arquivo):
    with open(arquivo) as arq:
        conteudo = arq.read()
        conteudo = conteudo.split("\n")
        indice = 0
        info = []
        info.append(conteudo[0])
        x=1
        genes = []
        dict = {}
        for i in conteudo[1:len(conteudo)]:
            indice +=1
            if(">" in i):
                info.append(i)
                genes.append(conteudo[x:indice])
                x=indice+1
            elif(indice==len(conteudo)-1):
                genes.append(conteudo[x:len(conteudo)])
        for i in range(len(info)):
            dict[info[i]] = "".join(genes[i])
        for i in dict.keys():
            x = i.split(" ")
            print("\n\nInformações: ")
            print(x[0])
            print(" ".join(x[1:]))
        for k in dict.values():
            print("\n\nSequência do gene: \n", k)
    return dict

