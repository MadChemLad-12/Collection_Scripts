# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[],
          play_order=[{
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0,
          }]):
    opponent_history.append(prev_play)
  
    if not prev_play:
        prev_play = 'R'
    opponent_history.append(prev_play)

    last_two = "".join(opponent_history[-2:])
    if len(last_two) == 2:
        play_order[0][last_two] += 1

    potential_plays = [
        prev_play + "R",
        prev_play + "P",
        prev_play + "S",
    ]

    sub_order = {
        k: play_order[0][k]
        for k in potential_plays if k in play_order[0]
    }

    prediction = max(sub_order, key=sub_order.get)[-1:]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]

  
### What are my opponents doing?
#Quincy is slowly going through each letter with long reppeting sequences
#Mrugesh is countering my most common last ten plays
#Kris is just playing the counter from my previous move
#abbey is actually learning from letter combinations and countering accordinly

#need to work on beating abbey and kris




  
    #guess = "R"
    #if len(opponent_history) > 2:
     #   guess = opponent_history[-2]

    #return guess



#To win the Ai needs to know ideal responce to counter
#needs to build behvour based on what was played previously