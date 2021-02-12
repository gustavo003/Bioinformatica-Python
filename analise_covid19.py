import fasta_read as fr
from infos import infos
arq = "coronavirus.fna"
dict = fr.read_fasta(arq)

x = [k for k in dict.values()]
y = input("Digite qualquer tecla para analisar as sequências: \n\n")
if(y):
    for i in range(len(x)):
        print("Para a sequência %d :" %(i+1))
        infos(x[i])
