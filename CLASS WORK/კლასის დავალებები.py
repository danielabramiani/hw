#i=4

#while i <=20
#  i += 4

#def misalmeba(saxeli):
    #print("mogesalmebi " + saxeli)

#misalmeba("nika")
#misalmeba("gabriel")
#misalmeba("luka")
#misalmeba("sandro")

#from turtle import * 

#    for i in range(4):
        #forward(100)
        #left(90)
       # forward(100)
#  #       left(90)

# def kalmis_wageba(x,y):
#     penup()
#     goto(x,y)
#     pendown() 

# draw_square()
# kalmis_wageba(0,200)

# draw_square()
# kalmis_wageba(-200,200)

# #third square
# draw_square()
# kalmis_wageba(-200,0)

#fourth square
#draw_square()

#exitonclick()
# #define aris ფუნქციის დასახვა
# def split_string(names_string):
#   names = names_string.split()
#   print(names)
  
# names = "dato nene megi"
# split_string(names)



# def =(name,num):
# print(name+num)

# name=Chiko
# num=33

# def =(name,num):
# print(name+num)

# name=Ninuca
# num=32 
#** kvadratshi ayvana

def abbrev_name(name):
    words = name.split()
    new_letter = ""
    first_letter = words[0][0].capitalize()
    second_letter = words[1][0].capitalize()
    new_letter += first_letter + "." + second_letter
    return new_letter