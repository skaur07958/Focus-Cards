import random

def focus(number):
  if number ==1:
    print("Focus on your wellbeing. This includes your mental and emotional wellbeing. Take time to reflect and relax.")
  elif number ==2:
    print("Focus on abundance because money and abundance is on the way. Keep a positive and healthy mind and the process will come even quicker.")
  elif number ==3:
    print("Focus on nature. Stay grounded and protected by nature. Take regular walks or be near animals. They are down-to-earth and intune with nature.")
  elif number ==4:
    print("Focus on manifestion. The universe if your oyster. The magician within you wants to play...now what shall I wish for today?")
  elif number ==5:
    print("Focus on work. Time to evaluate your work.")
  elif number ==6:
    print("Focus on your health.Health is wealth. Loook after your physical body")
  elif number ==7:
    print("Focus on self care. Selfcare can mean lots of things but love yourself like a Mom for a child.")
  elif number ==8:
    print("Focus on the environment.Is your home ideal? Does your room need cleaning/decluttering? Do it!")
  elif number ==9:
    print("Focus on travel. because you have places to go and people to see. You shall be travelling overseas very soon. ")
  elif number ==10:
    print("Focus on your new career. Time to look for a new career which is inline with your higher self.")
  elif number ==11:
    print("Focus on creativity. Start a new hobby. Does it seem fun? Does it make you feel alive? Do it!")
  elif number ==12:
    print("Focus on protection. You are protected regardless of what people send you.")
  elif number ==13:
    print("Focus on business. Business opportunities are coming so be prepared.")
  elif number ==14:
    print("Focus on friendships because friendships are about celebrating.")
  elif number ==15:
    print("Focus on healing because broken things need to be fixed before it moves on. Be loving and honest to yourself at this stage.")
  elif number ==16:
    print("Focus on money because money is on the way. You could end up with unexpected finances - so enjoy!")
  elif number ==17:
    print("Focus on your studies. You need to study so what are you waiting for? ")
  elif number ==18:
    print("Focus on love. Love and Romance are on the way. This could mean a spiritual connection is coming so be prepared...or not.")
  elif number ==19:
    print("Focus on change. It may feel like a lot is happening...just ride with it...")
  elif number ==20:
    print("Focus on the silver lining. We all have bad days, but remember....'this too shall pass'...")
  elif number ==21:
    print("Focus on prayers. Prayers are extremely powerful for you and for others.")

number = int(input('Choose a number between 1-21?\n'))
if number >=22:
  randNum = random.randint(1, 21)
  focus(randNum)
else:
  focus(number)
