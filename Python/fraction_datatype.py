class Fraction():
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        print(f"\nnew fraction: {self.numerator}/{self.denominator}")
    
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        print(f"Sum of 2 fraction: {new_numerator}/{new_denominator}")
    
    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        print(f"Product of 2 fraction: {new_numerator}/{new_denominator}")
        
    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        print(f"Difference of 2 fraction: {new_numerator}/{new_denominator}")
        
    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        print(f"Division of 2 fraction: {new_numerator}/{new_denominator}")
        

def main():
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)
    f3 = f1 + f2
    f4 = f1 * f2
    f5 = f1 - f2
    f6 = f1 / f2
    
        
    
if __name__ == "__main__":
    main()   