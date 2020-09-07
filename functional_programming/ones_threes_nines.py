'''
Given an integer between 0 and 26, make a variable (self.answer). That variable would be assigned to a string in this format:
'''


class ones_threes_nines:
    def __init__(self, num):
        self.answer = "nines:{}, threes:{}, ones:{}".format(num//9, (num%9)//3, ((num%9)%3))


'''
You need to find out how many ones, threes, and nines it would at least take for
the number of each to add up to the given integer when multiplied by one, three or nine (depends).

Examples
'''

a = ones_threes_nines(22)
print(a.answer)
# ➞ "nines:1, threes:0, ones:1"

#ones_threes_nines(15) ➞ "nines:1, threes:2, ones:0"

#ones_threes_nines(22) ➞ "nines:2, threes:1, ones:1"
