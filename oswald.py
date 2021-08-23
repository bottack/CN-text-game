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
