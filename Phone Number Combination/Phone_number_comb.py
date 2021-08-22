def FindCombination(digits,prev,combinations,numbcomb):
    if digits == []:
        combinations.append(prev)
        return
    for letter in numbcomb[digits[0]]:
        FindCombination(digits[1:],prev + letter,combinations,numbcomb)
    return combinations

class Solution(object):
    def letterCombinations(self, digits):
        prev = ''
        combinations = []
        digits = list(digits)
        numbcomb = {'2': 'abc',
                    '3': 'def',
                    '4': 'ghi',
                    '5': 'jkl',
                    '6': 'mno',
                    '7': 'pqrs',
                    '8': 'tuv',
                    '9': 'wxyz'}
        return FindCombination(digits,prev,combinations,numbcomb)
