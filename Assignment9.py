# Info:-
# Name   : Maaz 
# Dept   : CO-B
# Batch  : 4
# Sub    : Python Assignment-9
# Topic  :-
# 1) Create a module consisting of class holding various data members and member functions.
# (class can be on various file operations or mathematical operations or string operations)
# 2) Import the above module created and try to implement their member functions.
# 3) Also in the same file, create a user defined exception and implement it.
# Note:
# file operations should include all the file modes
# mathematical operations should include the functions from math module
# string operations should include string functions such as split()..etc
# Date   : 03-07-2023

# Program:-
import Mathematics as m;

class LessThan0Error(Exception):
    def __init__(self, args):
        super().__init__(args)
    pass;

print("Note: Enter numbers greater than 0.");
n1=int(input("Enter 1st no.: "));
n2=int(input("Enter 2nd no.: "));
print();

try:
    if n1<0 or n2<0:
        raise LessThan0Error("Entered number is smaller than 0.")
    else:
        ma=m.Maths();
        print("Operations :-");
        ma.operations(n1,n2);
except LessThan0Error as mtte:
    print(f"{type(mtte).__name__} : {mtte.args[0]}");


# Output:-
# Note: Enter numbers greater than 0.
# Enter 1st no.: 3
# Enter 2nd no.: 2

# Operations :-
# Square root of 3                            : 1.7320508075688772
# Smallest integer greater than or equal to 3 : 3
# Largest integer less than or equal to 3     : 3
# 3 raised to the power of 2                  : 9.0
# Exponential value of 3 (e^3)                : 20.085536923187668
# natural logarithm (base e) of 3             : 1.0986122886681098
# Base 10 logarithm of 3                      : 0.47712125471966244
# Sine of 3 (in radians)                      : 0.1411200080598672
# Cosine of 3 (in radians)                    : -0.9899924966004454
# Tangent of 3 (in radians)                   : -0.1425465430742778
# Converts angle 3 from degrees to radians    : 0.05235987755982989
# Converts angle 3 from radians to degrees    : 171.88733853924697