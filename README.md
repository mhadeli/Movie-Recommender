# Recommender
# Movie Recommender
## BlueBox Movie Recommendation System
# Overview
BlueBox is a text-based movie recommendation system. It aims to provide users with a list of recommended movies based on their search. It uses a LinkedList data structure for storing movies and provides search functionalities for retrieving movie recommendations.

# Features
Welcome function: It provides a warm welcome to the user when they run the program.

**Search:** Users can input a search term to find related movies. If there's no direct match, the program will suggest broadening the search.

**Broadening search:** If the exact search term doesn't yield any results, the user can broaden their search to get more results.

**Recommendation:** If no match is found even after broadening the search, the system will recommend a random movie.

# Libraries Used
random: Used to select a random movie for a recommendation if no match is found.
Usage
The user is asked to enter a search term to find related movies. The program will search for the term and return a list of matches if found.
If no match is found, the user will be asked if they want to broaden their search. If they agree, the program will perform a pattern search to find related movies.
The program will recommend a random movie to the user if no match is found.
# Data Structures and Algorithms
- LinkedList: Each movie is stored in a LinkedList. Each node in the LinkedList represents a movie.
- Linear Search: When a search term is entered, the program performs a linear search on LinkedList movies.
- Pattern Search: If no results are found using the linear search, the program can perform a pattern search on the user agreement.
# Modules
Movies: This module contains the list of movies that the recommendation system uses.
Linked_List: This module contains the Node and LinkedList classes used to store movies in the system.
