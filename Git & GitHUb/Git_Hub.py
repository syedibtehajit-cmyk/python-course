# git hub mein website kholde sign p kia and 
# git remote add origin https://github.com/syedibtehajit-cmyk/python-course.git is se add krwaya remotly
# git remote -v check kia fetch push aya mtab remotly add hogea

#Ab next command: git push

#Tumhari local branch ka naam master hai, isliye pehli push ke liye:

#git push -u origin master


#Is command ko tod kar samjho
#git push

#→ local commits ko GitHub par bhejo

#origin

#→ GitHub repository jo humne remote ke naam se save ki

#master

#→ tumhari current local branch

#-u

#→ local master ko remote origin/master ke saath track karwa do.

#Must remember
#
#🎯 Ab tumhara basic professional cycle:
#1. Code change karo
#        ↓
#2. git status
 #       ↓
#3. git diff
#        ↓
#4. git add .
 #       ↓
##5. git commit -m "message"
 #       ↓
#6. git push
#        ↓
#7. GitHub updated 

#Ab tumhare Git ke 2 directions clear hain
#LOCAL → GITHUB
#git push
#ITHUB → LOCAL
#git pull

#Agar kisi naye computer par GitHub wala project lana ho to kya karenge?

#Answer:

# git clone <repository-url>

# Git hub Clone Another LAptop or pc

# 1. Jis location par project lana hai wahan jao
#cd "C:\Users\IbtehaJ IT\Desktop\GitClonepractice"

# 2. GitHub repository clone karo
#git clone https://github.com/syedibtehajit-cmyk/python-course.git

# 3. Cloned project ke andar jao
#cd python-course

# 4. Check karo repository sahi clone hui hai
#git status

# 5. Git history check karo
#git log --oneline

# 6. Remote GitHub repository check karo
#git remote -v

print("MASTER BRANCH VERSION")
