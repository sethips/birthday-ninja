import requests
import json
import random

TOKEN = 'CAACEdEose0cBAORIgM1YVxZCFUO2bh85lODxnF5R8UXaY5Fy9zqa9vJ1YcXMfBjU8gIHZAxZB3RprJ2v777UYKD4WOZCZCRxssoZBbKnNSfatZAJ7Q5Rapo9WLlKi1pqFnHRFhZAHtlfBxZB9pdL2LCJiG4utZADuoe4F8WCYGyIA4Gx4gNjXV4TZAA9ZCs9s6GdrsUjdF4C5881fir36SqAZAo6IuWK0T5wMcVntrqM1wIeGXwZDZD'

comment_list = ['Thanks :)', 'Thank you so much :D', 'thanx', 'Thanks for making my day special! :)', 'Thanks a bunch! How are you doing these days?']

def get_birthday_feed():
  # Facebook graph API returns only 25 links at once.
  init_url = 'https://graph.facebook.com/me/feed?access_token=' + TOKEN
  
  flag = True
  while(flag):
    result = json.loads((requests.get(init_url)).text)
    #print result
    for i in range(0, len(result['data'])):
      print result['data'][i]['from']['name'] + " : " + result['data'][i]['message']
      print "(R)eply, (n)ext or (e)xit?"
      user_response = str(raw_input())
      if user_response == 'R' or user_response == 'r':
        comment = comment_list[random.randint(0, len(comment_list)-1)]
        print "Replying With : " + comment
        # send a post
      elif user_response == 'n' or user_response == "N":
        print "Skipping this guy"
      elif user_response == "e" or user_response == "E":
        print "Exiting"
        flag = False
        break
      else:
        print "No valid input"
      
    # get next set of data
    init_url = result['paging']['next']

get_birthday_feed()