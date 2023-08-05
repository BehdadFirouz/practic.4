min=int(input("adad kochektar ra vared konid :    "))
max=int(input("adad bozorgtar ra vared konid :    "))
i=1
for i in range(1, min+1):
    if min%i==0 and max%i==0:
        b_m_m=i
print(b_m_m)