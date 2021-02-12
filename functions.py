import re
import numpy as np


def valida(sequence):
    seqm = sequence.upper()
    total = seqm.count("A") +seqm.count("T") + seqm.count("C") + seqm.count("G")
    if (total==len(sequence)):
        return True
    else:
        print("A sequencia não é válida")
        return False



def frequencia(sequence):
    dict = {}
    for i in sequence.upper():
        if(i in dict): 
            dict[i] +=1
        else : dict[i]=1
        
    return dict

def porcentagem(sequence, dict):
    assert valida(sequence)
    porc = {}
    for i in dict.keys():
        porc[i] = str(round((dict[i]/len(sequence) * 100), 2)) + "%"
    return porc


def reverse(sequence):
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
    proteina = ""
    for i in range(inicio, len(sequencia)-2, 3):
        proteina = proteina +  tc[sequencia[i:i+3].upper()]
    return proteina

def all_proteins(sequence):
    list = []
    rever= reverse(sequence)
    list.append(traducao(sequence, 0))
    list.append(traducao(sequence, 1))
    list.append(traducao(sequence, 2))
    list.append(traducao(rever, 0))
    list.append(traducao(rever, 1))
    list.append(traducao(rever, 2))
    return list

def possible_proteins(sequence):
    proteinas = []
    atuais = []
    for i in sequence:
        if(i=="_"):
            if (atuais):
                for k in atuais: proteinas.append(k)
                atuais = []
        else:
            if(i=="M"):
                atuais.append("")
            for x in range(len(atuais)):
                atuais[x] +=i
    return proteinas

def all_possible_proteinas(sequence):
    proteinas = []

    lista = all_proteins(sequence)
    for i in lista:
        x = possible_proteins(i)
        if(x): proteinas.append(x)
    return proteinas 

    
def find_all_occurrences_re (sequence, pat):
    assert(valida(pat))
    occur = re.finditer(pat, sequence)
    
    res = []
    for x in occur:
        res.append(x.span()[0])
  
    return res

def needleman_wunsch(seq1, seq2):
    mn = np.zeros((len(seq1)+1, len(seq2)+1))
    check = np.zeros((len(seq1), len(seq2)))
    backtrack = np.zeros((len(seq1)+1, len(seq2)+1))
    match  = 1
    not_match = -1
    gap = -2
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if(seq1[i]==seq2[j]):
                check[i][j]=match
            else:
                check[i][j]=not_match
    for i in range(len(seq1)+1):
        mn[i][0] = i*gap
        backtrack[i][0] = 2
    for i in range(len(seq2)+1):
        mn[0][i] = i*gap
        backtrack[0][i] = 3
    for i in range(1, len(seq1)+1):
        for j in range(1, len(seq2)+1):    
            mn[i][j] =  max(mn[i-1][j-1]+check[i-1][j-1], mn[i-1][j]+gap, mn[i][j-1]+ gap)
            backtrack[i][j] = (max2(mn[i-1][j-1]+check[i-1][j-1], mn[i-1][j]+gap, mn[i][j-1]+ gap))

    print(Backtrack(seq1, seq2, backtrack))
def max2(x, y, z):
    if(x>y):
        if(x>z): return 1
        else: return 3
    else:
        if(y>z): return 2
        else: return 3

def Backtrack(seq1, seq2, back):
    res = ["", ""]
    i = len(seq1)
    j = len(seq2)
    while(i>0 or j >0):
        if(back[i][j]==1):
            res[0] = seq1[i-1] + res[0]
            res[1]  = seq2[j-1] +  res[1]
            i-=1
            j-=1
        elif(back[i][j]==3):
            res[0] = "-" + res[0]
            res[1] = seq2[j-1]+res[1]
            j-=1
        else:
            res[0] = seq1[i-1] + res[0]
            res[1] = "-" + res[1]
            i-=1
    
    return res

