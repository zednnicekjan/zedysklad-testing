
from guizero import *
from gpiozero import Button
import serial.tools.list_ports
import serial
import sys
import time
from threading import Thread

app = App (height=480, width=800)
app.bg = "#ff4d06"

# Pole pro ukládání stavů senzorů
pole = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# Funkce pro čtení stavu senzorů a zápis do pole
def cteni_stavu_senzoru():
    global pole
    for i, senzor in enumerate(senzory):
        pole[i] = 1 if senzor.is_pressed else 0

# Definice pinů pro optické senzory
piny_senzoru = [21, 20, 16, 12, 1, 23, 7, 8, 26, 24]  # Upravte podle skutečných pinů na vaší desce

# Inicializace optických senzorů
senzory = [Button(pin) for pin in piny_senzoru]

# Funkce pro měření stavu senzorů každou sekundu
def mereni_senzoru():
    while True:
        cteni_stavu_senzoru()
        time.sleep(1)

# Spuštění funkce pro měření senzorů v novém vlákně
thread = Thread(target=mereni_senzoru)
thread.start()




#Zde jdu kontrolovat napájení arduina. Pokud nebude arduino napájené, tak vyskočí error okno na panelu.
arduino = Button(17)


ports = serial.tools.list_ports.comports() #otevreni serioveho portu
for k in ports:
	if 'ACM' in k.device:
		print("pripojuji k ")
		print(k.device)
		ser = serial.Serial(k.device, 115200, timeout=5)
		if(ser.is_open):		
			print("pripojeno")
			ser.write(b'M110 S70\n')
			ser.write(b'M109 S190\n')
		else:
			print(nepripojeno)
			sys.exit()


def service():
	if arduino.is_pressed:
		print("Arduino je bez napajeni")
		Error_okno.show()
		time.sleep(5)
		sys.exit()
		
	else:
		print("Aruino je napájené")
		Error_okno.hide()
	print("Potřebuju opravit")




def Naskladnit():
	if arduino.is_pressed:
		print("Arduino je bez napájení")
		Error_okno.show()
	else:
		print("Aruino je napájené")
		Error_okno.hide()
	print("Požadavek pro Naskladnění")

	Hlavni_stranka.hide()
	Servisni_menu.hide()
	Zaskladnit_menu.show()
	Info_menu.hide()
	Vyskladnit_menu.hide()

	upozorneni.hide()
	hlavni_text_Z.show()
	hlavni_text_S.hide()
	button_zpet.show()
	button_info.hide()
	hlavni_text_V.hide()
	button_service.show()
	



def Vyskladnit():
	if arduino.is_pressed:
		print("Arduino je bez napájení")
		Error_okno.show()
	else:
		print("Aruino je napájené")
		Error_okno.hide()
		print("Požadavek pro Vyskladnění")
		Hlavni_stranka.hide()
		Servisni_menu.hide()
		Zaskladnit_menu.hide()
		Vyskladnit_menu.show()

		upozorneni.hide()
		hlavni_text_Z.show()
		hlavni_text_S.hide()
		button_zpet.show()
		button_info.hide()
		button_service.show()




def Service():
	Hlavni_stranka.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Servisni_menu.show()
	Kontrolni_okno.show()
	Info_menu.hide()

	upozorneni.show()
	hlavni_text_Z.hide()
	hlavni_text_S.show()
	button_zpet.show()
	button_info.hide()
	hlavni_text_V.hide()
	button_service.show()
	



def Zpet(): #Také jako hlavní stránka - default
	Hlavni_stranka.show()
	Servisni_menu.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Info_menu.hide()


	upozorneni.hide()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.hide()
	button_info.show()
	button_service.show()


def Info():
	Hlavni_stranka.hide()
	Servisni_menu.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Info_menu.show()


	upozorneni.hide()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.show()
	button_info.hide()
	button_service.show()





#                      !!!záhlaví!!! - to je furt stejné

zahlaví = Box(app, width = "fill", align ="top")
image1 = Picture(zahlaví, image = "logo_skoly.png", align = "left")
image2 = Picture(zahlaví, image = "logo_prace.png", align = "right")

#_________________________________________________________________________________________________



#                       !!!Main.Page!!!

Hlavni_stranka = Box(app)

hlavni_text_H = Text(Hlavni_stranka, "Automatický sklad", align = "top")
hlavni_text_H.text_size = 55
hlavni_text_H.font = "Calibry"


#               !!!tlačítka Naskladnit a vyskladnit!!!
tlacitovy_box = Box(Hlavni_stranka, width = "fill", align = "bottom", border = 4)
button1 = PushButton (tlacitovy_box, Vyskladnit, text="Vyskladnit", align = "left")
button1.text_size = 50
button1.font = "Calibry"
button2 = PushButton (tlacitovy_box, Naskladnit, text="Naskladnit", align = "right")
button2.text_size = 50
button2.font = "Calibry"


#__________________________________________________________________________________________________


#                   !!!Zaskladnit!!!
Zaskladnit_menu = Box(app)
Zaskladnit_menu.hide()
regal = Box(Zaskladnit_menu, width = "400",layout="grid", align = "top", border = 4)
def Policko9():
    zpracuj_policko(0, b'G2 P2 Z1\n')

def Policko8():
    zpracuj_policko(1, b'G2 P3 Z1\n')

def Policko7():
    zpracuj_policko(2, b'G2 P4 Z1\n')

def Policko6():
    zpracuj_policko(3, b'G2 P5 Z1\n')

def Policko5():
    zpracuj_policko(4, b'G2 P6 Z1\n')

def Policko4():
    zpracuj_policko(5, b'G2 P7 Z1\n')

def Policko3():
    zpracuj_policko(6, b'G2 P8 Z1\n')

def Policko2():
    zpracuj_policko(7, b'G2 P9 Z1\n')

def Policko1():
    zpracuj_policko(8, b'G2 P10 Z1\n')

def Policko0():
    zpracuj_policko(9, b'G2 P11 Z1\n')

def zpracuj_policko(index, prikaz):
    print(f"Požadavek na polohu {index}")  
    print("Čeká na info OK od Arduina") 
    
    if pole[index] == 0:
        Hlavni_stranka.hide()
        Servisni_menu.hide()
        Vyskladnit_menu.hide()
        Zaskladnit_menu.show()
        Info_menu.hide()

        upozorneni.hide()
        hlavni_text_Z.show()
        hlavni_text_S.hide()
        button_zpet.show()
        button_info.hide()
        button_service.hide()

        ser.write(prikaz)  # Provádí sériovou komunikaci s příslušným příkazem
        # Neprovádí se aktualizace pole pole[index] = 1
    else:
        # V případě, že prvek s daným indexem v poli není roven nule
        print(f"Policko {index} již obsazeno.")
        # Zde můžete provést další akce, pokud je políčko již obsazeno


hlavni_text_Z = Text(zahlaví, "Vyberte pozici")
hlavni_text_Z.text_size = 55
hlavni_text_Z.font = "Calibry"
hlavni_text_Z.hide()

# Definice políček pro tlačítka
Policko_9 = PushButton(regal, Policko9, image="logo_do_regalu_off.png", grid=[0,0])
Policko_8 = PushButton(regal, Policko8, image="logo_do_regalu_off.png", grid=[1,0])
Policko_7 = PushButton(regal, Policko7, image="logo_do_regalu_off.png", grid=[2,0])
Policko_6 = PushButton(regal, Policko6, image="logo_do_regalu_off.png", grid=[3,0])
Policko_5 = PushButton(regal, Policko5, image="logo_do_regalu_off.png", grid=[4,0])
Policko_4 = PushButton(regal, Policko4, image="logo_do_regalu_off.png", grid=[0,1])
Policko_3 = PushButton(regal, Policko3, image="logo_do_regalu_off.png", grid=[1,1])
Policko_2 = PushButton(regal, Policko2, image="logo_do_regalu_off.png", grid=[2,1])
Policko_1 = PushButton(regal, Policko1, image="logo_do_regalu_off.png", grid=[3,1])
Policko_0 = PushButton(regal, Policko0, image="logo_do_regalu_off.png", grid=[4,1])

# Seznam tlačítek
policka = [Policko_9, Policko_8, Policko_7, Policko_6, Policko_5, Policko_4, Policko_3, Policko_2, Policko_1, Policko_0]

# Funkce pro aktualizaci tlačítek na základě stavů v poli
def aktualizovat_tlacitka():
    global pole
    for i, hodnota in enumerate(pole):
        if hodnota == 1:
            policka[i].image = "logo_do_regalu_on.png"
        else:
            policka[i].image = "logo_do_regalu_off.png"

# Spustit aktualizaci tlačítek pravidelně
def spustit_aktualizaci_naskladnit():
    while True:
        aktualizovat_tlacitka()
        time.sleep(2)  # Počkejte 2 sekundy, než aktualizujete tlačítka znovu

# Spuštění aktualizace tlačítek v novém vlákně
aktualizace_1_thread = Thread(target=spustit_aktualizaci_naskladnit)
aktualizace_1_thread.start()

#________________________________________________________________________________________________


#                   !!!Vyskladnit!!!
Vyskladnit_menu = Box(app)
Vyskladnit_menu.hide()
regal2 = Box(Vyskladnit_menu, width = "400",layout="grid", align = "top", border = 4)
def Policko9():
    zpracuj_policko_vyskl(0, b'G2 P2 Z2\n')

def Policko8():
    zpracuj_policko_vyskl(1, b'G2 P3 Z2\n')

def Policko7():
    zpracuj_policko_vyskl(2, b'G2 P4 Z2\n')

def Policko6():
    zpracuj_policko_vyskl(3, b'G2 P5 Z2\n')

def Policko5():
    zpracuj_policko_vyskl(4, b'G2 P6 Z2\n')

def Policko4():
    zpracuj_policko_vyskl(5, b'G2 P7 Z2\n')

def Policko3():
    zpracuj_policko_vyskl(6, b'G2 P8 Z2n')

def Policko2():
    zpracuj_policko_vyskl(7, b'G2 P9 Z2\n')

def Policko1():
    zpracuj_policko_vyskl(8, b'G2 P10 Z2\n')

def Policko0():
    zpracuj_policko_vyskl(9, b'G2 P11 Z2\n')

def zpracuj_policko_vyskl(index, prikaz):
    print(f"Požadavek na polohu {index}")  
    print("Čeká na info OK od Arduina") 
    
    if pole[index] == 1:
        Hlavni_stranka.hide()
        Servisni_menu.hide()
        Vyskladnit_menu.hide()
        Zaskladnit_menu.show()
        Info_menu.hide()

        upozorneni.hide()
        hlavni_text_Z.show()
        hlavni_text_S.hide()
        button_zpet.show()
        button_info.hide()
        button_service.hide()

        ser.write(prikaz)  # Provádí sériovou komunikaci s příslušným příkazem
        # Neprovádí se aktualizace pole pole[index] = 1
    else:
        # V případě, že prvek s daným indexem v poli není roven nule
        print(f"Policko {index} již obsazeno.")
        # Zde můžete provést další akce, pokud je políčko již obsazeno


hlavni_text_V = Text(zahlaví, "Vyberte pozici")
hlavni_text_V.text_size = 55
hlavni_text_V.font = "Calibry"
hlavni_text_V.hide()

# Definice políček pro tlačítka
Policko_9 = PushButton(regal2, Policko9, image="logo_do_regalu_off.png", grid=[0,0])
Policko_8 = PushButton(regal2, Policko8, image="logo_do_regalu_off.png", grid=[1,0])
Policko_7 = PushButton(regal2, Policko7, image="logo_do_regalu_off.png", grid=[2,0])
Policko_6 = PushButton(regal2, Policko6, image="logo_do_regalu_off.png", grid=[3,0])
Policko_5 = PushButton(regal2, Policko5, image="logo_do_regalu_off.png", grid=[4,0])
Policko_4 = PushButton(regal2, Policko4, image="logo_do_regalu_off.png", grid=[0,1])
Policko_3 = PushButton(regal2, Policko3, image="logo_do_regalu_off.png", grid=[1,1])
Policko_2 = PushButton(regal2, Policko2, image="logo_do_regalu_off.png", grid=[2,1])
Policko_1 = PushButton(regal2, Policko1, image="logo_do_regalu_off.png", grid=[3,1])
Policko_0 = PushButton(regal2, Policko0, image="logo_do_regalu_off.png", grid=[4,1])

# Seznam tlačítek
policka = [Policko_9, Policko_8, Policko_7, Policko_6, Policko_5, Policko_4, Policko_3, Policko_2, Policko_1, Policko_0]

# Funkce pro aktualizaci tlačítek na základě stavů v poli
def aktualizovat_tlacitka():
    global pole
    for i, hodnota in enumerate(pole):
        if hodnota == 1:
            policka[i].image = "logo_do_regalu_on.png"
        else:
            policka[i].image = "logo_do_regalu_off.png"

# Spustit aktualizaci tlačítek pravidelně
def spustit_aktualizaci_vyskladnit():
    while True:
        aktualizovat_tlacitka()
        time.sleep(2)  # Počkejte sekundu, než aktualizujete tlačítka znovu

# Spuštění aktualizace tlačítek v novém vlákně
aktualizace_2_thread = Thread(target=spustit_aktualizaci_vyskladnit)
aktualizace_2_thread.start()

#_____________________________________________________________________________________________________

#                           !!!Servisní Menu!!!
Servisni_menu = Box(app)
Servisni_menu.hide()

#------------------------upozornění - vyskakovací okno------------------------------------------------
Kontrolni_okno = Window(app, title = "UPOZORNĚNÍ", height=300, width=650)
Kontrolni_okno.bg = "red"
text_upozorneni1 = Text(Kontrolni_okno, text = "Upozornění !!!")
text_upozorneni1.size = 50
text_upozorneni2 = Text(Kontrolni_okno, text = "Systém v ručním ovládání nepozná, zda není v kolizi.")
text_upozorneni2.size = 15
text_upozorneni3 = Text(Kontrolni_okno, text = " NEHAVARUJTE!! Díky.")
text_upozorneni3.size = 15
Kontrolni_okno.hide()
#-----------------------------------------------------------------------------------------------------


def X_plusa():
	print("X +" + vyber_vzdalenosti.value)
	ser.write(b'G0 X10\n')
	#ser.write(vyber_vzdalenosti.value)
	#ser.write(b'\n')
def X_minusa():
	print("X -" + vyber_vzdalenosti.value)
	ser.write(b'G0 X-10\n')
	#ser.write(vyber_vzdalenosti.value)
	#ser.write(b'\n')
def Y_plusa():
	print("Y +" + vyber_vzdalenosti.value)
	#ser.write(b'G0 Y')
	#ser.write(vyber_vzdalenosti.value)
	#ser.write(b'\n')
def Y_minusa():
	print("Y -" + vyber_vzdalenosti.value)
	#ser.write(b'G0 Y-')
	#ser.write(vyber_vzdalenosti.value)
	#ser.write(b'\n')
def Z_plusa():
	print("Z +" + vyber_vzdalenosti.value)
	#ser.write(b'G0 Z')
	#ser.write(vyber_vzdalenosti.value)
	#ser.write(b'\n')
def Z_minusa():
	print("Z -" + vyber_vzdalenosti.value)
	#ser.write(b'G0 Z-')
	#ser.write(vyber_vzdalenosti.value)
	#ser.write(b'\n')


hlavni_text_S = Text(zahlaví, "Nacházíte se v servisním módu")
hlavni_text_S.text_size = "30"
hlavni_text_S.font = "Calibry"
hlavni_text_S.hide()


upozorneni = Text(zahlaví, "Upozornění!: systém nepozná, zda není v kolizi. Nehavarujte!!! Diky", width = "fill", align = "top")
upozorneni_size = "20"
upozorneni.font = "Calibry"
upozorneni.hide()




stred = Box(Servisni_menu,width = "800", layout = "grid" , align ="top", border = 4)

vyber_vzdalenosti = Combo(stred, width ="15", height = "5" ,options = ["1 mm", "10 mm", "100 mm"], grid = [0,0])
dira = Text(stred, width = "15", text= "   ", grid = [1,0])

X_plus = PushButton(stred, X_plusa, text = "  X plus  ", image = "Xplus.png", grid=[2,0])
X_minus = PushButton(stred, X_minusa, text = "X minus", image = "Xminus.png", grid=[2,1])

Y_plus = PushButton(stred, Y_plusa, text = "  Y plus  ", image = "Yplus.png", grid=[3,0])
Y_minus = PushButton(stred, Y_minusa, text = "Y minus", image = "Yminus.png", grid=[3,1])

Z_plus = PushButton(stred, Z_plusa, text = "  Z plus ", image = "Zplus.png", grid=[4,0])
Z_minus = PushButton(stred, Z_minusa, text = "Z minus", image = "Zminus.png", grid=[4,1])



#_____________________________________________________________________________________________________


#                           !!!Error Menu!!!
Error_menu = Box(app)
Error_menu.hide()

#------------------------upozornění - vyskakovací okno------------------------------------------------
Error_okno = Window(app, title = "UPOZORNĚNÍ", height=300, width=650)
Error_okno.bg = "red"
text_error1 = Text(Error_okno, text = "Upozornění !!!")
text_error1.size = 50
text_error2 = Text(Error_okno, text = "Systém zaznamenal chybu. Příkaz, který požadujete se nevykonal správně.")
text_error2.size = 15
text_error3 = Text(Error_okno, text = "Zkontrolujte napájení Arduina.")
text_error3.size = 15

Error_okno.hide()

#_________________________________________________________________________________________________
#                       !!!zápatí!!!
zapati = Box(app, width = "fill", align = "bottom")
button_service = PushButton(zapati, Service,image = "service.png", align = "left")
button_service.show()
button_zpet = PushButton(zapati, Zpet, image = "sipka_zpet.png", align = "right")
button_zpet.hide()
button_info = PushButton(zapati, Info, image = "info.png", align = "right")

autori_text = Text(zapati, text = "Pavel Hrstka, Vít Růžička ©2021", align = "bottom")
autori_text.font = "Calibry"
autori_text.size = 25





Info_menu = Box (app)
Info_menu.hide()

velikost_pisma_info = 12
info_text1 = Text(Info_menu, text = "Tento model vznikl jako maturitní práce ve školním roce 2020/2021 za podpory SPŠ-KH,")
info_text2 = Text(Info_menu, text = "Krajské hospodářské komory Střední Čechy")
info_text3 = Text(Info_menu, text = "Jmenovitě bych rád poděkoval Vítkovi Růžičkovi, kteý mi velmi pomohl s programem řízení")
info_text4 = Text(Info_menu, text = "a značně se podílel také na 3D modelování. Když jsem začal, tak jsem byl v 3D modelování úplný nováček.")
info_text5 = Text(Info_menu, text = "Dále patří díky: Ing. Jozef Treml, Ing. Pavel Stejskal, Ing. Bc. Stanislav Moravec ")
info_text6 = Text(Info_menu, text = "")
info_text7 = Text(Info_menu, text = "")
info_text8 = Text(Info_menu, text = "V případě potřeby tak mě můžete kontaktovat na emailu: pavhr@email.cz nebo na telefonu: 737 857 928 ")

info_text1.size = velikost_pisma_info
info_text2.size = velikost_pisma_info
info_text3.size = velikost_pisma_info
info_text4.size = velikost_pisma_info
info_text5.size = velikost_pisma_info
info_text6.size = velikost_pisma_info






app.display ()

