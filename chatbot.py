import time

print("Hi! I'm your personal bot assistant.")
time.sleep(1)
print("How can I help?")
response = input("Enter your prompt: ")
if response == "yes":
    print("What is your problem?")
    print("1. PIN issues")
    print("2. Mobile banking app problems")
    print("3. Product info")
    number = int(input("Choose your concern: "))
if number == 1:
    print("1. Go to the nearest bank in your town")
    print("2. Take your ticket number")
    print("3. Go to the customer service")
    print("4. Give the data required by the CS")
    print("5. Request to reset the PIN")
    print("6. Propose the new PIN")
    print("7. Finish")
elif number == 2:
    print("1. Go to the nearest bank in your town")
    print("2. Take your ticket number")
    print("3. Go to the customer service")
    print("4. Go to the mobile banking terminal")
    print("5. Finish")
elif number == 3:
    print("1. Tabungan")
    print("2. Deposit")
    print("3. Giro")
    number2= int(input("Choose : "))
    if number2 == 1:        
        print("Tabungan adalah jenis produk perbankan yang digunakan untuk menyimpan uang seseorang di bank dengan tujuan mengumpulkan dana atau mengamankan uang. Biasanya, nasabah akan mendapatkan bunga dari tabungan yang dimilikinya.")
    elif number2 == 2:
        print("Giro adalah jenis produk perbankan yang berfungsi sebagai alat pembayaran elektronik. Dalam giro, nasabah dapat memindahkan uang ke rekening lain dengan mudah melalui transfer bank atau cek.")
    elif number2 == 3:
        print("Deposito adalah jenis produk perbankan yang digunakan untuk menyimpan uang dengan jangka waktu tertentu, biasanya mulai dari 1 bulan hingga 1 tahun atau bahkan lebih. Deposito memberikan bunga yang lebih tinggi dibandingkan dengan tabungan karena nasabah setuju untuk mengunci uangnya dalam jangka waktu tertentu.")