# Swrite function according to spec
def find_grades(grades,students):
    """
    grades is a dict mapping student names(str) to grades (str)
    students is a list of student names
    Returns a list containing the grades for students in same order.
    """
    Lnew = []
    for elem in students: #elem student name
        grade = grades[elem] # grades[elem] -> use student name to match dict key 
        Lnew.append(grade) # add to new list
    return Lnew

d = {'Ana': 'B', 'Matt':'C', 'John':'B', 'Katy': 'A'}
print(find_grades(d, ['Matt', 'Katy']))

# Write func following spec
def find_in_L(Ld,k):
    """
    Ld is a list of dicts
    k is an int
    Returns True if k is a key in any dicts of Ld, else False
    """
    for d in Ld: # for dict in list of dict
        if k in d: # look for k in ecah dict in list dict
            return True # found one
    return False # didn't find one

#example
d1 = {1:2, 3:4, 5:6}
d2 = {2:4, 4:6}
d3 = {1:1, 3:9, 4:16, 5:25}

print(find_in_L([d1,d2,d3], 2))
print(find_in_L([d1,d2,d3], 25))

#iterating over tuple of items from blah.items()
for x,y in d1.items():
    print(f"key {x} has value {y}")

# write func following specs
def count_matches(d):
    """
    d is a dict
    Returns how many entries in da have a matching key and value
    """
    matches = 0
    for v,k in d.items():
        if v==k:
            matches += 1
    return matches


d = {1:2, 3:4, 5:6}
print(count_matches(d))
d = {1:2, 'a':'a', 5:5}
print(count_matches(d))




# Long example code
song = "Hey  I was doing just fine before I met you I drink too much and thats an issue but Im okay Hey  you tell your friends it was nice to meet them But I hope I never see them again I know it breaks your heart Moved to the city in a broke down car And four years  no calls Now youre looking pretty in a hotel bar And I cant stop No  I cant stop So baby pull me closer in the backseat of your Rover That I know you cant afford Bite that tattoo on your shoulder Pull the sheets right off the corner Of the mattress that you stole From your roommate back in Boulder We aint ever getting older We aint ever getting older We aint ever getting older You look as good as the day I met you I forget just why I left you  I was insane Stay and play that Blink 182 song That we beat to death in Tucson  okay I know it breaks your heart Moved to the city in a broke down car And four years  no call Now Im looking pretty in a hotel bar And I cant stop No  I cant stop So baby pull me closer in the backseat of your Rover That I know you cant afford Bite that tattoo on your shoulder Pull the sheets right off the corner Of the mattress that you stole From your roommate back in Boulder We aint ever getting older We aint ever getting older We aint ever getting older So baby pull me closer in the backseat of your Rover That I know you cant afford Bite that tattoo on your shoulder Pull the sheets right off the corner Of the mattress that you stole From your roommate back in Boulder We aint ever getting older We aint ever getting older we aint ever getting older We aint ever getting older we aint ever getting older We aint ever getting older we aint ever getting older We aint ever getting older We aint ever getting older No we aint ever getting older"

def generate_word_dict(song):
    """ song is a string
    Returns a dictionary whose:
    * keys are song words
    * values are the frequency of each key in song
    """
    # remove special characters and convert to lowercase
    song_words = song.lower()
    words_list = song_words.split()
    word_dict = {}
    for w in words_list:
        if w in word_dict:
            # seen word again, so add one to frequency
            word_dict[w] += 1
        else:
            # first time seeing word, insert a dict entry with freq 1
            word_dict[w] = 1
    # return is a dict mapping str:int like {'word1':1, 'word2':3}
    return word_dict

word_dict = generate_word_dict(song)
# print(word_dict)
     
def find_frequent_word(word_dict):
    """ word_dict is a frequency dict mapping string:int
    Using word_dict, returns a tuple of 
    (list of keys in word_dict with the max freq, max freq)
    """
    # a list in case there is more than one word occuring that often
    words = []
    highest = max(word_dict.values())  # this is an int
    # loop to find words occurring with `highest` freq
    for k,v in word_dict.items():
        # k is a word and v is its frequency
        if v == highest:
            # word in dict has a value that matches `highest` so append it
            words.append(k)
    # return looks like (['word1', 'word2'], 4)
    return (words, highest)
    
most_freq = find_frequent_word(word_dict)
# print(most_freq)


def occurs_often(word_dict, x):
    """ word_dict is a frquency dict
        x is an int
    Side effect warning, this function mutates word_dict here modifies word_dict.

    Returns the list of tuples in order of highest freq to lowest freq > x. 
    Each tuple is (list of keys in word_dict with some freq, some freq)
    """
    freq_list = []
    word_freq_tuple = find_frequent_word(word_dict)
    # repeat for the frequencies greater than 'x'
    while word_freq_tuple[1] > x:
        # extract most frequent word(s) using function we wrote
        word_freq_tuple = find_frequent_word(word_dict)
        # keep track of most common words, append them in order
        freq_list.append(word_freq_tuple)
        # remove every entry that matches words in `word_freq_tuple`
        # so that you are left with next most frequent words
        for word in word_freq_tuple[0]:
            del(word_dict[word])
    return freq_list

# print(occurs_often(word_dict, 2))

# pick a song by uncommenting your favorite
#song = "I threw a wish in the well Dont ask me Ill never tell I looked to you as it fell And now youre in my way  Id trade my soul for a wish Pennies and dimes for a kiss I wasnt looking for this But now youre in my way  Your stare was holdin Ripped jeans skin was showin Hot night wind was blowin Where do you think youre going baby  Hey I just met you And this is crazy But heres my number So call me maybe  Its hard to look right At you baby But heres my number So call me maybe  Hey I just met you And this is crazy But heres my number So call me maybe  And all the other boys Try to chase me But heres my number So call me maybe  You took your time with the call I took no time with the fall You gave me nothing at all But still youre in my way  I beg and borrow and steal Have foresight and its real I didnt know I would feel it But its in my way  Your stare was holdin Ripped jeans skin was showin Hot night wind was blowin Where you think youre going baby  Hey I just met you And this is crazy But heres my number So call me maybe  Its hard to look right At you baby But heres my number So call me maybe  Hey I just met you And this is crazy But heres my number So call me maybe  And all the other boys Try to chase me But heres my number So call me maybe  Before you came into my life I missed you so bad I missed you so bad I missed you so so bad  Before you came into my life I missed you so bad And you should know that I missed you so so bad bad bad  Its hard to look right At you baby But heres my number So call me maybe  Hey I just met you And this is crazy But heres my number So call me maybe  And all the other boys Try to chase me But heres my number So call me maybe  Before you came into my life I missed you so bad I missed you so bad I missed you so so bad  Before you came into my life I missed you so bad And you should know that  So call me maybe"
#song = "Because you know Im all about that bass  Bout that bass no treble Im all about that bass Bout that bass no treble Im all about that bass Bout that bass no treble Im all about that bass Bout that bass bass bass bass  Yeah its pretty clear I aint no size two But I can shake it shake it like Im supposed to do Cause I got that boom boom that all the boys chase And all the right junk in all the right places I see the magazine workin that Photoshop We know that stuff aint real come on now make it stop If you got beauty beauty just raise em up Cause every inch of you is perfect from the bottom to the top Yeah my mama she told me dont worry about your size Shoo wop wop shaooh wop wop She says Boys like a little more booty to hold at night That booty uh that booty booty You know I wont be no stick figure silicone Barbie doll So if that what youre into then go head and move along Because you know Im all about that bass Bout that bass no treble Im all about that bass Bout that bass no treble Im all about that bass Bout that bass no treble Im all about that bass Bout that bass Hey Im bringing booty back Go head and tell them skinny girls that No Im just playing I know you think youre fat But Im here to tell you Every inch of you is perfect from the bottom to the top Yeah my mama she told me dont worry about your size Shoo wop wop shaooh wop wop She says Boys like a little more booty to hold at night That booty booty uh that booty booty You know I wont be no stick figure silicone Barbie doll So if thats what youre into then go head and move along Because you know Im all about that bass Bout that bass no treble Im all about that bass Bout that bass no treble Im all about that bass Bout that bass no treble Im all about that bass Bout that bass You know Im all about that bass Bout that bass no treble I said Im all about that bass Bout that bass no treble Im all about that bass Bout that bass no treble Im all about that bass Bout that bass Because you know Im all about that bass Bout that bass no treble Im all about that bass Bout that bass no treble Im all about that bass Bout that bass no treble Im all about that bass Bout that bass Hey Im all about that bass Bout that bass Hey Im all about that bass Bout that bass Hey Yeah yeah ohh You know you like this bass Hey "
#song = "It might seem crazy what Im about to say Sunshine shes here you can take a break Im a hot air balloon that could go to space With the air like I dont care baby by the way  Uh  Because Im happy Clap along if you feel like a room without a roof Because Im happy Clap along if you feel like happiness is the truth Because Im happy Clap along if you know what happiness is to you Because Im happy Clap along if you feel like thats what you wanna do  Here come bad news talking this and that yeah Well give me all you got and dont hold it back yeah Well I should probably warn you Ill be just fine yeah No offense to you dont waste your time Heres why  Because Im happy Clap along if you feel like a room without a roof Because Im happy Clap along if you feel like happiness is the truth Because Im happy Clap along if you know what happiness is to you Because Im happy Clap along if you feel like thats what you wanna do  Hey Go Uh  Happy Bring me down Cant nothing Bring me down My levels too high Bring me down Cant nothing Bring me down I said let me tell you now Bring me down Cant nothing Bring me down My levels too high Bring me down Cant nothing Bring me down I said  Because Im happy Clap along if you feel like a room without a roof Because Im happy Clap along if you feel like happiness is the truth Because Im happy Clap along if you know what happiness is to you Because Im happy Clap along if you feel like thats what you wanna do  Because Im happy Clap along if you feel like a room without a roof Because Im happy Clap along if you feel like happiness is the truth Because Im happy Clap along if you know what happiness is to you Because Im happy Clap along if you feel like thats what you wanna do  Hey Go Uh  Happy repeats Bring me down cant nothing Bring me down my levels too high Bring me down cant nothing Bring me down I said let me tell you now  Because Im happy Clap along if you feel like a room without a roof Because Im happy Clap along if you feel like happiness is the truth Because Im happy Clap along if you know what happiness is to you Because Im happy Clap along if you feel like thats what you wanna do   Because Im happy Clap along if you feel like a room without a roof Because Im happy Clap along if you feel like happiness is the truth Because Im happy Clap along if you know what happiness is to you Because Im happy Clap along if you feel like thats what you wanna do  Hey Cmon"
#song = "Oh  oh oh Oh  Yeah  Im gonna take my horse to the old town road Im gonna ride til I cant no more Im gonna take my horse to the old town road Im gonna ride til I cant no more Kio  Kio   I got the horses in the back Horse tack is attached Hat is matte black Got the boots thats black to match Ridin on a horse  ha You can whip your Porsche I been in the valley You aint been up off that porch  now  Cant nobody tell me nothin You cant tell me nothin Cant nobody tell me nothin You cant tell me nothin  Ridin on a tractor Lean all in my bladder Cheated on my baby You can go and ask her My life is a movie Bull ridin and boobies Cowboy hat from Gucci Wrangler on my booty  Cant nobody tell me nothin You cant tell me nothin Cant nobody tell me nothin You cant tell me nothin  Yeah  Im gonna take my horse to the old town road Im gonna ride til I cant no more Im gonna take my horse to the old town road Im gonna ride til I cant no more   Hat down  cross town  livin like a rock star Spent a lot of money on my brand new guitar Babys got a habit diamond rings and Fendi sports bras Ridin down Rodeo in my Maserati sports car Got no stress  Ive been through all that Im like a Marlboro Man so I kick on back Wish I could roll on back to that old town road I wanna ride til I cant no more   Yeah  Im gonna take my horse to the old town road Im gonna ride til I cant no more Im gonna take my horse to the old town road Im gonna ride til I cant no more"
song = "Hey  I was doing just fine before I met you I drink too much and thats an issue but Im okay Hey  you tell your friends it was nice to meet them But I hope I never see them again I know it breaks your heart Moved to the city in a broke down car And four years  no calls Now youre looking pretty in a hotel bar And I cant stop No  I cant stop So baby pull me closer in the backseat of your Rover That I know you cant afford Bite that tattoo on your shoulder Pull the sheets right off the corner Of the mattress that you stole From your roommate back in Boulder We aint ever getting older We aint ever getting older We aint ever getting older You look as good as the day I met you I forget just why I left you  I was insane Stay and play that Blink 182 song That we beat to death in Tucson  okay I know it breaks your heart Moved to the city in a broke down car And four years  no call Now Im looking pretty in a hotel bar And I cant stop No  I cant stop So baby pull me closer in the backseat of your Rover That I know you cant afford Bite that tattoo on your shoulder Pull the sheets right off the corner Of the mattress that you stole From your roommate back in Boulder We aint ever getting older We aint ever getting older We aint ever getting older So baby pull me closer in the backseat of your Rover That I know you cant afford Bite that tattoo on your shoulder Pull the sheets right off the corner Of the mattress that you stole From your roommate back in Boulder We aint ever getting older We aint ever getting older we aint ever getting older We aint ever getting older we aint ever getting older We aint ever getting older we aint ever getting older We aint ever getting older We aint ever getting older No we aint ever getting older"

song_dict = generate_word_dict(song)
print("***** WORDS IN SONG *****")
song_words = song.lower()
print(song_words.split())

print("***** WORD FREQUENCIES *****")
print(song_dict)

print("***** MOST COMMON WORD *****")
print(find_frequent_word(song_dict))

print("***** TOP MOST COMMON WORDS *****")
print(occurs_often(song_dict, 6))