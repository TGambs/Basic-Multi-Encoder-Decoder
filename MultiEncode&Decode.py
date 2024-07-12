def Encode():
    import base64

    def Title():
        print("")
        print("--------------------------------------------------------------------------------")
        print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        print(" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ MULTI ENCODER  / / / / / / / / / / / / / / / / / ")
        print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        print("--------------------------------------------------------------------------------")
        print("")
        print("Translates to Hex, Binary, Ascii85, Ascii, Base16, Base32, Base64")
        print("")

        

    def Input():
        text = input("Enter text: ")
        return text

    def ASCII(text):

        Atext = [None] * len(text)
            
        for y in range(len(text)):
            Atext[y] = text[y]        
            Atext[y] = ord(Atext[y])

        Ascii = "".join(str(Atext))
        Ascii = Ascii[1:(len(Ascii)-1)]
        
        return Ascii

    def HEX(text):
        Atext = [None] * len(text)

        for y in range(len(text)):
            Atext[y] = text[y]        
            Atext[y] = ord(Atext[y])        
            Atext[y] = hex(Atext[y])
            
        Hex = "".join(Atext)
        Hex = Hex.replace("0x","")
        return Hex


    def BINARY(text):
        Atext = [None] * len(text)

        for y in range(len(text)):
            Atext[y] = text[y]        
            Atext[y] = ord(Atext[y])
            Atext[y] = format(Atext[y], '#010b')     
            Atext[y] = (Atext[y])[2:]

        Binary = " ".join(Atext)
        return Binary

    def ASCII85(text):

        a1 = text.encode("UTF-8")
        a2 = base64.a85encode(a1)
        output85 = a2.decode("UTF-8")

        return output85

    def BASE(text):
        #BASE16 encoding
        a16 = text.encode("UTF-8")
        c16 = base64.b16encode(a16)
        b16 = c16.decode("UTF-8")

        #BASE32 encoding
        a32 = text.encode("UTF-8")
        c32 = base64.b32encode(a32)
        b32 = c32.decode("UTF-8")

        #BASe64 encoding
        a64 = text.encode("UTF-8")
        c64 = base64.b64encode(a64)
        b64 = c64.decode("UTF-8")

        return b16, b32, b64
        


        
    def DISPLAY(Ascii, Hex, Binary, output85, b16, b32, b64):
        print("\n","\n")
        print("")
        print("     _      ____     ____   ___   ___  ")
        print("    / \    / ___|   / ___| |_ _| |_ _| ")
        print("   / _ \   \___ \  | |      | |   | |  ")
        print("  / ___ \   ___) | | |___   | |   | |  ")
        print(" /_/   \_\ |____/   \____| |___| |___| ")
        print("------------------------------------------","\n") 
        print("The ascii translation of the input is:","\n","- ",Ascii,"\n")
        print("")
        print("     _      ____     ____   ___   ___    ___    ____   ")
        print("    / \    / ___|   / ___| |_ _| |_ _|  ( _ )  | ___|  ")
        print("   / _ \   \___ \  | |      | |   | |   / _ \  |___ \  ")
        print("  / ___ \   ___) | | |___   | |   | |  | (_) |  ___) | ")
        print(" /_/   \_\ |____/   \____| |___| |___|  \___/  |____/  ")
        print("----------------------------------------------------------","\n") 
        print("The ASCII85 translation of the input is:","\n","- ",output85,"\n")
        print("")
        print("   ____    _                                 ")
        print("  | __ )  (_)  _ __     __ _   _ __   _   _  ")
        print("  |  _ \  | | | '_ \   / _` | | '__| | | | | ")
        print("  | |_) | | | | | | | | (_| | | |    | |_| | ")
        print("  |____/  |_| |_| |_|  \__,_| |_|     \__, | ")
        print("                                      |___/  ")
        print("------------------------------------------------","\n") 
        print("The 8 bit binary translation of the input is:","\n","- ",Binary,"\n")
        print("")
        print("   _   _   _____  __  __ ")
        print("  | | | | | ____| \ \/ / ")
        print("  | |_| | |  _|    \  /  ")
        print("  |  _  | | |___   /  \  ")
        print("  |_| |_| |_____| /_/\_\ ")
        print("---------------------------","\n")    
        print("The hex translation of the input is:","\n","- ",Hex,"\n")
        print("")
        print("   ____       _      ____    _____  ")
        print("  | __ )     / \    / ___|  | ____| ")
        print("  |  _ \    / _ \   \___ \  |  _|   ")
        print("  | |_) |  / ___ \   ___) | | |___  ")
        print("  |____/  /_/   \_\ |____/  |_____| ")
        print("--------------------------------------","\n") 
        print("The Base16 trasnlation of the input is:","\n","- ",b16,"\n")
        print("The Base32 trasnlation of the input is:","\n","- ",b32,"\n")
        print("The Base64 trasnlation of the input is:","\n","- ",b64,"\n")
     
        

    def EncodeMain():
        Title()
        text = Input()
        Ascii = ASCII(text)
        Hex = HEX(text)
        Binary = BINARY(text)
        output85 = ASCII85(text)
        b16, b32, b64 = BASE(text)
        DISPLAY(Ascii, Hex, Binary, output85, b16, b32, b64)
        

    EncodeMain()

###############################################################################################

def Decode():
    import base64
    import binascii


    def Title():
        print("")
        print("--------------------------------------------------------------------------------")
        print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        print(" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ MULTI DECODER  / / / / / / / / / / / / / / / / / ")
        print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        print("--------------------------------------------------------------------------------")
        print("")
        print("Translates From Ascii85 , Hex, Ascii, Binary")
        print("")



    def Input():
        print("Types of Input: \n ")
        print("- A85  = Ascii85  // Example - 87cURDZ \n")
        print("- Hex  = Hex      // Example - 48656c6c6f \n")
        print("- Asc  = Ascii    // Example - 72, 101, 108, 108, 111 \n")
        print("- Bin  = Binary   // Example - 01001000 01100101 01101100 01101100 01101111 \n")
        Rtype = input("Enter which translation you would like: ")
        text = input("Enter text: ")
        return text, Rtype


    def ASCII(text):
        Ccount = 0
        pos = 0

        for y in range(len(text)):
            if text[pos] == ",":
                Ccount += 1
            pos += 1

        Array1 = [None] * (Ccount+1)

        data = text.split(", ")

        for x in range(Ccount+1):
            Array1[x] = data[x]
            Array1[x] = chr(int(Array1[x]))

        Ascii = "".join(Array1)

        return Ascii


    def BINARY(text):
        Scount = 0
        pos = 0

        for y in range(len(text)):
            if text[pos] == " ":
                Scount += 1
            pos += 1

        Array1 = [None] * (Scount+1)
        data = text.split(" ")

        for x in range(Scount+1):
            pos = 0
            total = 0
            Array1[x] = data[x]
            
        for x in range(Scount+1):
            pos = 0
            total = 0
            if (Array1[x])[pos] == "1":
                total += 128
                pos += 1
            else:
                pos += 1

            if (Array1[x])[pos] == "1":
                total += 64
                pos += 1
            else:
                pos += 1

            if (Array1[x])[pos] == "1":
                total += 32
                pos += 1
            else:
                pos += 1

            if (Array1[x])[pos] == "1":
                total += 16
                pos += 1
            else:
                pos += 1

            if (Array1[x])[pos] == "1":
                total += 8
                pos += 1
            else:
                pos += 1

            if (Array1[x])[pos] == "1":
                total += 4
                pos += 1
            else:
                pos += 1

            if (Array1[x])[pos] == "1":
                total += 2
                pos += 1
            else:
                pos += 1

            if (Array1[x])[pos] == "1":
                total += 1
                pos += 1
            else:
                pos += 1

            Array1[x] = chr(total)

        Binary = "".join(Array1)
        return Binary

    def ASCII85(text):

        a1 = text.encode("UTF-8")
        a2 = base64.a85decode(a1)
        output85 = a2.decode("UTF-8")

        return output85

    def HEX(text):

        Hex = binascii.unhexlify(text)
        Hex = Hex.decode("UTF-8")
        
        return Hex
        

    def A85DISPLAY(output85):
        print("")
        print("")
        print("     _      ____     ____   ___   ___    ___    ____   ")
        print("    / \    / ___|   / ___| |_ _| |_ _|  ( _ )  | ___|  ")
        print("   / _ \   \___ \  | |      | |   | |   / _ \  |___ \  ")
        print("  / ___ \   ___) | | |___   | |   | |  | (_) |  ___) | ")
        print(" /_/   \_\ |____/   \____| |___| |___|  \___/  |____/  ")
        print("----------------------------------------------------------","\n") 
        print("The translation of the input is:","\n","- ",output85,"\n")

    def HexDISPLAY(Hex):
        print("")
        print("")
        print("   _   _   _____  __  __ ")
        print("  | | | | | ____| \ \/ / ")
        print("  | |_| | |  _|    \  /  ")
        print("  |  _  | | |___   /  \  ")
        print("  |_| |_| |_____| /_/\_\ ")
        print("---------------------------","\n")    
        print("The translation of the input is:","\n","- ",Hex,"\n")

    def ASCDISPLAY(Ascii):
        print("")
        print("     _      ____     ____   ___   ___  ")
        print("    / \    / ___|   / ___| |_ _| |_ _| ")
        print("   / _ \   \___ \  | |      | |   | |  ")
        print("  / ___ \   ___) | | |___   | |   | |  ")
        print(" /_/   \_\ |____/   \____| |___| |___| ")
        print("------------------------------------------","\n")
        print("The translation of the input is:","\n","- ",Ascii,"\n")

    def BinDISPLAY(Binary):
        print("")
        print("   ____    _                                 ")
        print("  | __ )  (_)  _ __     __ _   _ __   _   _  ")
        print("  |  _ \  | | | '_ \   / _` | | '__| | | | | ")
        print("  | |_) | | | | | | | | (_| | | |    | |_| | ")
        print("  |____/  |_| |_| |_|  \__,_| |_|     \__, | ")
        print("                                      |___/  ")
        print("------------------------------------------------","\n") 
        print("The 8 bit binary translation of the input is:","\n","- ",Binary,"\n")

    def DecodeMain():
        Title()    
        text, Rtype = Input()

        if Rtype == "A85":
            output85 = ASCII85(text)
            A85DISPLAY(output85)

        elif Rtype == "Hex":
            Hex = HEX(text)
            HexDISPLAY(Hex)

        elif Rtype == "Asc":
            Ascii = ASCII(text)
            ASCDISPLAY(Ascii)

        elif Rtype == "Bin":
            Binary = BINARY(text)
            BinDISPLAY(Binary)

        else:
            print("----------- Invalid Translation Type -----------")
            input("press ENTER to continue")
            
    DecodeMain()

###########################################################################################            

def Main():
    EDchoice = input("Would you like to encode or decode text (e/d): ")

    if EDchoice == "e":
        Encode()
    elif EDchoice == "d":
        Decode()
    else:
        print(" - - - - - - - - - - INVALID INPUT - - - - - - - - - - ")
        input("press ENTER to continue")
        print("")


# Loop for multiple uses #
Main()
choice = str(input("Would you like another translation (y/n): "))
while (choice == "y"):
    Main()
    choice = str(input("Would you like another translation (y/n): "))
print("Goodbye!")
    
