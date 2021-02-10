
def valida(sequence):
    seqm = sequence.upper()
    total = seqm.count("A") +seqm.count("T") + seqm.count("C") + seqm.count("G")
    if (total==len(sequence)):
        return True
    else:
        print("A sequencia não é válida")
        return False



def frequencia(sequence):
    assert valida(sequence)
    dict = {}
    for i in sequence.upper():
        if(i in dict): dict[i] +=1
        else : dict[i]=1
    return dict


def reverse(sequence):
    assert valida(sequence)
    comp = ""
    for i in sequence:
        if (i=="A"):
            comp = "T" + comp
        elif(i=="T"):
            comp = "A" + comp
        elif(i=="G"):
            comp = "C" + comp
        elif(i=="C"):
            comp = "G" + comp
    return comp


def mRNA(sequencia):
    comp = reverse(sequencia)
    rna = comp.replace("T", "U")
    return rna




tc = {"GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
"TGT":"C", "TGC":"C",
"GAT":"D", "GAC":"D",
"GAA":"E", "GAG":"E",
"TTT":"F", "TTC":"F",
"GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G",
"CAT":"H", "CAC":"H",
"ATA":"I", "ATT":"I", "ATC":"I",
"AAA":"K", "AAG":"K",
"TTA":"L", "TTG":"L", "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
"ATG":"M", "AAT":"N", "AAC":"N",
"CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
"CAA":"Q", "CAG":"Q",
"CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R",
"TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S", "AGT":"S", "AGC":"S",
"ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
"GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
"TGG":"W",
"TAT":"Y", "TAC":"Y",
"TAA":"_", "TAG":"_", "TGA":"_"}

def aminoacido(amino):
    if(amino in tc): return tc[amino]
    else : return None


def traducao(sequencia, inicio):
    assert valida(sequencia)
    proteina = ""
    for i in range(inicio, len(sequencia)-2, 3):
        proteina = proteina + "-" + tc[sequencia[i:i+3].upper()]
    return proteina 

