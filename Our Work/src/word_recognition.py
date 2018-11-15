from image_preprocess import split_sentence, disp_image
import tensorflow as tf
import os,sys
from shutil import copyfile
import subprocess

def get_recognized_words_list(sentence_path ) :
    recognized_words_list = list()
    words_image_list = split_sentence(sentence_path)

    for each_word_image in words_image_list :
        copyfile(each_word_image, "../data/test.png")
        result = subprocess.run(['python3', 'main.py',"--wordbeamsearch"], stdout=subprocess.PIPE).stdout.decode('utf-8')
        result = result.strip()
        recognized_word = str()

        for each_char_index in range(len(result)-2 , 0 , -1) :
            if result[each_char_index] == '"' :
                recognized_word = recognized_word[::-1]
                recognized_words_list.append(recognized_word)
                break
            else :
                recognized_word += result[each_char_index]

    #os.system("rm w*.png")
    return recognized_words_list


if __name__ == "__main__" :
    print(get_recognized_words_list('test5.png'))
