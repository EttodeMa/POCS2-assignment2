import sys
from Bio import Phylo
import io

f = open("C:/Users/ettod/Downloads/rosalind_nkew.txt", "r")
pairs = [i.split("\n") for i in f.read().strip().split("\n\n")]


for i, line in pairs:
    x,y = line.split()
    tree = Phylo.read(io.StringIO(i), "newick")
    clades = tree.find_clades()
    for clade in clades:
        clade.branch_length = 1
    sys.stdout.write("%s" % tree.distance(x,y) + " ")
sys.stdout.write("\n")
