#    Infix expression	     Prefix expression	    Postfix expression
# 1.  A + B * C + D           + + A * B C D	         A B C * + D +
# 2. (A + B) * (C + D)        * + A B + C D	         A B + C D + *
# 3.  A * B + C * D           + * A B * C D	         A B * C D * +
# 4.  A + B + C + D           + + + A B C D	         A B + C + D +
