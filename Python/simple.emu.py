global icarus_mem
icarus_mem = ""
addn = 0
movn = 0
loadn = 0

try:
    with open("Simple_SSD.semd", "r+") as f:
        print("Hard drive opened successfully!")
except FileNotFoundError:
    print("SimpleEmuDisk(.semd) not detected.")
    with open("Simple_SSD.semd", "w") as f:
        print("Creating hard disk compatible with TX11 processor series(.semd)")
        print("Completed Successfully :)")
    with open("Simple_SSD.semd", "r+") as f:
        print("Opening Drive...")
while True:
    j = input("mov/load/add/sub:")
    j = j.lower()
    if j == "load":
        print(icarus_mem)
        loadn+=1
    if "add" in j:
        toadd = int(j[4:])
        res = int(icarus_mem)
        fin = res + toadd
        ic = str(fin)
        icarus_mem = ""
        icarus_mem+=ic
        addn += 1
    elif "mov" in j:
        length = len(j[4:])
        if length > 4:
            print("SmartRAM has detected that the memory is being overloaded. Keep within the limited amount!")
            continue
        icarus_mem = ""
        icarus_mem+=j[4:]
        movn += 1
    elif "sub" in j:
        tosub = int(j[4:])
        res = int(icarus_mem)
        fin = res - tosub
        ic = str(fin)
        icarus_mem = ""
        icarus_mem+=ic
    elif "mul" in j:
        tomul = int(j[4:])
        res = int(icarus_mem)
        fin = res * tomul
        ic = str(fin)
        icarus_mem = ""
        icarus_mem+=ic       
    elif "init.loop()" in j:
        while True:
            j = input("ePins loaded and ready for calculation!")
            executer(j)
    elif "cmp" in j:
        tocmp = str(j[4:])
        if tocmp == icarus_mem:
            print("Returned True")
        else:
            print("Returned False")
    elif j == "hlt":
        print("Execution details:")
        print(f"mov was executed {movn} time(s)")
        print(f"add was executed {addn} time(s)")
        print(f"load was executed {loadn} time(s)")
        alln = addn+movn+loadn
        print(f"You executed {alln} commands total")
        break
