from array import array

array=[]
while True:
    try:
        num=input("inserisci un valore intero")
        array.append(num)
        if num==0:
            break;
        else:
            array.append(num)
    except:
        print("casting non valido ")


























#def insfloat():
    #flag = 0
    #while flag != 1:
        #try:
           # numerofrazionario = input("inserisci un valore: ")
           # a = float(numerofrazionario)
           # flag = 1
           # return a
       # except ValueError:
          #  print("casting non valido")

#def int():
   # flag = 0
   # while flag != 1:
      ##  try:
          #  numerofrazionario = input("inserisci un valore: ")
         #   a = int(numerofrazionario)
          #  flag = 1
          ##  return a
        #except ValueError:
           # print("casting non valido")
#print(insfloat())#
