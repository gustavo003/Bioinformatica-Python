import fasta_read as fr
from infos import infos
arq = input("Digite o caminho do arquivo FASTA: ")
dict = fr.read_fasta(arq)

x = [k for k in dict.values()]
for i in range(len(x)):
    print("Para a sequência %d :" %(i+1))
    infos(x[i])
