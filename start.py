import pdb;
import math;
import random;
import string;
import time;
import calendar;
import re;
import os;

#startup
print("EXERCISE FOR: ", "startup");
str = 'Hello World!';

print(str);
print(str[0]);
print(str[2:5]);
print(str[2:]);
print(str * 2);
print(str + "TEST");
print();

# list
print("EXERCISE FOR: ", "list");
lt = [ 'abcd', 123, 2.23, 'john', 70.2 ];
tinylt = [ 123, 'john' ];

print(lt);
print(lt[0]);
print(lt[2:5]);
print(lt[2:]);
print(lt * 2);
print(lt + tinylt);
print();

# tuple
print("EXERCISE FOR: ", "tuple");
tuple = ( 'abcd', 123, 2.23, 'john', 70.2 );
tinytuple = ( 123, 'john' );

print(tuple);
print(tuple[0]);
print(tuple[2:5]);
print(tuple[2:]);
print(tuple * 2);
print(tuple + tinytuple);

lt[2] = 1000;
print(lt);
print();

#  tuple[2] = 1000; # type error

# dict
print("EXERCISE FOR: ", "dict");
dict = {};

dict['one'] = "This is one";
dict[2] = "This is two";

tinydict = {'name': "john", 'code': 6734, 'dept': "sales"};

print(dict);
print(dict['one']);
print(dict[2]);
print(tinydict);
print(tinydict.keys());
print(tinydict.values());
print();

# type convertion
print("EXERCISE FOR: ", "type convertion");
print('1');
print(int('11000000', 2));
print(complex(1, 1));
print(ord('A'));
print();

# if condition
print("EXERCISE FOR: ", "'if' condition");
a1, a2, a3, a4 = False, 0, "", None;
if (a1):
    print("a1: ", a1, " is true");
else:
    print("a1: ", a1, " is false");
if (a2):
    print("a2: ", a2, " is true");
else:
    print("a2: ", a2, " is false");
if (a3):
    print("a3: ", a3, " is true");
else:
    print("a3: ", a3, " is false");
if (a4):
    print("a4: ", a4, " is true");
else:
    print("a4: ", a4, " is false");
print();

# bit calculation
print("EXERCISE FOR: ", "bit calculation");
c1, d1 = int("11001010", 2), int("00110101", 2);
print(c1, " & ", d1, " = ", c1 & d1);
print(c1, " | ", d1, " = ", c1 | d1);
print(c1, " ^ ", d1, " = ", c1 ^ d1);
c2, d2  = int("1100", 2), int("0110", 2);
print(c2, " & ", d2, " = ", c2 & d2);
print(c2, " | ", d2, " = ", c2 | d2);
print(c2, " ^ ", d2, " = ", c2 ^ d2);
print(c2, " << 2 :", c2 << 2);
print();

# "is" operator
print("EXERCISE FOR: ", "'is' operator");
e1, e2, f1, f2 = 2, (1, 2), 2, (1, 2);
f3 = e2;
print(e1, " in ", e2, " -> ", e1 in e2);
print(id(e1), id(f1));
print(e1 is f1);
print("[e2: ", e2, "] is [f2: ", f2, "] -> ", e2 is f2);
print("[e2: ", e2, "] = [f2: ", f2, "] -> ", e2 == f2);
print("[e2: ", e2, "] is [f3: ", f3, "] -> ", e2 is f3);
print();

# while...else... loop
print("EXERCISE FOR: ", "while...else... loop");
count = 0;
while (count < 10):
    print("count: ", count);
    count += 4;
else:
    print("loop ended");
print();

# for...in... loop
print("EXERCISE FOR: ", "for...in... loop");
arrForLoop = [ "apple", "orange", "banana" ];
for fruit in arrForLoop:
    print(fruit);
    for i in range(len(fruit)):
        print(fruit[i]);
print();

# for loop with index
# break
# for...else...
print("EXERCISE FOR: ", "for...else... loop");
for i in range(2, 20):
    for j in range(2, i):
        if (i % j == 0):
            print(i, " equals ", j, " * ", i // j);
            break;
    else:
        print(i, " is a prime number");
else:
    print("over");
print();

# number / math
def cmp(i, j):
    return (i > j) - (i < j);
com1, com2 = complex(1, 1), complex(1, -1);
print(com1 * com2);      # 2 + 0j;
print(cmp(0, 1));        # -1
print(abs(-10));         # 10
print(math.log(math.e)); # 1.0
print(math.log10(10));   # 1.0
print(math.sin(math.pi));# 1.22e-16 (not equal to 0)

random.seed(47);
print(random.choice(range(10)));   # 5
print(random.randrange(2, 10, 2)); # 2
arrToShuffle = [ 1, 2, 3, 4, 5, 6, 7 ];
random.shuffle(arrToShuffle);
print(arrToShuffle);               # [1, 6, 2, 3, 7, 5, 4]
print(random.random());            # 0.39242....
print("\a");
print();

# string
print(r"\n");                      # \n
print("%+07.2f plus %+07.3f is %+02d" % (4.4, 5.6, 10)); # +004.40 plus +05.600 is +10
print(string.capwords("abcde,fg,hijk", ","));   # Abcde,Fg,Hijk
print("abcde,fg,hijk".capitalize());            # Abcde,fg,hijk
print('||'.join("abc"));                         # a||b||c
print(string.ascii_lowercase, string.ascii_uppercase, string.ascii_letters);
print("abcdeabc".center(10));
print("abcdeabc".count("a", 2));                   # 1
print("abcdefg".encode());                         # b'abcdefg'
print("abcdefg".index("a"));                       # 0
# print("abcdefg".index("h"));                     # ValueError
print("abcdefg".find("a"));                        # 0
print("abcdefg".find("h"));                        # -1
print(min("abcdefg"), max("abcdefg"));             # a, g
print("abecdefg".partition('e'));                  # (ab,e,cdefg)
print("abecdefg".rpartition('e'));                 # (abecd,e,fg)
print("abcdefg".split('e'));                       # [abcd,fg]
print("world of warcraft".title());                # World Of Warcraft
print();

# list
l = [ 'a', 'b', 'c', 'd', 'z', 'y', 'x' ];
print(max(l));
l.append('w');
print(l);
l.extend(['v', 'u']);
print(l);
print("index of 'd' in l: %d" % l.index('d'));
#  print("index of 'h' in l: %d" % l.index('h'));
def find(l, ele):
    try:
        index = l.index(ele);
    except ValueError:
        print("Oops");
        index = -1;
    return index;
print("index of 'h' in l: %d" % find(l, 'h'));
print(l.pop());
print(l);
print(l.pop(2));
print(l);

# tuple
t = ('A', 'B', 'C', 'D', 'Z', 'Y', 'X');
t2 = ('1', '2', '3');
t3 = t + t2;
print(t3);
print(min(t3));

# dict
dct1 = { 'abc': 456 };
dct2 = { 'abc': 123, 98.6: 37 };
print('dct1: ', dct1);
print("dct2['abc']:", dct2['abc']);
print("dct2[98.6]:", dct2[98.6]);
# print("dct2['a']: ", dct2['a']);                 # KeyError
print(dct2.update({'abc': 234}));
print("dct2:", dct2);
print(dct2.update({'efg': 789}));
print("dct2:", dct2);
print(dict.fromkeys('abc', 10));
print(dct2);
print();

# time
print(time.time());
print(time.clock());
timeTuple = time.localtime(time.time());
print(time.asctime(timeTuple));
print("year %d month %d day %d" % (timeTuple.tm_year, timeTuple.tm_mon, timeTuple.tm_mday));
print(calendar.month(2008, 1));
testtime = time.strptime('20180430', '%Y%m%d');
print(testtime);
print(testtime.tm_year);

# function
num1 = 1;
num2 = 2;
def testNumFunc(num):
    num = 10;
    return num;
print(num1);
print(testNumFunc(num1));
print(num1);
def testNumFunc2(num):
    num += 1;
    return;
print(num2);
print(testNumFunc2(num2));
print(num2);
arr1 = [1, 2, 3];
arr2 = [1, 2, 3];
def testArrFunc1(arr):
    arr = [2, 3, 4];
    return arr;
print(arr1);
print(testArrFunc1(arr1));
print(arr1);
def testArrFunc2(arr):
    arr.append([4, 5]);
    return arr;
print(arr2);
print(testArrFunc2(arr2));
print(arr2);
def swap(n1):
    print("id(n1): ", id(n1));
    n1 = 10;
    return;
print(id(num1));
num1 = 20;
print(id(num1));
swap(num1);
print(id(num1), num1);

# regex
p = re.compile('aa(bb)cc');
teststr = 'aabbcc';
m = p.match(teststr);
print(m.group(1));
print(re.sub(r'(aa)(bb)(cc)', r"\1dd", teststr));

# file io
foo = open("foo.txt", "w");
print("Name of the file:", foo.name);
foo.write("123\n");
foo.write("abc\n");
print("Openning mode: ", foo.mode);
foo.close();
print("Closed or not: ", foo.closed);
foo = open("foo.txt", "r+");
lines = foo.readlines();
for line in lines:
    if line.startswith("123"):
        foo.write("1234\n");
    else:
        foo.write(line);
else:
    foo.write("end\n");
foo.close();

print(os.path.splitext('aaa.txt')[1]);

