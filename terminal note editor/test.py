# def replace_line():
#     use = int(input("""please enter which number line
# you would like to overwrite: """))
#     use = use - 1
#     with open("text.txt","r") as n:
#         rrr = n.readlines()
#     with open("text.txt","w+") as n:
#         for i, r in enumerate(rrr):
#             if i not in [use]:
#                 n.write(r)
#             else:
#                 n.write("hi\n")
                
# def append_line():
#     use = int(input("""please enter which number line
# you would like to overwrite: """))
#     use = use - 1
#     with open("text.txt","r") as n:
#         rrr = n.readlines()
#     with open("text.txt","w") as n:
#         for i, r in enumerate(rrr):
#             if i  not in  [use]:
#                 n.write(r)
#             else:
#                 r = r.strip()
#                 n.write(r+" this has been added\n")

# def delete_a_line(): #passed test
#     use = int(input("""please enter which number line
# you would like to delete: """))
#     use = use - 1
#     with open("text.txt","r") as n:
#         rrr = n.readlines()
#     with open("text.txt","w") as n:
#         for i, r in enumerate(rrr):
#             if i not in [use]:
#                 n.write(r)
                
# delete_a_line()
def readaline(): #passed test
    n = open("text.txt","r")
    indie = int(input("Which line would you like to read? "))
    read = n.readlines()
    for index,line in enumerate(read):
        if index in [indie]:
            print(line)
        else:
            continue
    n.close()