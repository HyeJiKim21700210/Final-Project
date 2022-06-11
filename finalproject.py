import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('mushroom.csv')

def draw_line_top():
  print("\n\n----------------------------------------------------------------")

def draw_line_bottom():
  print("----------------------------------------------------------------\n\n")

def print_feature(input):

  try:
    name1 = input.iloc[0,0]
    name2 = input.iloc[0,1]
    cluster = input.iloc[0,2]

    ring1 = input.iloc[0,6]
    shape = input.iloc[0,13]
    color = input.iloc[0,12]
    season = input.iloc[0,14]
    location = input.iloc[0,15]
    toxic = input.iloc[0,16]
    similar = input.iloc[0,17]
    diameter1 = input.iloc[0,8]
    diameter2 = input.iloc[0,9]
    diameter = str(diameter1) +"~"+ str(diameter2)
    stipe1 = input.iloc[0,10]
    stipe2 = input.iloc[0,11]
    stipe = str(stipe1)+"~"+str(stipe2)

    if(ring1 == '1'):
      ring = 'O'
    else:
      ring = 'X'

    cluster1 =""

    if(cluster == 1):
      cluster1 += "solitery"

    cluster = input.iloc[0,3] 
    if(cluster ==1):
      if(cluster1 ==""):
        cluster1+= "couple"
      else:
        cluster1+= ", couple"
   
    cluster = input.iloc[0,4]
    if(cluster ==1):
      if(cluster1 == ""):
        cluster1 += "in groups"
      else:
        cluster1 += ", in groups"

    cluster = input.iloc[0,5]
    if(cluster ==1):
      if(cluster1 == ""):
        cluster1 += "fasciculate"
      else:
        cluster1 += ", fasciculate"
  


    draw_line_top()
    print("name(Korean):",name1)
    print("name(English):",name2)
    print("Cluster status:",cluster1)
    print("Fairy ring: ", ring)
    print("The shape of cap:",shape)
    print("The length of the cap's diameter:",diameter)
    print("The length of the stipe ")
    print("or mushroom itself length(if cannot have cap): ",stipe)
    print("Color:",color)
    print("Occurrence season:",season)
    print("Occurrence place: ",location)
    print("Toxicity: ",toxic)
    print("Similar thing:",similar)
    draw_line_bottom()
  except:
    draw_line_top()
    print("\n We could not find that mushroom.\n\n")
    draw_line_bottom()

def find_nameK(df, name):
  input = df.loc[df['name'].str.contains(name, na=False)]
  print_feature(input)

def find_nameE(df,name):
  input = df[df['english'].isin([name])]
  print_feature(input)


def explain_cluster():
  print("Cluster status")
  print("->It is a word that refers to the occurrence ")
  print("status of mushrooms and is classified as")
  print(" -Solitary: Occurred alone with nothing around.")
  print(" -Couple: Occurred twin.")
  print(" -In groups: Several strands grow together from one root")
  print(" -Fasciculate: Several mushrooms grow together into individuals.\n")
  
def explain_fairy():
  print("Fairy fing")
  print("->The shape of mushrooms growing in a row ")
  print("under a tree in a meadow or forest.\n")
  
def explain_cap():
  print("Cap")
  print("->It refers to the head of mushrooms, ")
  print("some species do not have it.\n")
  
def explain_stipe():
  print("Stipe")
  print("->It means the rest of the stem except for the cap of the mushroom\n")
  
def explain_place():
  print("Place")
  print("it refers to the place where mushrooms have occurred.")
  
def explain_color():
  print("Color") 
  print("->if mushroom have a cap, choose the color of the cap, ")
  print("or choose the color of the stem.\n")

def explain():
  draw_line_top()
  explain_cluster()
  explain_fairy()
  explain_cap()
  explain_stipe()
  explain_color()
  explain_place()
  draw_line_bottom()
  
  
def finding_str(cell, index, name):
  name = name.lower()
  cell = cell.loc[cell[index].str.contains(name, na=False)]
  return cell

def finding_length(cell, index,index2,answer):
  answer = int(answer)
  cell = cell[cell[index]<=answer]
  cell = cell[cell[index2]>=answer]
  return cell

def find_feature(df):
  while(1):
    draw_line_top()
    print("Cluster status")
    print("1.solitery 2.Couple 3.Ingroups 4.Fasciculate 0.I do not know. \nExplain Cluster status: e")
    answer = input()
    if(answer == '1'):
      cell = df[df['solitary'].isin([1])]
      break
    elif(answer =='2'):
      cell = df[df['couple'].isin([1])]
      break
    elif(answer =='3'):
      cell = df[df['in groups'].isin([1])]
      break
    elif(answer == '4'):
      cell = df[df['fasciculate'].isin([1])]
      break
    elif(answer =='0'):
      cell = df
    elif(answer =='e'):
      explain_cluster()
    else:
      print("enter the number (1,2,3,4,0)")

#Fairy ring
  while(1):
    draw_line_top()
    print("Fairy ring: 1 or 0, \nExplain Fairy ring: e")
    answer = input()
    if(answer =='1'):
      cell = cell[cell['fairy ring'].isin([1])]
      break
    elif(answer =='0'):
      cell = cell[cell['fairy ring'].isin([0])]
      break
    elif(answer == 'e'):
      explain_fairy()
    else:
      print("enter the number(1,0)")

#Cap
  while(1):
    draw_line_top()
    print("Cap: 1 or 0\nExplain Cap: e")
    answer = input()
    if(answer == '1'):
      print("Shape: ")
      print("round mountain, flat, sphere, hemisphere, bell, ear, stick,")
      print("concave, cone, egg, circle, irregular sphere, semicircle, star.")
      answer = input()
      cell = finding_str(cell, 'shape', answer)

      print("The length of cap's diameter:")
      answer = input()
      cell = finding_length(cell, 'head_low', 'head_high', answer)
      break;

    elif(answer== '0'):
      cell = cell[cell['cap'].isin([0])]
      break
         
    elif(answer == 'e'):
      explain_cap()
    else:
      print("enter the number(1,0)")

  
  #stipe_length
  while(1):
    draw_line_top()
    print("The length of stipe:")
    print("(If mushroom cannot have cap, than enter the length of mushroom)")
    print("Explain stipe: e")
    answer = input()
    if(answer == 'e'):
      explain_stipe()
    else:
      cell =finding_length(cell, 'stipe_low', 'stipe_high',answer)
      break

  #Color
  draw_line_top()
  print("Color: ")
  print("white, taupe, ivory, brown, poppy red, orange, red, olive,") 
  print("yellowish brown, blackish brown, reddish brown, indigo black, ")
  print("purple, grayish purple, beige, isabella, purplish brown, ")
  print("blackish brown, pink, yellow purple, gray,yellow.")
  print("I do not know: 0")
  answer = input()
  if(answer == '0'):
    cell = cell
  else:
    cell = finding_str(cell,'color',answer)
  
  #Season
  draw_line_top()
  print("Seasons: spring, summer, fall, winter")
  print("I do not know: 0")
  answer = input()
  if(answer == '0'):
    cell = cell
  else:
    cell = finding_str(cell,'season',answer)
    

  #Place
  while(1):
    draw_line_top()
    print("Place:")
    print("forest, fallen leaves, bare ground, needleleaf, broadleaf,")
    print("pine, bamboo, old tree, yard, oak, mixed forest, grassb, bran,  ")
    print("dump, garden, dead tree, beteen stones, wayside, pasture, ")
    print("copse, insect, mold, cliff,zelkova, sapin, pteridophyta, ")
    print("wasteland, farm. ")
    print("I do not know: 0 \nExplain Place: 1")
    answer = input()
    if(answer == '0'):
      cell = cell
      break
    elif(answer == '1'):
      explain_place()
    else:
      ell = finding_str(cell,'location',answer)
      break

  print_feature(cell)

while(1):
  #Menu print
  print("***************************MENU*****************************")
  print("1. find using name(Korean)")
  print("2. find using name (scientific name)")
  print("3. find using feature")
  print("4. what is the mean of index naming")
  print("0. Quit")
  print("************************************************************")
  print("enter the number")
  answer=input()

  #find using korean name
  if(answer == "1"):
    print("==> Enter the Korean name of the mushroom you want to find")
    name = input()
    find_nameK(df,name)

  #find using scientific name
  elif(answer == '2'):
    print("==> Enter the Scientific name of the mushroom you want to find")
    name = input()
    find_nameE(df,name)

  #find using feature
  elif(answer =='3'):
    find_feature(df)
  
  #explain print
  elif(answer == '4'):
    explain()

  elif(answer == '0'):
    print("Bye")
    break
  else:
    print("Please enter the number (1,2,3,4,0)")

