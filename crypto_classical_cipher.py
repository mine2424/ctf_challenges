import sys

all_words = 'abcdefghijklmnopqrstuvwxyz'

crypt_word = sys.argv[1]

ans_word = ''

shift_num = 3

for word in crypt_word:
    if (word == '_' or word == '{' or word == '}'):
        ans_word += word
        continue

    # TODO: 大文字を変換せずに解読したい
    find_idx = all_words.find(word.lower())

    # 3 word shift left
    if (find_idx < shift_num):
        new_idx = len(all_words) - (shift_num - (find_idx))
        print(new_idx)
        ans_word += all_words[new_idx]
    else:
        ans_word += all_words[find_idx - shift_num]

    ''' 3 word shift right
    if (find_idx >= len(all_words)-shift_num):
        new_idx = shift_num - (len(all_words) - find_idx)
        ans_word += all_words[new_idx]
    else:
        ans_word += all_words[find_idx + shift_num]
    '''

print(ans_word)
