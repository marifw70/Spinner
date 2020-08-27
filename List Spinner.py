listAwal= [[1,2,3], # set listAwal yang ingin di uji
            [4,5,6],
            [7,8,9]] 
def counterClockwise(x): #buat function dengan nama counterClockwise dan parameternya adalah x
    # set value a,b,c dari listnya index 0
    a = x[0][0] #set variabel a adalah index [0][0] dari si x
    b = x[0][1] #set variabel b adalah index [0][1] dari si x
    c = x[0][2] #set variabel c adalah index [0][2] dari si x
    # set value d,e,f dari list index 1
    d = x[1][0] #set variabel d adalah index [1][0] dari si x
    e = x[1][1] #set variabel e adalah index [1][1] dari si x
    f = x[1][2] #set variabel f adalah index [1][2] dari si x
    # set value g,h,i dari list index 2
    g = x[2][0] #set variabel g adalah index [2][0] dari si x
    h = x[2][1] #set variabel h adalah index [2][1] dari si x
    i = x[2][2] #set variabel i adalah index [2][2] dari si x
    return [[c,f,i],[b,e,h],[a,d,g]] # kembalikan variabel a,b,c,d,e,f,g,h,i dengan format yang sudah diset
print(counterClockwise(listAwal)) # ketika function counter dicetak dengan value dari parameter x, maka value yang ada di return akan dicetak


