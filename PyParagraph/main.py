import csv
import re


with open('paragraph_2.txt', 'r') as file:
    data = file.read()
   
    sentences = re.split("(?<=[.!?])\s+", data)
    words = data.split()
    word_count = len(words)
    sentence_count = len(sentences)
    average_letter_count = sum(len(word) for word in words) / len(words)
    average_sentence_length = word_count/sentence_count



print("Paragraph Analysis")
print("--------------------")

print("Approximate Word Count: " + str(word_count))
print("Approximate Sentence Count: " + str(sentence_count))
print("Average Letter Count: " + str(round(average_letter_count, 2)))
print("Average Sentence Length: " + str(round(average_sentence_length,2)))
print("\n")


with open("Paragraph_results_2.txt", 'w') as text_file:
    text_file.write("Paragraph Analysis\n")
    text_file.write("_________________\n")
    text_file.write("Approximate Word Count: " + str(word_count) + "\n")
    text_file.write("Approximate Sentence Count: " + str(sentence_count) + "\n")
    text_file.write("Average Letter Count: " + str(round(average_letter_count, 2)) + "\n")
    text_file.write("Average Sentence Length: " + str(round(average_sentence_length, 2)) + "\n")
    