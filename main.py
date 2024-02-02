import enchant


def morse_finder(sen, char="", morse=""):
    global temp, word
    temp += morse
    word += char
    if temp == sen[:len(temp)] and len(temp) == len(sen):
        answer_list.append(word)
        edit_temp_word(char, morse)
        return
    elif temp != sen[:len(temp)]:
        edit_temp_word(char, morse)
        return
    elif "tt" in word or "ee" in word:
        edit_temp_word(char, morse)
        return
    for letter in eng_car:
        morse_finder(sen, letter, eng_car[letter])
    edit_temp_word(char, morse)


def edit_temp_word(char, morse):
    global temp, word
    temp = temp[:(len(temp) - len(morse))]
    word = word[:(len(word) - len(char))]


eng_car = {
    "a": "01",
    "b": "1000",
    "c": "1010",
    "d": "100",
    "e": "0",
    "f": "0010",
    "g": "110",
    "h": "0000",
    "i": "00",
    "j": "0111",
    "k": "101",
    "l": "0100",
    "m": "11",
    "n": "10",
    "o": "111",
    "p": "0110",
    "q": "1101",
    "r": "010",
    "s": "000",
    "t": "1",
    "u": "001",
    "v": "0001",
    "w": "011",
    "x": "1001",
    "y": "1011",
    "z": "1100"}

answer_list = []
temp = ""
word = ""

dic = enchant.Dict("en_US")
sentence = []
final_list = []
ex = "0000001000100111 0111110100100100 00 0111 01100101111100100111110010"
ex = ex.split(" ")
for i in ex:
    morse_finder(i)

    for j in answer_list:
        if dic.check(j):
            final_list.append(j)

    sentence.append(final_list)
    final_list = []
    answer_list = []

print("*"*30)
for i in sentence:
    print(i)
