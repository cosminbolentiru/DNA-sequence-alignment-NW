# Global constants that can be changed for preferance
match = 1
mismatch = -1
gap = -1

#    str1 and str2 must be made up of 'A', 'B', 'C', 'D'

seq_1 = 'AGGTCACCT'
seq_2 = 'GGCACGT'

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


# diag function
def diagnaol_val(element, pos_1, pos_2, seq_1, seq_2):
    # if there is a match
    if seq_1[pos_1] == seq_2[pos_2]:
        new_d = (element + match)
        return new_d
    # if they dont match
    else:
        new_d = (element + mismatch)
        return new_d

# main function
def seq_align(seq1, seq2):
    len_1 = len(seq1)
    len_2 = len(seq2)
    top_x = base_list(len_1)
    left_y = base_list(len_2)
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
    pos_1 = 0
    pos_2 = 0
    x = 1
    y = 1
    while x < len_1:
        while y <=len_2:
            element = matrix[y-1][x-1]
            d_val = diagnaol_val(element, pos_1, pos_2, seq_1, seq_2)
            up = (matrix[(y-1)][x] + gap)
            left = (matrix[y][(x-1)] + gap)
            #choose best value
            replacement = max(d_val, up, left)
            matrix[y][x] = replacement
            y += 1
            pos_2 += 1
        y = 1
        x += 1
        pos_2 = 0
        pos_1 += 1

    # prints 2-D grid
    for i in range(len(matrix)):
            print(matrix[i])


# END OF FUNCTION
seq_align(seq_1, seq_2)
