from tkinter import* 
root=Tk()
root.geometry("560x550")
root.resizable(0,0)

x=1
def show(b):
		global x
		x=x+1
		if(x%2==0):
			if(b["text"]==""):
				b["fg"]="white"
				b["bg"]="black"
				b["width"]=10
				b["height"]=5
				b["text"]="0"
		elif(x%2==1):
			if(b["text"]==""):
				b["fg"]="white"
				b["bg"]="red"
				b["width"]=10
				b["height"]=5
				b["text"]="x"
		
		if(b1["text"]=="0" and b2["text"]=="0" and b3["text"]=="0"):
			print("Player 1 is Winner!!")
		
		else(b1["text"]=="x" and b2["text"]=="x" and b3["text"]=="x"):
			print("Player 2 is Winner!!")
		
		
b1=Button(root,text="",width=10,height=5,font=("Arial",20),command=lambda:show(b1))
b1.grid(row=0,column=0)

b2=Button(root,text="",width=10,height=5,font=("Arial",20),command=lambda:show(b2))
b2.grid(row=0,column=1)

b3=Button(root,text="",width=10,height=5,font=("Arial",20),command=lambda:show(b3))
b3.grid(row=0,column=2)

b4=Button(root,text="",width=10,height=5,font=("Arial",20),command=lambda:show(b4))
b4.grid(row=1,column=0)

b5=Button(root,text="",width=10,height=5,font=("Arial",20),command=lambda:show(b5))
b5.grid(row=1,column=1)

b6=Button(root,text="",width=10,height=5,font=("Arial",20),command=lambda:show(b6))
b6.grid(row=1,column=2)

b7=Button(root,text="",width=10,height=5,font=("Arial",20),command=lambda:show(b7))
b7.grid(row=2,column=0)

b8=Button(root,text="",width=10,height=5,font=("Arial",20),command=lambda:show(b8))
b8.grid(row=2,column=1)

b9=Button(root,text="",width=10,height=5,font=("Arial",20),command=lambda:show(b9))
b9.grid(row=2,column=2)

root.mainloop()