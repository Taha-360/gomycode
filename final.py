lfp = LabelFrame(fr, bg="violet", height=800, width=800, padx=50, pady=50)
lfp.grid(row=0, column=0)
lp = Label(lfp, text="Player", fg="pink", font=50)
lp.grid(row=0, column=1)

res = LabelFrame(fr, text="Result", bg="gray", fg="white", height=80, width=250, padx=50, pady=50)
res.grid(row=1, column=0)

lfc = LabelFrame(fr, bg="indigo", height=500, width=700, padx=50, pady=50)
lfc.grid(row=2, column=0)
lc = Label(lfc, text="Computer", fg="pink", font=40)
lc.grid(row=0, column=1)

buttons4plyr(lfp, res, lfc)

w.mainloop()
