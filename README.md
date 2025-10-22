# Valkyrie-database
A fun project that i will create to understand object oriented programming and further refine other concepts of coding by using data from my favourite game  'Honkai impact 3rd'.

This is a work-in-progress and may see changes along the way of me learning OOPs(object oriented programming) and various other libraries.

# About the project
* The program features a database of the valkyries from the game 'Honkai Impact 3rd' and for now belonging to the organisation called as Schikshal.The moment one runs the code a main menu will appear in the terminal which will give us 4 options:
1. adding a new valkyrie profile
2. view the entire database
3. view a specific valkyrie 
4. exit
* The user can fill the inputs as instructed and after pressing enter it gets stored inside a csv file so that option 2 and 3 can be used.The input for the first function are defined by the class Schikshal. 
The functions 'save' and 'load' are handling the saving and loading the data from the file. while the __str__ is used to make the data into string for easy processings.

# Libraries and skills used
* csv: The one handling the data 
* pandas: For structured display of the valkyries for option 2
* OOPs was used to organise the data.

# Existing problems
* Since its still a work in progress it has a few logical errors such as when one press option 2 the data is not following the dataFrame logic and instead showing it like a list. This will take sometime to fix 
* I also have to further refine my understanding of the ' load ' and ' save ' functions which I think is one of the potential cause.
* I feel like there is a need for more error handling in the code. Finding more loopholes and brainstorming more possibilities is important.
* My OOPs logic is barely at the beginner level, needs more work.

# Future Scope
* The data will be increased significantly and more factions will be added.To handle more factions I would need to create a login function so that one can login to see characters of different factions as well.
* Usage of API: I wish to use API skill and web scraping for; Suppose someone wants to know about a specific character, I can use APIs and web scraping to get a piece of their story from wikis that the community created.However if i cannot find any existing API keys then this idea might get scraped. 
* The program,once ready will be converted into a GUI based program instead of the current terminal based.