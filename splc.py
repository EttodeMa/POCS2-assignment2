from Bio import SeqIO
from Bio import Seq

lns = []
for line in SeqIO.parse("C:/Users/ettod/Downloads/rosalind_splc.txt", 'fasta'):
    s = str(line.seq)
    lns.append(s)

DNA = lns[0]
exons = lns[1:]

for ex in exons:
    se = DNA.split(ex)
    DNA = ''.join(se)
DNA_str = ''.join(DNA)

protein = Seq.translate(DNA_str)
print(protein[:-1])
