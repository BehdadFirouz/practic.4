def a ():
    toll=int(input("toll safhe ra vared konid :    "))
    arz=int(input("arz safhe ra vared konid :     "))
    for i in range(arz):
        for j in range(toll):
            if i%2==0 :
                if j%2==0:
                    print("#", end=" ")
                else :
                    print("*", end=" ")
            else:
                if j%2==0:
                    print("*", end=" ")
                else:
                    print("#", end=" ")
        print()
a()