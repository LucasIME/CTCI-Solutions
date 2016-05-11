def toBool(expression):
    if expression == '1':
        return True
    else:
        return False

def countEval( expression, result, memo):
    if len(expression) == 0:
        return 0
    if len(expression) == 1:
        if toBool(expression) == result:
            return 1
        else:
            return 0
    if (expression, result) in memo:
        return memo[(expression,result)]

    ways = 0
    for i in range(1, len(expression), 2):
        c = expression[i]
        left = expression[:i]
        right = expression[i+1:]

        #evaluating each side for each result
        leftTrue = countEval(left, True, memo)
        leftFalse = countEval(left, False, memo)
        rightFalse = countEval(right, False, memo)
        rightTrue = countEval(right, True, memo)
        total = (leftTrue + leftFalse) * (rightTrue + rightFalse)
        totalTrue = 0

        if c == '^':
            totalTrue = leftTrue * rightFalse + leftFalse*rightTrue
        elif c == '&':
            totalTrue = leftTrue * rightTrue
        elif c == '|':
            totalTrue = leftTrue*rightTrue + leftFalse*rightTrue + leftTrue*rightFalse

        subways = 0
        if result ==  True:
            subways = totalTrue
        else:
            subways = total - totalTrue

        ways += subways
    memo[(expression, result)] = ways
    return ways


def main():
    expression1 = "1^0|0|1"
    result1 = False
    expression2 = "0&0&0&1^1|0"
    result2  = True
    print countEval(expression1, result1, {})
    print countEval(expression2, result2, {})

if __name__ == '__main__':
    main()
