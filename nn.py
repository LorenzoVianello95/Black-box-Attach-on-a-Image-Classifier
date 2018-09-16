#author:Lorenzo Vianello 1805889
#THIS IS THE CODE TO TEST 4 CLASS OF BOAT, I CONSIDER ONLY THE 2 BIGGERS PROBABILITIES , DON'T WATCH THE OTHERS, IF FIRST<SECOND*ALPHA THEN AMBIGUITY

#libraries for write read and execute from prompt
import os
from subprocess import Popen,PIPE
from PIL import Image

nameFoto= "/home/lollo/Desktop/vap.jpg"
img = Image.open(nameFoto)
img.show()

#in_file = open("/home/lorenzo/Scrivania/sc5Test/ground_truth.txt","r")

#dictB={}
#l=0
#constant that represent the coefficient that the program multiply for the second bigger probability  
#alpha=2


print"NOW WILL BE CLASSIFY",nameFoto,"IMAGE\n___________________________________\n"
#dir_image="//home//lorenzo//Scrivania//sc5Test//"
#variabiles which take count of the time that the algorithm correctly classify an image and also the cases in wich in image is ambiguous 
#number_matching=0
#number_mismatching=0
#number_ambiguity=0
#variabiles that take the first and the second types whit bigger probability and their probability
type1=""
prob1=""
type2=""
prob2=""

cmd= "tensorflow/bazel-bin/tensorflow/examples/label_image/label_image  --graph=/home/lollo/Desktop/labelsgraph/output_graph1.pb --labels=/home/lollo/Desktop/labelsgraph/output_labels1.txt   --output_layer=final_result --image="+nameFoto+" --input_layer=Mul "
l=Popen(cmd, stdout=PIPE,stderr=PIPE,shell=True)
#collect what the command execution return
(out,err) = l.communicate();
#print (err)
in_line=str(err)
#print(in_line)
i=0
j=0
word=""

for index in range(0,len(in_line)):
        if (in_line[index].isalnum() or in_line[index]=="." or in_line[index]=="\n") and i<5:
             word=word+in_line[index]
             f=word.replace(".","").replace(" ","")
             #print(f)

             if((word == "gondola") or (word == "vaporettoactv"))and i==0:
                     type1=word
                     word=""
                     i=1
             if  f.isdigit() and i==1:
                     j=j+1
                     mom=float(word)
                     if mom>0 and mom<1 and j>7:
                         prob1=mom
                         word=""
                         i=2
                         j=0
             if((word == "vaporettoactv") or (word == "gondola"))and i==2:
                     type2=word
                     word=""
                     i=3
             if( f.isdigit() and i==3):
                     j=j+1
                     mom=float(word)
                     if mom>0 and mom<1 and j>7:
                         prob2=mom
                         word=""
                         i=10
        else:
            word=""     

print type1,prob1,type2,prob2 
    




print "4.1 Substitute model training"
# (1)prendo un set di imagini una per ogni class da classificare in my case( una del vaporetto una della gondola) e lo definisco S0 dove 0 sta ad indicare r
#(2) F CNN nel mio caso 
#iteritivamente da 0 a r( dove non ho capito che valore ha r forse lo prestabilisco io )
#{
#(3)creo training set con le immagini Sr che alla prima iterazione sono S0 e con cio che il mio classificatore prevede come labels 
#(4)con il training set calcolato mi costruisco la CNN F 
#(5)creo Sr+1 che e un insieme che contiene le immagini di Sr e le immagini di Sr leggermente variate :per x appartenente a Sr X+ksgn(JF[O(X)])        ossia k(costante)volte il segno della matrice jacobiana corrispondente ai label assegnati a x da O  
























