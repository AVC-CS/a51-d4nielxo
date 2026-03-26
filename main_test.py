import pytest
import re

def regex_test(expected, content):
    pos = 0
    for token in expected:
        res = re.search(token, content[pos:])
        if res is None:
            assert False, f'Expect: {token}'
        pos += res.start() + 1

@pytest.mark.T1
def test_main_1():
    # n=3, 2^3 = 8.00000
    content = open('result1.txt').read()
    print(content)
    regex_test([r'8\.0+'], content)

@pytest.mark.T2
def test_main_2():
    # n=10, 2^10 = 1024.00000
    content = open('result2.txt').read()
    print(content)
    regex_test([r'1024\.0+'], content)

@pytest.mark.T3
def test_main_3():
    # n=-5, 2^-5 = 0.03125
    content = open('result3.txt').read()
    print(content)
    regex_test([r'0\.03125'], content)

@pytest.mark.T4
def test_main_4():
    # n=-2, 2^-2 = 0.25000
    content = open('result4.txt').read()
    print(content)
    regex_test([r'0\.25'], content)
