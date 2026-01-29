word =input("Enter your word")
word_length= len(word)
numbers = []
for i in range (1,word_length +1):
      num = int(input(f"enter your number {i}:"))
      numbers.append(num)

print(numbers)


print(f"your word length is {(word_length)}")

avg= sum(numbers) / len(numbers)
print(f"The average of the number is{avg}")

if word_length >avg:
      print(f"The length of the word{word} is greater than average")

elif word_length <avg:
      print("The length of the word{word} is less than the average")

else:
      print("What you typed in is probably an error try again")
