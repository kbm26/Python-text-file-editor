# """
# make a new note 
# Read all notes
# Delete a note
# Delete all
# Edit a note
# """


def replace_line(): 
    line =input("""please enter which number line
you would like to overwrite: """)
    
    while line.isdigit() == False:
        line =input("""please enter which number line
you would like to overwrite: """)
    
    line = int(line)
    new_sentence = input("Type in new sentence: ")
    line = line - 1
    
    with open("text.txt","r") as n:
        rrr = n.readlines()
        
    with open("text.txt","w+") as n:
        for i, r in enumerate(rrr):
            if i not in [line]:
                n.write(r)
            else:
                n.write(f"{new_sentence}\n")
                
def append_line(): #passed personal test
    line = input("please enter which number line"
+"you would like to append to: ")
    
    while line.isdigit() == False:
        line = input("please enter which number line"
+"you would like to append to: ")
    
    line = int(line)
    line = line - 1
    
    with open("text.txt","r") as n:
        rrr = n.readlines()
        
    new_sentence = input("Type in new sentence: ")
    with open("text.txt","w") as n:
        for i, r in enumerate(rrr): 
            if i  not in  [line]:
                n.write(r)
            else:
                r = r.strip()
                n.write(r+f" {new_sentence}\n")

def maker(): #passed test
   new_note =input("please type what you would like to add to your note:\n")
   n = open("text.txt","a")
   n.write("\n"+new_note)
   n.close()
   
def readaline(): #passed test
    n = open("text.txt","r")
    line = input("Which line would you like to read: ")
    while line.isdigit() == False:
        line = input("Which line would you like to read: ")
    line = int(line)
    line = line -1
    
    read = n.readlines()
    
    for index,value in enumerate(read):
        if index in [line]:
            print("\n"+value)
        else:
            continue
    n.close()
    
def read_all(): #passed test
    with open ("text.txt","r+") as n :
        read = n.read()
        print("\n"+read)

    
def delete_a_line(): #passed test
    line = input("""please enter which number line
you would like to delete: """)
    
    while line.isdigit() == False:
        line = input("""please enter which number line
you would like to delete: """)
    
    line = int(line)
    line = line - 1
    
    with open("text.txt","r") as n:
        rrr = n.readlines()
    with open("text.txt","w") as n:
        for i, r in enumerate(rrr):
            if i not in [line]:
                n.write(r)

def delete_all(): #passed test
    with open ("text.txt","w") as n:
        n.write("")

def edit():
    noline = input("which line would you like to edit: ")
    
    while noline.isdigit() == False:
        noline = input("which line would you like to edit: ")
    
    noline = int(noline) - 1
    print("would you like to [Overwrite] a new line or [Append] to a line")
    mode = input("choose O or A: ")
    mode =mode.upper()
    
    # while True:
    #     if "A" not in mode or "O" not in mode:
    #         print("would you like to [Overwrite] a new line or [Append] to a line")
    #         mode = input("choose O or A: ")
    #         mode =mode.upper()
    #     else:
    #         break
    
    if mode == "O":
        replace_line()
    elif mode == "A":
        append_line()
    else:
        edit()
        
dictt ={"1. Make a new note":maker ,"2. Read all notes":read_all
    ,"3. Delete a note":delete_a_line ,"4. Delete all":delete_all 
,"5. Edit a note":edit,"6. Read a line":readaline}

def printer():
    array = ["1. Make a new note","2. Read all notes"
    ,"3. Delete a note","4. Delete all","5. Edit a note"
    ,"6. Read a line"]
    for title in array:
        print(title)
    return array
    
def inputter(array):
    user=str(input("please type what you would like to do: \n"))
    while user not in array:
        user=str(input("please type what you would like to do: \n"))
        if user in array:
            break
        else:
            continue
    return user
    
def comparer(array,user):
    for i in range(len(array)):
        if user in dictt:
            fun = dictt.get(user)
    fun()

a = printer()
b = inputter(a)
comparer(a,b)

