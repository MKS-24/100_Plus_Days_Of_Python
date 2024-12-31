intro = "Welcome_to_KBC"
description = """
Introduction:
    Step into the world of knowledge, strategy, and excitement with the KBC-inspired quiz game! 
    This game tests your general knowledge with a series of progressively difficult questions. 
    Each correct answer takes you closer to winning the ultimate prize, 
    while a single wrong answer could cost you your progress—unless you’ve reached a safety milestone!
"""
WorkingOfGame = """How Its Works
1.Questions and Answers:
    The game consists of 15 multiple-choice questions.
    Each question has four options: A, B, C, and D, with only one correct answer.
  
2.Lifelines:
To help you through tricky questions, you have 3 lifelines:
    50-50: Removes two incorrect options, leaving one correct and one incorrect choice.
    Phone a Friend: Simulates calling a friend for advice on the correct answer.
    Ask the Audience: Provides a percentage-based suggestion of the audience’s votes.

3.Levels and Milestones:
    The questions are divided into levels of increasing difficulty.
    There are two safety milestones: after answering 5th and 10th questions correctly, you are guaranteed a minimum prize even if you lose later.
    
4.Winning or Losing:
    Each correct answer increases your prize money.
    A wrong answer ends the game unless you have reached a milestone.

5.Prize Money for KBC India:
    Question No.	Prize Money
    1st Question	₹1,000
    2nd Question	₹2,000
    3rd Question	₹3,000
    4th Question	₹5,000
    5th Question	₹10,000
    6th Question	₹20,000
    7th Question	₹40,000
    8th Question	₹80,000
    9th Question	₹1,60,000
    10th Question	₹3,20,000
    11th Question	₹6,40,000
    12th Question	₹12,50,000
    13th Question	₹25,00,000
    14th Question	₹50,00,000
    15th Question	₹1 Crore (₹1,00,00,000) 

1 Crore (₹1,00,00,000) is the grand prize for answering all 15 questions correctly.
"""
objective = """Objective:
    Answer all 15 questions correctly to win the ultimate prize and become a quiz champion. 
    But beware! A single misstep could cost you everything. Use your knowledge, strategy, and lifelines wisely to reach the top!
"""
print("\033[1m",intro.center(90),description,WorkingOfGame,objective,"\033[0m",sep="\n")


question = [
    "1.Which planet is known as the Red Planet?",
    "2.Who invented the light bulb?",
    "3.How many continents are there in the world?",
    "4.What is the square of 12",
    "5.What is 15% of 200?",
    "6.If you subtract 20 from 100, then divide by 4, what is the result?",
    "7.When did Pakistan gain independence?",
    "8.What is the national flower of Pakistan?",
    "9.Who was the first Prime Minister of Pakistan?",
    "10.What is the chemical symbol for water?",
    "11.Which organ in the human body is responsible for pumping blood?",
    "12.What gas do plants release during photosynthesis?",
    "13.Who is known as the “Father of History”?",
    "14.Which empire built the Great Wall of China?",
    "15.Which country has won the most FIFA World Cups?",
]
answer = [
    "A) Earth \nB) Mars  \nC) Jupiter \nD) Venus",
    "A) Alexander Graham Bell \nB) Nikola Tesla \nC) Thomas Edison \nD) Benjamin Franklin",
    "A) 5 \nB) 6 \nC) 7 \nD) 8",
    "A) 120 \nB) 144 \nC) 132 \nD) 124",
    "A) 20 \nB) 30 \nC) 25 \nD) 30",
    "A) 20 \nB) 30 \nC) 25 \nD) 35",
    "A) 1945 \nB) 1946 \nC) 1947  \nD) 1948",
    "A) Jasmine  \nB) Rose \nC) Sunflower \nD) Tulip",
    "A) Liaquat Ali Khan \nB) Muhammad Ali Jinnah\nC) Ayub Khan \nD) Zulfikar Ali Bhutto",
    "A) CO2 \nB) H2O  \nC) O2 \nD) CH4",
    "A) Brain \nB) Lungs \nC) Heart  \nD) Liver",
    "A) Carbon dioxide \nB) Oxygen  \nC) Nitrogen \nD) Hydrogen",
    "A) Aristotle \nB) Socrates \nC) Herodotus  \nD) Plato",
    "A) Roman Empire \nB) Ottoman Empire \nC) Qin Dynasty \nD) Mughal Empire",
    "A) Germany \nB) Brazil  \nC) Italy \nD) Argentina",
]
fifty_fifty = [
    "A) Earth\nB) Mars",  
    "C) Thomas Edison\nD) Benjamin Franklin", 
    "A) 5\nC) 7",  
    "B) 144\nC) 132", 
    "A) 20\nD) 30", 
    "A) 20\nB) 30",  
    "C) 1947\nD) 1948",  
    "A) Jasmine\nC) Sunflower", 
    "A) Liaquat Ali Khan\nD) Zulfikar Ali Bhutto", 
    "B) H2O\nD) CH4", 
    "C) Heart\nD) Liver", 
    "B) Oxygen\nD) Hydrogen",  
    "A) Aristotle\nC) Herodotus", 
    "A) Roman Empire\nC) Qin Dynasty", 
    "B) Brazil\nC) Italy"  
]
Correct_Answer = ("B", "C", "C", "B", "D","A","C","A","A","B","C","B","C","C","B")


flag = False
Total_Amount = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
print("Ye Raha Pehla Sawaal Aapki Aap Ki Computer Screen Per..\n")
i = 0
while i < len(question):
    print(question[i])
    print(answer[i])

    
    if flag == False:
        play5050 = input("\n\033[1mDo you want to choose 50:50 life-line?\033[0m\nAnswer : ")
        if play5050.upper() == "YES":
            print(fifty_fifty[i])
            flag = True

    key = input(f"\nEnter Answer of the Question {i+1} : ")
    while(key.upper() > "D"):
        key = input(f"You Choose Wrong Option : ")
        if key.upper() == "A" or key.upper() == "B" or key.upper() == "C" or key.upper() == "D":
            break

    if key.upper() == Correct_Answer[i]:
        Winningamount = Total_Amount[i]
        print("\nSahi jawab!!",f"Fantastic! You're now at ₹{Winningamount}. Well done!\n",sep="\n")
        if(i<len(question)-1):
            playmore = input("Do you want to continue the game.\nAnswer : ")
            if(playmore.upper() == "NO"):
                print(f"\n\033[1mCongratulations! You've won ₹{Winningamount}. Well done for reaching this far. Thank you for playing!\033[0m")    
                break
    
    else:
        print("\n\033[1mI'm sorry, but you've answered incorrectly. You don't win any prize today. Thank you for playing, and we hope to see you again!\033[0m")
        break
    if(i<len(question)-1):
        print("\nYe Raha Agla Sawaal Aap Ki Computer Screen Per..\n")
    i+=1  