from Bio import SeqIO
def overlap(str1, str2):
    return str1[-3:] == str2[:3]


file = "C:/Users/ettod/Downloads/rosalind_grph.txt"
bio_seq = list(SeqIO.parse(file, "fasta"))

sequences_by_id = {record.id: str(record.seq) for record in bio_seq}

for id1 in sequences_by_id:
    for id2 in sequences_by_id:
        if id1 != id2 and overlap(sequences_by_id[id1],
                                  sequences_by_id[id2]):
            print(id1, id2)
