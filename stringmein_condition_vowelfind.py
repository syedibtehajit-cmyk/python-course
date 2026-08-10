name="karachi"
vowel=["a","e","i","o","u"]
cont=0
for i in name:
    if(i in vowel):
     cont=cont+1
print(cont)

name= "karachi"
vowels="aeiou"
count_constant=0

for i in name:
 if (i not in  vowels ):
    count_constant=count_constant+1
    
print(count_constant)