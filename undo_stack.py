undo_stack=[]
redo_stack=[]

def make_change():
     text=input("enter a string:")
     undo_stack.append(text)
     redo_stack.clear()

def undo():

    if undo_stack:
        x=undo_stack.pop()
    else:
        print("nothing to undo\n")
        return
    redo_stack.append(x)

def redo():
     if redo_stack:
          x=redo_stack.pop()
     else:
           print("nothing to redo\n:")
           return
     undo_stack.append(x)                   

def display():
     for i in undo_stack:
           print(i,end=" ")

while True:
     print("1.enter text")
     print("2.undo")      
     print("3.redo")
     print("4.current state")
     print("5.exit")

     choice=int(input("enter your choice:"))
     print()

     if choice==1:
        make_change()
        print()
        display()

     elif choice==2:  
        undo()
        print()
        display()

     elif choice==3:
        redo()
        print()
        display()

     elif choice==4:
         display()  

     else: 
       print("invalid input")