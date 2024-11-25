def subtract_matrix(lst1, lst2):
    sub_matrix  = []
    for i in range(len(lst1)): # 0 1 2
        rows = []
        for j in range(len(lst1[0])):  # 0 1 2
            rows.append(float(lst1[i][j])-float(lst2[i][j])) #()
        sub_matrix.append(rows)
    return sub_matrix




print(subtract_matrix([
  [1, 2, 2],
  [4, 5, 6],
  [7, 8, 9]
], [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]))

print(subtract_matrix([["2",0,0],[0,0,0],[0,0,0]],[["3",0,0],[0,0,0],[0,0,0.678]]))