"""
Output:

Enter an Infix Equation = a + b ^c
 Symbol  |  Stack  | Postfix
----------------------------
   c     |         | c
   ^     | ^       | c
   b     | ^       | cb
   +     | +       | cb^
   a     | +       | cb^a
         |         | cb^a+

         a+b^c (Infix) ->  +a^bc (Prefix)
"""
"""
中序转前序：
从字符串（从右至左）中取出一个字符
或者先将字符串反转，就从左至右，对结果再反转即最终结果
1，如果是操作数，则直接输出
2，如果是“）”直接压入栈中
3，如果是运算符但不是‘（’，‘）’，则不断进行以下处理
（1）如果栈为空，则运算符入栈
（2）如果栈顶为‘）’则此运算符进栈
（3）如果此运算符与栈顶的优先级相同或者更高，则入栈
（4）如果前三个都不满足，则运算符连续出栈，直到满足上面三个之一，然后该运算符进栈
（5）如果为‘（’，运算符连续出栈，直到遇到‘）’，将‘）’出栈丢之
"""

def infix_2_postfix(Infix):
    Stack = []
    Postfix = []
    priority = {
        "^": 3,
        "*": 2,
        "/": 2,
        "%": 2,
        "+": 1,
        "-": 1,
    }  # Priority of each operator
    print_width = len(Infix) if (len(Infix) > 7) else 7

    # Print table header for output
    print(
        "Symbol".center(8),
        "Stack".center(print_width),
        "Postfix".center(print_width),
        sep=" | ",
    )
    print("-" * (print_width * 3 + 7))

    for x in Infix:
        if x.isalpha() or x.isdigit():
            Postfix.append(x)  # if x is Alphabet / Digit, add it to Postfix
        elif x == "(":
            Stack.append(x)  # if x is "(" push to Stack
        elif x == ")":  # if x is ")" pop stack until "(" is encountered
            while Stack[-1] != "(":
                Postfix.append(Stack.pop())  # Pop stack & add the content to Postfix
            Stack.pop()
        else:
            if len(Stack) == 0:
                Stack.append(x)  # If stack is empty, push x to stack
            else:  # while priority of x is not > priority of element in the stack
                while len(Stack) > 0 and priority[x] <= priority[Stack[-1]]:
                    Postfix.append(Stack.pop())  # pop stack & add to Postfix
                Stack.append(x)  # push x to stack

        print(
            x.center(8),
            ("".join(Stack)).ljust(print_width),
            ("".join(Postfix)).ljust(print_width),
            sep=" | ",
        )  # Output in tabular format

    while len(Stack) > 0:  # while stack is not empty
        Postfix.append(Stack.pop())  # pop stack & add to Postfix
        print(
            " ".center(8),
            ("".join(Stack)).ljust(print_width),
            ("".join(Postfix)).ljust(print_width),
            sep=" | ",
        )  # Output in tabular format

    return "".join(Postfix)  # return Postfix as str


def infix_2_prefix(Infix):
    Infix = list(Infix[::-1])  # reverse the infix equation

    for i in range(len(Infix)):
        if Infix[i] == "(":
            Infix[i] = ")"  # change "(" to ")"
        elif Infix[i] == ")":
            Infix[i] = "("  # change ")" to "("

    return (infix_2_postfix("".join(Infix)))[
        ::-1
    ]  # call infix_2_postfix on Infix, return reverse of Postfix


if __name__ == "__main__":
    Infix = input("\nEnter an Infix Equation = ")  # Input an Infix equation
    Infix = "".join(Infix.split())  # Remove spaces from the input
    print("\n\t", Infix, "(Infix) -> ", infix_2_prefix(Infix), "(Prefix)")
