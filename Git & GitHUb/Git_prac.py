# git add . se sare file commit kardeta ha
# git commit comand git commit -m "Initial Python Course Files"
# git commit -m "Python course"

#Agar tumhara Gmail hai, maan lo:

#syedibtehaj@gmail.com

#To command hogi:

#git config --global user.email "syedibtehaj@gmail.com"

#⚠️ Apna asli Gmail likhna, mera example copy mat karna.

#Step 2: Name Set Karo

#git config --global user.name "Syed Ibtehaj Ishtiaque"

#Step 3: Verify

#git config --global --list

#Expected:

#user.name=Syed Ibtehaj Ishtiaque
#user.email=yourgmail@gmail.com

#Step 4: Commit

#Ab phir chalao:

#git commit -m "Initial Python Course Files"


#📚 Git Memory Card #1

#Start Project
 #     ↓
#git init

#Check Status
  #    ↓

#git status

#Track Files
 #     ↓
#git add .

#Save Snapshot
 #     ↓
#git commit

# Tumhare liye important distinction
# git status


# = Abhi project mein kya ho raha hai?

# git add .

# = Kis change ko commit ke liye ready karna hai?

# git commit

# = Current changes ka snapshot save karo.

# git log

# = Mere purane snapshots/commits dikhao.

# Ye 4 commands Git ke basic workflow ki core commands hain.

# Ab git log ka matlab ha snap shot kitne bane uski history btata ha

# git diff is mein pata chalata ha file mein kia chizen change ki han

# gitignore Kuch files/folders ko Git se ignore karna .gitignore file bana ha .py ni lagana is mein ye __pycache__/
#*.pyc
#.venv/
#.env
#yani jise git ignore kare 

#Pehle .gitignore ko stage karo:
# kisi ak item ko  file ke name ke commit karta ha "New-Item .gitignore -ItemType File
#
# "
#git add .gitignore


#Summary

#it status       → changes dekho
#git diff         → exact changes dekho
#git add          → staging
#git commit       → snapshot save
#git log          → history dekho
#.gitignore       → unwanted files ignore

#git ls-files "*__pycache__*" "*.pyc" __pycache and .pyc kis file ko track karha ha

# git rm --cached "Logging_sample_topic/__pycache__/logging.cpython-313.pyc
#pycache__/student_module.cpython-313.pyc
#project/tools/__pycache__/calculator.cpython-313.pyc" Isliye ab in 3 files ko Git ki tracking se remove karna hai, lekin computer se delete nahi karna.