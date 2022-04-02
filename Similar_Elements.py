'''
Input for this code block is 'binary_similarities_with_sg.json'
Output for this code block is a dictionary named 'elemental_similarities'
'''

'''
The elemental similarity matrix builder
'''
import json
import time

similarities = json.load(open('binary_similarities_with_sg.json','r')) # read in the data
# short_list = json.load(open('short_list_similarities.json', 'r'))

elemental_similarities = {} # initialize an empty elemental similarity matrix


tic = time.perf_counter() # start the timer

'''
A function that takes any compound and returns them both as a list of two element strings
'''
def elements(comp): # takes in one compound string
    both = [] 
    if comp[1].isupper(): # if the second letter is upper case
        both.append(comp[0]) # we know the first element is one letter
        both.append(comp[1:]) # and the second element just goes from letter 2 to the end 
    else: # if the second letter is lower case
        both.append(comp[:2]) # we know first element is two letters
        both.append(comp[2:]) # and the second element just goes from letter 3 to the end
    return both # send it

'''
This function takes two different compounds and checks if they share a common element
* side note * if they dont share a common element it returns an empty list
* side note 2 * the compound objects getting passed in have to be from the elements function output
'''
def compare(first,second): # foil it out...basically (a1,a2) vs (b1,b2) 
    similar = [] 
    if first[0] == second[0]: # first
        similar.append(first[1])
        similar.append(second[1])
        similar.append(first[0]) 
    elif first[0] == second[1]: # outer
        similar.append(first[1])
        similar.append(second[0])
        similar.append(first[0])
    elif first[1] == second[0]: # inner
        similar.append(first[0])
        similar.append(second[1])
        similar.append(first[1])
    elif first[1] == second[1]: # last
        similar.append(first[0])
        similar.append(second[0])
        similar.append(first[1])
    return similar # the first and second are the similar elements, the third is the common element

'''
The Driver Loop
This loops through the binary similarity list and adds entries to the empty elementary similarity matrix 
It uses the elements function and the compare function
'''
for k,v in similarities.items(): # the binary similarities file
    key_comp = elements(k) # a top level compound in the binary list {key_comp: {val_comp1:number1, val_comp2:number2, etc...}}
    for key,value in v.items(): 
        if value > 0: 
            val_comp = elements(key)
            coords = compare(key_comp,val_comp) # 3 item list containing [e1, e2, e3] where e1 is similar to e2 and e3 is the common element
            if len(coords) > 0: #if there was a similarity
                sim = coords.pop(2) # take out the common element
                coords = str(coords) # these are the similar elements
                sdrooc = coords[::-1] # these are the similar elements listed in reverse order
                if coords in elemental_similarities.keys(): 
                    elemental_similarities[coords][sim] = value # HERE is where the values getting listed twice is avoided because identical data is overwritten
                elif sdrooc in elemental_similarities.keys(): 
                    elemental_similarities[sdrooc][sim] = value # Same thing here, the reason is because IF the entry already exists it gets overwritten with the exact same key and value
                else: elemental_similarities[coords] = {sim:value} # if the element pair isn't already in the similarity matrix then make a new entry
                    

toc = time.perf_counter() - tic # stop the timer

print('similarities in ', toc,' seconds') 

# write to json file
tic = time.perf_counter()
json.dump(elemental_similarities, open('elemental_similarities.json', 'w'))
toc = time.perf_counter() - tic

# print('Still need to fix export to json : \n broken bc the keys in the dict cant be tuples \n Exported to json in ', toc, ' seconds')


'''
Exploration Snippets
Uncomment and run to view, recomment to disable
'''

'''
This one prints out the entire elemental similarity matrix string
'''
# for k,v in elemental_similarities.items():
#     print(k,v)
#     print('\n')

'''
This one prints out all the similarity entries for one element
'''
# elem = "Al" #Enter any element you want here
# for k,v in binary_data.items():
#     if elem in k:
#         print(k,v)
#         print('\n')

'''
This prints all the similarity ratings for any two specific elements
'''
# e1 = 'Hg'
# e2 = 'Ac'
# for k,v in similarities.items():
#     if e1 in k and e2 in k:
#         print(k,v)
#         print('\n')AttributeError

'''used for selectively looking at specific similarity ratings'''
# i=0
# for k,v in elemental_similarities.items():
#     for key,value in v.items():
#         if value > 1.2 and value < 1.4 : # and value > 0 :
#             i+=1
#             print(k,v,'\n'*2)
# print(i)
i = 0 # oh this little guy? I wouldnt worry about this little guy
