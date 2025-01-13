This project finds the columns to delete for achieving k-anonimity (for some k). 
Steps to reach k-anonymity are defined in main.py. Every step must be executed on its own.
By changing a value for the do-variable set in main.py. Somewhere a column deletion priority needs to be set, by the user.

For every step files are generated, opened, solved. Step 7 is responsible for the generation of the csv-files, possibly 
hiding columns, if necessary for reaching k-anonymity. 

The project starts from a csv-file, and ends with a csv-file possibly having hidden columns.
To this end, clingo (answer set programming) is being used. 


In principle, it should be usable with any csv-file having column names
, even though column names should at least have no spacing in between words. I haven't really

This project was created to complete an assignment at the Open University Nederland.