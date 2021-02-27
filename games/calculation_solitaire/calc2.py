# Calculation solitaire - Joseph Grimer - October 2018

import random
from copy import deepcopy

GAMES_PER_SEQUENCE_TEST = 512 # higher = increased accuracy of SEQUENCE test
INITIAL_SEQUENCES = 256 # 2048*8*14*8 # the higher the slower
MINIMUM_SCORE = 13 # quality control out of 52
RUNTS_PER_ROUND = 12 # should be fraction of initial sequences
CHILDREN_PER_ROUND = 255
GENETIC_VARIATION = 12 # / 36
MAX_ROUNDS = 96*12 # avoid infinite loop
TOLERANCE = 4 # will affect minumum score each round

def main():
    print("Calculation Solitaire Simulator")
    print("i.e. Not the actual game :P\n")

    print("INITIAL COMBOS: "+str(INITIAL_SEQUENCES)+" (higher is    better)")
#   print("GAMES_PER_SEQUENCE_TEST: "+str(GAMES_PER_SEQUENCE_TEST)+" (higher is better)")
    print("Mimumum score (to be selected for next round): "+str(MINIMUM_SCORE))

    print("Please await results (lower is better, 4-52)")
#   run()

#   top_row=[12,12,12,8]
#   bottom_row=[[12,3,7],[5],[6],[10,13]]
#   print(is_hopeful(top_row,bottom_row))
    deck = [11, 1, 5, 6, 3, 2, 5, 2, 13, 12, 9, 13, 1, 6, 8, 6, 4, 10, 11, 8, 12, 13,4, 7, 11, 12, 10, 7, 13, 9, 9, 8, 4, 11, 10, 9, 3, 2, 10, 6, 3, 12, 5, 1, 8, 7,7, 5]
    super_pruner(deck)

    print("end of program.")

def run():
    results = []
#   one_suit = range(1,14)
#   deck = (one_suit*4)[4:]
#   random.shuffle(deck)
    deck = [11, 1, 5, 6, 3, 2, 5, 2, 13, 12, 9, 13, 1, 6, 8, 6, 4, 10, 11, 8, 12, 13,4, 7, 11, 12, 10, 7, 13, 9, 9, 8, 4, 11, 10, 9, 3, 2, 10, 6, 3, 12, 5, 1, 8, 7,7, 5]
    print("Deck:"+str(deck))
    sequences = []
    bar = MINIMUM_SCORE
    best = [] # where I keep the best sequence found
    best_score = 13

    print("Generating sequences.")
    for i in range(0,INITIAL_SEQUENCES):
        # generate a new 'SEQUENCE'
        sequence = []
        for i in range(0,48):
            sequence.append(random.randint(0,3))
        sequences.append(sequence)

    print("Let the rounds begin")
    for j in range(0,MAX_ROUNDS):
        print("round: "+str(j)+"; sequences left: "+str(len(sequences)))
        new_sequences = []
        new_sequences_scores = []
        for sequence in sequences:
            result = play_game(sequence, deck)
            if result >=best_score:
                best = sequence
                best_score = result
            results.append(result)
        sequences = [best] #new_sequences
        bar = ((max(results)+bar)/2) #-TOLERANCE

        # generate more based on winner
        for k in range(0, CHILDREN_PER_ROUND):
            new_sequence = deepcopy(best)
            for l in range(0, GENETIC_VARIATION):
                choice_to_change = random.randint(0,best_score)
                new_sequence[choice_to_change-1] = random.randint(0,3)
            sequences.append(new_sequence)

        print("result: "+str(best_score))

    print("The rounds have ended. Best result: "+str(max(results)))
    #average = (sum(results)/float(len(results)))
    #print(average)
    #return average

def super_pruner(deck):

    # prepare game
    top_row=[1,2,3,4]
    bottom_row = [[],[],[],[]]
    
    # prepare tree
    sequence = []
    for i in range(0,48):
        sequence.append(random.randint(0,3))
    card_pointer = 47

    def play_turn(pointer):
        # check bottom sets for matches first
        # automatically place available - possibly bad strategy
        for j in range(1,5):
            if top_row[j-1] is not 13:
                for k in bottom_row:
                    if len(k) and k[-1]==top_row[j-1]+j:
                        top_row[j-1] = k.pop()
                        return pointer

        # else check top card for matches
        for j in range(1,5):
            if top_row[j-1] is not 13 and deck[pointer] == top_row[j-1]+j:
                top_row[j-1] = deck[pointer]
                return pointer-1

        # else put top card on a prefferred pile
        options = 4
        while   is_blocking_move(top_row,
                        bottom_row[sequence[pointer]],
                        deck[pointer]) and options:
#           print("max",max)
            sequence[pointer]=(sequence[pointer]+1)%4
            options-=1
        if options==0:
            print("You've followed a path that I cannot follow")
            return 0
#           print("I smell death... "+str(deck[pointer])+
#           " should not join "+str(bottom_row[sequence[pointer]])+
#           " when top row is " + str(top_row))
            
        bottom_row[sequence[pointer]].append(deck[pointer])
        return pointer-1

    # simulate the game - using the above function - 96 max turns
    for i in range(1,96):
        print("playing turn",card_pointer)
        card_pointer = play_turn(card_pointer)
        if not card_pointer:
            print("out of cards")
            break
    
    print("game over",str(card_pointer),top_row,bottom_row)


def play_game(sequence, deck):
    # reset the game with the pre-shuffled deck
    top_row = [1,2,3,4]
    bottom_row = [[],[],[],[]] # would tuples be better ? no
    card_pointer = 47

    def play_turn(pointer):
        # else check top card for matches
        for j in range(1,5):
            if top_row[j-1] is not 13 and deck[pointer] == top_row[j-1]+j:
                top_row[j-1] = deck[pointer]
                return pointer-1

        # check bottom sets for matches
        # automatically place available - possibly bad strategy
        for j in range(1,5):
            if top_row[j-1] is not 13:
                for k in bottom_row:
                    if len(k) and k[-1]==top_row[j-1]+j:
                        top_row[j-1] = k.pop()
                        return pointer

        # else put top card on a prefferred pile
        bottom_row[sequence[pointer]].append(deck[pointer])
        return pointer-1

    # simulate the game - using the above function - 96 max turns
    for i in range(1,96):
        card_pointer = play_turn(card_pointer)
        if not card_pointer:
            break

    # score the game based on cards played to sets
    result = 52 - (
        len(bottom_row[0])+
        len(bottom_row[1])+
        len(bottom_row[2])+
        len(bottom_row[3]) )
    return result

def is_blocking_move(top_row, bottom_column, new_card):
    ranks_used = [4]*13

    # top row counts
    col_iterator = 0
    for col in top_row:
        col_iterator += 1
        while col is not 0:
            ranks_used[col-1] -= 1
            col = (col-col_iterator)%13
    
#   bottom_row[new_column].append(new_card)

    for x in bottom_column:
        if precedes(x,new_card) > ranks_used[x-1]:
            return True
    return False

def is_hopeful(top_row, bottom_row):
    
    # init
    ranks_used = [0]*13
    #print("top row")
    #print(top_row)
    #print("bottom row")
    #print(bottom_row)
    
    # top row counts
    col_iterator = 0
    for col in top_row:
        col_iterator += 1
        ranks_used[col] += 1
        while col is not col_iterator:
            col = ((col-col_iterator)%13)
            ranks_used[col] += 1


    #   bottlenecks = [rank for rank in ranks_used if ranks_used[rank]==1]
        
    #print("ranks")
    #print(ranks_used)
    
    # bottom row checks based on bottlenecks
    for column in bottom_row:
        x_i = 0
        for x in column:
            for y in column[x_i:]:
                if precedes(x,y)>(4-ranks_used[x-1]):
                    return False
                    #print("broken rank count "+    str(ranks_used[x-1])+
                    #" x>"+str(x)+
                    #" y>"+str(y)+
                    #" card precedes>"+str(card_precedes(x,y)))
            x_i+=1
    # todo this doesn't yet count for cross-locks
    return True

def succeess(card_A, card_B):
    return 4-precedes(card_B,card_A) # exception for 12 and such?

def precedes(card_A, card_B): # only 13*12=166 combos
    matches = 0
    card_B %= 13
    for column in range(1,5):
        card_C = card_A%13
        while card_C!=0:
            card_C=(card_C+column)%13
            if card_C==card_B:
                matches+=1
                break
    return matches

main()

##################### elephant graveyeard
"""
print("hello")
def tactic_A(number, top_row, bottom_row,nothing): # 13
    return 0
def tactic_B(number, top_row, bottom_row,nothing): # 14
    return random.randint(0,3)
def tactic_C(number,top_row,bottom_row,nothing): # 14
    best_col = 0
    best_col_sum = -1
    for i in range(0,4):
        col_sum = sum(bottom_row[i])
        if best_col_sum==-1 or col_sum < best_col_sum:
            best_col_sum = col_sum
            best_col = i
    return best_col
def tactic_D(number,top_row,bottom_row,nothing):
    best_col = 0
    best_col_sum = -1
    for i in range(0,4):
        col_sum = sum(bottom_row[i])
        if best_col_sum==-1 or col_sum > best_col_sum:
            best_col_sum = col_sum
            best_col = i
    return best_col
def tactic_E(number,top_row,bottom_row,biases):
    for bias in biases:
        for i in range(0,4):
            if bias == bottom_row[i]:
                return i
    # else
    return 0
def tactic_F(number,top_row,bottom_row,biaseses):
    for bias in biaseses[number-1]:
        for i in range(0,4):
            if bias == bottom_row[i]:
                return i
    # else
    return 0
def strategy_F():
    def create_F_SEQUENCE():
        biaseses = []
        for j in range(1,14):
            biases_high = range(1,14)
            random.shuffle(biases_high)
            biaseses.append(biases_high)
        return biaseses
    sequences = []
    # init the sequences
    for i in range(0,INITIAL_SEQUENCES):
        sequences.append(create_F_SEQUENCE())
    # start running then SEQUENCEing
    max = 0
    for h in range(0,12):
        good_sequences = []
        print("SEQUENCEing run "+str(h)+" sequences"+str(len(sequences)))
        for SEQUENCE in sequences:
            result = run_tactic(tactic_F,SEQUENCE)
            if result>14:
                good_sequences.append(SEQUENCE)
                #print("a good SEQUENCE: "+str(result))
                if result>=max:
                    print("new best: "+str(result))
                    max = result
        if len(good_sequences)>1:
            new_sequences = []
            for k in range(0,len(good_sequences)/2):
                sequences.append(create_F_SEQUENCE()) # random runts
            for k in range(0,len(good_sequences)): # new related sequences
                new_sequence = random.choice(good_sequences)
                mutation_no = random.randint(0,12)
                new_sequence[mutation_no] = random.choice(good_sequences)[mutation_no]
                new_sequences.append(new_sequence)
            sequences=good_sequences+new_sequences
        else:
            print("our winner:")
            print(sequences)
            print(run_tactic(tactic_F,sequences[0]))
            break
def tactic_G(number,top_row,bottom_row,slot_pointers):
    pref = slot_pointers[number]
    return pref
def strategy_G():
    bar = MINIMUM_SCORE
    print("I have set initial bar to "+str(bar))
    def create_G_SEQUENCE():
        slot_pointers = []
        for j in range(0,14):
            slot_pointers.append(random.randint(0,3))
        return slot_pointers
    sequences = []
    # init the sequences
    for i in range(0,INITIAL_SEQUENCES):
        sequences.append(create_G_SEQUENCE())
    # start running then SEQUENCEing
    max = 0
    best_SEQUENCE = []
    for h in range(0,12):
#       bar+=1
        good_sequences = []
        print(str(h)+") sequences="+str(len(sequences))+" bar="+str(bar))
        for SEQUENCE in sequences:
            result = run_tactic(tactic_G,SEQUENCE)
            if result>bar:
                good_sequences.append(SEQUENCE)
                #print("a good SEQUENCE: "+str(result))
                if result>=max:
                    print("new best SEQUENCE: "+str(result))
                    max = result
                    best_SEQUENCE = SEQUENCE
                    bar=int(max-TOLERANCE)
        if len(good_sequences)>1:
            new_sequences = []
            for k in range(0,len(good_sequences)/2):
                sequences.append(create_G_SEQUENCE()) # random runts
            for k in range(0,len(good_sequences)): # new sequences based on 
                new_sequence = random.choice(good_sequences)
                mutation_no = random.randint(0,12)
                new_sequence[mutation_no] = random.choice(good_sequences)[mutation_no]
                # i.e. one different from parent SEQUENCE
                new_sequences.append(new_sequence)
            sequences=good_sequences+new_sequences
        else:
            print("our winner:")
            groups = [[],[],[],[]]
            counter = 0;
            for item in best_SEQUENCE:
                if counter==0:
                    groups[item].append('A')
                elif counter==10:
                    groups[item].append('J')
                elif counter==10:
                    groups[item].append('Q')
                elif counter==10:
                    groups[item].append('K')
                else:
                    groups[item].append(str(counter))
                counter+=1
            print(groups)
            print(run_tactic(tactic_G,sequences[0]))
            break

                
def tactic_H(number,top_row,bottom_row,nn):
    # 9 inputs > nn > 4 outputs
    inputs = [number]
    outputs = [0.5,0.5,0.5,0.5]
    for col in bottom_row:
        if len(col):
            inputs.append(1.0/col[-1])
        else:
            inputs.append(0.01)
    for col in top_row:
        inputs.append(col)
    index = 0
    for input in inputs:
        for j in range(0,4):
            outputs[j]*=((input/13.0)*nn[index])
            index += 1
    h_output = 0
    h_output_val = 0.0
    index = 0
    for output in outputs:
        if output>h_output_val:
            h_output = index
            h_output_val = output
        index+=1
    return h_output #max(outputs)
def create_H_SEQUENCE():
    neuron_map=[]
    for i in range(0,36):
        neuron_map.append(random.uniform(0.01,0.99))
    return neuron_map
def strategy_H():
    bar = MINIMUM_SCORE
    sequences = []

    # init the sequences
    for i in range(0,INITIAL_SEQUENCES):
        sequences.append(create_H_SEQUENCE())

    # start running then SEQUENCEing
    max = 0
    best_SEQUENCE = []
    for h in range(0,MAX_ROUNDS):
        good_sequences = []
        print(str(h)+") sequences="+str(len(sequences))+" bar="+str(bar))
        for SEQUENCE in sequences:
            result = run_tactic(tactic_H,SEQUENCE)
            if result>bar:
                good_sequences.append(SEQUENCE)
                if result>=max:
                    print("new best SEQUENCE: "+str(result))
                    max = result
                    best_SEQUENCE = SEQUENCE
                    bar=int(max-TOLERANCE)
        if len(good_sequences)>1:
            new_sequences = []
            for i in range(0,RUNTS_PER_ROUND):
                new_sequences.append(create_H_SEQUENCE())
            for i in range(0,len(good_sequences)):
                new_sequence = random.choice(good_sequences)
                for j in range(0,MUTATIONS_PER_CHILD):
                    neuron_no = random.randint(0,35)
                    new_sequence[neuron_no] = random.choice(good_sequences)[neuron_no]
                new_sequences.append(new_sequence)
            sequences=good_sequences+new_sequences
        else:
            break
    print("our winner:")
    print(best_SEQUENCE)

def run_tactic(callback,variables):
    results = []
    for h in range(1,GAMES_PER_SEQUENCE_TEST):
        top_row = [1,2,3,4]
        bottom_row = [[],[],[],[]] # would tuples be better ? no

        one_suit = range(1,14)
        deck = one_suit + one_suit + one_suit + one_suit

        random.shuffle(deck)

        def play_turn():
            # check bottom sets for matches
            for j in range(1,5):
                if top_row[j-1] is not 13:
                    for k in bottom_row:
                        if len(k) and k[-1]==top_row[j-1]+j:
                            top_row[j-1] = k.pop()
                            return True

            if len(deck):
                # else check top card for matches
                for j in range(1,5):
                    if top_row[j-1] is not 13 and len(deck) and deck[-1]==top_row[j-1]+j:
                        top_row[j-1] = deck.pop()
                        return True

                # else put top card on a prefferred pile
                bottom_row[callback(deck[-1],top_row,bottom_row,variables)].append(deck.pop())
                return True
            return False

        for i in range(1,96):
            if not play_turn():
                break

        results.append(
            52-(len(bottom_row[0])+len(bottom_row[1])+len(bottom_row[2])+len(bottom_row[3])))
    average = (sum(results)/float(len(results)))
    #print(average)
    return average

"""
