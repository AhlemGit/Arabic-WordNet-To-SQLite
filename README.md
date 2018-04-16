# Arabic-WordNet-To-SQLite
This repository is about how to build an SQLite version of the Arabic WordNet database available in the package "AWNBrowser_2.0.1" downloadable here: https://sourceforge.net/projects/awnbrowser/

This is done following these steps:
* First, identify the folder AWNBrowser_2.0.1\AWN\wordnet which contains .dat files (This folder represents the database in the Derby format).
* Second, install the RazorSQL tool and follow the steps explained in the screeshots provided in the folder "Extracting CSV files" of this repository, to extract the database tables in CSV format.
* Finally, install the DB Browser for SQLite tool and use it to build the SQLite database version, as explained in screeshots found in "Building the SQLite version" folder.

The extracted CSV files are available to download here: 
https://drive.google.com/open?id=1gQmjsSkn4SqZAMtWH7VmRJBTYfyP087N

The SQLite version of the AWN database that we provide is available here: 
https://drive.google.com/open?id=1naidKW2b8_9cS-DkmCJg4AA1OedlB7wc

We made some changes from the intial database as we added 2 tables: "WORDEXTENDED" and "FORMEXTENDED", which are copies of "WORD" and "FORM" intial tables respectively, with an additional column providing the unvocalized form of words. This is done in order to be able to perform sql queries using unvocalized words. 

We used this version in the following work:  
> Ameur, M. S. H., Khadir, A. C., & Guessoum, A. (2017, October). An Automatic Approach for WordNet Enrichment Applied to Arabic WordNet. In International Conference on Arabic Language Processing (pp. 3-18). Springer, Cham.

This repository also includes a source code providing some functions to query the AWN SQLite database about hypernyms and hyponyms. The program could be found in "Access functions" folder.

# Copyright

Princeton WordNet data Version 2.0 (extract)  
2003, Princeton University

Arabic WordNet database schema    
Authorship: Adam Pease, Manuel Bertran, Piek Vossen, Christiane Fellbaum, Bill Black  
2006, Articulate Software, Princeton University, University of Manchester, UPC.

Arabic WordNet data  
Authorship: Musa Alkhalifa, Sabri Elkateb   
2007, UPC and the University of Manchester.

Arabic WordNet SQLite version  
2018, University of Science and Technology Houari Boumediene  

# Licence Terms

The SQLite database is subject to the Apache
License, Version 2.0, http://www.apache.org/licenses/LICENSE-2.0

And as in the initial package,

The Apache Derby database library is subject to the Apache
License, Version 2.0, http://www.apache.org/licenses/LICENSE-2.0

The Princeton WordNet data in the distributed database is subject to the WordNet license,
http://wordnet.princeton.edu/license.

The Arabic WordNet data in the distribution is subject to the Creative Commons Attribution-
ShareAlike license, Version 3.0, http://creativecommons.org/licenses/by-sa/3.0/


