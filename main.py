#Одну я помню: сказку эту поведаю теперь я свету. Уланы с пестрыми значками, драгуны с конскими хвостами, все промелькнули перед нам, все побывали тут.
import math
def scan_text():
    #text = input("Введите текст: ")
    text = "Одну я помню: сказку эту поведаю теперь я свету. Уланы с пестрыми значками, драгуны с конскими хвостами, все промелькнули перед нам, все побывали тут."
    return text

def output_single(letters,numbers,size,arsize,condition):
    if (condition == 1):
        print(" ______","______","______","____________","___________","___________","_______________",sep="_")
    else:
        if (condition == 2):
            print(" ______","______","______","____________","___________","___________","________________",sep="_")
        else:
            print(" ______","______","______","____________","___________","___________","_________________",sep="_")

    print("|i     |",end="")
    if(condition==1):
        print("x(i)  |", end="")
    else:
        if(condition==2):
            print("x(i)   |", end="")
        else:
            print("x(i)    |", end="")
    print("N(i)   |", end="")
    print("N(i)/N    |", end="")
    print("p(x(i))    |", end="")
    print("I(x(i))    |", end="")
    print("I(x(i))*p(x(i))|", end="\n")
    for i in range(0,arsize):
        chance = numbers[i] / size
        l = -math.log2(chance)
        inf = chance * l
        if((i+1)//100>=1):
            print("|   ", i + 1, "|", end="", sep="")
        else:
            if ((i + 1) / 10 >= 1):
                print("|    ", i + 1, "|", end="", sep="")
            else:
                print("|     ", i + 1, "|", end="", sep="")
        print("     ", letters[i], "|", end="", sep="")
        if (numbers[i] // 10 > 0):
            print("     ", numbers[i], "|", end="", sep="")
            print("    ", numbers[i], "/", size, "|", end="", sep="")
        else:
            print("      ", numbers[i], "|", end="", sep="")
            print("     ", numbers[i], "/", size, "|", end="", sep="")


        print("     ", "%.4f" % chance, "|", end="", sep="")
        print("     ", "%.4f" % l, "|", end="", sep="")
        print("     ", "%.8f" % inf, "|", end="\n", sep="")
    print(" ‾‾‾‾‾‾", "‾‾‾‾‾‾", "‾‾‾‾‾‾", "‾‾‾‾‾‾‾‾‾‾‾‾", "‾‾‾‾‾‾‾‾‾‾‾", "‾‾‾‾‾‾‾‾‾‾‾", "‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾",sep="‾")
    return 0

text = scan_text()
array_l = []
array_n = []
cond = False
data = 0
for i in range(0,len(text)):
    for y in range(0,len(array_l)):
        cond = False
        if (array_l[y] == text[i].lower()):
            cond = True
            data = y
            break
    if(cond == True):
        array_n[data] += 1
    else:
        array_l.append(text[i].lower())
        array_n.append(1)

DOUBLEarray_l = []
DOUBLEarray_n = []
cond = False
data = 0
for i in range(0,len(text)-1):
    for y in range(0,len(DOUBLEarray_l)-1):
        cond = False
        if (DOUBLEarray_l[y] == text[i].lower()+text[i+1].lower()):
            cond = True
            data = y
            break
    if(cond == True):
        DOUBLEarray_n[data] += 1
    else:
        DOUBLEarray_l.append(text[i].lower()+text[i+1].lower())
        DOUBLEarray_n.append(1)

TRIPLEarray_l = []
TRIPLEarray_n = []
cond = False
data = 0
for i in range(0,len(text)-2):
    for y in range(0,len(TRIPLEarray_l)-2):
        cond = False
        if (TRIPLEarray_l[y] == text[i].lower()+text[i+1].lower()+text[i+2].lower()):
            cond = True
            data = y
            break
    if(cond == True):
        TRIPLEarray_n[data] += 1
    else:
        TRIPLEarray_l.append(text[i].lower()+text[i+1].lower()+text[i+2].lower())
        TRIPLEarray_n.append(1)
output_single(array_l, array_n, len(text),len(array_l),1)
output_single(DOUBLEarray_l, DOUBLEarray_n, len(text)-1,len(DOUBLEarray_l),2)
output_single(TRIPLEarray_l, TRIPLEarray_n, len(text)-2,len(TRIPLEarray_l),3)

