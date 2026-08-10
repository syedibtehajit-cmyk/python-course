numbers = [10, -5, 20, -8, 30, -1, 15] #ye ha yani parameter jis ko sort karna ha
positive_sum=0
counts=0
Average=0

for i in numbers: # loop chale list ki ak ak value dakhe ga
    if(i > 0): # i bara ho 0 se to condition true hogai warna terminate
        positive_sum=positive_sum+i # iska matlab ha jo jo postive no i mein atte ho us ko add krke sum ke variable mein dal do

        counts = counts +1 # iska matlab ha jo postive number us mein ak 1 add karte jao to count hojaiga 

Average= positive_sum/counts #iska matlab jo value positive sum count ke variable mein ho usko averge kardo

print("Postive number Sum",positive_sum,"Positive number count :",counts, "Postive no ka average",Average) # simple print ha