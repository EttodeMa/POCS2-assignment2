with open("C:/Users/ettod/Downloads/rosalind_tree.txt") as x:
    i = x.readlines()

tot_edg = int(i[0])
edg = 0

for f in i:
    edg += 1

min_edg = tot_edg - edg
print(min_edg)