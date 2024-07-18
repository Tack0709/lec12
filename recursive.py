# @fn factorial(n)
#  @brief nからの階乗を計算する
#  @param   n (int): 1つ目の引数
#  @return   int: n*factorial(n-1), n==0, n==1のとき1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# @fn fibonacci(n)
#  @brief nまでのフィボナッチ計算をする
#  @param   n (int): 1つ目の引数
#  @return   int: fibonacci(n-1)+fibonacci(n-2), n==0のとき0, n==1のとき1
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
