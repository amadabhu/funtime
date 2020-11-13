class Solution:
    def removeVowels(self, S: str) -> str:
        vowels = list('aeiou')
        s_ls = list(S)
        seperator = ""
        new_ls = []
        for letter in s_ls:
            if letter not in vowels:
                new_ls.append(letter)
            else:
                continue
        S = seperator.join(new_ls)
        return S
