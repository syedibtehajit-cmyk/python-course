
#🌿 Git Branch Commands — Notes

#1. Current branch check
 #git branch

#Batata hai abhi kis branch par ho.

#* = current branch.

#2. New branch create karna
#git branch feature-practice

#Sirf branch banata hai.

#⚠️ Automatically branch par switch nahi karta.

#3. Branch par switch karna
#git switch feature-practice

#Existing branch par le jata hai.

# 4. Branch create + immediately switch

#Ye shortcut bohot useful hai:

#git switch -c feature-practice

#Matlab:

#create branch
 #    +
#switch branch
#5. Branch delete karna

#Jab feature merge ho chuka ho aur branch ki zarurat na ho:

#git branch -d feature-practice
#6. Branch merge karna ⭐

#Pehle jis branch mein feature lana hai, us par switch karo.

#Example:

#git switch master

#Phir:

#git merge feature-practice

#Meaning:

#feature-practice
 #      ↓
  #   merge
   #    ↓
    # master

#⚠️ Golden rule:

#JIS BRANCH MEIN FEATURE LANA HAI
#US BRANCH PAR PEHLE SWITCH KARO.
#🧠 Tumhare liye Branch workflow
#git branch

#↓

#git switch -c feature-practice

#↓

#Code change

#↓

#git status

#↓

#git add .

#↓

#git commit -m "Add feature"

#↓

#Feature complete hone ke baad:

#git switch master

#↓

#git merge feature-practice
#📌 Short memory trick
#branch  = branch dekho
#branch NAME = branch banao
#switch NAME = branch badlo
#switch -c NAME = banao + badlo
#merge NAME = doosri branch ka kaam current branch mein lao
#branch -d NAME = branch delete

