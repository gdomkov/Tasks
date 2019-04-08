1.
d = input()
str(d)
print(d)

2.


def remove_char(s):
    return s[1:len(s) - 1]


3.
text = ''.join(reversed(input()))
print(text)

4.
a = input()
print(a.replace(' ', ''))

5.
f = '123'
b = int(f)

6.


def smash(words):
    out = ""
    for word in words:
        out += word + " "
    return out.strip()


7.


def reverseWords(string):
    return ' '.join(string.split()[::-1])


8.


def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)


9.


def reverse(st):
    return " ".join(reversed(st.split())).strip()


10.


def string_to_array(string):
    return string.split(" ")


11.


def format_money(amount):
    return '$%0.2f' % amount


12.


def shortcut(s):
    return s.translate(None, 'aeiou')


13.


def repeat_it(string, n):
    if type(string) is not str:
        return 'Not a string'
    return string * n


14.


def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()


15.


def check(list, x):
    while True:
        if x in list:
            return True
        else:
            return False
    pass


16.


def lowercase_count(strng):
    return sum(a.islower() for a in strng)


17.


def name_shuffler(str_):
    return ' '.join(str_.split(' ')[::-1])


18.


def contamination(text, char):
    return char * len(text)


19.


def toJadenCase(string):
    return " ".join(w.capitalize() for w in string.split())


20.


def high_and_low(numbers):  # z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn), min(nn))


21.


def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True


22.


def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))


23.


def solution(string, ending):
    return string.endswith(ending)


24.


def capitals(word):
    return [i for (i, c) in enumerate(word) if c.isupper()]


25.


def digitize(n):
    return [int(d) for d in str(n)]