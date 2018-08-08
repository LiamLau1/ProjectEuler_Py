s = list('ece:;==j');
for i in range(len(s)):
    s[i] = chr(ord(s[i]) - i);

s = ''.join(s)
print(s)
