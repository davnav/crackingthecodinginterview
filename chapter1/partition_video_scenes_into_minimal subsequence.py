# You are working on developing a movie with Amazon Video that consists of a series of shots: short pieces of video from a particular camera angle. You want to devise an application to easily group identical shots in a video into scenes (a sequence of shots). Shots are identical when they are labeled with the same letter, and everything in between identical shots is considered part of same scene. There is already an algorithm that breaks the video up into shots and labels them.
# Write a function which will partition a sequence of shot labels into minimal subsequences so that a shot label only appears in a single subsequence. The output should be the length of each subsequence.
# Input The input to the function/method consists of an argument - inputList, a list of characters representing the sequence of shots.
# Output Return a list of integers representing the length of each scene, in the order in which it appears in the given sequence of shots.

# Examples Example 1: Input inputList = [a, b, c]
# Output [1, 1, 1]
# Explanation: Because there are no recurring shots, all shots can be in the minimal length 1 subsequence.
# Example 2: Input inputList = [a, b, c, a]
# Output [4]

# Explanation: Because a appears more than once, everything between the first and last appearance of a must be in the same list.

# Example 3: Input: inputList = [a, b, a, b, c, b, a, c, a, d, e, f, e,
# g, d, e, h, i, j, h, k, l, i, j]

# Output: [9, 7, 8]

# Testcase 1: Input: [a, b, c, d, a, e, f, g, h, i, j, e]
# Expected Return Value: 5 7

# Testcase 2: Input: [z, z, c, b, z, c, h, f, i, h, i]
# Expected Return Value: 6 5

def split_sequence_shots(inputList):
    l = len(inputList)
    i=0
    
    count_table = {}
    splitindex={}
    for outer_item in inputList:
        # item = inputList[i]
        
        part_list = [0]*2
        i += 1
        # part_list
        # print(count_table.get(outer_item))
        if count_table.get(outer_item) ==None:
            part_list[0] =i
            count_table[outer_item] =part_list
        # print(i)
        for  j in range(i,l-1):
            if outer_item == inputList[j]:
                
                if count_table.get(outer_item) != None :
                    part_list[1] = j
                    count_table[outer_item] = part_list
                else:
                    part_list[0] =j 
                    # print(i) 
                    count_table[outer_item] = part_list
                    
        
    print(count_table) 
        
                   
inputList = ['a', 'b', 'a', 'b', 'c', 'b', 'a', 'c', 'a', 'd', 'e', 'f', 'e',
 'g', 'd', 'e', 'h', 'i', 'j', 'h', 'k', 'l', 'i', 'j']
split_sequence_shots(inputList)