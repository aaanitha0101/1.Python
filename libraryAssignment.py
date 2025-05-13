class libraryImport():
    def Subfields():
        list=['ML','NN','CV','Robotics','SP','NLP']
        print("Sub fields in AI are:")
        for temp in list:
            print(temp)
    def OddEven():
        num=int(input("Enter the number"))
        if (num%2==0):
            print(num," is even")
            msg="Even"
        else:
            print(num,"is odd")
            msg="Odd"
        return msg
    def Elegible():
        gen=input("Your Gender:")
        age=int(input("Your age:"))
        if (gen=="Male" and age>21):
            print("U r a eligible male")
        elif(gen=="Female" and age>18):
            print("U r a eligible female")
        else:
            print('u r not an eligible to be married')
    def percentage():
        sub1=int(input("Subject1="))
        sub2=int(input("Subject2="))
        sub3=int(input("Subject3="))
        sub4=int(input("Subject4="))
        sub5=int(input("Subject5="))
        tot=sub1+sub2+sub3+sub4+sub5
        print("Total:",tot)
        percent=(tot/500)*100
        print("Percentage:",percent)
    def triangle():
        h=int(input("Eneter the height:"))
        b=int(input("ENter the base:"))
        print("Area formula: (Height*Breadth)/2")
        area=int(1/2*(b*h))
        print("Area of triagnle",area)
        s1=int(input("Enter len of the side1:"))
        s2=int(input("Enter len of the side2:"))
        s3=int(input("Enter len of the side3:"))
        print("perimeter formula: side1+side2+side3")
        per=s1+s2+s3
        print("Perimeter of Triangle",per)