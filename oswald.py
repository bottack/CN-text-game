def start():
  # give some prompts.
  print("""
/*///****/#&%@@@@@&&&&&%#%%&%%((#/(#%%%%(((#(#(//(/((#&&@&%##(#%&&&&&@@@@@@%&&##%#(%/%%%###%#%@&@@@@
//////**(&&@@@@@@@&@&@&&&%&&##(#%#%(&%%%%/(#%&@@#%%(//(#%&#(/#&%&%&@@@@@&@@@&%%%(%%(%%%&@%#%%%%&&%@@
////**/#&@@@@@@@@@@@@@@@@&&##%####%(%%%(%##%#/((&&&&&#(#(((((#&@&&@@@@@@@@%/((#%###(%%(%%&&%&&%%&&%@
//////%@@@@@@@@@@@@@@@@@@%@&&#%%#/(((%##%&%#(###(/#%&@%%%%%&#&#%%&@@@@@&#%///####%&&&@%##&%@@&%&%%&&
/*/////&@@@@@@@@@@@@@@@@@@&@&&&&&&&%&%%%#%%%&/(##((/#%&@@%@@@&@&@@&@%##&&&%%%&&&&&&&#&&@@@&&&&&&&%##
//////#@@@@@@@@@@@@@@@@%@%&@@@@@@@&@@@&&@@&&#(#(///#%%%%&@@&@@@@&&&%###%%#%#%%&&&&&&%@&&@@&&&&&%%//#
//////@@@@@@@@@@@@@@@@@@@@&&@@@@@@@@@@&&&&&(&%%#(/((%%&@@@@@@&&&%(%##(((/#(%#%#&&&&@&&&&&&&%&%##%###
/*///&@@@@@@@@@@@@@@@@@@@@@@&@%&%%%&&&%@@@&&&@&&##%%&&#@@@@@@@&%%%#(%#((####%%&&&%&&@&&&@&%%##((##(%
////(@@@@@@@@@@@@@@@@@@@@@@@&@&&@@@@&@@@@@&@&&&&&%&/%%@@@&&&&&&&&&%%%%%####&&&&&&&&&&&&&&&%#(((((((#
////(@&(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%&&%&@&&&&%%%%%%&%%%%%%(#(((##%%&&&&&&&&&&&&&&%%#%##(#(#
//////(@@@@@@@@@@@@@@@@@&%&&&@@@@@&@@@&@&@@&@&&&&&&&%##((/(((/((////*/##%%&&&&&@&@@&&%%###(((((((%##
//////&@@@@ @@@@@     %%%%  %#  ###%%%&@@&&&&%%&%%%##((((((/*******//##%%%&%&&&&%%%%###(#(/(/(/(((/(
///////%@@@ @@@@@  &%%%###  (/ ((/((((#%#%%%%##//////**/**********/((((####%%#(((/(/(/(/*/////((((((
///////(@@@ @@@@&  &%%####  ( //(///////((///***////*****,,,,,,,,,*,,,**///(/***/////(//////(/(#####
////////&@@ @@@@@  &&#%%##    (((/////*/////////////*****,,,,*,,,,,*,,,,**,*******/*/////////(((#(#%
**///*/(&@@ @@@@@     %###    ((((////******,***,,,,,****,,****,,,,,,,*,******/****///////////(#%%#%
//*/****/@@ @&@@@  &&&%%##  # .(((//////*****,*,*******,,**,,*,,,*,,,***,*********,*******////#####%
/////////&@ @&&@@  @@&%%##  (  ///((////**/******,,*,,**,*,*************,*****,***,******///((##((%%
//////////@ @@&@@  &&&%###  //  */**///////******/********************///*//////*****,*****/((((####
////////    @@@@@  &&&%#((  //  ////**////**//////(///////////////((((#%%%%%%#(#(///*////////(#((###
////*/*/*//(%@@@@@@&&%#(//(((/////((##%%%#######(#(/(///*/**(((##%%&&&&&&&&&%%%#(#%(##(((((((#((#(%%
//////*******@@@@@&&&%####(#(#(#%#%%%%&&@&@&&&&&&&%(///****/(((%&&&&&@&&%////******//(((####%%###%##
//////*//****/@@@@&&&&&%&&&%%%%%(//////(#&&@@@@@@@&(//**,***//(%&@@@&&&&&#%&&&&&@&&%&%####%##%%%####
//////*****/*/%&@@&&&&@@@&&%%%#%&@@&@@@@@@@@@@@@@@&//*******/(%&&&&&%##%#**(#&@@@@&@&&%@&%#%&&%#####
//***/**/(##(**@@&%&&@@@@@@@@%&&@@@@@@@&#(/(&&%((#(//**,,****/(#(/*/%#/*****((#%##%##%#(#%&%%#(#((((
/*////*%#(####&@@&%%&&&&@@&@@@@&%##&%&##///////*/((/********///((******////**,,,**///((%((***//*/**/
**/////&@@@@&&%@&%%%%####((%%#((//****//////#(*//((/**,,,,**//////**//((###(////((#%&%%(/***,*******
///////#&@@@@@@@&##%((((((((#%&%%###(%##((//**/((//*********/////////****//*//((//****,,,,,,,*******
///*///#(%@&&%@@@%%#((//*//***//////////***/*/((//***,,,,**/****//*//*********,,*,,,,,,,,,,,,,,,****
///////(// #/ # @& ## ( //* .* ***,*//***/*///((//***,,,********//////**,,*,*,,,,,,,,,,,,*,*,,****/*
//////////*##(##&%%%#(((///*/*/****/****/*///(((//*,,,,*,*********///***,*,,,,,,,,,,,,,****,*****//(
////////(//#(*/(#%%%%#(((//(////********/////(///***,,,,***********//****,,*,,*,,,,,*,,**,****//((((
*//////*/# . ** /(&&/ ((/(((( ///*/////*//*//(((##///**/*((#((///**//*********,*,********/**/((((((#
/////////*(/%////(/@&&%%#((((////////*//////(#%%&&&&%%%&&&&&&&&%%%###(*******,******/****//((((%(#(#
///////**// ( &.#/(@@.@%%#### ((((///////*/*/&&&@@@@@@@@@@@@@@@@&&&&%#*************/***///((/((#####
/////*//**///#(#&##@@@&&&&%###(((((///////**/&@@@@@@@@@@@@@@@@@@@@@&&/****,********///*////(#((##(#%
////*//////*/*/#%&%&@@&%&%&%#%##(((/(//*/***/%&@@@@@@@@@@@@&%((///************,*****////*//((((((#%%
///////////*/*./ /&@@ @&&,%%%##((((/////*////////(#%&@@@@@%/************************//*//*//(/((##%&
//////*/*/**/**/////&&@@&%%###((/(((////////////////*//(////***////*****//*******/****/**(/((/((###%
///////////*  /*////(&&&@.%%#(#(((//////(//(///((/******,****,**/***/(*/*//////*/******///////((####
////////**///*/***/*/&&&&&%##(#((((//(((/(((((////(((///****/(#%%##(///((((((((/////***/////#(######
/*///*/////*/*//**/**&&%%%%&%###((((((#/###(##%&&&&%%####%#######%#%%%%&&&&&&&%#((////*///((((####%(
///////*////*//******/&%&&&&&###((((((#%&@@@@@@@@@&@@@&&&@@&@@&&&@&@&&&&&&&&%#%&&#(///*//(#(%##(###%
///////**/*/***/******&&&&&&&&%##((/((%&@&%#(((//**/*//*,********/**/**///////***///////((########%#
////////*/********/*//*@&&&&&&&%%#((/(/**((####(////******,***//**///(#((##(/*//*///*//((%%%%#%%##&&
*///////*/*//***/*/*****&@&&@&@@&%##(/////(/((##%##%#%%####%%%%%%%%%%####(//////****//(#&&&&%%%%&&&&
/////////////*/*******//*/@@@@@@@@&%##((//////((###%%&%%&&&&&&&&&&&%##(((///*/****///(%&&&&%%&&&@@@@
//////////**/*/*/****//****/@@@@@@@@@&##((((/((/((((###%%%%%&%%###((////**//*/*////(#%&@&&&%&&&&@@@&
//////////////*/************/*@@@@@@@&&###(//////*********,,,,,*,,**,**,,*****//(((%%&&&&&%&@@@@&@@@
///////***/*///*/*******/*******&@@@@@@%%#(////*****,,,,,**,*,,,,*,,*,**,**/**///(#%&&&&&&@@@&@@@@@@
////////// ***.* ** / *,.*.* ******&@@@&#(#((////************/**,***,******///((#%%&&@@@&@@@@@@@@@@@
/////*///*/////*******/*************&@@@@@%%(#////********************/*/*//((#%&@@@@&&@@@@@@@@@@@@@
//***//**/*  **  */ * * **** **,,***#&@@@&@&%%#((((///******////**//////(((#%%&&&@&&@@@@@@@@@@@@@@@@
//////*/  *  /*  */ ** *****  *  ****&@@@@@@@&&&%#(###(##((((###(#####%#%&&@&&&&@@@@@@@@@@@@@@@@@@@@
*/////****/**/************************@@@@@@@@@@@@@&@@&&@@@&&&@@@&&@&@&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@
//**///********************,,,*********&@@@@@@@@@@@@@@@&&&&&&@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
//////*//////*/************************&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
/////*@****@***&*@*@*@***(*/@**,*,******@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
//*******/************************(%%&@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
**/****************/#####%%%%%&&&&&&@&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
**/******(#%#%#%%%%%%%%%%%&&%&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
""")
  print("\n	November 22, 1963. Dallas, Texas.")
  print("\nYou are John Fitzgerald Kennedy, the 35th president of the United States. You are in Dallas to try to smooth over relations between bickering politicians.")
  print("\nYou are travelling through downtown Dallas in the back of a convertible. You are surrounded by security, and there is a crowd cheering and waving flags.")
  print("\nIt is just like many other events just like it. You are surrounded by secret service security agents. despite this,")
  print("\nYou feel anxious and unsettled. You recently recieved intelligence that the Soviet Union has obtained compromising material on you")
  print("\nThere are those, even in your own intelligence agencies, who, you are sure, would see you removed from power, fearing that you may be blackmailed.")
  print("\nWhat do you do?")
  print("\n1)Smile and wave to the crowd.")
  print("\n2)Wave to the crowd and smile") 
  print("\n3)scan the crowd, and the people around you")
  # convert the player's input() to lower_case
  answer = input(">").lower()

  if "1" in answer:
    # if player typed "1" lead him to NEXT ROOM()
   jfk1_1()
  elif "2" in answer:
    # else if player typed "2" lead him to NEXT ROOM()
    jfk1_1()
  elif "3" in answer:
    # else if player typed "3" orlead him to NEXT ROOM()
    jfk1_2()
  else:
    # else call game_over() function with the "reason" argument
    game_over("INSERT REASON HERE")

# game_over function accepts an argument called "reason"
def game_over(reason):
  # print the "reason" in a new line (\n)
  print("\n" + reason)
  print("Game Over!")
  # ask player to play again or not by activating play_again() function
  play_again()

  # function to ask play again or not
def play_again():
  print("\nDo you want to play again? (y or n)")
  
  # convert the player's input to lower_case
  answer = input(">").lower()

  if "y" in answer:
    # if player typed "yes" or "y" start the game from the beginning
    start()
  else:
    # if user types anything besides "yes" or "y", exit() the program
    exit()

# NEXT_ROOM
def jfk1_1():
  # some prompts
  # '\n' is to print the line in a new line
  print("\n You smile and wave to the crowd. Your wife Jackie does the same. You look out at the sea of waving flags and cheering figures, and the scene takes on a sinister tone.")
  print("\n You can't put your finger on it, but you feel like something bad is going to happen.")
  print("\nWhat do you do?")
  print("\n1) Smile and wave.")
  print("\n2) Wave and smile.")

  # take input()
  answer = input(">")

  if answer == "1":
    jfk_death()
  elif answer == "2":
   jfk_death()

def jfk1_2():
  # some prompts
  # '\n' is to print the line in a new line
  print("\n You decide that you shouldn't ignore the discomfiting feeling that you're in danger")
  print("\n You look first, at your security detail. They are mostly watching the crowd. Everyone seems relatively relaxed.")
  print("\n Next, you look around. behind you is a large square office building. A book despository or library. A window is open on the sixth floor.")
  print("\n You look to your right and you see a crowd of families. A couple of people are filming you.")
  print("\n You look to your left, and you see more families watching the procession. You do not notice any threat. You still feel discomfited.")
  print("\nWhat do you do?")
  print("\n1) Smile and wave")
  print("\n2) Wave and smile.")
  # take input()
  answer = input(">").lower()

  if answer == "1":
    # lead him to the NEXT ROOM()
    jfk_death()
  elif answer == "2":
    jfk_death()

def jfk_death():
  # some prompts
  # '\n' is to print the line in a new line
  print("\nSuddenly, you feel like you've been punched hard in your back. You try to exclaim, but you cannot. You look at your wife. She looks horrified.")
  print("\nYou raise your hands to your throat, and they come away wet with blood. You look desperately to your secret service agents, who are now scrambling towards you to protect you. Your driver also looks to have been shot.")
  print("\nBefore anyone can reach you, your world goes black. You have been shot in the head, and you are dead. The last thing you hear is the scream of your wife.")
  print("\n Do you want to continue? Y or N.")
  # take input()
  answer = input("Continue? Y or N").upper()

  if answer == "Y":
    # lead him to the NEXT ROOM()
    oswald1_1()

  else:
    # game_over() with "reason"
    game_over("Thanks for playing! That was only the intro though. if you continue, there is a whole longer story.")

def oswald1_1():
  # some prompts
  # '\n' is to print the line in a new line
  print("""
  .   .        .   . ..  ..................   ....... ................./(%##,.........................
 . .            ..... ... .......... ........ ...... ..........,*,(#*#/..,...*......................
.......  ...    .  .   ...   . ......  . .  ............,/.,//#*&%##*(%@%%%*&*.(*../(...............
  .  .. ......       .. ..... .....  ...............**,*%&%(#*(#//#,%&(&&%#@&%#&(/&/@%#(,...........
. ..   . .......  .. .  . ...  ......... .... *(&#&&&@/&#//*#&&%#&@%#@(%#%%#(/@&&&&&@@,%&*..........
 . ...    ..   .. . ...... ...... .  .... ..%%&&%@&%#%#((%%%&&&&&&&@@#%@(%%(*/*./(%&&@@&&@**........
.  .....  ...   ...... ..... ...... ....../&&@@@@%#@@@&@%&&@##&@&@&@@&*###(,,..,...,/&#@@@&(&,......
.. ........  ..... . . .. .. ...........#(&&&&%%%(&@&&@&@@@%&&&&@&#(*,..,.*.,...........,#&&&&#.....
. ......      .   ..  ................/&@@&&&&&@(@&@@@@@&%/.....,.........................,(@%@&/...
... . .. . .  .   . . . ......... ... @@@@&@&(*,.,*,.............................  ......../@@@@@&#.
  ... .. .  .. . .    .   .......... @&@@@@@#.,.................................... ........*&&@&@@&
.  ..   .  .  .    . .. ....... ....&&@@@@&/,..............................................,(@@@@@@&
.. ..........  . .... ............. @@@@&@,.,,,.,............................................*&&@@&@
....  ... .......... ... .......... @@@@@%,,,,..*............................................,#@@&@@
....... .... .  ..  .... .....,.... &@@@@&**,,,,%,..........................................,,(&@@@&
... ...  ..   .. .  ....  .........*@@@@@&&/,*,//,.................,.......................,,*#&&@@@
......  ....  .   . ... ...........(@@@@@@&#,.,,,....................................,.....,/(@@@@@#
.....  .....      . ........ .......&@@@@@&*,,,,*((**/%&(,......................*,,,,......,##&&&@@%
......... ..... .   . ... .......... &@@@@*,.*@&//,.,/#@@@@@&@%*.......*%@&&@&/,.....,/&#.../&&@@&@.
........ .      .    . ..............%@@@&..,(*,(@&&@&@%@/@&&%/,.......*&@@@@@@@&@/,,,*,,,..(&&@@&..
 . .        .     . . .     ......##,#@@@,...,,/(*/*......,/.,,,.....*,,,@/***&&&(@@@@%/,,../@@@@...
. ..     ..                   ...@%,,.(@...................,,...,....,*,.*,,,,,*/**(%@@@*...,@&@%, .
...     ..          ...  .     ..#.**../......................,,.....,*............,.,,......(@,.*&@
..      .        .   .   .    ...,,*,*&/,...................,,.......,*............................&
  ...                 .    .   . ..,.%&.(.....................,........,,...................,.&*.,,,
....  .. . .    .   ..  .         .,,,,,,...,,.............,,,,..........,,.............,,,...#/..,.
....     . ...       .  . . ....   .....*....,............. @@%%(/**@@&@/.,,............,,...,,..,..
  ...    . .     .    ..     .    . *....,,,...............,,*,,,**,///,................,,,,,.......
  ... .  .... .      .  .. .   .. .... ,.,/..,...........,,,,,....,....,,*...........,..,,*.,.......
&@&&@&&&&&@&@@@@@@@@@@@@@@@@@@@@@@@.......***,.......,,*,................,,,.,/......,,,,*..........
&&@&@@ &.(.@@ @&@ @@@&**@* @@@@@@&@ ....../*,,.,.,...**,.*(,./&@@@@@&#/,(/*((..,..,..**,,...........
@@@@@@@@&@@@@@@@@@@@@@@@&&@@&@@&@&@ ...... #*,.*.*.,....,.,.......,,,,.,.,....,.,,,,,,..,...........
@@@@@@ . @. @ %@@& &/. @&.&@@@@@@&@......../(**,.,,,**,,,*,*(#%@&&&&(*,,,..,.,,,*,,,,..,............
@@@@@& @@&. @ /*@@ #(, &@ %(@@@@@@@........(/((*,.,*,..,......,.,,....,..,,((,,**,*,,...............
@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@&@.... ...*,,,/(*,,,,....,,........,..,,**,,*,,/,,,,...............
/.@&@@&@@..,@@.#@(.@& . &@.(@#.@@&@ ......*,.,,,,((#*,.,,,,,.....,,......,,,***,,...................
&&*( .@ . ../@.%@&.@@@ .@@.   .@&%@. . . ./,,,,,,/*,,*#,,*..*,.,***,.,*//((*,,,,,,.,,,..............
@%   @@&@@  @@@   @@@@ *@&....,&@@@ ......,,,,,,.,.,..,,*(&&%@&@&&%((#&/*,,,,....,..,...............
&@%.@ @@@@&@@**,%@ @@@@@ .#@@ @@@@@ ...............,.....,,//((((/#/*,.,........,...................
&@% & @@@@@@@   @  @@@@@% #@..@@@@&    (,.........,..........,..,.,..,.......,......................""")
  print("\n November 22, 1963. Dallas, Texas.")
  print("\n You are Lee Harvey Oswald, an ex-marine.")
  print("\nUntil recently, you lived in Belarus after defecting to the Soviet Union. There, you met a wife.")
  print("\nYou found life in the Soviet Union to be dreary. You worked hard but had little to do other than work, and you didn't make many friends")
  print("\nYou requested to return to the US. In exchange for dropping the charges against you for betraying your country,")
  print("\n you were told you would have to do something for the government. At the time, you agreed. How bad could it be?")
  print("\n It wasn't until you met your CIA handler, 'Mr Gray' that you realised you may be in over your head")
  print("\n He told you that if you wanted to live free in the US with your Belarussian wife, you had to do kill the president.")
  print("\n That is how you have found yourself on the sixth floor of the Dallas book depository. You got a job here to faciltate your plot.")
  print("\n You have a 6.5mm Carcano rifle with a hunting scope. It was provided by your handler.")
  print("\n The weight of what you're about to do is crushing. You never imagined being in a situation like this. You are nervous and excited.")
  print("\n What do you do?")
  print("\n 1)Steel your nerves.")
  print("\n 2)Check your rifle.")

  # take input()
  answer = input()
  if answer == "1":
     oswald_nerves()
  elif answer == "2":
     oswald_rifle()

def oswald_nerves():
    print("\nYou try to calm down. You try to focus on the task ahead of you. You can't get the idea out of your head that you may be here as a set-up.")
    print("\n Even if you shoot the president, how are you going to get away with it?")
    print("\n You were told that if you don't do it, someone else will, and you will still get the blame.")
    print("\n You try to put your misgivings aside. you feel panic rising in your chest.")
    print("\n What do you do?")
    print("\n 1)Take deep breaths, remember your military training")
    print("\n 2)Focus on the enormity of what you're about to do.")
    
    answer = input()
    if answer == "1":
     oswald_shoot()
    elif answer == "2":
     oswald_panic()

def oswald_panic():
    print("""
    *,,.....                                              %#%%#%&%*..............,,,
,......                                            %&&@&&&&&&&@&%&.............,
.....                                      ..   .%%&&&%&&&&&@&&@%@%%............
....                                      .... &&&&&&&&&&&@@%&&&&&%&&...........
...                                     ......*@@&&&&@&&&&,*,*.#%&&%&&,.        
..                                     ./......../(%%#%&@(,,%//,..,,,,,,, *#..  
.                                      .#(*,,.....(/**(###%%,,*......,.,*(..... 
.                                      ./&%**,,,.##(/***,,*,*,,,,,,..,,/,,...,,*
                                       .*(//..,**/&&(%/*,,*//*,,*,***(*.,,,,(/**
                                        ....,,,. ,/(&/((**,///*(/(#%#,,,,,*(////
                                          ......      ,/((%(%/##%@&/,,,,,,*(*///
                                            .. .           *%#&/&#(/*(((/*#///*/
                                             ..                /(/#/#(#/////*///
                                             ..                    /(*%////**/**
.                                             .                     /*//****///*
..                                          ...                     (#*/****////
...                                        ....                     */*(/**/////
...                                      ......                      (/*//(/////
....                                    ........                     *#*#**///(#""")
    print("\nYou think about how world history is going to pivot around your actions in the next few minutes. You hear the motorcade getting closer. You have a panic attack. Your heart is racing, you are shaking, your arms are tingling, and you feel like you are suffocating.")
    print("\nYou need to calm down, or you won't be able to do anything.")
    print("\n What do you do?")
    print("\n1)Breathing exercises")
    print("\n2)Light a cigarette and focus on a comforting memory")
    answer = input()
    if answer == "1":
        oswald_nerves()
    elif answer == "2":
        oswald_nerves()

def oswald_rifle():
    print ("""
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@
@@
@@
@@
@@@@
@@@
@&&&&&
@&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&@&&#&&&&&&&&%#&&(,@@@&&&&&&&&&@@&&&&&@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
@&&&&&&&&&&&&&&&&&&&&&&&&@&@&&, */(####,*/**/*/*(((/. #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
@&&&&&&&&&&&&&&&&&&&&&/((//*(#(((### .. ,,,,,..,,**///(((,,,*,,...,,,../..,,,,.,.*(((*...... . ...&&
@&&&&&&&&&&&&&&&&&&&&%#&&&&                     .                    ,/((((&&&&&&&&&&&
@&&&& ....................*(/,   ..*(#########%%%%%%%&, ,%&%&&&&&&&&&&&&&&&&&&&&&&&&&&&&
@&&&&*,,          */(*   (#%%&&&&/&#&&*/////###%&&&&&&&&&&&&&&&,, *&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&.,              .&&.,,**/(##((#/*/(%&&&@@&&&&&&&&&&&.*.#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&,. ./%%&&&#      .   ,.   ..,,,.,..,,....**&%%#*,.   .(&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&##,     *(/,*,%#.  .(#%%(%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
@                                                                                                  &
&                                                                                                  &
@&
@&&
@&&
@&
&&
@@@&
@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
@""")
    print ("\nYou check over your rifle. it is relatively new, and in good condition. It is loaded and cocked, with the safety on.")
    print ("\nHowever, your handler provided you with a new scope for this mission.")
    print ("\n At the time, you were very nervous and didn't want to spend any more time than you needed to talking to Mr Gray.")
    print ("\n But now you think about it, he didn't give a very good reason for you to use that scope versus another...")
    print ("\n you hear the motorcade growing closer.")
    print ("\nWhat do you do?")
    print ("\n1)Get ready to shoot.")
    print ("\n2)Check scope")
    answer = input()
    
    if answer=="1":
     oswald_shoot()
    elif answer=="2":
     oswald_scope()

def oswald_scope():
    print("\nYou check the scope.")
    print("""
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#####(&@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#%%%%%%%&%%(@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%(#&#%%%%&&%%&@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(#(&%%%%%&&&&&%%@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#(##%%%%%%##%%%%#%%%%%&&&%@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(#(%#%%#%%%%%%%%%&&&&&@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%@@&&&&@&%%%%&&&@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#&@@@&&@%&&%&&(@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*##%&&&%%%%%#(##&%(@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(##%%%%%%%&&@&@@&&&.%@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@&*(###%%%%%&%%%%%&&&#(#@@(&&@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@/((  ./#%#%%%%%%%&&&&(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@(((((##(####%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@(((((#######%###%%%%%%%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@((((((############%%%%%%%(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@#@@@(((#############%%%&%%%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@##########%%%%&%&%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@&#####%%%%%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@&@@@&&@#%%%%%%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@&%%@@@@@%%%(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@#&&&&%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@""")
    print("\nIt is a side-mounted 4x18 made by Ordinance Optics. Not exactly top of the line. You wonder why you were provided with this.")
    print("\nUpon closer inspection, you realise that the scope itself is slightly misaligned. You cannot fix it here, as the housing itself has been subtly bent.")
    print("\nYour mind races. You have been given an inaccurate gun intentionally. Now you really know you are a patsy. You were intended to shoot and miss, while the real assassin makes the kill")
    print("\n Your only part in this story is to take the blame for it. You feel betrayed.")
    print("\n What do you do?")
    print("\n1)Abort the mission. If they want to kill the president, they can do it without your help. Maybe you'll be arrested. But they wont have as much evidence.")
    print("\n2)Make a mental calculation for how to adjust for the inaccurate scope. If you're going to take the blame for killing the president, you may as well kill the president")
    print("\n3)See if it is possible, to protect the president. watch for threats, and shoot them before they can shoot JFK. Maybe you can get out of trouble if you protect him?")
    answer = input()
    if answer == "1":
        oswald_abort()
    elif answer == "2":
        oswald_adjustshot()
    elif answer == "3":
        oswald_protect()

def oswald_protect():
    print("""
                                                                                                                                                          
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                `,i*nn+;,                                                                                             
                                             ;#i+zz##znnn#.                                                                                           
                                           `#nnzz#nnzxxxxx#,                                                                                          
                                           *zxxn##MMxxxMnzz*,                                                                                         
                                          ,zzMxz+xMMMxxxznnzi`                                                                                        
                                          *zzxxx+#MMMMMMxznxx*                                                                                        
                                          ,zxznz#*+zMMMM*#nxxz:                                                                                       
                                           izznn++z##nM#:*zxn#x                                                                                       
                                           +nznMxz######i#nxM#n`                                                                                      
                                           zxnnnnzzz##z##znxMz#`                                                                                      
                                           +xWxnnnnzxzzz#znxnz;  `;;       `                                                                          
                                           ,zM#+nnnnnnzxxxMMM+``,:+#``    .z*     .:;**i:                                                             
                                      `,` :+xx#+*zxnnnxxzxWM#. :z#+#z##**+++z*+++#zz#+#z+                                                             
                                     ::+n:zzMM;++*#nxxxxnW@x+` :###zx#nznzx*xzzznnnz#+z#*                                                             
                                     +..znnnnni;:;#nMMMxM@@zn. ,zzzzi+:.:#i;:,*+;+nMMMMMz                                                             
                                  `:*##zzzxnnMxz++nnW@@MW@Wzi          :;+i:::*+i, ``,,,`                                                             
                                 ,+zzznnxxxMMWWWWxx@@WWW@WMn:      `;i*zzzii**#Mxnz##++*i;;::::::,,,,,,,,,,,............```````````                   
                               `*zzzzzznznni+#nMWWWWWWWMWWM;;:##:` `znn+*+nnxMxMzi###zzzznnnnnnnnnnnnnxxxnzzzzzzzz#######+##++++++*                   
                              `*nznnnnnnxn#,,,::i*++#+++++*+xnnxM+*+*+W;:::xMMMMMi*:,::::::;;::;;;;;i;;;;*....,,,,,,,,,,,,,,,,,,,,.                   
                              iznnnnnnnnnxz::::,,,,:::::::;n#zxMn*i*#nniiiinxWxWxxnMzzzznnnnnnxxxxxxxxxxx+                                            
                             ,nnnnnnnnnnnxn;;;:;;;;;;;;;::#n++#nnxnxMWMxxxMWzMxxxMxMz**+*****iiii**i;+i;;.                                            
                             #nnnnnnnnnnxxxii;;iiiiiiiiii#xMn;ii+xnnxM#nWMxxnnMnMxMx.            ``  ``                                               
                            ;nnnnnnnnnnnnxM+****++++##znxxnMM+,;+nni##nxMMnn#znzxzn;                                                                  
                            #znnnnnnnnnnnxxnzzzzznnxMWWMnznxMn##*n* ..zMMWxnz+##+`                                                                    
                           `nnnnnxxxxnnnxxxWWWMMWW@@@@MzznnxMxxziz`  :MxxMWMz:,,                                                                      
                           ,xnnnnxxxxxMxxxxWW@@M@@@@@WnnnnxMMMxz++  `zMxMxx#*                                                                         
                           ixnnnnnnnnxxxxxMWWWW@WWWWWnnnxxMMWMxn#: `+MMMMx+                                                                           
                           *nxnnnnnnnnnnnxWWWWxMMMMnxnxxxxMW@Wxi, .zxMxMxx;                                                                           
                           zxxxxxxnnnnnnxMWWWWMxWxnzxxxxxxM@@@Mi .zMMxxxxz`                                                                           
                           nxxMxxxxxxxnnxWWWWWMnxxxnxxxxxMW@@@@x,zMMMMxxx;                                                                            
                          .xxxxMxnnnxxxxxWWWWWMnxxxMxxxxMx@WW@WWMMMMxxxxn`                                                                            
                          *xnxxMWxnnnnxnWWWWWWMxxMnxxMxMxMWWWMMMMMMMxxxx*                                                                             
                          +nxxxxMWMnxxMMMWWWWWWxxxxxxxxxxWWMMMMWMMxMxxxn`                                                                             
                          zMxxxxxMWMxxMWWMMWWWxxxnxxMxnxxWMMMMWMMMxMxxx:                                                                              
                         `nxMxxxMxMWMxMMxxxMMMMxxnMxMxxx@WMMMWMMxxxxxx#                                                                               
                         .xxxxMxxMMMWWxxMMxMMMMxMxMxMxxW@MMWWMMMxxxxxn.                                                                               
                         ;xxxx@@MxMMWWWxxxMMMMMxxMMxMxx@WMMMxMMMxxxxM;                                                                                
                         *MxxMWzxMMMMW@WMxxMMMxxxxxMxxW@WMMxxMMxxxxMn`                                                                                
                         zMMxWMzxnxMMMW@WMxxWMxxxxxMxinWWMMxMMMMMMMx,                                                                                 
                        `xMMMMMzxnxxWWWW@WMMMMxxxxxM+  `:nWMMMMMMWx.                                                                                  
                        :MMxMWWxxxxxWxMW@@WxMMxxxxxn`  ,+M@@WWWMMxxz*,                                                                                
                        zMMMMMWxxxMxMxxM@@WWxxxxxxM; .zWWW@WMWxxxxxnz#.                                                                               
                        zMxMWWWxxxxxWxxxM@@@WxxxxWn:#WMMWWWWWxnnxnnnnz*                                                                               
                       `MWMWMWMxxxxxMxxxMW@@@@WMW@n@@nzMWWWWMxxxn#znnnz.                                                                              
                       ,xMWMWxMxxxxMxxxxxW@@@@@#@@#@@WMWWWW@Wxnxz+znnnz:                                                                              
                      `zMnMMMxxMxxxMxxxxxW@W@@##@##@WxxMWWWWWWMnz#znnnzi                                                                              
                      .MMW@MMxnnxMWMxxxxMWW@@@#@@@@WW@WMWWWWMMWnzzznnnn*                                                                              
                       #MMWxMMMMxWMxxxxxM@@@@@@WM@@WW@WWWWMWWWWxnzznnnn*                                                                              
                       nxWxMWWxMMWMMMxxxWW@@W@@WWWWWMWWxWWWMWWMMnzznnnz+                                                                              
                       xnWMMMW@WWMMMxWM@WW@@@@@WxxWMMWMMWWWWWM@Mxnnnnnn#                                                                              
                      `xxWxnxMWWW@@@WWW@W@@@@WWMMxMMMWWMMWWW@@WMMxznnxnz                                                                              
                      .MMMxzxxxMMMxMWWWM@@W@WWMxMxMMWWWMMMWWMWMMxMnznxn+                                                                              
                      ,MMxxnMxxxxMxMMMxM@@WWMWWWMxMMWWWWMMx;zMMMxxMxnnn.                                                                              
                      `nWWMMMnxxMxxWMMxW@WWWMMMMWMxWWWWWWz.iWMWMMxnMWWz                                                                               
                       *WW@@WWMWWMWWWWWWMWWMMMMMMMMMWWWW#` ixMMxxMxxxx,                                                                               
                       iMMWMWMMWW@WW@WMxWMMMMWMMWWMMMWWn`  +MxMxxMMMx`                                                                                
                       iMMWMMMMMMWWMxxxMMxWWWWWWWWMMMM+`   #MMxxxWxxz                                                                                 
                       *MWMMMMxxxMxxxMWMMxMWWWWWWWWMMi     #MMMxMMxx+                                                                                 
                       iMMWMxxMMMMMMWMMMMnM@@WWWWWWx:      zMxxMWxxx*                                                                                 
                       ,MWWMMMMMMMWWMMMMxnW@WWWWWx*`       zMxxMMxxx;                                                                                 
                       `xMWMMMMMMMMMMMMMxnWWWWWxi`         zMxMWxxxx,                                                                                 
                        #WMMMMMMMMMMMMMxxnMWx+:`           zMxMMxxxx`                                                                                 
                        .MMWWMWWMMMMMMMxMx+,               nxMMMxxxn                                                                                  
                         *MMWMMMMMMMMMMMxx*               `nxMxMMxx+                                                                                  
                         `xWMWMMMMMMMMMMxxz               .MMMMMMxM;                                                                                  
                          ;WWMMMMWMxxMMMxxM`              ,MMxWxxxx:                                                                                  
                       ,+#*MWMMMWMMMxMMMxxM,              .MMxMxMMn`                                                                                  
                     ,zWMMW@WMMWWWMxxxxxxxxi              .MMMWWMMx                                                                                   
                    `xMMMMW@@MM@WMMMxxxxxxxn`             `MWWWWWM#                                                                                   
                    ;MMMMMW@#WMWWMMMxxxxxxxMi             ;WMxxxMMi                                                                                   
                    ixMMMWxW@@MWWWMMxxxxxxxxz`            iMMMMxzM:                                                                                   
                    ;MMMMWMW@@@WWMMMxxxxxxxxn;            #WWMxxnM:                                                                                   
                    ,MMWMMWW@@@@WMxMMxxxxxxxnz`           +MMWMxnMi                                                                                   
                    `xWWMWMW@@@@@Wxxxxxxxxxxxxi           *MMMMMxM*                                                                                   
                     zWWWMM@@WW@WWMxMxxxxxxxxnn,          +WWMMMMxx,                                                                                  
                     #MWWMW@@WWWWMMxMMMxxxxxxnn:          xWMWMWMMxn,                                                                                 
                     zMMMMW@@@WWWWMMMxMMxxxxnnnn+        .WMWWWMMMxxx*,                                                                               
                    `xMWMnM@xiWWWM@WWMMMMMMxxxxMx`       ;WMWMWWWWMMMMx#;,`                                                                           
                    .xMWWWMWW.iWWxWWWWMWWMMMWWWMx.       *WMMWMWWWWMMMMMMMxn,                                                                         
                    ,MMMMMMMW; ;xxMxM@MMMxxxxxxxxi       +MMMWWWWWMMMMWWWMMM#                                                                         
                    .xMWWWMMW#  .xMMMWMWxxxxxxxxM#       #WWWWWWWWWWWWWMMMMW#                                                                         
                     #MMMMxMMM`  ,xMWWMMxnxxxxxxxi       :WWWWWWMxWWWWMMMMzi`                                                                         
                     `+MWMMMxz    `*MWW@MxxxnxMM+`        `,,,.`  .ii**;,`                                                                            
                       `....`      .xMWWxxxxxMx;                                                                                                      
                                    ,;MWMMMWx*.                                                                                                       
                                      ;z#**:`                                                                                                         
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      """)
    print("\n You decide you aren't going to play by the CIA's rules. You were never the greatest soldier, or the most loyal citizen, but you'll be damned if you're going to be a tool of the CIA")
    print("\nYou scan the crowd for threats. You know there must be another assassin, or a CIA observer, and while your chances of spotting them and stopping them are slim, what else can you do?")
    print("\nAs you look, some movement catches your eye. Behind a grassy gnoll, a policeman is crouched, taking a rifle out of a bag.")
    print("\nAs you watch, the policeman affixes a suppressor to the end of the rifle. You know that this is the second assassin. His bag is the same as the one you were provided.")
    print("\n The presidential motorcade is directly below and in front of you, moving along the street. Time is short.")
    print("\nWhat do you do?")
    print("\n1)Shoot assassin.")
    print("\n2)Play your role. Shoot President.")
    answer = input()
    if answer == "1":
        oswald_shootassassin()
    elif answer =="2":
        oswald_shoot_kill()

def oswald_shootassassin():
    print("""
                                                                                                                                                          
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                `,i*nn+;,                                                                                             
                                             ;#i+zz##znnn#.                                                                                           
                                           `#nnzz#nnzxxxxx#,                                                                                          
                                           *zxxn##MMxxxMnzz*,                                                                                         
                                          ,zzMxz+xMMMxxxznnzi`                                                                                        
                                          *zzxxx+#MMMMMMxznxx*                                                                                        
                                          ,zxznz#*+zMMMM*#nxxz:                                                                                       
                                           izznn++z##nM#:*zxn#x                                                                                       
                                           +nznMxz######i#nxM#n`                                                                                      
                                           zxnnnnzzz##z##znxMz#`                                                                                      
                                           +xWxnnnnzxzzz#znxnz;  `;;       `                                                                          
                                           ,zM#+nnnnnnzxxxMMM+``,:+#``    .z*     .:;**i:                                                             
                                      `,` :+xx#+*zxnnnxxzxWM#. :z#+#z##**+++z*+++#zz#+#z+                                                             
                                     ::+n:zzMM;++*#nxxxxnW@x+` :###zx#nznzx*xzzznnnz#+z#*                                                             
                                     +..znnnnni;:;#nMMMxM@@zn. ,zzzzi+:.:#i;:,*+;+nMMMMMz                                                             
                                  `:*##zzzxnnMxz++nnW@@MW@Wzi          :;+i:::*+i, ``,,,`                                                             
                                 ,+zzznnxxxMMWWWWxx@@WWW@WMn:      `;i*zzzii**#Mxnz##++*i;;::::::,,,,,,,,,,,............```````````                   
                               `*zzzzzznznni+#nMWWWWWWWMWWM;;:##:` `znn+*+nnxMxMzi###zzzznnnnnnnnnnnnnxxxnzzzzzzzz#######+##++++++*                   
                              `*nznnnnnnxn#,,,::i*++#+++++*+xnnxM+*+*+W;:::xMMMMMi*:,::::::;;::;;;;;i;;;;*....,,,,,,,,,,,,,,,,,,,,.                   
                              iznnnnnnnnnxz::::,,,,:::::::;n#zxMn*i*#nniiiinxWxWxxnMzzzznnnnnnxxxxxxxxxxx+                                            
                             ,nnnnnnnnnnnxn;;;:;;;;;;;;;::#n++#nnxnxMWMxxxMWzMxxxMxMz**+*****iiii**i;+i;;.                                            
                             #nnnnnnnnnnxxxii;;iiiiiiiiii#xMn;ii+xnnxM#nWMxxnnMnMxMx.            ``  ``                                               
                            ;nnnnnnnnnnnnxM+****++++##znxxnMM+,;+nni##nxMMnn#znzxzn;                                                                  
                            #znnnnnnnnnnnxxnzzzzznnxMWWMnznxMn##*n* ..zMMWxnz+##+`                                                                    
                           `nnnnnxxxxnnnxxxWWWMMWW@@@@MzznnxMxxziz`  :MxxMWMz:,,                                                                      
                           ,xnnnnxxxxxMxxxxWW@@M@@@@@WnnnnxMMMxz++  `zMxMxx#*                                                                         
                           ixnnnnnnnnxxxxxMWWWW@WWWWWnnnxxMMWMxn#: `+MMMMx+                                                                           
                           *nxnnnnnnnnnnnxWWWWxMMMMnxnxxxxMW@Wxi, .zxMxMxx;                                                                           
                           zxxxxxxnnnnnnxMWWWWMxWxnzxxxxxxM@@@Mi .zMMxxxxz`                                                                           
                           nxxMxxxxxxxnnxWWWWWMnxxxnxxxxxMW@@@@x,zMMMMxxx;                                                                            
                          .xxxxMxnnnxxxxxWWWWWMnxxxMxxxxMx@WW@WWMMMMxxxxn`                                                                            
                          *xnxxMWxnnnnxnWWWWWWMxxMnxxMxMxMWWWMMMMMMMxxxx*                                                                             
                          +nxxxxMWMnxxMMMWWWWWWxxxxxxxxxxWWMMMMWMMxMxxxn`                                                                             
                          zMxxxxxMWMxxMWWMMWWWxxxnxxMxnxxWMMMMWMMMxMxxx:                                                                              
                         `nxMxxxMxMWMxMMxxxMMMMxxnMxMxxx@WMMMWMMxxxxxx#                                                                               
                         .xxxxMxxMMMWWxxMMxMMMMxMxMxMxxW@MMWWMMMxxxxxn.                                                                               
                         ;xxxx@@MxMMWWWxxxMMMMMxxMMxMxx@WMMMxMMMxxxxM;                                                                                
                         *MxxMWzxMMMMW@WMxxMMMxxxxxMxxW@WMMxxMMxxxxMn`                                                                                
                         zMMxWMzxnxMMMW@WMxxWMxxxxxMxinWWMMxMMMMMMMx,                                                                                 
                        `xMMMMMzxnxxWWWW@WMMMMxxxxxM+  `:nWMMMMMMWx.                                                                                  
                        :MMxMWWxxxxxWxMW@@WxMMxxxxxn`  ,+M@@WWWMMxxz*,                                                                                
                        zMMMMMWxxxMxMxxM@@WWxxxxxxM; .zWWW@WMWxxxxxnz#.                                                                               
                        zMxMWWWxxxxxWxxxM@@@WxxxxWn:#WMMWWWWWxnnxnnnnz*                                                                               
                       `MWMWMWMxxxxxMxxxMW@@@@WMW@n@@nzMWWWWMxxxn#znnnz.                                                                              
                       ,xMWMWxMxxxxMxxxxxW@@@@@#@@#@@WMWWWW@Wxnxz+znnnz:                                                                              
                      `zMnMMMxxMxxxMxxxxxW@W@@##@##@WxxMWWWWWWMnz#znnnzi                                                                              
                      .MMW@MMxnnxMWMxxxxMWW@@@#@@@@WW@WMWWWWMMWnzzznnnn*                                                                              
                       #MMWxMMMMxWMxxxxxM@@@@@@WM@@WW@WWWWMWWWWxnzznnnn*                                                                              
                       nxWxMWWxMMWMMMxxxWW@@W@@WWWWWMWWxWWWMWWMMnzznnnz+                                                                              
                       xnWMMMW@WWMMMxWM@WW@@@@@WxxWMMWMMWWWWWM@Mxnnnnnn#                                                                              
                      `xxWxnxMWWW@@@WWW@W@@@@WWMMxMMMWWMMWWW@@WMMxznnxnz                                                                              
                      .MMMxzxxxMMMxMWWWM@@W@WWMxMxMMWWWMMMWWMWMMxMnznxn+                                                                              
                      ,MMxxnMxxxxMxMMMxM@@WWMWWWMxMMWWWWMMx;zMMMxxMxnnn.                                                                              
                      `nWWMMMnxxMxxWMMxW@WWWMMMMWMxWWWWWWz.iWMWMMxnMWWz                                                                               
                       *WW@@WWMWWMWWWWWWMWWMMMMMMMMMWWWW#` ixMMxxMxxxx,                                                                               
                       iMMWMWMMWW@WW@WMxWMMMMWMMWWMMMWWn`  +MxMxxMMMx`                                                                                
                       iMMWMMMMMMWWMxxxMMxWWWWWWWWMMMM+`   #MMxxxWxxz                                                                                 
                       *MWMMMMxxxMxxxMWMMxMWWWWWWWWMMi     #MMMxMMxx+                                                                                 
                       iMMWMxxMMMMMMWMMMMnM@@WWWWWWx:      zMxxMWxxx*                                                                                 
                       ,MWWMMMMMMMWWMMMMxnW@WWWWWx*`       zMxxMMxxx;                                                                                 
                       `xMWMMMMMMMMMMMMMxnWWWWWxi`         zMxMWxxxx,                                                                                 
                        #WMMMMMMMMMMMMMxxnMWx+:`           zMxMMxxxx`                                                                                 
                        .MMWWMWWMMMMMMMxMx+,               nxMMMxxxn                                                                                  
                         *MMWMMMMMMMMMMMxx*               `nxMxMMxx+                                                                                  
                         `xWMWMMMMMMMMMMxxz               .MMMMMMxM;                                                                                  
                          ;WWMMMMWMxxMMMxxM`              ,MMxWxxxx:                                                                                  
                       ,+#*MWMMMWMMMxMMMxxM,              .MMxMxMMn`                                                                                  
                     ,zWMMW@WMMWWWMxxxxxxxxi              .MMMWWMMx                                                                                   
                    `xMMMMW@@MM@WMMMxxxxxxxn`             `MWWWWWM#                                                                                   
                    ;MMMMMW@#WMWWMMMxxxxxxxMi             ;WMxxxMMi                                                                                   
                    ixMMMWxW@@MWWWMMxxxxxxxxz`            iMMMMxzM:                                                                                   
                    ;MMMMWMW@@@WWMMMxxxxxxxxn;            #WWMxxnM:                                                                                   
                    ,MMWMMWW@@@@WMxMMxxxxxxxnz`           +MMWMxnMi                                                                                   
                    `xWWMWMW@@@@@Wxxxxxxxxxxxxi           *MMMMMxM*                                                                                   
                     zWWWMM@@WW@WWMxMxxxxxxxxnn,          +WWMMMMxx,                                                                                  
                     #MWWMW@@WWWWMMxMMMxxxxxxnn:          xWMWMWMMxn,                                                                                 
                     zMMMMW@@@WWWWMMMxMMxxxxnnnn+        .WMWWWMMMxxx*,                                                                               
                    `xMWMnM@xiWWWM@WWMMMMMMxxxxMx`       ;WMWMWWWWMMMMx#;,`                                                                           
                    .xMWWWMWW.iWWxWWWWMWWMMMWWWMx.       *WMMWMWWWWMMMMMMMxn,                                                                         
                    ,MMMMMMMW; ;xxMxM@MMMxxxxxxxxi       +MMMWWWWWMMMMWWWMMM#                                                                         
                    .xMWWWMMW#  .xMMMWMWxxxxxxxxM#       #WWWWWWWWWWWWWMMMMW#                                                                         
                     #MMMMxMMM`  ,xMWWMMxnxxxxxxxi       :WWWWWWMxWWWWMMMMzi`                                                                         
                     `+MWMMMxz    `*MWW@MxxxnxMM+`        `,,,.`  .ii**;,`                                                                            
                       `....`      .xMWWxxxxxMx;                                                                                                      
                                    ,;MWMMMWx*.                                                                                                       
                                      ;z#**:`                                                                                                         
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      """)
    print("\nYou aim at the assassin, as he takes aim at the president. You try to adjust for the scope's being misaligned.")
    print("\nYou fire!")
    print("\nThe shot goes wide, impacting the earth about 8 feet to the right of the assassin. He notices the impact, but continues to aim at JFK.")
    print("\nYou fire twice more, aiming at different points each time. Your last shot lands inches from his head. As you fire the last shot, you see his suppressed rifle jerk in his hands.")
    print("\n swivelling your aim, to look at the motorcade, you see that JFK has been shot badly, and the motorcade is speeding off.")
    print("\n you try to reaqcuire the assassin in your scope, but he has gone, and so has his rifle.")
    print("\n you are acutely aware that it is going to seem like the loud gunshots that coincided with the president being shot will attract a lot of attention to this building very shortly.")
    print("\n It is time to leave. What do you do?")
    print("\n1)Drop rifle and leave")
    print("\n2)Hide rifle and leave")
    answer=input()
    if answer =="1":
        michaelstart()
    elif answer =="2":
        michaelstart()



def oswald_shoot():
    print("""
    %&%%%#%&%###%@((&&%&#&%&%%%%%##/*#(((%%#%%%%%#/(/#/.,**(/##%#(*#%%%%&(%%%&%%%*#*
%%#/&%%@%&%&(&&%(@&%#&&&%%%&#&%((((,/#&%%%%#%%((//**(,,///#%%%(/(%%%#.#%%%%#%/(#
&((*&&&@&&%%#&*%%%%%%@&%##&%%#&%(((##%@&@%&#%%%(((./((#*%(#&%#*&%%###*#*%&(((#%/
&%((@/%&%%#(&&&#%&&&#&&%*#%%&&@@@@@@@@@@@@@@@@@@@&&#%##(&#&&#&%%%&%&&/#&&%%%%&&%
&&&#@%&&@%(%%&&&@(&%%&&%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%&&%&&@&&&%@@&&&&&&@&&&&
&%%&&#&@%&%@@&&@@@&&&@@@@@@@@@@@@(#*/*/,*,,,*/*@@@@@@@@@@@%%%%#%#&%#%@%%@@@@@@@&
&&&&&&%&&%%&@&(&@@%@@@@@@@@@&            I          /@@@@@@@@#(@&&&%&&@&@&@@&&&&@
#&&&&&&&@&@&@&&&&@@@@@@@@&/              I              ,%@@@@@@&%%(@&&@&@@%&&&&@&@
%@&&&&&@&&@&@&%&@@@@@@@(*                I              ,@@@@@@@##&%&@%@@%&@&@@&&
&&%&%#&%%%&&@@&@@@@@@@,                  I                 #@@@@@@%#%#&&/%%%&&&&&@
&&&%&&**###&@&#@@@@@@,                   I                .%@@@@@(,#,/&@&&%&&%&##
#(#/,%%##//,&&@@@@@@@                    I                 .*@@@@@@#%#,.          
. .......,*//&@@@@@@---------------------*-----------------,@@@@@@,              
 .           .&@@@@@                     I                  ,@@@@@@,              
 . ...   .    (@@@@@@                    I                  (@@@@@&               
. . .         .@@@@@@@                   I                 @@@@@@,               
.              ,@@@@@@@.                 I              (@@@@@@*                
                ,@@@@@@@.                I            .*@@@@@@@,                 
 *                (@@@@@@@,              I           /@@@@@@@&.                  
  .*.               (@@@@@@@@@           I          %@@@@@@@@&.                    
                      ,@@@@@@@@@@@@@/***#/(&@@@@@@@@@@@@@@@@*           ... .   
                    .   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@                   
..                    @@@@@@@@&@@@@@@@@@@@@@@@@@@@@@&&@&@@@@@@@                 
 .       .          &@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@                
...... .          *@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                
...........   .. .@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@&@@@@@%@@@@@@@@                
................  @@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@&&@@@@(@@@@@@@@  ..      ...   
................./@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@#@@@@@@# . .. .        .
.............,*..@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@&%&@@%@@@@@@@.    ..    .....""")
    print("\nThe motorcade comes into view. You tuck yourself into the shadows and raise your rifle")
    print("\nYou scan the crowd, you see occasional policemen dotted around the crowd. the crowd itself is mostly made up of families.")
    print("\n As the president's car comes into view you see a little activity off to one side. it looks like a police marksman is getting into position on a grassy knoll to cover the motorcade. He isn't looking at you.")
    print("\n To your shock, the president looks around, seemingly looks directly up at your hiding place. You tuck yourself deeper in the shadows and hope he doesn't raise the alarm")
    print("\nIt is now or never. You affix your crosshairs on the president's back.")
    print("\nWhat do you do?")
    print("\n1)Shoot to kill.")
    print("\n2)Shoot to miss.")
    answer = input()
    if answer == "1":
        oswald_shoot_kill()
    elif answer == "2":
        oswald_shoot_miss()

def oswald_shoot_kill():
    print("""
                                                                                                                                                          
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                `,i*nn+;,                                                                                             
                                             ;#i+zz##znnn#.                                                                                           
                                           `#nnzz#nnzxxxxx#,                                                                                          
                                           *zxxn##MMxxxMnzz*,                                                                                         
                                          ,zzMxz+xMMMxxxznnzi`                                                                                        
                                          *zzxxx+#MMMMMMxznxx*                                                                                        
                                          ,zxznz#*+zMMMM*#nxxz:                                                                                       
                                           izznn++z##nM#:*zxn#x                                                                                       
                                           +nznMxz######i#nxM#n`                                                                                      
                                           zxnnnnzzz##z##znxMz#`                                                                                      
                                           +xWxnnnnzxzzz#znxnz;  `;;       `                                                                          
                                           ,zM#+nnnnnnzxxxMMM+``,:+#``    .z*     .:;**i:                                                             
                                      `,` :+xx#+*zxnnnxxzxWM#. :z#+#z##**+++z*+++#zz#+#z+                                                             
                                     ::+n:zzMM;++*#nxxxxnW@x+` :###zx#nznzx*xzzznnnz#+z#*                                                             
                                     +..znnnnni;:;#nMMMxM@@zn. ,zzzzi+:.:#i;:,*+;+nMMMMMz                                                             
                                  `:*##zzzxnnMxz++nnW@@MW@Wzi          :;+i:::*+i, ``,,,`                                                             
                                 ,+zzznnxxxMMWWWWxx@@WWW@WMn:      `;i*zzzii**#Mxnz##++*i;;::::::,,,,,,,,,,,............```````````                   
                               `*zzzzzznznni+#nMWWWWWWWMWWM;;:##:` `znn+*+nnxMxMzi###zzzznnnnnnnnnnnnnxxxnzzzzzzzz#######+##++++++*                   
                              `*nznnnnnnxn#,,,::i*++#+++++*+xnnxM+*+*+W;:::xMMMMMi*:,::::::;;::;;;;;i;;;;*....,,,,,,,,,,,,,,,,,,,,.                   
                              iznnnnnnnnnxz::::,,,,:::::::;n#zxMn*i*#nniiiinxWxWxxnMzzzznnnnnnxxxxxxxxxxx+                                            
                             ,nnnnnnnnnnnxn;;;:;;;;;;;;;::#n++#nnxnxMWMxxxMWzMxxxMxMz**+*****iiii**i;+i;;.                                            
                             #nnnnnnnnnnxxxii;;iiiiiiiiii#xMn;ii+xnnxM#nWMxxnnMnMxMx.            ``  ``                                               
                            ;nnnnnnnnnnnnxM+****++++##znxxnMM+,;+nni##nxMMnn#znzxzn;                                                                  
                            #znnnnnnnnnnnxxnzzzzznnxMWWMnznxMn##*n* ..zMMWxnz+##+`                                                                    
                           `nnnnnxxxxnnnxxxWWWMMWW@@@@MzznnxMxxziz`  :MxxMWMz:,,                                                                      
                           ,xnnnnxxxxxMxxxxWW@@M@@@@@WnnnnxMMMxz++  `zMxMxx#*                                                                         
                           ixnnnnnnnnxxxxxMWWWW@WWWWWnnnxxMMWMxn#: `+MMMMx+                                                                           
                           *nxnnnnnnnnnnnxWWWWxMMMMnxnxxxxMW@Wxi, .zxMxMxx;                                                                           
                           zxxxxxxnnnnnnxMWWWWMxWxnzxxxxxxM@@@Mi .zMMxxxxz`                                                                           
                           nxxMxxxxxxxnnxWWWWWMnxxxnxxxxxMW@@@@x,zMMMMxxx;                                                                            
                          .xxxxMxnnnxxxxxWWWWWMnxxxMxxxxMx@WW@WWMMMMxxxxn`                                                                            
                          *xnxxMWxnnnnxnWWWWWWMxxMnxxMxMxMWWWMMMMMMMxxxx*                                                                             
                          +nxxxxMWMnxxMMMWWWWWWxxxxxxxxxxWWMMMMWMMxMxxxn`                                                                             
                          zMxxxxxMWMxxMWWMMWWWxxxnxxMxnxxWMMMMWMMMxMxxx:                                                                              
                         `nxMxxxMxMWMxMMxxxMMMMxxnMxMxxx@WMMMWMMxxxxxx#                                                                               
                         .xxxxMxxMMMWWxxMMxMMMMxMxMxMxxW@MMWWMMMxxxxxn.                                                                               
                         ;xxxx@@MxMMWWWxxxMMMMMxxMMxMxx@WMMMxMMMxxxxM;                                                                                
                         *MxxMWzxMMMMW@WMxxMMMxxxxxMxxW@WMMxxMMxxxxMn`                                                                                
                         zMMxWMzxnxMMMW@WMxxWMxxxxxMxinWWMMxMMMMMMMx,                                                                                 
                        `xMMMMMzxnxxWWWW@WMMMMxxxxxM+  `:nWMMMMMMWx.                                                                                  
                        :MMxMWWxxxxxWxMW@@WxMMxxxxxn`  ,+M@@WWWMMxxz*,                                                                                
                        zMMMMMWxxxMxMxxM@@WWxxxxxxM; .zWWW@WMWxxxxxnz#.                                                                               
                        zMxMWWWxxxxxWxxxM@@@WxxxxWn:#WMMWWWWWxnnxnnnnz*                                                                               
                       `MWMWMWMxxxxxMxxxMW@@@@WMW@n@@nzMWWWWMxxxn#znnnz.                                                                              
                       ,xMWMWxMxxxxMxxxxxW@@@@@#@@#@@WMWWWW@Wxnxz+znnnz:                                                                              
                      `zMnMMMxxMxxxMxxxxxW@W@@##@##@WxxMWWWWWWMnz#znnnzi                                                                              
                      .MMW@MMxnnxMWMxxxxMWW@@@#@@@@WW@WMWWWWMMWnzzznnnn*                                                                              
                       #MMWxMMMMxWMxxxxxM@@@@@@WM@@WW@WWWWMWWWWxnzznnnn*                                                                              
                       nxWxMWWxMMWMMMxxxWW@@W@@WWWWWMWWxWWWMWWMMnzznnnz+                                                                              
                       xnWMMMW@WWMMMxWM@WW@@@@@WxxWMMWMMWWWWWM@Mxnnnnnn#                                                                              
                      `xxWxnxMWWW@@@WWW@W@@@@WWMMxMMMWWMMWWW@@WMMxznnxnz                                                                              
                      .MMMxzxxxMMMxMWWWM@@W@WWMxMxMMWWWMMMWWMWMMxMnznxn+                                                                              
                      ,MMxxnMxxxxMxMMMxM@@WWMWWWMxMMWWWWMMx;zMMMxxMxnnn.                                                                              
                      `nWWMMMnxxMxxWMMxW@WWWMMMMWMxWWWWWWz.iWMWMMxnMWWz                                                                               
                       *WW@@WWMWWMWWWWWWMWWMMMMMMMMMWWWW#` ixMMxxMxxxx,                                                                               
                       iMMWMWMMWW@WW@WMxWMMMMWMMWWMMMWWn`  +MxMxxMMMx`                                                                                
                       iMMWMMMMMMWWMxxxMMxWWWWWWWWMMMM+`   #MMxxxWxxz                                                                                 
                       *MWMMMMxxxMxxxMWMMxMWWWWWWWWMMi     #MMMxMMxx+                                                                                 
                       iMMWMxxMMMMMMWMMMMnM@@WWWWWWx:      zMxxMWxxx*                                                                                 
                       ,MWWMMMMMMMWWMMMMxnW@WWWWWx*`       zMxxMMxxx;                                                                                 
                       `xMWMMMMMMMMMMMMMxnWWWWWxi`         zMxMWxxxx,                                                                                 
                        #WMMMMMMMMMMMMMxxnMWx+:`           zMxMMxxxx`                                                                                 
                        .MMWWMWWMMMMMMMxMx+,               nxMMMxxxn                                                                                  
                         *MMWMMMMMMMMMMMxx*               `nxMxMMxx+                                                                                  
                         `xWMWMMMMMMMMMMxxz               .MMMMMMxM;                                                                                  
                          ;WWMMMMWMxxMMMxxM`              ,MMxWxxxx:                                                                                  
                       ,+#*MWMMMWMMMxMMMxxM,              .MMxMxMMn`                                                                                  
                     ,zWMMW@WMMWWWMxxxxxxxxi              .MMMWWMMx                                                                                   
                    `xMMMMW@@MM@WMMMxxxxxxxn`             `MWWWWWM#                                                                                   
                    ;MMMMMW@#WMWWMMMxxxxxxxMi             ;WMxxxMMi                                                                                   
                    ixMMMWxW@@MWWWMMxxxxxxxxz`            iMMMMxzM:                                                                                   
                    ;MMMMWMW@@@WWMMMxxxxxxxxn;            #WWMxxnM:                                                                                   
                    ,MMWMMWW@@@@WMxMMxxxxxxxnz`           +MMWMxnMi                                                                                   
                    `xWWMWMW@@@@@Wxxxxxxxxxxxxi           *MMMMMxM*                                                                                   
                     zWWWMM@@WW@WWMxMxxxxxxxxnn,          +WWMMMMxx,                                                                                  
                     #MWWMW@@WWWWMMxMMMxxxxxxnn:          xWMWMWMMxn,                                                                                 
                     zMMMMW@@@WWWWMMMxMMxxxxnnnn+        .WMWWWMMMxxx*,                                                                               
                    `xMWMnM@xiWWWM@WWMMMMMMxxxxMx`       ;WMWMWWWWMMMMx#;,`                                                                           
                    .xMWWWMWW.iWWxWWWWMWWMMMWWWMx.       *WMMWMWWWWMMMMMMMxn,                                                                         
                    ,MMMMMMMW; ;xxMxM@MMMxxxxxxxxi       +MMMWWWWWMMMMWWWMMM#                                                                         
                    .xMWWWMMW#  .xMMMWMWxxxxxxxxM#       #WWWWWWWWWWWWWMMMMW#                                                                         
                     #MMMMxMMM`  ,xMWWMMxnxxxxxxxi       :WWWWWWMxWWWWMMMMzi`                                                                         
                     `+MWMMMxz    `*MWW@MxxxnxMM+`        `,,,.`  .ii**;,`                                                                            
                       `....`      .xMWWxxxxxMx;                                                                                                      
                                    ,;MWMMMWx*.                                                                                                       
                                      ;z#**:`                                                                                                         
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      """)
    print("\nYou pull the trigger and the rifle jerks in your hands.")
    print("\nA cloud of dust to the side of the motorcade puffs up. Secret service agents are alerted by the gunshot and start moving towards the president.")
    print("\nYou quickly aim and fire again two more times, both times missing. on your third shot, you hear a shot overlap with yours!")
    print("\nThe president's head jerks to one side and you see a flash of pink mist. He has been shot in the head. You don't think you were the one that did it.")
    print("\nThe crowd starts to panic and scream. The president's car speeds off. You realise quite quickly that you don't have much time to escape.")
    print("\nWhat do you do?")
    print("\n1)Hide your rifle and leave")
    print("\n Drop your rifle and leave")
    answer = input()
    if answer =="1":
        michaelstart()
    elif answer == "2":
        michaelstart()

def oswald_shoot_miss():
    print("""
                                                                                                                                                          
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                `,i*nn+;,                                                                                             
                                             ;#i+zz##znnn#.                                                                                           
                                           `#nnzz#nnzxxxxx#,                                                                                          
                                           *zxxn##MMxxxMnzz*,                                                                                         
                                          ,zzMxz+xMMMxxxznnzi`                                                                                        
                                          *zzxxx+#MMMMMMxznxx*                                                                                        
                                          ,zxznz#*+zMMMM*#nxxz:                                                                                       
                                           izznn++z##nM#:*zxn#x                                                                                       
                                           +nznMxz######i#nxM#n`                                                                                      
                                           zxnnnnzzz##z##znxMz#`                                                                                      
                                           +xWxnnnnzxzzz#znxnz;  `;;       `                                                                          
                                           ,zM#+nnnnnnzxxxMMM+``,:+#``    .z*     .:;**i:                                                             
                                      `,` :+xx#+*zxnnnxxzxWM#. :z#+#z##**+++z*+++#zz#+#z+                                                             
                                     ::+n:zzMM;++*#nxxxxnW@x+` :###zx#nznzx*xzzznnnz#+z#*                                                             
                                     +..znnnnni;:;#nMMMxM@@zn. ,zzzzi+:.:#i;:,*+;+nMMMMMz                                                             
                                  `:*##zzzxnnMxz++nnW@@MW@Wzi          :;+i:::*+i, ``,,,`                                                             
                                 ,+zzznnxxxMMWWWWxx@@WWW@WMn:      `;i*zzzii**#Mxnz##++*i;;::::::,,,,,,,,,,,............```````````                   
                               `*zzzzzznznni+#nMWWWWWWWMWWM;;:##:` `znn+*+nnxMxMzi###zzzznnnnnnnnnnnnnxxxnzzzzzzzz#######+##++++++*                   
                              `*nznnnnnnxn#,,,::i*++#+++++*+xnnxM+*+*+W;:::xMMMMMi*:,::::::;;::;;;;;i;;;;*....,,,,,,,,,,,,,,,,,,,,.                   
                              iznnnnnnnnnxz::::,,,,:::::::;n#zxMn*i*#nniiiinxWxWxxnMzzzznnnnnnxxxxxxxxxxx+                                            
                             ,nnnnnnnnnnnxn;;;:;;;;;;;;;::#n++#nnxnxMWMxxxMWzMxxxMxMz**+*****iiii**i;+i;;.                                            
                             #nnnnnnnnnnxxxii;;iiiiiiiiii#xMn;ii+xnnxM#nWMxxnnMnMxMx.            ``  ``                                               
                            ;nnnnnnnnnnnnxM+****++++##znxxnMM+,;+nni##nxMMnn#znzxzn;                                                                  
                            #znnnnnnnnnnnxxnzzzzznnxMWWMnznxMn##*n* ..zMMWxnz+##+`                                                                    
                           `nnnnnxxxxnnnxxxWWWMMWW@@@@MzznnxMxxziz`  :MxxMWMz:,,                                                                      
                           ,xnnnnxxxxxMxxxxWW@@M@@@@@WnnnnxMMMxz++  `zMxMxx#*                                                                         
                           ixnnnnnnnnxxxxxMWWWW@WWWWWnnnxxMMWMxn#: `+MMMMx+                                                                           
                           *nxnnnnnnnnnnnxWWWWxMMMMnxnxxxxMW@Wxi, .zxMxMxx;                                                                           
                           zxxxxxxnnnnnnxMWWWWMxWxnzxxxxxxM@@@Mi .zMMxxxxz`                                                                           
                           nxxMxxxxxxxnnxWWWWWMnxxxnxxxxxMW@@@@x,zMMMMxxx;                                                                            
                          .xxxxMxnnnxxxxxWWWWWMnxxxMxxxxMx@WW@WWMMMMxxxxn`                                                                            
                          *xnxxMWxnnnnxnWWWWWWMxxMnxxMxMxMWWWMMMMMMMxxxx*                                                                             
                          +nxxxxMWMnxxMMMWWWWWWxxxxxxxxxxWWMMMMWMMxMxxxn`                                                                             
                          zMxxxxxMWMxxMWWMMWWWxxxnxxMxnxxWMMMMWMMMxMxxx:                                                                              
                         `nxMxxxMxMWMxMMxxxMMMMxxnMxMxxx@WMMMWMMxxxxxx#                                                                               
                         .xxxxMxxMMMWWxxMMxMMMMxMxMxMxxW@MMWWMMMxxxxxn.                                                                               
                         ;xxxx@@MxMMWWWxxxMMMMMxxMMxMxx@WMMMxMMMxxxxM;                                                                                
                         *MxxMWzxMMMMW@WMxxMMMxxxxxMxxW@WMMxxMMxxxxMn`                                                                                
                         zMMxWMzxnxMMMW@WMxxWMxxxxxMxinWWMMxMMMMMMMx,                                                                                 
                        `xMMMMMzxnxxWWWW@WMMMMxxxxxM+  `:nWMMMMMMWx.                                                                                  
                        :MMxMWWxxxxxWxMW@@WxMMxxxxxn`  ,+M@@WWWMMxxz*,                                                                                
                        zMMMMMWxxxMxMxxM@@WWxxxxxxM; .zWWW@WMWxxxxxnz#.                                                                               
                        zMxMWWWxxxxxWxxxM@@@WxxxxWn:#WMMWWWWWxnnxnnnnz*                                                                               
                       `MWMWMWMxxxxxMxxxMW@@@@WMW@n@@nzMWWWWMxxxn#znnnz.                                                                              
                       ,xMWMWxMxxxxMxxxxxW@@@@@#@@#@@WMWWWW@Wxnxz+znnnz:                                                                              
                      `zMnMMMxxMxxxMxxxxxW@W@@##@##@WxxMWWWWWWMnz#znnnzi                                                                              
                      .MMW@MMxnnxMWMxxxxMWW@@@#@@@@WW@WMWWWWMMWnzzznnnn*                                                                              
                       #MMWxMMMMxWMxxxxxM@@@@@@WM@@WW@WWWWMWWWWxnzznnnn*                                                                              
                       nxWxMWWxMMWMMMxxxWW@@W@@WWWWWMWWxWWWMWWMMnzznnnz+                                                                              
                       xnWMMMW@WWMMMxWM@WW@@@@@WxxWMMWMMWWWWWM@Mxnnnnnn#                                                                              
                      `xxWxnxMWWW@@@WWW@W@@@@WWMMxMMMWWMMWWW@@WMMxznnxnz                                                                              
                      .MMMxzxxxMMMxMWWWM@@W@WWMxMxMMWWWMMMWWMWMMxMnznxn+                                                                              
                      ,MMxxnMxxxxMxMMMxM@@WWMWWWMxMMWWWWMMx;zMMMxxMxnnn.                                                                              
                      `nWWMMMnxxMxxWMMxW@WWWMMMMWMxWWWWWWz.iWMWMMxnMWWz                                                                               
                       *WW@@WWMWWMWWWWWWMWWMMMMMMMMMWWWW#` ixMMxxMxxxx,                                                                               
                       iMMWMWMMWW@WW@WMxWMMMMWMMWWMMMWWn`  +MxMxxMMMx`                                                                                
                       iMMWMMMMMMWWMxxxMMxWWWWWWWWMMMM+`   #MMxxxWxxz                                                                                 
                       *MWMMMMxxxMxxxMWMMxMWWWWWWWWMMi     #MMMxMMxx+                                                                                 
                       iMMWMxxMMMMMMWMMMMnM@@WWWWWWx:      zMxxMWxxx*                                                                                 
                       ,MWWMMMMMMMWWMMMMxnW@WWWWWx*`       zMxxMMxxx;                                                                                 
                       `xMWMMMMMMMMMMMMMxnWWWWWxi`         zMxMWxxxx,                                                                                 
                        #WMMMMMMMMMMMMMxxnMWx+:`           zMxMMxxxx`                                                                                 
                        .MMWWMWWMMMMMMMxMx+,               nxMMMxxxn                                                                                  
                         *MMWMMMMMMMMMMMxx*               `nxMxMMxx+                                                                                  
                         `xWMWMMMMMMMMMMxxz               .MMMMMMxM;                                                                                  
                          ;WWMMMMWMxxMMMxxM`              ,MMxWxxxx:                                                                                  
                       ,+#*MWMMMWMMMxMMMxxM,              .MMxMxMMn`                                                                                  
                     ,zWMMW@WMMWWWMxxxxxxxxi              .MMMWWMMx                                                                                   
                    `xMMMMW@@MM@WMMMxxxxxxxn`             `MWWWWWM#                                                                                   
                    ;MMMMMW@#WMWWMMMxxxxxxxMi             ;WMxxxMMi                                                                                   
                    ixMMMWxW@@MWWWMMxxxxxxxxz`            iMMMMxzM:                                                                                   
                    ;MMMMWMW@@@WWMMMxxxxxxxxn;            #WWMxxnM:                                                                                   
                    ,MMWMMWW@@@@WMxMMxxxxxxxnz`           +MMWMxnMi                                                                                   
                    `xWWMWMW@@@@@Wxxxxxxxxxxxxi           *MMMMMxM*                                                                                   
                     zWWWMM@@WW@WWMxMxxxxxxxxnn,          +WWMMMMxx,                                                                                  
                     #MWWMW@@WWWWMMxMMMxxxxxxnn:          xWMWMWMMxn,                                                                                 
                     zMMMMW@@@WWWWMMMxMMxxxxnnnn+        .WMWWWMMMxxx*,                                                                               
                    `xMWMnM@xiWWWM@WWMMMMMMxxxxMx`       ;WMWMWWWWMMMMx#;,`                                                                           
                    .xMWWWMWW.iWWxWWWWMWWMMMWWWMx.       *WMMWMWWWWMMMMMMMxn,                                                                         
                    ,MMMMMMMW; ;xxMxM@MMMxxxxxxxxi       +MMMWWWWWMMMMWWWMMM#                                                                         
                    .xMWWWMMW#  .xMMMWMWxxxxxxxxM#       #WWWWWWWWWWWWWMMMMW#                                                                         
                     #MMMMxMMM`  ,xMWWMMxnxxxxxxxi       :WWWWWWMxWWWWMMMMzi`                                                                         
                     `+MWMMMxz    `*MWW@MxxxnxMM+`        `,,,.`  .ii**;,`                                                                            
                       `....`      .xMWWxxxxxMx;                                                                                                      
                                    ,;MWMMMWx*.                                                                                                       
                                      ;z#**:`                                                                                                         
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      """)
    print("\nYou aim your sights to the side of the motorcade, intending to miss. You don't want to be responsible for this death.")
    print("\n You pull the trigger, and the rifle jerks in your hands.")
    print("\nYou expected to see a puff of dust, but instead, your bullet seems to hit the driver of JFK's motorcade. Your rifle is inaccurate! you fire two further shots, this time aiming at the president. Both harmlessly skitter off the road. ")
    print("\n As you fire your third shot, you hear a shot overlap with yours and the president collapses forward in a cloud of pink mist. You know he is dead. You know you didn't do it.")
    print("\n Regardless, you know that the police wouldnt be overly convinced by this argument.")
    print("\nWhat do you do?")
    print("\n1)Drop your rifle and hurry out of the room")
    print("\n2)Carefully hide your rifle and leave the room")
    answer = input()
    if answer == "1":
        michaelstart()
    elif answer == "2":
        michaelstart()

def oswald_adjustshot():
    print("""
                                                                                                                                                          
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                `,i*nn+;,                                                                                             
                                             ;#i+zz##znnn#.                                                                                           
                                           `#nnzz#nnzxxxxx#,                                                                                          
                                           *zxxn##MMxxxMnzz*,                                                                                         
                                          ,zzMxz+xMMMxxxznnzi`                                                                                        
                                          *zzxxx+#MMMMMMxznxx*                                                                                        
                                          ,zxznz#*+zMMMM*#nxxz:                                                                                       
                                           izznn++z##nM#:*zxn#x                                                                                       
                                           +nznMxz######i#nxM#n`                                                                                      
                                           zxnnnnzzz##z##znxMz#`                                                                                      
                                           +xWxnnnnzxzzz#znxnz;  `;;       `                                                                          
                                           ,zM#+nnnnnnzxxxMMM+``,:+#``    .z*     .:;**i:                                                             
                                      `,` :+xx#+*zxnnnxxzxWM#. :z#+#z##**+++z*+++#zz#+#z+                                                             
                                     ::+n:zzMM;++*#nxxxxnW@x+` :###zx#nznzx*xzzznnnz#+z#*                                                             
                                     +..znnnnni;:;#nMMMxM@@zn. ,zzzzi+:.:#i;:,*+;+nMMMMMz                                                             
                                  `:*##zzzxnnMxz++nnW@@MW@Wzi          :;+i:::*+i, ``,,,`                                                             
                                 ,+zzznnxxxMMWWWWxx@@WWW@WMn:      `;i*zzzii**#Mxnz##++*i;;::::::,,,,,,,,,,,............```````````                   
                               `*zzzzzznznni+#nMWWWWWWWMWWM;;:##:` `znn+*+nnxMxMzi###zzzznnnnnnnnnnnnnxxxnzzzzzzzz#######+##++++++*                   
                              `*nznnnnnnxn#,,,::i*++#+++++*+xnnxM+*+*+W;:::xMMMMMi*:,::::::;;::;;;;;i;;;;*....,,,,,,,,,,,,,,,,,,,,.                   
                              iznnnnnnnnnxz::::,,,,:::::::;n#zxMn*i*#nniiiinxWxWxxnMzzzznnnnnnxxxxxxxxxxx+                                            
                             ,nnnnnnnnnnnxn;;;:;;;;;;;;;::#n++#nnxnxMWMxxxMWzMxxxMxMz**+*****iiii**i;+i;;.                                            
                             #nnnnnnnnnnxxxii;;iiiiiiiiii#xMn;ii+xnnxM#nWMxxnnMnMxMx.            ``  ``                                               
                            ;nnnnnnnnnnnnxM+****++++##znxxnMM+,;+nni##nxMMnn#znzxzn;                                                                  
                            #znnnnnnnnnnnxxnzzzzznnxMWWMnznxMn##*n* ..zMMWxnz+##+`                                                                    
                           `nnnnnxxxxnnnxxxWWWMMWW@@@@MzznnxMxxziz`  :MxxMWMz:,,                                                                      
                           ,xnnnnxxxxxMxxxxWW@@M@@@@@WnnnnxMMMxz++  `zMxMxx#*                                                                         
                           ixnnnnnnnnxxxxxMWWWW@WWWWWnnnxxMMWMxn#: `+MMMMx+                                                                           
                           *nxnnnnnnnnnnnxWWWWxMMMMnxnxxxxMW@Wxi, .zxMxMxx;                                                                           
                           zxxxxxxnnnnnnxMWWWWMxWxnzxxxxxxM@@@Mi .zMMxxxxz`                                                                           
                           nxxMxxxxxxxnnxWWWWWMnxxxnxxxxxMW@@@@x,zMMMMxxx;                                                                            
                          .xxxxMxnnnxxxxxWWWWWMnxxxMxxxxMx@WW@WWMMMMxxxxn`                                                                            
                          *xnxxMWxnnnnxnWWWWWWMxxMnxxMxMxMWWWMMMMMMMxxxx*                                                                             
                          +nxxxxMWMnxxMMMWWWWWWxxxxxxxxxxWWMMMMWMMxMxxxn`                                                                             
                          zMxxxxxMWMxxMWWMMWWWxxxnxxMxnxxWMMMMWMMMxMxxx:                                                                              
                         `nxMxxxMxMWMxMMxxxMMMMxxnMxMxxx@WMMMWMMxxxxxx#                                                                               
                         .xxxxMxxMMMWWxxMMxMMMMxMxMxMxxW@MMWWMMMxxxxxn.                                                                               
                         ;xxxx@@MxMMWWWxxxMMMMMxxMMxMxx@WMMMxMMMxxxxM;                                                                                
                         *MxxMWzxMMMMW@WMxxMMMxxxxxMxxW@WMMxxMMxxxxMn`                                                                                
                         zMMxWMzxnxMMMW@WMxxWMxxxxxMxinWWMMxMMMMMMMx,                                                                                 
                        `xMMMMMzxnxxWWWW@WMMMMxxxxxM+  `:nWMMMMMMWx.                                                                                  
                        :MMxMWWxxxxxWxMW@@WxMMxxxxxn`  ,+M@@WWWMMxxz*,                                                                                
                        zMMMMMWxxxMxMxxM@@WWxxxxxxM; .zWWW@WMWxxxxxnz#.                                                                               
                        zMxMWWWxxxxxWxxxM@@@WxxxxWn:#WMMWWWWWxnnxnnnnz*                                                                               
                       `MWMWMWMxxxxxMxxxMW@@@@WMW@n@@nzMWWWWMxxxn#znnnz.                                                                              
                       ,xMWMWxMxxxxMxxxxxW@@@@@#@@#@@WMWWWW@Wxnxz+znnnz:                                                                              
                      `zMnMMMxxMxxxMxxxxxW@W@@##@##@WxxMWWWWWWMnz#znnnzi                                                                              
                      .MMW@MMxnnxMWMxxxxMWW@@@#@@@@WW@WMWWWWMMWnzzznnnn*                                                                              
                       #MMWxMMMMxWMxxxxxM@@@@@@WM@@WW@WWWWMWWWWxnzznnnn*                                                                              
                       nxWxMWWxMMWMMMxxxWW@@W@@WWWWWMWWxWWWMWWMMnzznnnz+                                                                              
                       xnWMMMW@WWMMMxWM@WW@@@@@WxxWMMWMMWWWWWM@Mxnnnnnn#                                                                              
                      `xxWxnxMWWW@@@WWW@W@@@@WWMMxMMMWWMMWWW@@WMMxznnxnz                                                                              
                      .MMMxzxxxMMMxMWWWM@@W@WWMxMxMMWWWMMMWWMWMMxMnznxn+                                                                              
                      ,MMxxnMxxxxMxMMMxM@@WWMWWWMxMMWWWWMMx;zMMMxxMxnnn.                                                                              
                      `nWWMMMnxxMxxWMMxW@WWWMMMMWMxWWWWWWz.iWMWMMxnMWWz                                                                               
                       *WW@@WWMWWMWWWWWWMWWMMMMMMMMMWWWW#` ixMMxxMxxxx,                                                                               
                       iMMWMWMMWW@WW@WMxWMMMMWMMWWMMMWWn`  +MxMxxMMMx`                                                                                
                       iMMWMMMMMMWWMxxxMMxWWWWWWWWMMMM+`   #MMxxxWxxz                                                                                 
                       *MWMMMMxxxMxxxMWMMxMWWWWWWWWMMi     #MMMxMMxx+                                                                                 
                       iMMWMxxMMMMMMWMMMMnM@@WWWWWWx:      zMxxMWxxx*                                                                                 
                       ,MWWMMMMMMMWWMMMMxnW@WWWWWx*`       zMxxMMxxx;                                                                                 
                       `xMWMMMMMMMMMMMMMxnWWWWWxi`         zMxMWxxxx,                                                                                 
                        #WMMMMMMMMMMMMMxxnMWx+:`           zMxMMxxxx`                                                                                 
                        .MMWWMWWMMMMMMMxMx+,               nxMMMxxxn                                                                                  
                         *MMWMMMMMMMMMMMxx*               `nxMxMMxx+                                                                                  
                         `xWMWMMMMMMMMMMxxz               .MMMMMMxM;                                                                                  
                          ;WWMMMMWMxxMMMxxM`              ,MMxWxxxx:                                                                                  
                       ,+#*MWMMMWMMMxMMMxxM,              .MMxMxMMn`                                                                                  
                     ,zWMMW@WMMWWWMxxxxxxxxi              .MMMWWMMx                                                                                   
                    `xMMMMW@@MM@WMMMxxxxxxxn`             `MWWWWWM#                                                                                   
                    ;MMMMMW@#WMWWMMMxxxxxxxMi             ;WMxxxMMi                                                                                   
                    ixMMMWxW@@MWWWMMxxxxxxxxz`            iMMMMxzM:                                                                                   
                    ;MMMMWMW@@@WWMMMxxxxxxxxn;            #WWMxxnM:                                                                                   
                    ,MMWMMWW@@@@WMxMMxxxxxxxnz`           +MMWMxnMi                                                                                   
                    `xWWMWMW@@@@@Wxxxxxxxxxxxxi           *MMMMMxM*                                                                                   
                     zWWWMM@@WW@WWMxMxxxxxxxxnn,          +WWMMMMxx,                                                                                  
                     #MWWMW@@WWWWMMxMMMxxxxxxnn:          xWMWMWMMxn,                                                                                 
                     zMMMMW@@@WWWWMMMxMMxxxxnnnn+        .WMWWWMMMxxx*,                                                                               
                    `xMWMnM@xiWWWM@WWMMMMMMxxxxMx`       ;WMWMWWWWMMMMx#;,`                                                                           
                    .xMWWWMWW.iWWxWWWWMWWMMMWWWMx.       *WMMWMWWWWMMMMMMMxn,                                                                         
                    ,MMMMMMMW; ;xxMxM@MMMxxxxxxxxi       +MMMWWWWWMMMMWWWMMM#                                                                         
                    .xMWWWMMW#  .xMMMWMWxxxxxxxxM#       #WWWWWWWWWWWWWMMMMW#                                                                         
                     #MMMMxMMM`  ,xMWWMMxnxxxxxxxi       :WWWWWWMxWWWWMMMMzi`                                                                         
                     `+MWMMMxz    `*MWW@MxxxnxMM+`        `,,,.`  .ii**;,`                                                                            
                       `....`      .xMWWxxxxxMx;                                                                                                      
                                    ,;MWMMMWx*.                                                                                                       
                                      ;z#**:`                                                                                                         
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      """)
    print("\n You finish making your mental adjustments for the scope and fix your sight on the president. You shoot.")
    print("\n it misses! you see a cloud of dust kick up somewhere off to the right of the car. The scope was far less accurate than you had thought")
    print("\n You fire 2 more times. Each misses. You try to adjust your aim each time, but the gun is simply not consistent. As you are coming to terms with this, you hear another shot overlap with yours.")
    print("\n As you watch, the president's head explodes in a pink mist, and he collapses into his wife's lap. You feel sick. It is time to leave")
    print("\nWhat do you do?")
    print("\n1)Try to hide the rifle, and leave")
    print("\n2)Drop the rifle and go.")
    answer = input()
    if answer == "1":
        michaelstart()
    elif answer == "2":
        michaelstart()
    
    
def oswald_abort():
    print("\nYou decide you cannot do it. You are going to abort the mission, and try to forget this ever happened. If the CIA want to punish you, so be it.")
    print("\nYou uncock your rifle, to make it safe, and you hide it amongst some boxes. As you do this, you hear loud cracks and screams.")
    print("\nYou look out of the window to see chaos breaking loose. The president's car is speeding off with secret service agents shielding it with their body")
    print("\nYou see that the president's head is a red ruin. There must have been a second shooter. You need to get out of here.")
    print("\nWhat do you do?")
    print("\n1)Finish hiding your rifle, and leave")
    print("\n2)Just leave")
    answer = input()
    if answer == "1":
        michaelstart()
    elif answer == "2":
        michaelstart()

def michaelstart():
 print("\n this is where michael's story starts.")

# start the game
start()

# The code block below pertains to the 3rd part: The arrest. Subject to changes, text art etc. The code block above has not been modified
def spacing():
    for i in range(2):
        print("\n")

import sys,time,os
def typewrite(title):
    for char in title:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char !="\n":
            time.sleep(0.1)
        else:
            time.sleep(0.5)

title="THE LEE HARVEY OSWALD RECORD: THE ARREST"

def game_title():
    spacing()
    print("THE LEE HARVEY OSWALD RECORD: THE ARREST")

def game_over():
    spacing()
    print("GAME OVER! YOU DIEDED :(")
    spacing()
    play_again()

def game_cleared():
    spacing()
    print("GAME CLEARED! ^_^")
    spacing()
    play_again()

def play_again():
    spacing()
    print("THANK YOU FOR PLAYING!")
    spacing()
    play_again=input("PRESS Y TO PLAY AGAIN")

    if play_again == "y" or "Y":
         start_game()
    else:
        exit()

def the_arrest():
    spacing()
    dealey_plaza()

def dealey_plaza():
    spacing()
    print("November 23, 1963\n")
    print("12:40 PM")
    spacing()
    print("You run acrross Dealey Plaza and two City Buses approach going in opposite directions.")
    print("Bus 1 is headed to North Oak Cliff and Bus 2 is headed to South Oak Cliff.") 
    print("Which Bus do you take?")
    spacing()
    print("1. Bus 1")
    print("2. Bus 2")
    spacing()
    
    answer = input("")

    if "1" in answer:
        spacing()
        bus1()
    elif "2" in answer:
        spacing()
        bus2()
    else:
        if input != '1' or '2':
            spacing()
            dealey_plaza()

def bus1():
    print("November 23, 1963\n")
    print("12:50")
    spacing()
    print("You're stuck in heavy traffic, escape is unlikely and paranoia thickens.") 
    print("Everyone is looking at you, whispering.") 
    print("You are disgruntled and frustrated so you are going to:")
    spacing()
    print("1. Ask the driver to let you transfer then take a Taxi Cab.")
    print("2. Stay on the bus as it is far too risky to stay out in public.")
    spacing()

    answer = input("")

    if "1" in answer:
        spacing()
        transfer1_1()
    elif "2" in answer:
        spacing()
        transfer1_2()
    else:
        if input != '1' or '2':
            spacing()
            bus1()

def transfer1_1():
    spacing()
    home()

def transfer1_2():
    spacing()
    home()
   
def bus2():
    spacing()
    print("November 23, 1963\n")
    print("12:50")
    spacing()
    print("You're stuck in heavy traffic, escape is unlikely and paranoia thickens.") 
    print("Everyone is looking at you, whispering.") 
    print("You are disgruntled and frustrated so you are going to:")
    spacing()
    print("1. Ask the driver to let you transfer and take a Taxi Cab")
    print("2. Stay on the bus as it is far too risky to stay out in public.")
    spacing()

    answer = input("")

    if "1" in answer:
        spacing()
        transfer2_1()
    elif "2" in answer:
        spacing()
        print("Game Over. The reason for Traffic was a blockade setup by Dallas Police.")
        print("The City Bus you took was raided and the Radio Broadcast instuction was to shoot you on sight.")
        spacing()
        game_over()
    else:
        if input != '1' or '2':
            spacing()
            bus2()

def transfer2_1():
    spacing()
    home()

def transfer2_2():
    spacing()
    game_over()
    spacing()
    print("Game Over. Dallas Police raided the bus and you were shot and killed on sight!")

def home():
    spacing()
    print("November 23, 1963\n")
    print("13:00")
    spacing()
    print("You arrive at your stay in. The House keeper Earlene Roberts greets you and makes small talk.")
    print("There is no time to waste, every second counts and Police sirens are rampant everywhere.")
    print("You decide to...")
    spacing()
    print("1. Speak to Earlene, pretend you do not know anything, gather some belongings and catch the next Bus out of town.")
    print("2. Ignore Earlene, quickly change clothes, grab your gun, IDs and money then catch the next Bus out of town.")
    spacing()

    answer = input("")

    if "1" in answer:
        spacing()
        bus_stop1()
    elif "2" in answer:
        spacing()
        bus_stop2()
    else:
        if input != '1' or '2':
            spacing()
            home()

def bus_stop1():
    spacing()
    print("November 23, 1963\n")
    print("13:15")
    spacing()
    print("You are at the Bus Stop and a Dallas Police Car drives past you at high speed.")
    print("The Police Car doubles back, turns around and steers towards you.")
    print("The Police Car approcahes and pulls up some feet ahead of you.")
    print("As the blinding lights fill you with despair the Police Officer driving speaks from the window.")
    print("He's shouting but you can not hear a thing as the siren screeches.")
    print("The driver's side door opens as the Police Officer steps out.")
    spacing()
    print("1. The Police Officer just want's to ask something so you play along.")
    print("2. You are not taking any chances and fire as many rounds as you can at the Police Officer.")
    spacing()
    
    answer = input("")

    if "1" in answer:
        spacing()
        print("You were identified from the description broadcasted on State Radio.")
        print("Dallas Police Officer J. D. Tippit was warning you to disarm and drop to the ground!")
        game_cleared()
    elif "2" in answer:
        spacing()
        print("You left your gun back at your stay-in. Dallas Police Officer J. D. Tippit shot you dead!")
        game_over()
    else:
        if input != '1' or '2':
            spacing()
            bus_stop1()

def bus_stop2():
    spacing()
    print("November 23, 1963\n")
    print("13:15")
    spacing()
    print("You are at the Bus Stop and a Dallas State Police Car drives past you at high speed.")
    print("The car doubles back, turns around and steers towards you.")
    print("The Police Car approcahes and pulls up some feet ahead of you")
    print("As the blinding lights fill you with despair the Police Officer driving speaks from the window.")
    print("He's shouting but you can not hear a thing as the siren screeches.")
    print("The driver's side door opens as the Police Officer steps out.")
    spacing()
    print("1. The Officer just want's to ask something so you play along.")
    print("2. You are not taking any chances and fire as many rounds as you can into the vehicler.")
    spacing()

    answer = input("")

    if "1" in answer:
        spacing()
        jd_tippit1()
    elif "2" in answer:
        spacing()
        jd_tippit2()
    else:
        if input != '1' or '2':
            spacing()
            bus_stop2()

def jd_tippit1():
    spacing()
    print("Game Over. Dallas Police Officer J. D. Tippit was warning you to dissarm and drop to the ground!")
    print("The Police Radio Broadcast instruction was to shoot you on sight, you are dead!")
    spacing() 
    game_over()
    
def jd_tippit2():
    spacing()
    print("You have killed a State Police Officer, 4 founds went off and you are certain someone must have heard.")
    print("\nThere are no signs of pursuing Police Units so you:")
    spacing()
    print("1. Look around for nearby civillians and tie up all loose ends -- with no witnesses the getaway will be clean.")
    print("2. Flee. Run as far away from the area as possible. There is a shoe store nearby you aare certain you can blend in.")
    spacing()

    answer = input("")

    if "1" in answer:
        spacing()
        shooting1()
    elif "2" in answer:
        spacing()
        shooting2()
    else:
        if input != '1' or '2':
            spacing()
            jd_tippit2

def shooting1():
    spacing()
    print("Game Over. Dallas Police's Emergency Respose Unit watching you fron across the junction responded with Leathal Force!")
    print("You acted suspicious, the House Keeper Earlene Roberts called Dallas Police immediately after seeing you take your gun and run.")
    print("She also noticed the clothes you wore when you came home fit the suspect's description on the News Broadcast.")
    print("Earlene watched you gun down Police Officer J. D. Tippit in cold blood from the window which is across from the Bus Stop.")
    spacing()
    game_over()

def shooting2():
    spacing()
    print("November 23, 1963\n")
    print("13:30")
    spacing()
    print("You run around the block and stumble into George's Shoe Store.")
    print("It's quite busy and the manager Jonny Brewer greets you.")
    print("As sirens get louder, more and more police cars survey the area.")
    print("Everyone in the store is talking about the shooting at the Motorcade.")
    print("You are getting sloppy, tired and scared. You have made your mind up...")
    spacing()
    print("1. You have come too far to let it end here, take a hostage and take control. This will work!")
    print("2. Hang back for a bit then leave for the Theatre down the road that should be perfect cover. Nobody should know about the shooting in there.")
    spacing()

    answer = input("")

    if "1" in answer:
        spacing()
        shoe_store1()
    elif "2" in answer:
        shoe_store2()
    else:
        if input != '1' or '2':
            spacing()
            shooting2()

def shoe_store1():
    spacing()
    print("Game Over. Jonny could smell the danger off you as soon as you walked in, he shoots you the second you reach for your gun.")
    spacing()
    game_over

def shoe_store2():
    print("November 23, 1963\n")
    print("13:40")
    spacing() 
    print("You run down to the Texas Theatre and there is nobody at the Ticket Desk so you stroll on in.")
    print("Dallas Police Officer Nick McDonald notices your appeareance, sees this and follows you inside.")
    print("His foot steps echo behind yours so you clasp at your gun...")
    spacing()
    print("1 Do not give the Police Offer a chance to draw his weapon, shoot first.")
    print("2 You have done a lot of running, you are tired and out of ideas. You put hands up and surrender.")
    spacing()

    answer = input("")

    if "1" in answer:
        spacing()
        theatre1()
    elif "2" in answer:
        spacing()
        theatre2()
    else:
        if input != '1' or '2':
            spacing()
            shoe_store2()

def theatre1():
    spacing()
    print("Game Over. You fired 4 shots killing Police Officer J. D. Tippit.")
    print(" Your Gun jammed up and Dallas Police Officer Nick Mcdonald shot you dead.")
    spacing()
    game_over

def theatre2():
    spacing()
    print("Game cleared. You are now in custody. You have been baught but you are still alive.")
    spacing()
    game_cleared()
    spacing()
    play_again()

def start_game():
    typewrite(title)
    the_arrest()

def end_game():
    print("THANK YOU FOR PLAYING! ")

start_game()
