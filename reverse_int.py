class reverse_int:
    def reverse(self, x: int) -> int:

        pos_limit = 0x7FFFFFFF
        neg_limit = -0x80000000

        str_x = str(x)

        if x < 0:
            str_x = "-" + str_x[::-1][:-1]
            x = int(str_x)
        else:
            str_x = str_x[::-1]
            x = int(str_x)

        if x < 0:  ##checking for overflow when negative
            val = x & neg_limit
            if (val == neg_limit):
                return x
            else:
                return 0

        elif x == 0:  ## returning 0 if x is 0
            return x

        else:  ##checking for overflow when positive
            val = x & pos_limit
            if (val == x):
                return x
            else:
                return 0

