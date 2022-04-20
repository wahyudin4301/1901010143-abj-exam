while True:
    lanjut=input("Input DataInventory Baru (ya/tidak)? ")
    if lanjut == "ya" or lanjut == "Ya":
        file = open ("db-inventory.txt","a")
        print("*"*40)
        nama_perangkat = input("Nama Perangkat : ")
        Lokasi = input("Lokasi : ")
        print("-"*40)
        file.write("Nama Perangkat : " + nama_perangkat +", \t Lokasi : " + Lokasi +"\n")
        file.close()
    elif lanjut == "tidak" or i == "Tidak" :
        file = open ("db-inventory.txt","r")
        print("*"*40)
        for item in file:
            item = item.strip()
            print(item)
        break