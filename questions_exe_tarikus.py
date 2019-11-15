import winsound

def beep():
    
    frequency = 2500
    duration = 300
    winsound.Beep(frequency, duration)

    
def intro():
    print()
    print()
    print()
    print("""
                !=========================Assalamu alaikum===========================!
                !This program is created by * Torikus sadik Raihan *                 !
                !Special thanks for Atikur Rahman,Shakil Babu, Shorna Ahmed Apu ,    !
                !Arafat Hossain Broh! This is just a simple program. Try it and ans  !
                !some questions.If you are correct then program will tell you that'  !
                !==========================Happy coding==============================!
        """)
    print()
    print()
    print()
intro()
#intro() ends from here.


#Question1 starts from here

def q1():
    print('    Easy questions :)')
    print()
    print()
    print("""
    1. ** ei cinno ke python a ki bole?""")
    print()
    prosno1 = input(str('    Ekhane apnar uttor likhun: '))
    if prosno1 == 'Exponent' or prosno1 =='exponent' or prosno1 == 'expo':
        print()
        print("    Correct!! ")
    else:
        print(beep())
        print("    wrong!! try next :P")
        print()
q1()

#Question2 starts from here.

def q2():
    print()
    print("""
    2. Python a Modulus amra keno bebohar kori?
              a. Vagfol dekhar jonno     b. Vagsesh dekhar jonno
              c. vag korar jonno         d. Gun korbar jonno.""")
    print()
    prosno2 = input(str('    Ekhane apnar uttor likhun: '))
    if prosno2 == 'b':
        print()
        print("    Correct!!")
    else:
        print(beep())
        print("    wrong!! try next")
        print()
q2()

#Question 3 start from here:

def q3():
    print()
    print("""
    3. Integer division / floored quotient er kaj ki ?
    
    a. Vag kora            b.Gun kora
    c. vagsesh ber kora    d. Sudhu integer value print kora?
    """)
    prosno3=input(str('    Ekhane apnar uttor likun:'))
    if prosno3 == 'd':
        print('    Correct!!!')
    else:
        print(beep())
        print('    Wrong!! try next')
        print()

q3()

#Question 4 start from here

def q4():
    print()
    print("""
    4. Ei program tar output ki hobe?
    True naki False?
    program:
    >>>42 == 41
""")
    print()
    prosno4 = input(str('    Ekhane apnar uttor likhun:'))
    if prosno4 == 'False':
        print('    Correct!!!')
    else:
        print(beep())
        print('    Wrong!!! Try next!')
        print()
q4()

#Question 5 starts from here

def q5():
    print()
    print("""
    5. Nicher program ta ki shothik?
    yes or no?
    >>> 'Assalamu alaikum!
    
""")
    print()
    prosno5 = input(str('    Ekhane apnar uttor likhun:'))
    if prosno5 == 'no' or prosno5=='Na' or prosno5== 'No':
        print('    Correct!!! ')
    else:
        print(beep())
        print('    Wrong!!! Try next!')
        print()
q5()

#Question 6 starts from here

def q6():
    print()
    print("""
    6. Nicher program ta ki shothik?
    yes or no?
    
    >>> 5 +
    
    
    """)
    print()
    prosno6 = input(str('    Ekhane apnar uttor likhun:'))
    if prosno6 =='No' or prosno6=='no' or prosno6=='na':
        print('    Correct!!! ')
    else:
        print(beep())
        print('    Wrong!!! Try next!')
        print()
q6()

        
#Question7 starts from here

def q7():
    print()
    print("""
    7.  Nicer program tar output ki?
    >>> 'Alice' + 'Bob'
    a. Alicebob
    b. bobAlice
    c. Alice Bob
    d. AliceBob
""")
    print()
    prosno7 = input(str('    Ekhane apnar uttor likhun:'))
    if prosno7 == 'd' or prosno7=='d.':
        print('    Correct!!! ')
    else:
        print(    beep())
        print('    Wrong!!! Try next!')
        print()
q7()

#Question8 starts from here.

def q8():
    print()
    print("""
    8. Nicher program ti ki error throw korbe?
    >>> 'Apple' * 'Bananan'
    yes or no type bellow.?
    
""")
    print()
    prosno8 = input(str('    Ekhane apnar uttor likhun:'))
    if prosno8 == 'yes' or prosno8 == 'Yes' or prosno8 == 'YES' or prosno8 == 'ha':
        print('    Correct!!! ')
    else:
        print(    beep())
        print('    Wrong!!! Try next!')
        print()
q8()

#Question9 starts from here.

def q9():
    print()
    print("""
    9.  Amra jodi kono string ba list er mot songkha ba letter ber korte cai tahole kon function use korbo?
    a. print()
    b. len()
    c. def()
    d. thor()
""")
    print()
    prosno9 = input(str('    Ekhane apnar uttor likhun:'))
    if prosno9 == 'b' or prosno9 == 'b.':
        print('    Correct!!! ')
    else:
        print(    beep())
        print('    Wrong!!! Try next!')
        print()
q9()


#Question10 starts from here

def q10():
    print()
    print("""
    10. Nicher operator guloke aksathe ki bola jay?
    ==
    !=
    <
    >
    <=
    >=
    
""")
    print()
    prosno10 = input(str('    Ekhane apnar uttor likhun:'))
    if prosno10 == 'comparison operator' or prosno10 == 'comparison' or prosno10 == 'Comparison':
        print('    Correct!!! ')
    else:
        print(    beep())
        print('    Wrong!!! Try next!')
        print()
q10()





def q11():
    print('    Do you wanna make yourself surprise?')
    sur= input(str('    If you want type yes you dont want type no: '))
    
    if sur=='Yes' or sur== 'yes':
        print("""
            !=======================================================================
            !   ___                         __   ______     _                    _  !
            ! |  _ \                       / _| |  ____|   | |                  | | !
            ! | |_) | ___  ___ ___    ___ | |_  | |__ _   _| |_ _   _ _ __ ___  | | !
            ! |  _ < / _ \/ __/ __|  / _ \|  _| |  __| | | | __| | | | '__/ _ \ | | !
            ! | |_) | (_) \__ \__ \ | (_) | |   | |  | |_| | |_| |_| | | |  __/ |_| !
            ! |____/ \___/|___/___/  \___/|_|   |_|   \__,_|\__|\__,_|_|  \___| (_) !
            !                                                                       !
            ============================Torikus Sadik Raihan=======================
""")
    else:
        print('Sorry! i cant show you!')
q11()

def thanks():
    you = input(str("    Do you wanna get a wish for yourself? yes or no:"))
    if you == 'yes' or you == 'Yes' or you == 'YES':
     print("""
===========================Thanks For Using This Application=======================
""")
    else:
        print("Go to home")
thanks()
