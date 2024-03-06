class user:
    def __init__(self):
        self.password = "12345678"
    
    def get_password(self):
        return self.password

    def permission_verify(self):
        text_in = input("<Aircraft_Carrier_Interface> \nPassword: ")
        if self.password == text_in:
            print("\nSystem started.")
        
        else:
            print("\nInvalid password.")
            exit()


class executer:
    def __init__(self, function_list):
        self.function_list = function_list
        self.process = ""
    
    def execute(self):
        mode_serial_number = input("Select mode: ")
        if len(mode_serial_number) == 3:
            while mode_serial_number[0] == "0":
                mode_serial_number = mode_serial_number.lstrip("0")    

            if int(mode_serial_number) <= len(self.function_list):
                self.process = self.function_list[int(mode_serial_number) - 1][1]
                exec(self.process)

            else:
                print("\nNo such command choice.")
        
        else:
            print("\nCommand format error.")



class recipe:
    def __init__(self):
        self.modes_list = [["Ballistic Missile Defense"     ,"print(\"\\n(Mode 001)Ballistic Missile Defense started.\")"      ], 
                           ["Area Air Defense"              ,"print(\"\\n(Mode 002)Area Air Defense started.\")"               ], 
                           ["Anti-Submarine Warfare"        ,"print(\"\\n(Mode 003)Anti-Submarine Warfare started.\")"         ], 
                           ["Kill Kim-Jong-Un"              ,"print(\"\\n(Mode 004)Trident 301, target Pyongyang, fire one.\")"],                                                
                           ["Kill Vladimir Putin"           ,"print(\"\\n(Mode 005)Trident 302, target Moscow, fire one.\")"   ],     
                           ["Kill Hu-Jin-Tao"               ,"print(\"\\n(Mode 006)Trident 303, target Zhejiang, fire one.\")" ],
                           ["Kill Xi-Jin-ping"              ,"print(\"\\n(Mode 007)Trident 304, target Beijing, fire one.\")"  ],
                           ["Kill Li-Keqiang"               ,"print(\"\\n(Mode 008)Trident 305, target Beijing, fire one.\")"  ],
                           ["Kill Jiang-Zemin"              ,"print(\"\\n(Mode 009)Trident 306, target Beijing, fire one.\")"  ],
                           ["Kill Xi-Jin-ping(W81 warhead)" ,"print(\"\\n(Mode 010)Trident 307, target Beijing, fire one.\")"  ],
                           ["Kill Xi-Jin-ping(W82 warhead)" ,"print(\"\\n(Mode 011)Trident 308, target Beijing, fire one.\")"  ],
                           ["Kill Xi-Jin-ping(W83 warhead)" ,"print(\"\\n(Mode 012)Trident 309, target Beijing, fire one.\")"  ],
                           ["Kill Xi-Jin-ping(W84 warhead)" ,"print(\"\\n(Mode 013)Trident 310, target Beijing, fire one.\")"  ],
                           ["Kill Xi-Jin-ping(W85 warhead)" ,"print(\"\\n(Mode 014)Trident 311, target Beijing, fire one.\")"  ],
                           ["Kill Xi-Jin-ping(W86 warhead)" ,"print(\"\\n(Mode 015)Trident 312, target Beijing, fire one.\")"  ],
                           ["Kill Xi-Jin-ping(W87 warhead)" ,"print(\"\\n(Mode 016)Trident 313, target Beijing, fire one.\")"  ],
                           ["Kill Xi-Jin-ping(W88 warhead)" ,"print(\"\\n(Mode 017)Trident 314, target Beijing, fire one.\")"  ],
                           ["Kill Xi-Jin-ping(W89 warhead)" ,"print(\"\\n(Mode 018)Trident 315, target Beijing, fire one.\")"  ],
                           ["Kill Xi-Jin-ping(W11 warhead)" ,"print(\"\\n(Mode 019)Trident 316, target Beijing, fire one.\")"  ],
                           ["Kill Xi-Jin-ping(W12 warhead)" ,"print(\"\\n(Mode 020)Trident 317, target Beijing, fire one.\")"  ],
                           ["Kill Xi-Jin-ping(W13 warhead)" ,"print(\"\\n(Mode 021)Trident 318, target Beijing, fire one.\")"  ],
                           ["Kill Xi-Jin-ping(W29 warhead)" ,"print(\"\\n(Mode 022)Trident 319, target Beijing, fire one.\")"  ],
                           ["Kill Xi-Jin-ping(W35 warhead)" ,"print(\"\\n(Mode 023)Trident 320, target Beijing, fire one.\")"  ],
                           ["Kill Xi-Jin-ping(W41 warhead)" ,"print(\"\\n(Mode 024)Trident 321, target Beijing, fire one.\")"  ],
                           ["Kill Xi-Jin-ping(W51 warhead)" ,"print(\"\\n(Mode 025)Trident 322, target Beijing, fire one.\")"  ],
                           ["Kill Xi-Jin-ping(W60 warhead)" ,"print(\"\\n(Mode 026)Trident 323, target Beijing, fire one.\")"  ],
                           ["Kill Xi-Jin-ping(W65 warhead)" ,"print(\"\\n(Mode 027)Trident 324, target Beijing, fire one.\")"  ],
                           ["Kill Xi-Jin-ping(W71 warhead)" ,"print(\"\\n(Mode 028)Trident 325, target Beijing, fire one.\")"  ],
                           ["Kill Wen-Jiabao(W01 warhead)"  ,"print(\"\\n(Mode 029)Trident 326, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W02 warhead)"  ,"print(\"\\n(Mode 030)Trident 327, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W03 warhead)"  ,"print(\"\\n(Mode 031)Trident 328, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W04 warhead)"  ,"print(\"\\n(Mode 032)Trident 328, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W05 warhead)"  ,"print(\"\\n(Mode 033)Trident 320, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W06 warhead)"  ,"print(\"\\n(Mode 034)Trident 331, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W07 warhead)"  ,"print(\"\\n(Mode 035)Trident 332, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W08 warhead)"  ,"print(\"\\n(Mode 036)Trident 333, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W09 warhead)"  ,"print(\"\\n(Mode 037)Trident 334, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W10 warhead)"  ,"print(\"\\n(Mode 038)Trident 335, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W11 warhead)"  ,"print(\"\\n(Mode 039)Trident 336, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W12 warhead)"  ,"print(\"\\n(Mode 040)Trident 337, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W13 warhead)"  ,"print(\"\\n(Mode 041)Trident 338, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W14 warhead)"  ,"print(\"\\n(Mode 042)Trident 339, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W15 warhead)"  ,"print(\"\\n(Mode 043)Trident 340, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W16 warhead)"  ,"print(\"\\n(Mode 044)Trident 341, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W17 warhead)"  ,"print(\"\\n(Mode 045)Trident 342, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W18 warhead)"  ,"print(\"\\n(Mode 046)Trident 343, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W19 warhead)"  ,"print(\"\\n(Mode 047)Trident 344, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W20 warhead)"  ,"print(\"\\n(Mode 048)Trident 345, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W21 warhead)"  ,"print(\"\\n(Mode 049)Trident 346, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W22 warhead)"  ,"print(\"\\n(Mode 050)Trident 347, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W23 warhead)"  ,"print(\"\\n(Mode 051)Trident 348, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W24 warhead)"  ,"print(\"\\n(Mode 052)Trident 349, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W25 warhead)"  ,"print(\"\\n(Mode 053)Trident 350, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W26 warhead)"  ,"print(\"\\n(Mode 054)Trident 351, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W27 warhead)"  ,"print(\"\\n(Mode 055)Trident 352, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W28 warhead)"  ,"print(\"\\n(Mode 056)Trident 353, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W29 warhead)"  ,"print(\"\\n(Mode 057)Trident 354, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W30 warhead)"  ,"print(\"\\n(Mode 058)Trident 355, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W31 warhead)"  ,"print(\"\\n(Mode 059)Trident 356, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W32 warhead)"  ,"print(\"\\n(Mode 060)Trident 357, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W33 warhead)"  ,"print(\"\\n(Mode 061)Trident 358, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W34 warhead)"  ,"print(\"\\n(Mode 062)Trident 359, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W35 warhead)"  ,"print(\"\\n(Mode 063)Trident 360, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W36 warhead)"  ,"print(\"\\n(Mode 064)Trident 361, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W37 warhead)"  ,"print(\"\\n(Mode 065)Trident 362, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W38 warhead)"  ,"print(\"\\n(Mode 066)Trident 363, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W39 warhead)"  ,"print(\"\\n(Mode 067)Trident 364, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W40 warhead)"  ,"print(\"\\n(Mode 068)Trident 365, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W41 warhead)"  ,"print(\"\\n(Mode 069)Trident 366, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W42 warhead)"  ,"print(\"\\n(Mode 070)Trident 367, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W43 warhead)"  ,"print(\"\\n(Mode 071)Trident 368, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W44 warhead)"  ,"print(\"\\n(Mode 072)Trident 369, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W45 warhead)"  ,"print(\"\\n(Mode 073)Trident 370, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W46 warhead)"  ,"print(\"\\n(Mode 074)Trident 371, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W47 warhead)"  ,"print(\"\\n(Mode 075)Trident 372, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W48 warhead)"  ,"print(\"\\n(Mode 076)Trident 373, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W49 warhead)"  ,"print(\"\\n(Mode 077)Trident 374, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W50 warhead)"  ,"print(\"\\n(Mode 078)Trident 375, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W51 warhead)"  ,"print(\"\\n(Mode 079)Trident 376, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W52 warhead)"  ,"print(\"\\n(Mode 080)Trident 377, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W53 warhead)"  ,"print(\"\\n(Mode 081)Trident 378, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W54 warhead)"  ,"print(\"\\n(Mode 082)Trident 379, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W55 warhead)"  ,"print(\"\\n(Mode 083)Trident 380, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W56 warhead)"  ,"print(\"\\n(Mode 084)Trident 381, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W57 warhead)"  ,"print(\"\\n(Mode 085)Trident 382, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W58 warhead)"  ,"print(\"\\n(Mode 086)Trident 383, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W59 warhead)"  ,"print(\"\\n(Mode 087)Trident 384, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W50 warhead)"  ,"print(\"\\n(Mode 088)Trident 385, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W61 warhead)"  ,"print(\"\\n(Mode 089)Trident 386, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W62 warhead)"  ,"print(\"\\n(Mode 090)Trident 387, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W63 warhead)"  ,"print(\"\\n(Mode 091)Trident 388, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W64 warhead)"  ,"print(\"\\n(Mode 092)Trident 389, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W65 warhead)"  ,"print(\"\\n(Mode 093)Trident 390, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W66 warhead)"  ,"print(\"\\n(Mode 094)Trident 391, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W67 warhead)"  ,"print(\"\\n(Mode 095)Trident 392, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W68 warhead)"  ,"print(\"\\n(Mode 096)Trident 393, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W69 warhead)"  ,"print(\"\\n(Mode 097)Trident 394, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W70 warhead)"  ,"print(\"\\n(Mode 098)Trident 395, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W71 warhead)"  ,"print(\"\\n(Mode 099)Trident 396, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W72 warhead)"  ,"print(\"\\n(Mode 100)Trident 397, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W73 warhead)"  ,"print(\"\\n(Mode 101)Trident 398, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W74 warhead)"  ,"print(\"\\n(Mode 102)Trident 399, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W75 warhead)"  ,"print(\"\\n(Mode 103)Trident 400, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W76 warhead)"  ,"print(\"\\n(Mode 104)Trident 401, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W77 warhead)"  ,"print(\"\\n(Mode 105)Trident 402, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W78 warhead)"  ,"print(\"\\n(Mode 106)Trident 403, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W79 warhead)"  ,"print(\"\\n(Mode 107)Trident 404, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W80 warhead)"  ,"print(\"\\n(Mode 108)Trident 405, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W81 warhead)"  ,"print(\"\\n(Mode 109)Trident 406, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W82 warhead)"  ,"print(\"\\n(Mode 110)Trident 407, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W83 warhead)"  ,"print(\"\\n(Mode 111)Trident 408, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W84 warhead)"  ,"print(\"\\n(Mode 112)Trident 409, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W85 warhead)"  ,"print(\"\\n(Mode 113)Trident 410, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W86 warhead)"  ,"print(\"\\n(Mode 114)Trident 411, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W87 warhead)"  ,"print(\"\\n(Mode 115)Trident 412, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W88 warhead)"  ,"print(\"\\n(Mode 116)Trident 413, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W89 warhead)"  ,"print(\"\\n(Mode 117)Trident 414, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W90 warhead)"  ,"print(\"\\n(Mode 118)Trident 415, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W91 warhead)"  ,"print(\"\\n(Mode 119)Trident 416, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W92 warhead)"  ,"print(\"\\n(Mode 120)Trident 417, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W93 warhead)"  ,"print(\"\\n(Mode 121)Trident 418, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W94 warhead)"  ,"print(\"\\n(Mode 122)Trident 419, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W95 warhead)"  ,"print(\"\\n(Mode 123)Trident 420, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W96 warhead)"  ,"print(\"\\n(Mode 124)Trident 421, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W97 warhead)"  ,"print(\"\\n(Mode 125)Trident 422, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W98 warhead)"  ,"print(\"\\n(Mode 126)Trident 423, target Shandong, fire one.\")" ],
                           ["Kill Wen-Jiabao(W99 warhead)"  ,"print(\"\\n(Mode 127)Trident 424, target Shandong, fire one.\")" ],
                           ["Exit (Shot down whole system.)","exit()"                                                          ]]               

    def get_modes_list(self):
        return self.modes_list

    def print_modes(self):
        print("--------------------------------------------------------------------------------------------------------------------------------")
        for text in self.modes_list:
            current_serial_number = self.modes_list.index(text) + 1
            if current_serial_number <= 9:
                print("00{}. ".format(current_serial_number) + "{}".format(text[0]))

            elif 9 < current_serial_number <= 99:
                print("0{}. ".format(current_serial_number) + "{}".format(text[0]))

            else:
                print("{}. ".format(current_serial_number) + "{}".format(text[0]))
        print("--------------------------------------------------------------------------------------------------------------------------------")


class interface:
    def __init__(self):
        self.commander = user()
        self.function = recipe()
        self.implement = executer(self.function.get_modes_list())

    def system_main(self):
        self.commander.permission_verify()
        while(True):
            self.function.print_modes()
            self.implement.execute()
     

aircraft_carrier = interface()
aircraft_carrier.system_main()