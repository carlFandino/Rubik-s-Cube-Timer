""""""
import tkinter as tk
import random
import sqlite3
#If it throws an error create file/type "af.dll","aft.dll","ao.dll","at.dll" and "vcTimes.dll"
conn = sqlite3.connect("u_d.db")
_datas = conn.cursor()

#_datas.execute("UPDATE _users SET __ao5 = 0,__ao12 = 0,__ao100 = 0,__ao50 = 0,best=0,worst=0")
moves  =   ["L", "L2", "L'",
            "R", "R2", "R'",
            "F", "F2", "F'",
            "B", "B2", "B'",
            "U", "U2", "U'",
            "D", "D2", "D'"]
cnt = 0
output = []
prev = 'ZZ'
inspection = 16
isInspection = False

myTime = 0
__author__ = "giancarl.fandino@gmail.com" #Carl Gian Dinglasan Fandino

scrambleText = tk.Label(bg="black",fg="white",text=output,height=1,width=55,font=("Italic",30))
time = tk.Label(bg="black",fg="white",text=myTime,width=39,height=10,font=("Courier",40))
isTimeStarted = False







Ao5Text = tk.Label(bg="black",fg="white",text=(f"Ao5:"),font=("MS sans",25))
Ao12Text = tk.Label(bg="black",fg="white",text=(f"Ao12:"),font=("MS sans",25))
Ao50Text = tk.Label(bg="black",fg="white",text=(f"Ao50:"),font=("MS sans",25))
Ao100Text = tk.Label(bg="black",fg="white",text=(f"Ao100:"),font=("MS sans",25))
bestText = tk.Label(bg="black",fg="white",text=(f"Best:"),font=("MS sans",25))
worstText = tk.Label(bg="black",fg="white",text=(f"Worst:"),font=("MS sans",25))

numberOfSolvesText = tk.Label(bg="black",fg="white",text=(f"Solves in Total: "),font=("MS sans",25))

UpColor = "white"
LeftColor = "orange"
FaceColor = "lime"
RightColor = "red"
BackColor = "blue"
DownColor = "yellow"

                 #0  #1  #2
scrambleImage = ["w","w","w"
                 #3  #4  #5
                ,"w","w","w"
                 #6  #7  #8
                ,"w","w","w",
     #9  #10 #11 #12 #13 #14 #15 #16 #17 #18 #19 #20
     "o","o","o","g","g","g","r","r","r","b","b","b",
     #21  #22 #23 #24 #25 #26 #27 #28 #29 #30 #31 #32
     "o","o","o","g","g","g","r","r","r","b","b","b",
     #33 #34 #35 #36 #37 #38 #39 #40 #41 #42 #43 #44
     "o","o","o","g","g","g","r","r","r","b","b","b",
                 #45 #46 #47
                 "y","y","y",
                 #48 #49 #50
                 "y","y","y",
                 #51 #52 #53
                 "y","y","y"]   
scrambleImage[0] = tk.Label(width=4,height=2,bg="white")
scrambleImage[0].pack()
scrambleImage[1] = tk.Label(width=4,height=2,bg="white")
scrambleImage[1].pack()
scrambleImage[2] = tk.Label(width=4,height=2,bg="white")
scrambleImage[2].pack()
scrambleImage[3] = tk.Label(width=4,height=2,bg="white")
scrambleImage[3].pack()
scrambleImage[4] = tk.Label(width=4,height=2,bg="white")
scrambleImage[4].pack()
scrambleImage[5] = tk.Label(width=4,height=2,bg="white")
scrambleImage[5].pack()
scrambleImage[6] = tk.Label(width=4,height=2,bg="white")
scrambleImage[6].pack()
scrambleImage[7] = tk.Label(width=4,height=2,bg="white")
scrambleImage[7].pack()
scrambleImage[8] = tk.Label(width=4,height=2,bg="white")
scrambleImage[8].pack()
scrambleImage[9] = tk.Label(width=4,height=2,bg="orange")
scrambleImage[9].pack()
scrambleImage[10] = tk.Label(width=4,height=2,bg="orange")
scrambleImage[10].pack()
scrambleImage[11] = tk.Label(width=4,height=2,bg="orange")
scrambleImage[11].pack()
scrambleImage[21] = tk.Label(width=4,height=2,bg="orange")
scrambleImage[21].pack()
scrambleImage[22] = tk.Label(width=4,height=2,bg="orange")
scrambleImage[22].pack()
scrambleImage[23] = tk.Label(width=4,height=2,bg="orange")
scrambleImage[23].pack()
scrambleImage[33] = tk.Label(width=4,height=2,bg="orange")
scrambleImage[33].pack()
scrambleImage[34] = tk.Label(width=4,height=2,bg="orange")
scrambleImage[34].pack()
scrambleImage[35] = tk.Label(width=4,height=2,bg="orange")
scrambleImage[35].pack()
scrambleImage[12] = tk.Label(width=4,height=2,bg="lime")
scrambleImage[12].pack()
scrambleImage[13] = tk.Label(width=4,height=2,bg="lime")
scrambleImage[13].pack()
scrambleImage[14] = tk.Label(width=4,height=2,bg="lime")
scrambleImage[14].pack()
scrambleImage[24] = tk.Label(width=4,height=2,bg="lime")
scrambleImage[24].pack()
scrambleImage[25] = tk.Label(width=4,height=2,bg="lime")
scrambleImage[25].pack()
scrambleImage[26] = tk.Label(width=4,height=2,bg="lime")
scrambleImage[26].pack()
scrambleImage[36] = tk.Label(width=4,height=2,bg="lime")
scrambleImage[36].pack()
scrambleImage[37] = tk.Label(width=4,height=2,bg="lime")
scrambleImage[37].pack()
scrambleImage[38] = tk.Label(width=4,height=2,bg="lime")
scrambleImage[38].pack()
scrambleImage[15] = tk.Label(width=4,height=2,bg="red")
scrambleImage[15].pack()
scrambleImage[16] = tk.Label(width=4,height=2,bg="red")
scrambleImage[16].pack()
scrambleImage[17] = tk.Label(width=4,height=2,bg="red")
scrambleImage[17].pack()
scrambleImage[27] = tk.Label(width=4,height=2,bg="red")
scrambleImage[27].pack()
scrambleImage[28] = tk.Label(width=4,height=2,bg="red")
scrambleImage[28].pack()
scrambleImage[29] = tk.Label(width=4,height=2,bg="red")
scrambleImage[29].pack()
scrambleImage[39] = tk.Label(width=4,height=2,bg="red")
scrambleImage[39].pack()
scrambleImage[40] = tk.Label(width=4,height=2,bg="red")
scrambleImage[40].pack()
scrambleImage[41] = tk.Label(width=4,height=2,bg="red")
scrambleImage[41].pack()
scrambleImage[18] = tk.Label(width=4,height=2,bg="blue")
scrambleImage[18].pack()
scrambleImage[19] = tk.Label(width=4,height=2,bg="blue")
scrambleImage[19].pack()
scrambleImage[20] = tk.Label(width=4,height=2,bg="blue")
scrambleImage[20].pack()
scrambleImage[30] = tk.Label(width=4,height=2,bg="blue")
scrambleImage[30].pack()
scrambleImage[31] = tk.Label(width=4,height=2,bg="blue")
scrambleImage[31].pack()
scrambleImage[32] = tk.Label(width=4,height=2,bg="blue")
scrambleImage[32].pack()
scrambleImage[42] = tk.Label(width=4,height=2,bg="blue")
scrambleImage[42].pack()
scrambleImage[43] = tk.Label(width=4,height=2,bg="blue")
scrambleImage[43].pack()
scrambleImage[44] = tk.Label(width=4,height=2,bg="blue")
scrambleImage[44].pack()
scrambleImage[45] = tk.Label(width=4,height=2,bg="yellow")
scrambleImage[45].pack()
scrambleImage[46] = tk.Label(width=4,height=2,bg="yellow")
scrambleImage[46].pack()
scrambleImage[47] = tk.Label(width=4,height=2,bg="yellow")
scrambleImage[47].pack()
scrambleImage[48] = tk.Label(width=4,height=2,bg="yellow")
scrambleImage[48].pack()
scrambleImage[49] = tk.Label(width=4,height=2,bg="yellow")
scrambleImage[49].pack()
scrambleImage[50] = tk.Label(width=4,height=2,bg="yellow")
scrambleImage[50].pack()
scrambleImage[51] = tk.Label(width=4,height=2,bg="yellow")
scrambleImage[51].pack()
scrambleImage[52] = tk.Label(width=4,height=2,bg="yellow")
scrambleImage[52].pack()
scrambleImage[53] = tk.Label(width=4,height=2,bg="yellow")
scrambleImage[53].pack()

def scramble():
    global cnt,output,prev
    while  cnt < 20:
        pos = random.randrange(18)
        if moves[pos][0]  != prev[0]:
            output.append(moves[pos])
            prev = moves[pos]
            cnt += 1
    return output
scramble()
def __StartTime__():
    global time,myTime,isTimeStarted
    if  isTimeStarted == True:
        myTime += 0.013
        time.config(text="%.2f"%myTime)
        time.after(1,__StartTime__)

def scrambleImage_():
    global scrambleImage
    global output
    #white
    scrambleImage[0].place(relx=0.70,rely=0.208)
    scrambleImage[0].config(bg=UpColor)
    scrambleImage[1].place(relx=0.729,rely=0.208)
    scrambleImage[1].config(bg=UpColor)
    scrambleImage[2].place(relx=0.7579,rely=0.208)
    scrambleImage[2].config(bg=UpColor)
    scrambleImage[3].place(relx=0.70,rely=0.250)
    scrambleImage[3].config(bg=UpColor)
    scrambleImage[4].place(relx=0.729,rely=0.250)
    scrambleImage[4].config(bg=UpColor)
    scrambleImage[5].place(relx=0.7579,rely=0.250)
    scrambleImage[5].config(bg=UpColor)
    scrambleImage[6].place(relx=0.70,rely=0.292)
    scrambleImage[6].config(bg=UpColor)
    scrambleImage[7].place(relx=0.729,rely=0.292)
    scrambleImage[7].config(bg=UpColor)
    scrambleImage[8].place(relx=0.7579,rely=0.292)
    scrambleImage[8].config(bg=UpColor)
    #orange
    scrambleImage[9].place(relx=0.6129,rely=0.335)
    scrambleImage[9].config(bg=LeftColor)
    scrambleImage[10].place(relx=0.6419,rely=0.335)
    scrambleImage[10].config(bg=LeftColor)
    scrambleImage[11].place(relx=0.670,rely=0.335)
    scrambleImage[11].config(bg=LeftColor)
    scrambleImage[21].place(relx=0.6129,rely=0.379)
    scrambleImage[21].config(bg=LeftColor)
    scrambleImage[22].place(relx=0.6419,rely=0.379)
    scrambleImage[22].config(bg=LeftColor)
    scrambleImage[23].place(relx=0.670,rely=0.379)
    scrambleImage[23].config(bg=LeftColor)
    scrambleImage[33].place(relx=0.6129,rely=0.422)
    scrambleImage[33].config(bg=LeftColor)
    scrambleImage[34].place(relx=0.6419,rely=0.422)
    scrambleImage[34].config(bg=LeftColor)
    scrambleImage[35].place(relx=0.670,rely=0.422)
    scrambleImage[35].config(bg=LeftColor)
    #green
    scrambleImage[12].place(relx=0.6989,rely=0.335)
    scrambleImage[12].config(bg=FaceColor)
    scrambleImage[13].place(relx=0.7279,rely=0.335)
    scrambleImage[13].config(bg=FaceColor)
    scrambleImage[14].place(relx=0.7570,rely=0.335)
    scrambleImage[14].config(bg=FaceColor)
    scrambleImage[24].place(relx=0.6989,rely=0.379)
    scrambleImage[24].config(bg=FaceColor)
    scrambleImage[25].place(relx=0.7279,rely=0.379)
    scrambleImage[25].config(bg=FaceColor)
    scrambleImage[26].place(relx=0.7570,rely=0.379)
    scrambleImage[26].config(bg=FaceColor)
    scrambleImage[36].place(relx=0.6989,rely=0.422)
    scrambleImage[36].config(bg=FaceColor)
    scrambleImage[37].place(relx=0.7279,rely=0.422)
    scrambleImage[37].config(bg=FaceColor)
    scrambleImage[38].place(relx=0.7570,rely=0.422)
    scrambleImage[38].config(bg=FaceColor)
    #red
    scrambleImage[15].place(relx=0.786,rely=0.335)
    scrambleImage[15].config(bg=RightColor)
    scrambleImage[16].place(relx=0.815,rely=0.335)
    scrambleImage[16].config(bg=RightColor)
    scrambleImage[17].place(relx=0.8439,rely=0.335)
    scrambleImage[17].config(bg=RightColor)
    scrambleImage[27].place(relx=0.786,rely=0.379)
    scrambleImage[27].config(bg=RightColor)
    scrambleImage[28].place(relx=0.815,rely=0.379)
    scrambleImage[28].config(bg=RightColor)
    scrambleImage[29].place(relx=0.8439,rely=0.379)
    scrambleImage[29].config(bg=RightColor)
    scrambleImage[39].place(relx=0.786,rely=0.422)
    scrambleImage[39].config(bg=RightColor)
    scrambleImage[40].place(relx=0.815,rely=0.422)
    scrambleImage[40].config(bg=RightColor)
    scrambleImage[41].place(relx=0.8439,rely=0.422)
    scrambleImage[41].config(bg=RightColor)
    #blue
    scrambleImage[18].place(relx=0.8739,rely=0.335)
    scrambleImage[18].config(bg=BackColor)
    scrambleImage[19].place(relx=0.9027,rely=0.335)
    scrambleImage[19].config(bg=BackColor)
    scrambleImage[20].place(relx=0.9315,rely=0.335)
    scrambleImage[20].config(bg=BackColor)
    scrambleImage[30].place(relx=0.8739,rely=0.379)
    scrambleImage[30].config(bg=BackColor)
    scrambleImage[31].place(relx=0.9027,rely=0.379)
    scrambleImage[31].config(bg=BackColor)
    scrambleImage[32].place(relx=0.9315,rely=0.379)
    scrambleImage[32].config(bg=BackColor)
    scrambleImage[42].place(relx=0.8739,rely=0.422)
    scrambleImage[42].config(bg=BackColor)
    scrambleImage[43].place(relx=0.9027,rely=0.422)
    scrambleImage[43].config(bg=BackColor)
    scrambleImage[44].place(relx=0.9315,rely=0.422)
    scrambleImage[44].config(bg=BackColor)
    #yellow
    scrambleImage[45].place(relx=0.6995,rely=0.466)
    scrambleImage[45].config(bg=DownColor)
    scrambleImage[46].place(relx=0.7282,rely=0.466)
    scrambleImage[46].config(bg=DownColor)
    scrambleImage[47].place(relx=0.7570,rely=0.466)
    scrambleImage[47].config(bg=DownColor)
    scrambleImage[48].place(relx=0.6995,rely=0.509)
    scrambleImage[48].config(bg=DownColor)
    scrambleImage[49].place(relx=0.7282,rely=0.509)
    scrambleImage[49].config(bg=DownColor)
    scrambleImage[50].place(relx=0.7570,rely=0.509)
    scrambleImage[50].config(bg=DownColor)
    scrambleImage[51].place(relx=0.6995,rely=0.552)
    scrambleImage[51].config(bg=DownColor)
    scrambleImage[52].place(relx=0.7282,rely=0.552)
    scrambleImage[52].config(bg=DownColor)
    scrambleImage[53].place(relx=0.7570,rely=0.552)
    scrambleImage[53].config(bg=DownColor)
    
    for scrambleMoves in output:
        
        if scrambleMoves == "R":
           scrambleImage[15]["bg"],scrambleImage[16]["bg"],scrambleImage[17]["bg"],scrambleImage[29]["bg"],scrambleImage[41]["bg"],scrambleImage[40]["bg"],scrambleImage[39]["bg"],scrambleImage[27]["bg"],scrambleImage[14]["bg"],scrambleImage[26]["bg"],scrambleImage[38]["bg"],scrambleImage[2]["bg"],scrambleImage[5]["bg"],scrambleImage[8]["bg"],scrambleImage[18]["bg"],scrambleImage[30]["bg"],scrambleImage[42]["bg"],scrambleImage[47]["bg"],scrambleImage[50]["bg"],scrambleImage[53]["bg"] = scrambleImage[39]["bg"],scrambleImage[27]["bg"],scrambleImage[15]["bg"],scrambleImage[16]["bg"],scrambleImage[17]["bg"],scrambleImage[29]["bg"],scrambleImage[41]["bg"],scrambleImage[40]["bg"],scrambleImage[47]["bg"],scrambleImage[50]["bg"],scrambleImage[53]["bg"],scrambleImage[14]["bg"],scrambleImage[26]["bg"],scrambleImage[38]["bg"],scrambleImage[8]["bg"],scrambleImage[5]["bg"],scrambleImage[2]["bg"],scrambleImage[42]["bg"],scrambleImage[30]["bg"],scrambleImage[18]["bg"]            
           continue
        
        if scrambleMoves == "R2":
           scrambleImage[15]["bg"],scrambleImage[16]["bg"],scrambleImage[17]["bg"],scrambleImage[29]["bg"],scrambleImage[41]["bg"],scrambleImage[40]["bg"],scrambleImage[39]["bg"],scrambleImage[27]["bg"],scrambleImage[14]["bg"],scrambleImage[26]["bg"],scrambleImage[38]["bg"],scrambleImage[2]["bg"],scrambleImage[5]["bg"],scrambleImage[8]["bg"],scrambleImage[18]["bg"],scrambleImage[30]["bg"],scrambleImage[42]["bg"],scrambleImage[47]["bg"],scrambleImage[50]["bg"],scrambleImage[53]["bg"] = scrambleImage[39]["bg"],scrambleImage[27]["bg"],scrambleImage[15]["bg"],scrambleImage[16]["bg"],scrambleImage[17]["bg"],scrambleImage[29]["bg"],scrambleImage[41]["bg"],scrambleImage[40]["bg"],scrambleImage[47]["bg"],scrambleImage[50]["bg"],scrambleImage[53]["bg"],scrambleImage[14]["bg"],scrambleImage[26]["bg"],scrambleImage[38]["bg"],scrambleImage[8]["bg"],scrambleImage[5]["bg"],scrambleImage[2]["bg"],scrambleImage[42]["bg"],scrambleImage[30]["bg"],scrambleImage[18]["bg"]
           scrambleImage[15]["bg"],scrambleImage[16]["bg"],scrambleImage[17]["bg"],scrambleImage[29]["bg"],scrambleImage[41]["bg"],scrambleImage[40]["bg"],scrambleImage[39]["bg"],scrambleImage[27]["bg"],scrambleImage[14]["bg"],scrambleImage[26]["bg"],scrambleImage[38]["bg"],scrambleImage[2]["bg"],scrambleImage[5]["bg"],scrambleImage[8]["bg"],scrambleImage[18]["bg"],scrambleImage[30]["bg"],scrambleImage[42]["bg"],scrambleImage[47]["bg"],scrambleImage[50]["bg"],scrambleImage[53]["bg"] = scrambleImage[39]["bg"],scrambleImage[27]["bg"],scrambleImage[15]["bg"],scrambleImage[16]["bg"],scrambleImage[17]["bg"],scrambleImage[29]["bg"],scrambleImage[41]["bg"],scrambleImage[40]["bg"],scrambleImage[47]["bg"],scrambleImage[50]["bg"],scrambleImage[53]["bg"],scrambleImage[14]["bg"],scrambleImage[26]["bg"],scrambleImage[38]["bg"],scrambleImage[8]["bg"],scrambleImage[5]["bg"],scrambleImage[2]["bg"],scrambleImage[42]["bg"],scrambleImage[30]["bg"],scrambleImage[18]["bg"]            
           continue
        
        if scrambleMoves == "R'":
           scrambleImage[39]["bg"],scrambleImage[27]["bg"],scrambleImage[15]["bg"],scrambleImage[16]["bg"],scrambleImage[17]["bg"],scrambleImage[29]["bg"],scrambleImage[41]["bg"],scrambleImage[40]["bg"],scrambleImage[47]["bg"],scrambleImage[50]["bg"],scrambleImage[53]["bg"],scrambleImage[14]["bg"],scrambleImage[26]["bg"],scrambleImage[38]["bg"],scrambleImage[8]["bg"],scrambleImage[5]["bg"],scrambleImage[2]["bg"],scrambleImage[42]["bg"],scrambleImage[30]["bg"],scrambleImage[18]["bg"] = scrambleImage[15]["bg"],scrambleImage[16]["bg"],scrambleImage[17]["bg"],scrambleImage[29]["bg"],scrambleImage[41]["bg"],scrambleImage[40]["bg"],scrambleImage[39]["bg"],scrambleImage[27]["bg"],scrambleImage[14]["bg"],scrambleImage[26]["bg"],scrambleImage[38]["bg"],scrambleImage[2]["bg"],scrambleImage[5]["bg"],scrambleImage[8]["bg"],scrambleImage[18]["bg"],scrambleImage[30]["bg"],scrambleImage[42]["bg"],scrambleImage[47]["bg"],scrambleImage[50]["bg"],scrambleImage[53]["bg"]            
           continue

        if scrambleMoves == "U":
           scrambleImage[9]["bg"],scrambleImage[0]["bg"],scrambleImage[20]["bg"],scrambleImage[10]["bg"],scrambleImage[3]["bg"],scrambleImage[6]["bg"],scrambleImage[11]["bg"],scrambleImage[12]["bg"],scrambleImage[7]["bg"],scrambleImage[13]["bg"],scrambleImage[8]["bg"],scrambleImage[14]["bg"],scrambleImage[15]["bg"],scrambleImage[5]["bg"],scrambleImage[16]["bg"],scrambleImage[2]["bg"],scrambleImage[17]["bg"],scrambleImage[18]["bg"],scrambleImage[1]["bg"],scrambleImage[19]["bg"] = scrambleImage[12]["bg"],scrambleImage[6]["bg"],scrambleImage[11]["bg"],scrambleImage[13]["bg"],scrambleImage[7]["bg"],scrambleImage[8]["bg"],scrambleImage[14]["bg"],scrambleImage[15]["bg"],scrambleImage[5]["bg"],scrambleImage[16]["bg"],scrambleImage[2]["bg"],scrambleImage[17]["bg"],scrambleImage[18]["bg"],scrambleImage[1]["bg"],scrambleImage[19]["bg"],scrambleImage[0]["bg"],scrambleImage[20]["bg"],scrambleImage[9]["bg"],scrambleImage[3]["bg"],scrambleImage[10]["bg"]
           continue
        
        if scrambleMoves == "U2":
           scrambleImage[9]["bg"],scrambleImage[0]["bg"],scrambleImage[20]["bg"],scrambleImage[10]["bg"],scrambleImage[3]["bg"],scrambleImage[6]["bg"],scrambleImage[11]["bg"],scrambleImage[12]["bg"],scrambleImage[7]["bg"],scrambleImage[13]["bg"],scrambleImage[8]["bg"],scrambleImage[14]["bg"],scrambleImage[15]["bg"],scrambleImage[5]["bg"],scrambleImage[16]["bg"],scrambleImage[2]["bg"],scrambleImage[17]["bg"],scrambleImage[18]["bg"],scrambleImage[1]["bg"],scrambleImage[19]["bg"] = scrambleImage[12]["bg"],scrambleImage[6]["bg"],scrambleImage[11]["bg"],scrambleImage[13]["bg"],scrambleImage[7]["bg"],scrambleImage[8]["bg"],scrambleImage[14]["bg"],scrambleImage[15]["bg"],scrambleImage[5]["bg"],scrambleImage[16]["bg"],scrambleImage[2]["bg"],scrambleImage[17]["bg"],scrambleImage[18]["bg"],scrambleImage[1]["bg"],scrambleImage[19]["bg"],scrambleImage[0]["bg"],scrambleImage[20]["bg"],scrambleImage[9]["bg"],scrambleImage[3]["bg"],scrambleImage[10]["bg"] 
           scrambleImage[9]["bg"],scrambleImage[0]["bg"],scrambleImage[20]["bg"],scrambleImage[10]["bg"],scrambleImage[3]["bg"],scrambleImage[6]["bg"],scrambleImage[11]["bg"],scrambleImage[12]["bg"],scrambleImage[7]["bg"],scrambleImage[13]["bg"],scrambleImage[8]["bg"],scrambleImage[14]["bg"],scrambleImage[15]["bg"],scrambleImage[5]["bg"],scrambleImage[16]["bg"],scrambleImage[2]["bg"],scrambleImage[17]["bg"],scrambleImage[18]["bg"],scrambleImage[1]["bg"],scrambleImage[19]["bg"] = scrambleImage[12]["bg"],scrambleImage[6]["bg"],scrambleImage[11]["bg"],scrambleImage[13]["bg"],scrambleImage[7]["bg"],scrambleImage[8]["bg"],scrambleImage[14]["bg"],scrambleImage[15]["bg"],scrambleImage[5]["bg"],scrambleImage[16]["bg"],scrambleImage[2]["bg"],scrambleImage[17]["bg"],scrambleImage[18]["bg"],scrambleImage[1]["bg"],scrambleImage[19]["bg"],scrambleImage[0]["bg"],scrambleImage[20]["bg"],scrambleImage[9]["bg"],scrambleImage[3]["bg"],scrambleImage[10]["bg"]             
           continue
        

        if scrambleMoves == "U'":
           scrambleImage[12]["bg"],scrambleImage[6]["bg"],scrambleImage[11]["bg"],scrambleImage[13]["bg"],scrambleImage[7]["bg"],scrambleImage[8]["bg"],scrambleImage[14]["bg"],scrambleImage[15]["bg"],scrambleImage[5]["bg"],scrambleImage[16]["bg"],scrambleImage[2]["bg"],scrambleImage[17]["bg"],scrambleImage[18]["bg"],scrambleImage[1]["bg"],scrambleImage[19]["bg"],scrambleImage[0]["bg"],scrambleImage[20]["bg"],scrambleImage[9]["bg"],scrambleImage[3]["bg"],scrambleImage[10]["bg"] = scrambleImage[9]["bg"],scrambleImage[0]["bg"],scrambleImage[20]["bg"],scrambleImage[10]["bg"],scrambleImage[3]["bg"],scrambleImage[6]["bg"],scrambleImage[11]["bg"],scrambleImage[12]["bg"],scrambleImage[7]["bg"],scrambleImage[13]["bg"],scrambleImage[8]["bg"],scrambleImage[14]["bg"],scrambleImage[15]["bg"],scrambleImage[5]["bg"],scrambleImage[16]["bg"],scrambleImage[2]["bg"],scrambleImage[17]["bg"],scrambleImage[18]["bg"],scrambleImage[1]["bg"],scrambleImage[19]["bg"]            
           continue
        
        if scrambleMoves == "F":
           scrambleImage[36]["bg"],scrambleImage[45]["bg"],scrambleImage[46]["bg"],scrambleImage[37]["bg"],scrambleImage[47]["bg"],scrambleImage[38]["bg"],scrambleImage[39]["bg"],scrambleImage[26]["bg"],scrambleImage[27]["bg"],scrambleImage[15]["bg"],scrambleImage[14]["bg"],scrambleImage[8]["bg"],scrambleImage[13]["bg"],scrambleImage[7]["bg"],scrambleImage[6]["bg"],scrambleImage[12]["bg"],scrambleImage[35]["bg"],scrambleImage[23]["bg"],scrambleImage[24]["bg"],scrambleImage[11]["bg"] = scrambleImage[38]["bg"],scrambleImage[39]["bg"],scrambleImage[27]["bg"],scrambleImage[26]["bg"],scrambleImage[15]["bg"],scrambleImage[14]["bg"],scrambleImage[8]["bg"],scrambleImage[13]["bg"],scrambleImage[7]["bg"],scrambleImage[6]["bg"],scrambleImage[12]["bg"],scrambleImage[11]["bg"],scrambleImage[24]["bg"],scrambleImage[23]["bg"],scrambleImage[35]["bg"],scrambleImage[36]["bg"],scrambleImage[47]["bg"],scrambleImage[46]["bg"],scrambleImage[37]["bg"],scrambleImage[45]["bg"]           
           continue
        
        if scrambleMoves == "F2":            
           scrambleImage[36]["bg"],scrambleImage[45]["bg"],scrambleImage[46]["bg"],scrambleImage[37]["bg"],scrambleImage[47]["bg"],scrambleImage[38]["bg"],scrambleImage[39]["bg"],scrambleImage[26]["bg"],scrambleImage[27]["bg"],scrambleImage[15]["bg"],scrambleImage[14]["bg"],scrambleImage[8]["bg"],scrambleImage[13]["bg"],scrambleImage[7]["bg"],scrambleImage[6]["bg"],scrambleImage[12]["bg"],scrambleImage[35]["bg"],scrambleImage[23]["bg"],scrambleImage[24]["bg"],scrambleImage[11]["bg"] = scrambleImage[38]["bg"],scrambleImage[39]["bg"],scrambleImage[27]["bg"],scrambleImage[26]["bg"],scrambleImage[15]["bg"],scrambleImage[14]["bg"],scrambleImage[8]["bg"],scrambleImage[13]["bg"],scrambleImage[7]["bg"],scrambleImage[6]["bg"],scrambleImage[12]["bg"],scrambleImage[11]["bg"],scrambleImage[24]["bg"],scrambleImage[23]["bg"],scrambleImage[35]["bg"],scrambleImage[36]["bg"],scrambleImage[47]["bg"],scrambleImage[46]["bg"],scrambleImage[37]["bg"],scrambleImage[45]["bg"]
           scrambleImage[36]["bg"],scrambleImage[45]["bg"],scrambleImage[46]["bg"],scrambleImage[37]["bg"],scrambleImage[47]["bg"],scrambleImage[38]["bg"],scrambleImage[39]["bg"],scrambleImage[26]["bg"],scrambleImage[27]["bg"],scrambleImage[15]["bg"],scrambleImage[14]["bg"],scrambleImage[8]["bg"],scrambleImage[13]["bg"],scrambleImage[7]["bg"],scrambleImage[6]["bg"],scrambleImage[12]["bg"],scrambleImage[35]["bg"],scrambleImage[23]["bg"],scrambleImage[24]["bg"],scrambleImage[11]["bg"] = scrambleImage[38]["bg"],scrambleImage[39]["bg"],scrambleImage[27]["bg"],scrambleImage[26]["bg"],scrambleImage[15]["bg"],scrambleImage[14]["bg"],scrambleImage[8]["bg"],scrambleImage[13]["bg"],scrambleImage[7]["bg"],scrambleImage[6]["bg"],scrambleImage[12]["bg"],scrambleImage[11]["bg"],scrambleImage[24]["bg"],scrambleImage[23]["bg"],scrambleImage[35]["bg"],scrambleImage[36]["bg"],scrambleImage[47]["bg"],scrambleImage[46]["bg"],scrambleImage[37]["bg"],scrambleImage[45]["bg"]            
           continue

        if scrambleMoves == "F'":
           scrambleImage[38]["bg"],scrambleImage[39]["bg"],scrambleImage[27]["bg"],scrambleImage[26]["bg"],scrambleImage[15]["bg"],scrambleImage[14]["bg"],scrambleImage[8]["bg"],scrambleImage[13]["bg"],scrambleImage[7]["bg"],scrambleImage[6]["bg"],scrambleImage[12]["bg"],scrambleImage[11]["bg"],scrambleImage[24]["bg"],scrambleImage[23]["bg"],scrambleImage[35]["bg"],scrambleImage[36]["bg"],scrambleImage[47]["bg"],scrambleImage[46]["bg"],scrambleImage[37]["bg"],scrambleImage[45]["bg"] = scrambleImage[36]["bg"],scrambleImage[45]["bg"],scrambleImage[46]["bg"],scrambleImage[37]["bg"],scrambleImage[47]["bg"],scrambleImage[38]["bg"],scrambleImage[39]["bg"],scrambleImage[26]["bg"],scrambleImage[27]["bg"],scrambleImage[15]["bg"],scrambleImage[14]["bg"],scrambleImage[8]["bg"],scrambleImage[13]["bg"],scrambleImage[7]["bg"],scrambleImage[6]["bg"],scrambleImage[12]["bg"],scrambleImage[35]["bg"],scrambleImage[23]["bg"],scrambleImage[24]["bg"],scrambleImage[11]["bg"]            
           continue

        if scrambleMoves == "B'":
           scrambleImage[18]["bg"],scrambleImage[30]["bg"],scrambleImage[42]["bg"],scrambleImage[19]["bg"],scrambleImage[20]["bg"],scrambleImage[32]["bg"],scrambleImage[44]["bg"],scrambleImage[43]["bg"],scrambleImage[41]["bg"],scrambleImage[29]["bg"],scrambleImage[17]["bg"],scrambleImage[2]["bg"],scrambleImage[1]["bg"],scrambleImage[0]["bg"],scrambleImage[9]["bg"],scrambleImage[21]["bg"],scrambleImage[33]["bg"],scrambleImage[51]["bg"],scrambleImage[52]["bg"],scrambleImage[53]["bg"] = scrambleImage[20]["bg"],scrambleImage[19]["bg"],scrambleImage[18]["bg"],scrambleImage[32]["bg"],scrambleImage[44]["bg"],scrambleImage[43]["bg"],scrambleImage[42]["bg"],scrambleImage[30]["bg"],scrambleImage[2]["bg"],scrambleImage[1]["bg"],scrambleImage[0]["bg"],scrambleImage[9]["bg"],scrambleImage[21]["bg"],scrambleImage[33]["bg"],scrambleImage[51]["bg"],scrambleImage[52]["bg"],scrambleImage[53]["bg"],scrambleImage[41]["bg"],scrambleImage[29]["bg"],scrambleImage[17]["bg"]             
           continue
        
        if scrambleMoves == "B":
           scrambleImage[20]["bg"],scrambleImage[19]["bg"],scrambleImage[18]["bg"],scrambleImage[32]["bg"],scrambleImage[44]["bg"],scrambleImage[43]["bg"],scrambleImage[42]["bg"],scrambleImage[30]["bg"],scrambleImage[2]["bg"],scrambleImage[1]["bg"],scrambleImage[0]["bg"],scrambleImage[9]["bg"],scrambleImage[21]["bg"],scrambleImage[33]["bg"],scrambleImage[51]["bg"],scrambleImage[52]["bg"],scrambleImage[53]["bg"],scrambleImage[41]["bg"],scrambleImage[29]["bg"],scrambleImage[17]["bg"] = scrambleImage[18]["bg"],scrambleImage[30]["bg"],scrambleImage[42]["bg"],scrambleImage[19]["bg"],scrambleImage[20]["bg"],scrambleImage[32]["bg"],scrambleImage[44]["bg"],scrambleImage[43]["bg"],scrambleImage[41]["bg"],scrambleImage[29]["bg"],scrambleImage[17]["bg"],scrambleImage[2]["bg"],scrambleImage[1]["bg"],scrambleImage[0]["bg"],scrambleImage[9]["bg"],scrambleImage[21]["bg"],scrambleImage[33]["bg"],scrambleImage[51]["bg"],scrambleImage[52]["bg"],scrambleImage[53]["bg"]            
           continue
        
        if scrambleMoves == "B2":
           scrambleImage[20]["bg"],scrambleImage[19]["bg"],scrambleImage[18]["bg"],scrambleImage[32]["bg"],scrambleImage[44]["bg"],scrambleImage[43]["bg"],scrambleImage[42]["bg"],scrambleImage[30]["bg"],scrambleImage[2]["bg"],scrambleImage[1]["bg"],scrambleImage[0]["bg"],scrambleImage[9]["bg"],scrambleImage[21]["bg"],scrambleImage[33]["bg"],scrambleImage[51]["bg"],scrambleImage[52]["bg"],scrambleImage[53]["bg"],scrambleImage[41]["bg"],scrambleImage[29]["bg"],scrambleImage[17]["bg"] = scrambleImage[18]["bg"],scrambleImage[30]["bg"],scrambleImage[42]["bg"],scrambleImage[19]["bg"],scrambleImage[20]["bg"],scrambleImage[32]["bg"],scrambleImage[44]["bg"],scrambleImage[43]["bg"],scrambleImage[41]["bg"],scrambleImage[29]["bg"],scrambleImage[17]["bg"],scrambleImage[2]["bg"],scrambleImage[1]["bg"],scrambleImage[0]["bg"],scrambleImage[9]["bg"],scrambleImage[21]["bg"],scrambleImage[33]["bg"],scrambleImage[51]["bg"],scrambleImage[52]["bg"],scrambleImage[53]["bg"]
           scrambleImage[20]["bg"],scrambleImage[19]["bg"],scrambleImage[18]["bg"],scrambleImage[32]["bg"],scrambleImage[44]["bg"],scrambleImage[43]["bg"],scrambleImage[42]["bg"],scrambleImage[30]["bg"],scrambleImage[2]["bg"],scrambleImage[1]["bg"],scrambleImage[0]["bg"],scrambleImage[9]["bg"],scrambleImage[21]["bg"],scrambleImage[33]["bg"],scrambleImage[51]["bg"],scrambleImage[52]["bg"],scrambleImage[53]["bg"],scrambleImage[41]["bg"],scrambleImage[29]["bg"],scrambleImage[17]["bg"] = scrambleImage[18]["bg"],scrambleImage[30]["bg"],scrambleImage[42]["bg"],scrambleImage[19]["bg"],scrambleImage[20]["bg"],scrambleImage[32]["bg"],scrambleImage[44]["bg"],scrambleImage[43]["bg"],scrambleImage[41]["bg"],scrambleImage[29]["bg"],scrambleImage[17]["bg"],scrambleImage[2]["bg"],scrambleImage[1]["bg"],scrambleImage[0]["bg"],scrambleImage[9]["bg"],scrambleImage[21]["bg"],scrambleImage[33]["bg"],scrambleImage[51]["bg"],scrambleImage[52]["bg"],scrambleImage[53]["bg"]            
           continue         

        if scrambleMoves == "D":
           scrambleImage[47]["bg"],scrambleImage[46]["bg"],scrambleImage[47]["bg"],scrambleImage[50]["bg"],scrambleImage[53]["bg"],scrambleImage[52]["bg"],scrambleImage[51]["bg"],scrambleImage[48]["bg"],scrambleImage[45]["bg"],scrambleImage[36]["bg"],scrambleImage[37]["bg"],scrambleImage[38]["bg"],scrambleImage[39]["bg"],scrambleImage[40]["bg"],scrambleImage[41]["bg"],scrambleImage[33]["bg"],scrambleImage[34]["bg"],scrambleImage[35]["bg"],scrambleImage[42]["bg"],scrambleImage[43]["bg"],scrambleImage[44]["bg"] = scrambleImage[45]["bg"],scrambleImage[48]["bg"],scrambleImage[45]["bg"],scrambleImage[46]["bg"],scrambleImage[47]["bg"],scrambleImage[50]["bg"],scrambleImage[53]["bg"],scrambleImage[52]["bg"],scrambleImage[51]["bg"],scrambleImage[33]["bg"],scrambleImage[34]["bg"],scrambleImage[35]["bg"],scrambleImage[36]["bg"],scrambleImage[37]["bg"],scrambleImage[38]["bg"],scrambleImage[42]["bg"],scrambleImage[43]["bg"],scrambleImage[44]["bg"],scrambleImage[39]["bg"],scrambleImage[40]["bg"],scrambleImage[41]["bg"]            
           continue
        
        if scrambleMoves == "D'":
           scrambleImage[45]["bg"],scrambleImage[48]["bg"],scrambleImage[45]["bg"],scrambleImage[46]["bg"],scrambleImage[47]["bg"],scrambleImage[50]["bg"],scrambleImage[53]["bg"],scrambleImage[52]["bg"],scrambleImage[51]["bg"],scrambleImage[33]["bg"],scrambleImage[34]["bg"],scrambleImage[35]["bg"],scrambleImage[36]["bg"],scrambleImage[37]["bg"],scrambleImage[38]["bg"],scrambleImage[42]["bg"],scrambleImage[43]["bg"],scrambleImage[44]["bg"],scrambleImage[39]["bg"],scrambleImage[40]["bg"],scrambleImage[41]["bg"] = scrambleImage[47]["bg"],scrambleImage[46]["bg"],scrambleImage[47]["bg"],scrambleImage[50]["bg"],scrambleImage[53]["bg"],scrambleImage[52]["bg"],scrambleImage[51]["bg"],scrambleImage[48]["bg"],scrambleImage[45]["bg"],scrambleImage[36]["bg"],scrambleImage[37]["bg"],scrambleImage[38]["bg"],scrambleImage[39]["bg"],scrambleImage[40]["bg"],scrambleImage[41]["bg"],scrambleImage[33]["bg"],scrambleImage[34]["bg"],scrambleImage[35]["bg"],scrambleImage[42]["bg"],scrambleImage[43]["bg"],scrambleImage[44]["bg"]            
           continue
        
        if scrambleMoves == "D2":
           scrambleImage[47]["bg"],scrambleImage[46]["bg"],scrambleImage[47]["bg"],scrambleImage[50]["bg"],scrambleImage[53]["bg"],scrambleImage[52]["bg"],scrambleImage[51]["bg"],scrambleImage[48]["bg"],scrambleImage[45]["bg"],scrambleImage[36]["bg"],scrambleImage[37]["bg"],scrambleImage[38]["bg"],scrambleImage[39]["bg"],scrambleImage[40]["bg"],scrambleImage[41]["bg"],scrambleImage[33]["bg"],scrambleImage[34]["bg"],scrambleImage[35]["bg"],scrambleImage[42]["bg"],scrambleImage[43]["bg"],scrambleImage[44]["bg"] = scrambleImage[45]["bg"],scrambleImage[48]["bg"],scrambleImage[45]["bg"],scrambleImage[46]["bg"],scrambleImage[47]["bg"],scrambleImage[50]["bg"],scrambleImage[53]["bg"],scrambleImage[52]["bg"],scrambleImage[51]["bg"],scrambleImage[33]["bg"],scrambleImage[34]["bg"],scrambleImage[35]["bg"],scrambleImage[36]["bg"],scrambleImage[37]["bg"],scrambleImage[38]["bg"],scrambleImage[42]["bg"],scrambleImage[43]["bg"],scrambleImage[44]["bg"],scrambleImage[39]["bg"],scrambleImage[40]["bg"],scrambleImage[41]["bg"]
           scrambleImage[47]["bg"],scrambleImage[46]["bg"],scrambleImage[47]["bg"],scrambleImage[50]["bg"],scrambleImage[53]["bg"],scrambleImage[52]["bg"],scrambleImage[51]["bg"],scrambleImage[48]["bg"],scrambleImage[45]["bg"],scrambleImage[36]["bg"],scrambleImage[37]["bg"],scrambleImage[38]["bg"],scrambleImage[39]["bg"],scrambleImage[40]["bg"],scrambleImage[41]["bg"],scrambleImage[33]["bg"],scrambleImage[34]["bg"],scrambleImage[35]["bg"],scrambleImage[42]["bg"],scrambleImage[43]["bg"],scrambleImage[44]["bg"] = scrambleImage[45]["bg"],scrambleImage[48]["bg"],scrambleImage[45]["bg"],scrambleImage[46]["bg"],scrambleImage[47]["bg"],scrambleImage[50]["bg"],scrambleImage[53]["bg"],scrambleImage[52]["bg"],scrambleImage[51]["bg"],scrambleImage[33]["bg"],scrambleImage[34]["bg"],scrambleImage[35]["bg"],scrambleImage[36]["bg"],scrambleImage[37]["bg"],scrambleImage[38]["bg"],scrambleImage[42]["bg"],scrambleImage[43]["bg"],scrambleImage[44]["bg"],scrambleImage[39]["bg"],scrambleImage[40]["bg"],scrambleImage[41]["bg"]            
           continue 

        if scrambleMoves == "L":
           scrambleImage[9]["bg"],scrambleImage[10]["bg"],scrambleImage[11]["bg"],scrambleImage[23]["bg"],scrambleImage[35]["bg"],scrambleImage[34]["bg"],scrambleImage[33]["bg"],scrambleImage[21]["bg"],scrambleImage[12]["bg"],scrambleImage[24]["bg"],scrambleImage[36]["bg"],scrambleImage[6]["bg"],scrambleImage[3]["bg"],scrambleImage[0]["bg"],scrambleImage[44]["bg"],scrambleImage[32]["bg"],scrambleImage[20]["bg"],scrambleImage[45]["bg"],scrambleImage[48]["bg"],scrambleImage[51]["bg"] = scrambleImage[33]["bg"],scrambleImage[21]["bg"],scrambleImage[9]["bg"],scrambleImage[10]["bg"],scrambleImage[11]["bg"],scrambleImage[23]["bg"],scrambleImage[35]["bg"],scrambleImage[34]["bg"],scrambleImage[0]["bg"],scrambleImage[3]["bg"],scrambleImage[6]["bg"],scrambleImage[20]["bg"],scrambleImage[32]["bg"],scrambleImage[44]["bg"],scrambleImage[45]["bg"],scrambleImage[48]["bg"],scrambleImage[51]["bg"],scrambleImage[12]["bg"],scrambleImage[24]["bg"],scrambleImage[36]["bg"]            
           continue

        if scrambleMoves == "L'":
           scrambleImage[33]["bg"],scrambleImage[21]["bg"],scrambleImage[9]["bg"],scrambleImage[10]["bg"],scrambleImage[11]["bg"],scrambleImage[23]["bg"],scrambleImage[35]["bg"],scrambleImage[34]["bg"],scrambleImage[0]["bg"],scrambleImage[3]["bg"],scrambleImage[6]["bg"],scrambleImage[20]["bg"],scrambleImage[32]["bg"],scrambleImage[44]["bg"],scrambleImage[45]["bg"],scrambleImage[48]["bg"],scrambleImage[51]["bg"],scrambleImage[12]["bg"],scrambleImage[24]["bg"],scrambleImage[36]["bg"] = scrambleImage[9]["bg"],scrambleImage[10]["bg"],scrambleImage[11]["bg"],scrambleImage[23]["bg"],scrambleImage[35]["bg"],scrambleImage[34]["bg"],scrambleImage[33]["bg"],scrambleImage[21]["bg"],scrambleImage[12]["bg"],scrambleImage[24]["bg"],scrambleImage[36]["bg"],scrambleImage[6]["bg"],scrambleImage[3]["bg"],scrambleImage[0]["bg"],scrambleImage[44]["bg"],scrambleImage[32]["bg"],scrambleImage[20]["bg"],scrambleImage[45]["bg"],scrambleImage[48]["bg"],scrambleImage[51]["bg"]           
           continue
                 
        if scrambleMoves == "L2":
           scrambleImage[9]["bg"],scrambleImage[10]["bg"],scrambleImage[11]["bg"],scrambleImage[23]["bg"],scrambleImage[35]["bg"],scrambleImage[34]["bg"],scrambleImage[33]["bg"],scrambleImage[21]["bg"],scrambleImage[12]["bg"],scrambleImage[24]["bg"],scrambleImage[36]["bg"],scrambleImage[6]["bg"],scrambleImage[3]["bg"],scrambleImage[0]["bg"],scrambleImage[44]["bg"],scrambleImage[32]["bg"],scrambleImage[20]["bg"],scrambleImage[45]["bg"],scrambleImage[48]["bg"],scrambleImage[51]["bg"] = scrambleImage[33]["bg"],scrambleImage[21]["bg"],scrambleImage[9]["bg"],scrambleImage[10]["bg"],scrambleImage[11]["bg"],scrambleImage[23]["bg"],scrambleImage[35]["bg"],scrambleImage[34]["bg"],scrambleImage[0]["bg"],scrambleImage[3]["bg"],scrambleImage[6]["bg"],scrambleImage[20]["bg"],scrambleImage[32]["bg"],scrambleImage[44]["bg"],scrambleImage[45]["bg"],scrambleImage[48]["bg"],scrambleImage[51]["bg"],scrambleImage[12]["bg"],scrambleImage[24]["bg"],scrambleImage[36]["bg"]
           scrambleImage[9]["bg"],scrambleImage[10]["bg"],scrambleImage[11]["bg"],scrambleImage[23]["bg"],scrambleImage[35]["bg"],scrambleImage[34]["bg"],scrambleImage[33]["bg"],scrambleImage[21]["bg"],scrambleImage[12]["bg"],scrambleImage[24]["bg"],scrambleImage[36]["bg"],scrambleImage[6]["bg"],scrambleImage[3]["bg"],scrambleImage[0]["bg"],scrambleImage[44]["bg"],scrambleImage[32]["bg"],scrambleImage[20]["bg"],scrambleImage[45]["bg"],scrambleImage[48]["bg"],scrambleImage[51]["bg"] = scrambleImage[33]["bg"],scrambleImage[21]["bg"],scrambleImage[9]["bg"],scrambleImage[10]["bg"],scrambleImage[11]["bg"],scrambleImage[23]["bg"],scrambleImage[35]["bg"],scrambleImage[34]["bg"],scrambleImage[0]["bg"],scrambleImage[3]["bg"],scrambleImage[6]["bg"],scrambleImage[20]["bg"],scrambleImage[32]["bg"],scrambleImage[44]["bg"],scrambleImage[45]["bg"],scrambleImage[48]["bg"],scrambleImage[51]["bg"],scrambleImage[12]["bg"],scrambleImage[24]["bg"],scrambleImage[36]["bg"]            
           continue            
scrambleImage_()



myAllsolves = []
Ao5Solves = []
Ao12Solves = []
Ao50Solves = []
Ao100Solves = []




def __calAo5__():
    global Ao5Solves
    Ao5Solves = [float(i) for i in Ao5Solves]
    Ao5Solves.pop(Ao5Solves.index(min(Ao5Solves)))
    Ao5Solves.pop(Ao5Solves.index(max(Ao5Solves)))
    equal = sum(Ao5Solves)
    divide = equal/3
    final = "%.2f"%divide
    return final


def __calAo12__():
    global Ao12Solves
    Ao12Solves = [float(i) for i in Ao12Solves]
    Ao12Solves.pop(Ao12Solves.index(min(Ao12Solves)))
    Ao12Solves.pop(Ao12Solves.index(max(Ao12Solves)))
    equal = sum(Ao12Solves)
    divide = equal/10
    final = "%.2f"%divide
    return final

def __calAo50__():
    global Ao50Solves
    Ao50Solves = [float(i) for i in Ao50Solves]
    Ao50Solves.pop(Ao50Solves.index(min(Ao50Solves)))
    Ao50Solves.pop(Ao50Solves.index(max(Ao50Solves)))
    equal = sum(Ao50Solves)
    divide = equal/48
    final = "%.2f"%divide
    return final

def __calAo100__():
    global Ao100Solves
    Ao100Solves = [float(i) for i in Ao100Solves]
    Ao100Solves.pop(Ao100Solves.index(min(Ao100Solves)))
    Ao100Solves.pop(Ao100Solves.index(max(Ao100Solves)))
    equal = sum(Ao100Solves)
    divide = equal/98
    final = "%.2f"%divide
    return final

### Load All of my Solves
with open("vcTimes.dll","r") as allsolvesFiles1:
    SavedSolves = allsolvesFiles1.read()
    
    

with open("vcTimes.dll","w") as allsolvesFiles2:
    allsolvesFiles2.write(SavedSolves)
    

with open("vcTimes.dll","r") as allsolvesFiles3:
    SavedSolves = allsolvesFiles3.read()
    split1 = SavedSolves.split()
    myAllsolves = split1
    
###

### Load Ao5
with open("af.dll","r") as ao5Files1:
    SavedAo5Solves = ao5Files1.read()
    
    

with open("af.dll","w") as ao5Files2:
    ao5Files2.write(SavedAo5Solves)
    

with open("af.dll","r") as ao5Files3:
    SavedAo5Solves = ao5Files3.read()
    split2 = SavedAo5Solves.split()
    Ao5Solves = split2
    
###   

### Load Ao12
with open("at.dll","r") as ao12Files1:
    SavedAo12Solves = ao12Files1.read()
    

with open("at.dll","w") as ao12Files2:
    ao12Files2.write(SavedAo12Solves)
    

with open("at.dll","r") as ao12Files3:
    SavedAo12Solves = ao12Files3.read()
    split3 = SavedAo12Solves.split()
    Ao12Solves = split3
    
###

### Load Ao50
with open("aft.dll","r") as ao50Files1:
    SavedAo50Solves = ao50Files1.read()
    

with open("aft.dll","w") as ao50Files2:
    ao50Files2.write(SavedAo50Solves)
    

with open("aft.dll","r") as ao50Files3:
    SavedAo50Solves = ao50Files3.read()
    split4 = SavedAo50Solves.split()
    Ao50Solves = split4
    
###

### Load Ao100
with open("ao.dll","r") as ao100Files1:
    SavedAo100Solves = ao100Files1.read()
    

with open("ao.dll","w") as ao100Files2:
    ao100Files2.write(SavedAo100Solves)
    

with open("ao.dll","r") as ao100Files3:
    SavedAo100Solves = ao100Files3.read()
    split5 = SavedAo100Solves.split()
    Ao100Solves = split5
    
###
callData = _datas.execute("SELECT __ao5,__ao12,__ao50,__ao100,upColor,DownColor,leftColor,rightColor,backColor,faceColor,best,worst from _users")
LoadData = _datas.fetchone()

Ao5Text.config(text=(f"Ao5: {LoadData[0]}")) 
Ao12Text.config(text=(f"Ao12: {LoadData[1]}")) 
Ao50Text.config(text=(f"Ao50: {LoadData[2]}")) 
Ao100Text.config(text=(f"Ao100: {LoadData[3]}")) 

bestText.config(text=(f"Best: {LoadData[10]}")) 
worstText.config(text=(f"Worst: {LoadData[11]}"))
RefresherIgnore = tk.Label()
def Refresher():
    global Ao5Solves,Ao12Solves,Ao50Solves,Ao100Solves,ao5Files,Ao5Text

    datas = _datas.execute("SELECT __ao5,__ao12,__ao50,__ao100,upColor,DownColor,leftColor,rightColor,backColor,faceColor,best,worst from _users")
    #print(_datas.fetchone())


    
    

    if len(Ao5Solves) == 5:
        a = __calAo5__()
        Ao5Text.config(text=(f"Ao5: {a}"))
        _datas.execute(f"UPDATE _users SET __ao5 = {a} ")

    if len(Ao12Solves) == 12:
        a = __calAo12__()
        Ao12Text.config(text=(f"Ao12: {a}"))
        _datas.execute(f"UPDATE _users SET __ao12 = {a} ")

    if len(Ao50Solves) == 50:
        a = __calAo50__()
        Ao50Text.config(text=(f"Ao50: {a}"))
        _datas.execute(f"UPDATE _users SET __ao50 = {a} ")

    if len(Ao100Solves) == 100:
        a = __calAo100__()
        Ao100Text.config(text=(f"Ao100: {a}"))
        _datas.execute(f"UPDATE _users SET __ao100 = {a} ")
        
    
    Ao5Solves = [str(i) for i in Ao5Solves]
    Ao12Solves = [str(i) for i in Ao12Solves]
    Ao50Solves = [str(i) for i in Ao50Solves]
    Ao100Solves = [str(i) for i in Ao100Solves]

    with open("af.dll","w") as ao5Files4:
        for i in Ao5Solves:            
            ao5Files4.write(i + " ")

    with open("at.dll","w") as ao12Files4:
        for i in Ao12Solves:            
            ao12Files4.write(i + " ")

    with open("aft.dll","w") as ao50Files4:
        for i in Ao50Solves:            
            ao50Files4.write(i + " ")

    with open("ao.dll","w") as ao100Files4:
        for i in Ao100Solves:            
            ao100Files4.write(i + " ")

    with open("vcTimes.dll","w") as myAllsolvesFiles:
        for i in myAllsolves:            
            myAllsolvesFiles.write(i + " ")
    if len(myAllsolves) != 0:
        _datas.execute(f"UPDATE _users SET best = '{min(myAllsolves)}',worst = '{max(myAllsolves)}'")
        bestText.config(text=(f"Best: {min(myAllsolves)}")) 
        worstText.config(text=(f"Worst: {max(myAllsolves)}"))

    numberOfSolvesText.config(text=(f"Solves in Total: {len(myAllsolves)}"))
    conn.commit()
    RefresherIgnore.after(100,Refresher)


Refresher()
def backToDefaults():
    scrambleText.place(relx=0,rely=0.0)
    time.place(relx=-0.005,rely=0.057)
    Ao5Text.place(relx=0,rely=0.2)
    Ao12Text.place(relx=0,rely=0.28)
    Ao50Text.place(relx=0,rely=0.36)
    Ao100Text.place(relx=0,rely=0.44)
    bestText.place(relx=0.3,rely=0.65)
    worstText.place(relx=0.5,rely=0.65)
    numberOfSolvesText.place(relx=0,rely=0.65)

class main(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.__MainPage__() 

    def __MainPage__(self):
        global scrambleText,time,output,scrambleImage,Ao5Text,Ao12Text,Ao50Text,Ao100Text
        scrambleText.config(text=output)
        backToDefaults()
        for i in scrambleImage:
            scrambleImage[0].place_configure(relx=0.70,rely=0.208)
            scrambleImage[1].place_configure(relx=0.729,rely=0.208)
            scrambleImage[2].place_configure(relx=0.7579,rely=0.208)
            scrambleImage[3].place_configure(relx=0.70,rely=0.250)
            scrambleImage[4].place_configure(relx=0.729,rely=0.250)
            scrambleImage[5].place_configure(relx=0.7579,rely=0.250)
            scrambleImage[6].place_configure(relx=0.70,rely=0.292)
            scrambleImage[7].place_configure(relx=0.729,rely=0.292)
            scrambleImage[8].place_configure(relx=0.7579,rely=0.292)
            scrambleImage[9].place_configure(relx=0.6129,rely=0.335)
            scrambleImage[10].place_configure(relx=0.6419,rely=0.335)
            scrambleImage[11].place_configure(relx=0.670,rely=0.335)
            scrambleImage[21].place_configure(relx=0.6129,rely=0.379)
            scrambleImage[22].place_configure(relx=0.6419,rely=0.379)
            scrambleImage[23].place_configure(relx=0.670,rely=0.379)
            scrambleImage[33].place_configure(relx=0.6129,rely=0.422)
            scrambleImage[34].place_configure(relx=0.6419,rely=0.422)
            scrambleImage[35].place_configure(relx=0.670,rely=0.422)
            scrambleImage[12].place_configure(relx=0.6989,rely=0.335)
            scrambleImage[13].place_configure(relx=0.7279,rely=0.335)
            scrambleImage[14].place_configure(relx=0.7570,rely=0.335)
            scrambleImage[24].place_configure(relx=0.6989,rely=0.379)
            scrambleImage[25].place_configure(relx=0.7279,rely=0.379)
            scrambleImage[26].place_configure(relx=0.7570,rely=0.379)
            scrambleImage[36].place_configure(relx=0.6989,rely=0.422)
            scrambleImage[37].place_configure(relx=0.7279,rely=0.422)
            scrambleImage[38].place_configure(relx=0.7570,rely=0.422)
            scrambleImage[15].place_configure(relx=0.786,rely=0.335)
            scrambleImage[16].place_configure(relx=0.815,rely=0.335)
            scrambleImage[17].place_configure(relx=0.8439,rely=0.335)
            scrambleImage[27].place_configure(relx=0.786,rely=0.379)
            scrambleImage[28].place_configure(relx=0.815,rely=0.379)
            scrambleImage[29].place_configure(relx=0.8439,rely=0.379)
            scrambleImage[39].place_configure(relx=0.786,rely=0.422)
            scrambleImage[40].place_configure(relx=0.815,rely=0.422)
            scrambleImage[41].place_configure(relx=0.8439,rely=0.422)
            scrambleImage[18].place_configure(relx=0.8739,rely=0.335)
            scrambleImage[19].place_configure(relx=0.9027,rely=0.335)
            scrambleImage[20].place_configure(relx=0.9315,rely=0.335)
            scrambleImage[30].place_configure(relx=0.8739,rely=0.379)
            scrambleImage[31].place_configure(relx=0.9027,rely=0.379)
            scrambleImage[32].place_configure(relx=0.9315,rely=0.379)
            scrambleImage[42].place_configure(relx=0.8739,rely=0.422)
            scrambleImage[43].place_configure(relx=0.9027,rely=0.422)
            scrambleImage[44].place_configure(relx=0.9315,rely=0.422)
            scrambleImage[45].place_configure(relx=0.6995,rely=0.466)
            scrambleImage[46].place_configure(relx=0.7282,rely=0.466)
            scrambleImage[47].place_configure(relx=0.7570,rely=0.466)
            scrambleImage[48].place_configure(relx=0.6995,rely=0.509)
            scrambleImage[49].place_configure(relx=0.7282,rely=0.509)
            scrambleImage[50].place_configure(relx=0.7570,rely=0.509)
            scrambleImage[51].place_configure(relx=0.6995,rely=0.552)
            scrambleImage[52].place_configure(relx=0.7282,rely=0.552)
            scrambleImage[53].place_configure(relx=0.7570,rely=0.552)
    def __KeyPress__(event):
        global time,scrambleText,isTimeStarted,isInspection,myTime,scrambleImage
        toForget = [scrambleText,Ao5Text,Ao12Text,Ao50Text,Ao100Text,numberOfSolvesText,bestText,worstText]
        if isTimeStarted == False:
            if  isInspection == False:
                for i in scrambleImage:
                    i.place_forget()
                for i in toForget:
                    i.place_forget()
                time.config(fg="blue")
            elif isInspection:
                pass

        elif isTimeStarted == True:
            if  isInspection == False:
                
                time.config(fg="red")
            elif isInspection:
                pass
    def __KeyRelease__(event):
        global time,scrambleText,isTimeStarted,cnt,output,prev,myTime,Ao5Solves,Ao12Solves,Ao50Solves,Ao100Solves,Ao5Text,Ao12Text,Ao50Text,Ao100Text

        toForget = [scrambleText,Ao5Text,Ao12Text,Ao50Text,Ao100Text,numberOfSolvesText,bestText,worstText]
        if not isTimeStarted:
            for i in toForget:
                i.place_forget()
            time.config(fg="white")
            isTimeStarted = True
            myTime = 0
            __StartTime__()
        elif isTimeStarted:
            myTime = "%.2f"%myTime
            myAllsolves.append(myTime)
            Ao5Solves.append(myTime)
            Ao12Solves.append(myTime)
            Ao50Solves.append(myTime)
            Ao100Solves.append(myTime)     
            cnt = 0
            prev = "ZZ"
            output.clear()
            scramble()
            scrambleImage_()
            isTimeStarted = False
            time.config(text=myTime,fg="white")
            scrambleText.config(text=scramble())
            backToDefaults()
app = main()
if __name__ == '__main__':
    app.master.title("Rubik's Cube Timer")
    app.master.config(bg="gray")
    app.master.geometry("1250x900")
    app.master.maxsize(1250,900)
    app.master.bind("<space>",main.__KeyPress__)
    app.master.bind("<KeyRelease-space>",main.__KeyRelease__)
    app.mainloop()
