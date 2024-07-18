import argparse
from recursive import fibonacci
from recursive import factorial


def main():
    parser = argparse.ArgumentParser(
        description='factorial or fibonacci one number')
    parser.add_argument('arg1', type=int,
                        help='first argment')

    args = parser.parse_args()
    a = args.arg1

    print(a)

    print(factorial(a))
    print(fibonacci(a))


if __name__ == '__main__':
    main()
