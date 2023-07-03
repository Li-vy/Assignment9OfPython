import math as m;
class Maths:
    def __init__(self) -> None:
        pass

    def operations(self,n1,n2):
        print(f"Square root of {n1}                            : {m.sqrt(n1)}");
        print(f"Smallest integer greater than or equal to {n1} : {m.ceil(n1)}");
        print(f"Largest integer less than or equal to {n1}     : {m.floor(n1)}");
        print(f"{n1} raised to the power of {n2}                  : {m.pow(n1,n2)}");
        print(f"Exponential value of {n1} (e^{n1})                : {m.exp(n1)}");        
        print(f"natural logarithm (base e) of {n1}             : {m.log(n1)}");        
        print(f"Base 10 logarithm of {n1}                      : {m.log10(n1)}");     
        print(f"Sine of {n1} (in radians)                      : {m.sin(n1)}");   
        print(f"Cosine of {n1} (in radians)                    : {m.cos(n1)}");   
        print(f"Tangent of {n1} (in radians)                   : {m.tan(n1)}");   
        print(f"Converts angle {n1} from degrees to radians    : {m.radians(n1)}");   
        print(f"Converts angle {n1} from radians to degrees    : {m.degrees(n1)}");
        pass;

