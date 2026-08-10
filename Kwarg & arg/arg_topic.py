#def student(*arg):
   # for i in arg:
     # print(len(arg))
#student("aa","aaa","aasd")

def calculate(*arg):
      sum=0
      for i in arg:
            sum=sum+i
      print(sum)

calculate(10, 20, 30, 40)