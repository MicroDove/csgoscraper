from Match import Match
from matchtable import matchtable


def main():
    match_table = matchtable()
    print(match_table)
    for i in match_table:
        print(match_table[i])


if __name__ == "__main__":
    main()
