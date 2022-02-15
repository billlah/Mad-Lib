
import random

users = ""

while users != "keluar":

    users = input("Masukan perintah (mulai/keluar) : ")

    if users == "keluar":
        break

    users = int(input("Masukan angka random: "))
    users_max_input = 10

    hasil = random.randint(users,users_max_input)

    if hasil == 1:
        correct = "Ayah budi sedang makan dengan ayam goreng"
        print("Ayah budi .... makan .... ayam goreng")
        answer = str(input("Lengakapi kalimat di atas: "))
        if answer == correct:
            print("Jawaban kamu benar")
        else:
            print("Jawaban mu kurang tepat")
    elif hasil == 2:
        correct = "Ibu ku sedang memasak mie di dapur"
        print("Ibu ku ...... memasak ... di .....")
        answer = str(input("Lengakapi kalimat di atas: "))
        if answer == correct:
            print("Jawaban kamu benar")
        else:
            print("Jawaban mu kurang tepat")
    elif hasil == 3:
        correct = "Rudi bermain sepak bola di lapangan bersama teman"
        print("Rudi bermain ..... bola .. lapangan ..... teman")
        answer = str(input("Lengakapi kalimat di atas: "))
        if answer == correct:
            print("Jawaban kamu benar")
        else:
            print("Jawaban mu kurang tepat")
    elif hasil == 4:
        correct = "Habibie menonton film sing di bioskop"
        print("Habibie ........ film sing di .......")
        answer = str(input("Lengakapi kalimat di atas: "))
        if answer == correct:
            print("Jawaban kamu benar")
        else:
            print("Jawaban mu kurang tepat")
    elif hasil == 5:
        correct = "Pak yanto mencuci motor di tempat cuci motor"
        print("... yanto mencuci ..... di ...... cuci .....")
        answer = str(input("Lengakapi kalimat di atas: "))
        if answer == correct:
            print("Jawaban kamu benar")
        else:
            print("Jawaban mu kurang tepat")
    elif hasil == 6:
        correct = "Aisayah sedang menemani adiknya di rumah"
        print("Aisyah ...... menemani ....... di .....")
        answer = str(input("Lengakapi kalimat di atas: "))
        if answer == correct:
            print("Jawaban kamu benar")
        else:
            print("Jawaban mu kurang tepat")
    elif hasil == 7:
        correct = "Adit sedang memainkan gitar"
        print("Adit sedang ......... gitar")
        answer = str(input("Lengakapi kalimat di atas: "))
        if answer == correct:
            print("Jawaban kamu benar")
        else:
            print("Jawaban mu kurang tepat")
    elif hasil == 8:
        correct = "Rumah jarwo sangat sepi"
        print("..... jarwo ...... sepi")
        answer = str(input("Lengakapi kalimat di atas: "))
        if answer == correct:
            print("Jawaban kamu benar")
        else:
            print("Jawaban mu kurang tepat")
    elif hasil == 9:
        correct = "Bagus adalah anak yang pintar di sekolah"
        print("Bagus ...... anak .... pintar di .......")
        answer = str(input("Lengakapi kalimat di atas: "))
        if answer == correct:
            print("Jawaban kamu benar")
        else:
            print("Jawaban mu kurang tepat")
    elif hasil == 10:
        correct = "Bu ratna membeli ikan di pasar seharga 50 ribu"
        print(".. ratna membeli .... di .... ....... 50 ....")
        answer = str(input("Lengakapi kalimat di atas: "))
        if answer == correct:
            print("Jawaban kamu benar")
        else:
            print("Jawaban mu kurang tepat")
    
