# we will see if this works 
# Global constants that can be changed for preferance 
match = 1
mismatch = -1
gap = -1
gap_penalty = -1

# main function that will take 2 sequences as strings and will print
#     a list of the base pairs (seq1, seq2) that will represent where they
#     match
# Str Str -> listof Str
# Requires:
#    str1 and str2 must be made up of 'A', 'B', 'C', 'D'

seq_1 = 'AGGTCACCT'
seq_2 = 'GGCACGT'

# outcome:
#   'AGGTCACCT'
#   '-GG-CACGT'

# EXAMPLE OF 2D ARRAY:
#
#     A  G  G  T  C  A  C  C  T
#   0-1 -2 -3 -4 -5 -6 -7 -8 -9
# G-1 
# G-2
# C-3
# A-4
# C-5
# G-6
# T-7

# horizontal move = gap in seq 2
# vertical move = gap in seq 1

# produces a list of letters (list = one seq)
def seq_list(seq):
    lst_seq = []
    for i in range(len(seq)):
        lst_seq = lst_seq + [seq[i]]
    return lst_seq

# list of numbers representing the base cases x and y with gap penalty)
def base_list(length):
    end = length + 1
    num_lst = []
    for i in range(end):
        num_lst = num_lst + [i * -1]
    return num_lst
        
# main function 
def seq_align(seq1, seq2):
    # length of each sequence
    len_1 = len(seq1)
    len_2 = len(seq2)
    #list representing base grid with gap penalty
    top_x = base_list(len_1)
    left_y = base_list(len_2)
    # list representing bases in each sequence
    lst_seq1 = seq_list(seq1)
    lst_seq2 = seq_list(seq2)
    
    # ///////////////////////////////////////////////
    # new try for printing the filled matirx 
    # fill matrix with all 0's
        # each element will be list of len(seq2)+1
    matrix = []
    for i in range(len_2 + 1):
        if i == 0:
            matrix = matrix + [top_x]
        else:
            temp_lst = [left_y[i]]
            for j in range(len_1):
                if j != 0:
                    temp_lst = temp_lst + [0]
            matrix = matrix + [temp_lst]
    # //////////////////////////////////////////////
    for i in range(len_2):
        for j in range(len_1):
            if (i != 0 and j != 0):
                # for diagnol
                if lst_seq1[j-1] == lst_seq2[i-1]:
                    diagnol = (matrix[i-1][j-1] + match) # match score
                else:
                    diagnol = (matrix[i-1][j-1] - mismatch)
                up = (matrix[i-1][j] - gap)
                left = (matrix[i][j-1] - gap)
                
                element = max(diagnol, up, left)
                matrix[i][j] = element
                
                #print(matrix)
    # ///////////////////////////////////////////////
    for i in range(len(matrix)):
            print(matrix[i])    


# END OF FUNCTION
seq_align(seq_1, seq_2)
