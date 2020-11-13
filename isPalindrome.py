class isPalindrome:
    def isPalindrome(self, x: int) -> bool:

        str_x = str(x)
        str_x_pal = str_x[::-1]

        if str_x == str_x_pal:
            return True
        else:
            return False
