from Bio import SeqIO
from Bio.Seq import reverse_complement


def hamm_dist(seq1, seq2):
    return sum([1 if seq1[i] != seq2[i] else 0 for i in range(len(seq1))])


def inshalla(seq):
    corrected = []
    corr, erro = [], []

    for i in seq:
        if seq.count(i) + seq.count(reverse_complement(i)) >= 2:
            corr.append(i)
        else:
            erro.append(i)

    for x in erro:
        for v in corr:
            if hamm_dist(x, v) == 1:
                corrected.append((x, v))
                break
            if hamm_dist(x, reverse_complement(v)) == 1:
                corrected.append((x, reverse_complement(v)))
                break
    return corrected


seq = []
file = "C:/Users/ettod/Downloads/rosalind_corr.txt"
fasta = list(SeqIO.parse(file, "fasta"))
for ID in fasta:
    seq.append(str(ID.seq))
d = inshalla(seq)
for erro, corr in d:
    with (open("C:/Users/ettod/Downloads/rosalind_corr_answ.txt", "a") as p):
        p.write("{}->{}\n".format(erro, corr))
