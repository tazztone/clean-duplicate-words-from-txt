# clean-duplicate-words-from-txt
This Python script cleans duplicate words from all the .txt files in the same directory as the script itself.

created with chatgpt 3.5
This Python script processes all the .txt files in the same directory as the script itself. It does the following:

    Uses the os module to determine the directory where the script is located (or the current working directory if it's running in an interactive environment).
    Defines a function called clean_text_file that takes an input text file path and an output text file path as arguments.
    Inside the clean_text_file function, it uses an OrderedDict to keep track of unique words in the text file.
    It reads the content of the input file, uses a regular expression (r'\b\w+\b') to split the content into words while preserving punctuation.
    Converts each word to lowercase to ensure that words with different capitalization are treated as the same word.
    Adds each unique word to the OrderedDict.
    Writes the unique words back to the output file while preserving their order.

The script then iterates through all the files in the directory where the script is located and checks if they have a .txt extension. For each .txt file found, it calls the clean_text_file function to clean the file and save the cleaned version with a "cleaned_" prefix in the same directory. Finally, it prints a message indicating that the text has been cleaned and saved to the corresponding output file.
