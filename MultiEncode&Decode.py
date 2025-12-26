def Encode():
    import base64

    def Title():
        print("")
        print("--------------------------------------------------------------------------------")
        print(r"\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        print(r" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ MULTI ENCODER  / / / / / / / / / / / / / / / / / ")
        print(r"\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
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


    # New additions below
    def Morse(text):
        
        # Complete Morse code dictionary from the International Morse Code standards
        morseDict = {
            'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
            'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
            'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
            'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
            'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
            'Z': '--..',
            
            '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
            '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
            
            '.': '.-.-.-', ',': '--..--', '?': '..--..',
            "'": '.----.', '!': '-.-.--', '/': '-..-.',
            '(': '-.--.', ')': '-.--.-', '&': '.-...',
            ':': '---...', ';': '-.-.-.', '=': '-...-',
            '+': '.-.-.', '-': '-....-', '_': '..--.-',
            '"': '.-..-.'
            }

        # change all text to capitals to match dictionary
        # and strip any whitespace at the beginning
        text = text.strip().upper()
        mCode = []
        invalCount = 0

        for ch in text:
            if ch == ' ':
                mCode.append('   ')
            elif ch in morseDict:
                mCode.append(morseDict[ch])
            else:
                print("Invalid character detected: ",ch,"\n Substituting with ?")
                mCode.append('?')
                invalCount += 1

        mCode = ' '.join(mCode)
        if invalCount >0:
            print("There are", invalCount, "invalid characters detected")
            
        return mCode


        
    def DISPLAY(Ascii, Hex, Binary, output85, b16, b32, b64, morse):
        print("\n","\n")
        print("")
        print(r"     _      ____     ____   ___   ___  ")
        print(r"    / \    / ___|   / ___| |_ _| |_ _| ")
        print(r"   / _ \   \___ \  | |      | |   | |  ")
        print(r"  / ___ \   ___) | | |___   | |   | |  ")
        print(r" /_/   \_\ |____/   \____| |___| |___| ")
        print("------------------------------------------","\n") 
        print("The ascii translation of the input is:","\n","- ",Ascii,"\n")
        print("")
        print(r"     _      ____     ____   ___   ___    ___    ____   ")
        print(r"    / \    / ___|   / ___| |_ _| |_ _|  ( _ )  | ___|  ")
        print(r"   / _ \   \___ \  | |      | |   | |   / _ \  |___ \  ")
        print(r"  / ___ \   ___) | | |___   | |   | |  | (_) |  ___) | ")
        print(r" /_/   \_\ |____/   \____| |___| |___|  \___/  |____/  ")
        print("----------------------------------------------------------","\n") 
        print("The ASCII85 translation of the input is:","\n","- ",output85,"\n")
        print("")
        print(r"   ____    _                                 ")
        print(r"  | __ )  (_)  _ __     __ _   _ __   _   _  ")
        print(r"  |  _ \  | | | '_ \   / _` | | '__| | | | | ")
        print(r"  | |_) | | | | | | | | (_| | | |    | |_| | ")
        print(r"  |____/  |_| |_| |_|  \__,_| |_|     \__, | ")
        print(r"                                      |___/  ")
        print("------------------------------------------------","\n") 
        print("The 8 bit binary translation of the input is:","\n","- ",Binary,"\n")
        print("")
        print(r"   _   _   _____  __  __ ")
        print(r"  | | | | | ____| \ \/ / ")
        print(r"  | |_| | |  _|    \  /  ")
        print(r"  |  _  | | |___   /  \  ")
        print(r"  |_| |_| |_____| /_/\_\ ")
        print("---------------------------","\n")    
        print("The hex translation of the input is:","\n","- ",Hex,"\n")
        print("")
        print(r"   ____       _      ____    _____  ")
        print(r"  | __ )     / \    / ___|  | ____| ")
        print(r"  |  _ \    / _ \   \___ \  |  _|   ")
        print(r"  | |_) |  / ___ \   ___) | | |___  ")
        print(r"  |____/  /_/   \_\ |____/  |_____| ")
        print("--------------------------------------","\n") 
        print("The Base16 trasnlation of the input is:","\n","- ",b16,"\n")
        print("The Base32 trasnlation of the input is:","\n","- ",b32,"\n")
        print("The Base64 trasnlation of the input is:","\n","- ",b64,"\n")
        print("")
        print(r"   __  __                             ")
        print(r"  |  \/  |  ___   _ __   ___    ___   ")
        print(r"  | |\/| | / _ \ | '__| / __|  / _ \  ")
        print(r"  | |  | || (_) || |    \__ \ |  __/  ")
        print(r"  |_|  |_| \___/ |_|    |___/  \___|  ")
        print("----------------------------------------", "\n")
        print("The Morse code translation of the input is:", "\n", morse, "\n")
     
        

    def EncodeMain():
        Title()
        text = Input()
        Ascii = ASCII(text)
        Hex = HEX(text)
        Binary = BINARY(text)
        output85 = ASCII85(text)
        b16, b32, b64 = BASE(text)
        morse = Morse(text)
        DISPLAY(Ascii, Hex, Binary, output85, b16, b32, b64, morse)
        

    EncodeMain()

###############################################################################################

def Decode():
    import base64
    import binascii


    def Title():
        print("")
        print("--------------------------------------------------------------------------------")
        print(r"\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        print(r" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ MULTI DECODER  / / / / / / / / / / / / / / / / / ")
        print(r"\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
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
        print(r"     _      ____     ____   ___   ___    ___    ____   ")
        print(r"    / \    / ___|   / ___| |_ _| |_ _|  ( _ )  | ___|  ")
        print(r"   / _ \   \___ \  | |      | |   | |   / _ \  |___ \  ")
        print(r"  / ___ \   ___) | | |___   | |   | |  | (_) |  ___) | ")
        print(r" /_/   \_\ |____/   \____| |___| |___|  \___/  |____/  ")
        print("----------------------------------------------------------","\n") 
        print("The translation of the input is:","\n","- ",output85,"\n")

    def HexDISPLAY(Hex):
        print("")
        print("")
        print(r"   _   _   _____  __  __ ")
        print(r"  | | | | | ____| \ \/ / ")
        print(r"  | |_| | |  _|    \  /  ")
        print(r"  |  _  | | |___   /  \  ")
        print(r"  |_| |_| |_____| /_/\_\ ")
        print("---------------------------","\n")    
        print("The translation of the input is:","\n","- ",Hex,"\n")

    def ASCDISPLAY(Ascii):
        print("")
        print(r"     _      ____     ____   ___   ___  ")
        print(r"    / \    / ___|   / ___| |_ _| |_ _| ")
        print(r"   / _ \   \___ \  | |      | |   | |  ")
        print(r"  / ___ \   ___) | | |___   | |   | |  ")
        print(r" /_/   \_\ |____/   \____| |___| |___| ")
        print("------------------------------------------","\n")
        print("The translation of the input is:","\n","- ",Ascii,"\n")

    def BinDISPLAY(Binary):
        print("")
        print(r"   ____    _                                 ")
        print(r"  | __ )  (_)  _ __     __ _   _ __   _   _  ")
        print(r"  |  _ \  | | | '_ \   / _` | | '__| | | | | ")
        print(r"  | |_) | | | | | | | | (_| | | |    | |_| | ")
        print(r"  |____/  |_| |_| |_|  \__,_| |_|     \__, | ")
        print(r"                                      |___/  ")
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

    match EDchoice:
        case "e":
            Encode()
        case "d":
            Decode()
        case "q":
            sys.exit("Quitting Program")
        case _:
            print(" - - - - - - - - - - INVALID INPUT - - - - - - - - - - ")
            input("press ENTER to continue")

##    if EDchoice == "e":
##        Encode()
##    elif EDchoice == "d":
##        Decode()
##    else:
##        print(" - - - - - - - - - - INVALID INPUT - - - - - - - - - - ")
##        input("press ENTER to continue")
##        print("")


# Loop for multiple uses #
Main()
choice = str(input("Would you like another translation (y/n): "))

while (choice != "n"):
    match choice:
        case "y":
            Main()
            choice = str(input("Would you like another translation (y/n): "))
        case "n":
            sys.exit("Quitting Program")
        case "":
            print(" - - - - - - - - - - INVALID INPUT - - - - - - - - - - ")
            choice = str(input("Would you like another translation (y/n): "))
        
##while (choice == "y"):
##    if choice == "n":
##        sys.exit("Quitting Program")
##        break
##    else:
##        Main()
##        choice = str(input("Would you like another translation (y/n): "))

            
print("\n----- Program Ended -----")
    
