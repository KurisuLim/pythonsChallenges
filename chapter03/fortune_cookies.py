#Fortune Cookie
#
#In this program every time the program restart, there will be a
#random generated number from 1 to 5. And each number will represent
#a unique fortune.

import random;

fortuneCookies = random.randint(1,5);
fortune1 = "Today it's up to you to create the peacefulness you long for."
fortune2= "A friend asks only your time not your money."
fortune3 = "If you refuse to accepts anything but the best, you very often get it."
fortune4 = "A smile is your passport into the hearts of others."
fortune5 = "A good way to keep healthy is to eat more Chinese food."

if fortuneCookies == 1:
    print("Fortune: ",fortune1);

elif fortuneCookies == 2:
    print("Fortune: ",fortune2);

elif fortuneCookies == 3:
    print("Fortune: ",fortune3);

elif fortuneCookies == 4:
    print("Fortune: ",fortune4);

elif fortuneCookies == 5:
    print("Fortune: ",fortune5);

input("\nThanks for playing! Have a great day! Press Enter to end the program");
