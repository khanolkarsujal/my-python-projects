import random 


last_digit = 1
# generate list in sequence 


while True:


    def computer_choice():

        random_num = random.randint(1,3)

        
        computer_choice_list = []

        for i in range(random_num):

                computer_choice_list.append(str(last_digit))
                last_digit += 1

                last_digit = computer_choice_list[-1]

                


        return computer_choice_list , last_digit

    res , current = computer_choice(last_digit)

    word = ""
    for n in res:
        word += n
    print(f"The computer choice is :{word}")


    last_digit = 1


    while last_digit !=  "21":

        user_num = input("Enter  next number  upto 3 :")



        if user_num.isdigit() == False:
            print("try again")

            if len(user_num) > 3:
                print("try again ... enter only upto 3 digits ")

        last_num = 1


        valid_list = []
        for i in range(1,4):
            valid_list.append(str(last_num))
            last_num += 1

        last_digit = valid_list[-1]


        user_num_list = []
        for n in user_num:
            user_num_list.append(str(n))


        print(user_num_list)

        if user_num_list != valid_list[:len(user_num_list)]:
            
            print("try again.. and Enter the digits in sequence !")

        if last_digit == "21":
            print("GAME OVER")























