import random
#Itt adjuk meg a szavak listáját
word_list = ["hal","majom","banán"]

#random szám generálás, a lista hosszánál 1-el kevesebbnek kell lennie a tartomány végének, mert a lista elemeit 0-tól számoljuk, míg a len(listanév) funkció 1-től számol
rand_num = random.randint(0,len(word_list)-1)
#itt kerül kiválasztásra a random szó a listából
word = word_list[rand_num]
#listára bontja a kiválasztott szó karaktereit, pl: ['h','a','l']
game_word_list = list(word)

print(word)

#ez a lista az általunk eltalált betűket fogja tartalmazni
guess_word = []

# itt jön létre a találgatós lista, ez így néz ki a halas példánál maradva: ['_','_','_'] és ide kerül majd be később a találatunk így (de nem most): ['_','a','_'] 
#while (feltétel): Azt jelenti, hogy a while-on belüli parancsok annyiszor lefutnak, amíg a feltétel igaz. Ha nem iktatnánk be a+=1-et, akkor végtelen ciklus lenne, soha nem állna le
a = 0
while a<len(word):
    guess_word.append("_")
    a+=1
print(guess_word)

# Itt kéri be a karaktert a felhasználótól egész addig, amíg ki nem találta a szót
while game_word_list != guess_word:
    guess = input("Adj meg egy betűt: ").lower()
    b=0
    for letter in word:
        if letter == guess:
            #print("Talált")
            guess_word[b] = guess # itt cserélődik le '_' a kitalált karakterre a kitalálós listában
            b+=1
        else:
            #print("Nem talált!")
            b+=1
    print(guess_word)
else:
    print("Nyertél!")
