# Polymoprhism: Method Overloading (compile time polymorphism or static polymorphism)
# Method Overloading: Same method name with different number of arguments
# technically Method overloading is not supported in Python
# But we can achieve this by using default arguments



class Geometry:
    def area(self):
        print("Area method in Geometry class")
        
    def area(self, a , b=0):
        if b == 0:
            print("Area of square:", a*a)
        else:
            print("Area of rectangle:", a*b)

        
def main():
    g = Geometry()
    g.area(5)
    g.area(10, 20)
    g.area(7)
    
if __name__ == "__main__":
    main()