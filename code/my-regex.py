# %% 연산자 in
s = 'python kotrin'

# 연산자 in 사용 검색
print('py' in s)
print('kot' in s)
print('onkot' in s)

# %% 메소드 find()
s = 'python kotrin'

# 일반 문자열 메소드를 통한 검색
print(s.find('py'))
print(s.find('kot'))
print(s.find('onkot')) # 찾는 문자열이 없으면 -1

# %% 메소드 index()
s = 'python kotrin'
print(s.index('rin'))
print(s.index('java')) # 오류 발생

# %% 모듈 re
import re             # re.serarch() 사용
from re import search # serarch() 바로 사용

# %% function search
import re

m = re.search('thon', 'python kotlin')
print(type(m)) # re.Match 유형
print(m) # re.Match 객체 내용 

# %% method group() span() start() end()
from re import search

s = 'python kotrin'
m = search('thon', s)
print(m)
print(m.group()) # 실제 일치하는 문자열

# 일치하는 문자열의 위치 첨자
x, y = m.start(), m.end()
print(x, y, m.span())
print(s[x:y])

# %%
from re import search, findall

s = 'Copy file, move file1, rename file2 or remove file3'
p = 'file[12]?'
m = search(p, s)
print(m.group())
print(m.span(), m.start(), m.end())

fa = findall(p, s)
print(fa)
