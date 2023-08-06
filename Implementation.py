def show(x, res, f):
    global computer_choice, r,lfp  
    
    choix = np.random.choice(['rock', 'paper', 'scissor'])
    Label(f, text=f"Computer's choice is {choix}", bg='yellow', padx=2, pady=5).grid(row=4, column=1)
    Label(lfp, text=f"your choice is {x}", bg='yellow', padx=2, pady=5).grid(row=4, column=1)
    
    if x == choix:
        r.config(text="ta3adol", bg="red", fg="black")  
    elif (x == "rock" and choix == "scissor") or (x == "scissor" and choix == "paper") or (x == "paper" and choix == "rock"):
        r.config(text="rbe7ti! yaay", bg="light green", fg="black")  
    else:
        r.config(text="khserti! :)", bg="light blue", fg="black")  

def buttons4plyr(lf, res, f):
    global r  
    r = Label(res, text="still zero", bg="green")
    r.grid(row=10, column=1)
    
    rock_btn = Button(lf, text="Rock", command=lambda: show("rock", res, f))
    rock_btn.grid(row=1, column=0)
    
    paper_btn = Button(lf, text="Paper", command=lambda: show("paper", res, f))
    paper_btn.grid(row=1, column=1)
    
    scissor_btn = Button(lf, text="Scissor", command=lambda: show("scissor", res, f))
    scissor_btn.grid(row=1, column=2)
