
This is a simple command-line application for managing a database of Pokemon and trainers. It uses SQLite3 to store the data in a local database file.

Usage
To use the application, simply run the main.py script. The application will prompt you for your name and then display a menu of options:

Add a new Pokemon
Delete an existing Pokemon
Display All Pokemon
Update a Pokemon
Battle a Random Pokemon
Exit
You can select an option by typing its number and pressing enter.

The Add a new Pokemon option allows you to add a new Pokemon to the database. You will be prompted to enter the Pokemon's name, type, moveset, HP, attack, defense, and speed.

The Delete an existing Pokemon option allows you to delete a Pokemon from the database. You will be prompted to enter the ID of the Pokemon you wish to delete.

The Display All Pokemon option displays a list of all the Pokemon in the database.

The Update a Pokemon option allows you to update the details of an existing Pokemon. You will be prompted to enter the ID of the Pokemon you wish to update, as well as its new name, type, moveset, HP, attack, defense, and speed.

The Battle a Random Pokemon option allows you to battle a randomly selected Pokemon from the database.

The Exit option exits the application.

Dependencies
This application uses the following dependencies:

SQLite3 (included with Python)
colorama (for colored console output)