import sys
import sqlparse

def main():
    query_lst = []
    for arg in sys.argv:
        q = sqlparse.format(arg, reindent=True, keyword_case='upper')
        query_lst.add(q)
        print(type(q))
        print(q)
        


if __name__=='__main__':
    main()