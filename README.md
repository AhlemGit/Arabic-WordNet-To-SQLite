# Arabic-WordNet-To-SQLite
This repository is about how to build an SQLite version of the Arabic WordNet database available in the package "AWNBrowser_2.0.1" downloadable here: https://sourceforge.net/projects/awnbrowser/

This is done following these steps:
* First, identify the folder AWNBrowser_2.0.1\AWN\wordnet which contains .dat files (They are in the format of a Derby database).
* Second, install the RazorSQL tool and follow the steps explained in the screeshots provided in the folder "Extracting CSV files" of this repository, to extract the database tables in CSV format.
* Finally, install the DB Browser for SQLite tool and use it to build the SQLite database version, as explained in screeshots found in "Building the SQLite version" folder.

The SQLite version of the AWN database that we provide is available here: 
https://drive.google.com/open?id=1naidKW2b8_9cS-DkmCJg4AA1OedlB7wc

We made some changes from the intial database as we added 2 tables: "WORDEXTENDED" and "FORMEXTENDED", which are copies of "WORD" and "FORM" intial tables respectively, with an additional column providing the unvocalized form of words. This is done in order to be able to perform sql queries using unvocalized words.  
