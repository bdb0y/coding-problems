import re

# url: https://leetcode.com/problems/regular-expression-matching/

def isMatch(s: str, p: str) -> bool:
        if '**' in p:
            i = p.index('*')
            p = p.replace('*', '')
            p = p[:i] + '*' + p[i:]
        if re.search('^{0}$'.format(p), s):
            return True
        return False
    
    
s, p = input().split()

print(str(isMatch(s, p)).lower())