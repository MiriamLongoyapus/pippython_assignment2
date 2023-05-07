#1. Write a Python program to get a single string from two given strings
#, separated by a space, and swap the first two characters of each string
def separate(string1,string2):
    text1=string2[:3] + string1[3:]
    text2=string1[3:] + string2[:3]
    return text1+" "+text2
print(separate("kotlin","python"))


#2.  Write a Python function that takes a list of words and returns the 
#longest word and the length of the longest one
def list_word(word):
    count=0
    for i in word:
        if len(i)>=count:
            count=len(i)
            return count
print(list_word(["JavaScript","Python"]))

#3. Write a Python program that accepts a comma-separated sequence of words
# as input and prints the distinct words in sorted form (alphanumerically).
def sort_words(word):
    word=word.split(",")
    
#4.. Write a Python function that takes two lists and returns True if they
# have at least one common member.
def common(list1,list2):
    # anser=True
    for a in list1:
        for b in list2:
            if a==b:
                anser=True
                return anser
print(common([3,4,8,9],[5,6,8,4]))
#5. Write a Python program to convert a list to a list of dictionaries.
#Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", 
#"#800000", "#FFFF00"]

#6. Write a Python program to check whether all dictionaries in a list are 
#empty or not
dictionary_list=[{},{},{},{}]
print((not a for a in dictionary_list ))

#7. Given a list of numbers, use list comprehension to remove all odd numbers
# from the list:
numbers = [3,5,45,97,32,22,10,19,39,43]
remove_odd=[n for n in numbers if n%2!=0]
print(remove_odd)


#8. Find the common numbers in two lists (without using a tuple or set) 
list_a = 1, 2, 3, 4, 
list_b = 2, 3, 4, 5
common_numbers=[a for a in list_a if a in list_b]
print(common_numbers)

#9. Use a nested list comprehension to find all of the numbers from 1-1000
#  that are divisible by any single digit besides 1 (2-9)
all_numbers=list(range(1,1000))
all__numbers=list(range(2,9))
division = [number for number in range(1,1000) if True in [True for x in range(2,9) if number % x == 0]]
print(division)

#10. Write a Python function to remove all vowels in a string
def remove_vowel(word):
    empty=""
    vowel=["a,e,i,o,u"]
    for i in range (len(word)):
        if word[i] is not vowel:
            empty+=word[i]
            return empty
print(remove_vowel("python"))       
            

