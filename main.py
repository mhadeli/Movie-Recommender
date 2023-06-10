from Movies import movies, titles
from Linked_List import Node, LinkedList
import random

bluebox_movies = LinkedList(movies[0][0])

def welcome():
    print("Hello There!\n Welcome to BlueBox, your one stop shop for the best films.\n Enjoy!")

welcome()

print("Please enter a search term to get a list of recommended movies.")
x = input("--> ")
while type(x) is not str:
    print("Please enter either numerical or alphabetical values in to the search engine...")
    x = input("--> ")
print("Searching for " + x + "...")

search_results = []
def linear_search(search_list, search_item):
    for item in search_list:
        if search_item.lower() == item.lower():
            search_results.append(search_list[0])
            return print(search_results)

pattern_search_results = []
def pattern_search(search_list, search_item):
    for idx in range(len(search_list)):
        match_count = 0
        for char in range(len(search_item)):
            if search_item[char] == search_list[idx + char]:
                match_count += 1
        if match_count == len(search_item):
            pattern_search_results.append(search_list[0])
            print(pattern_search_results)
        else:
            break


#Function below creates a Linked List for each movie and will iterate through each node in the list.

for elem in movies:
    movie = LinkedList()
    movie.head_node = Node(elem[0])
    for idx in range(len(elem)):
        movie.head_node.set_next_node(elem[idx])
        current_node = movie.head_node.get_next_node()
    y = linear_search(elem, x)


if not search_results:
    z = input("The search term you entered yielded no results. \nWould you like to broaden your search? \nPlease enter either Y (for yes) or N (for no): ")
    if z.lower() == "Y".lower():
        for elem in movies:
            movie = LinkedList()
            movie.head_node = Node(elem[0])
            for idx in range(len(elem)):
                movie.head_node.set_next_node(elem[idx])
                current_node = movie.head_node.get_next_node()
            a = pattern_search(elem, x)
    while z.lower() != "Y".lower() and z.lower() != "N".lower():
        print("Invalid input. Let's try this again.")
        z = input("The search term you entered yielded no results. \nWould you like to broaden your search? \nPlease enter either Y (for yes) or N (for no): ")
    #elif z.lower() == "N".lower():
        #print("\n")

    if not pattern_search_results:
        for elem in titles:
            if x.lower() == elem[0].lower():
                search_results.append(elem)
        if search_results:
            print("Looks like we might have a title (or a few) that might interest you... ")
            for item in search_results:
                print(item)

if not search_results:
    print("There are no results for your search. However, may we recommend the following title? ")
    print(random.choice(titles))

print("\nThank you for using BlueBox!!! Feel free to re-run the program and we will find some more great classics for you :)")





