class student:
    """
    student class helps to implementation
    of basic parameter of student.__int__ 
    function helps to pass the parameter 
    in class and self show the locality of object and printParameter 
    helps to print the passing parameter 
    """
    def __init__(self, name, age):# self shows class object
        print('init called')
        self.name = name
        self.age = age

    def printParameter(self):
        print('parameter are:')
        print("Name-", self.name)
        print("Age-", self.age)

if __name__ == '__main__':
    print(student.__doc__)#print the document string
    
    s1=student('sahil','23')#create object
    
    print("---------")
    s1.printParameter()#call class function 
    print(dir(student))
