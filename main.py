# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(file_open):
    file_open = open("./story.txt", "r")
    read_file = str(file_open.read())
    return(read_file)

print("The main story is as follows: \n")   
print(read_file_content(file_open = "./story.txt"))
print()

def count_words(file_open2):
    file_open2 = read_file_content("./story.txt")
    read_file_split = file_open2.split()
    count ={}
    for i in read_file_split:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count

print("While the words count in the story is as follows: \n")
print(count_words(file_open2 = "./story.txt"))



    