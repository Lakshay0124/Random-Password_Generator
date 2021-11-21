
import random
import string
b2=string.ascii_letters
b3=string.punctuation
zy=random.randint(1,9)
zy1=random.randint(1,9)
zy2=random.randint(1,9)
zy3=random.randint(1,9)
ty=random.choice(b2)
ty1=random.choice(b2)
ty2=random.choice(b2)
ty3=random.choice(b2)
ty4=random.choice(b2)
ty5=random.choice(b2)
ty6=random.choice(b2)
ty7=random.choice(b2)
xy=random.choice(b3)
xy1=random.choice(b3)
xy2=random.choice(b3)
xy3=random.choice(b3)
xy4=random.choice(b3)
gg=(ty+str(zy1)+xy1+ty2+str(zy)+xy2+ty3+ty4+xy3+str(zy2)+ty5+xy+str(zy3)+ty6+xy4+ty7)
print(f"Your Password is - {gg}")
hj=input("Do you want to save that password yes or no -  ")
if (hj=="yes"):
    hj1=input("For What Wesbite You Want To Save - ")
    hj2=input("What Is The Username - ")
    with open("saved_password.txt","a") as f:
        f.write(f"""        
{hj2}               {hj1}              {gg}                """)
else:
    print("Okay")  
