# Bash-on-python
Something similar at bash and simple programming language on Python

Start a test.py; in main.py main functions; in lang.py work with language programming. 
When you launch test.py will appear "terminal" (Example: > ). 
List commands and functions will expand. You can help me with this :)
If you need discover info about command just write "man [command]" or see file help.tc. 

# Info about files

The funcs directory is responsible for running functions from the user, i.e. for my programming language. To create this you need to: 
1. Create a file with the extension .tcy 
2. Write to the file (as I will write right now! And then it will not work correctly!). Write: on the first line Name = and any name. On the second Ver = and any version. And on the third File = and file (necessarily with the extension!) it can be either .py or .tcy (this is the programming language file itself). All. 
3. Create a file with the same name and extension that you specified in File. Well, we write the code there. each line must end with ; . 
4. When we have written the code, we save the file. We go to the terminal and write: xc -void file in which we wrote the information (where Name, etc.) st
Command: xc -void name_info_file.tcy st

----

Help.tc it stores information about commands, that is, for the man command.

----

in Mn.tc information about the terminal itself is stored.

----

In logs.tc saves all the commands that you wrote in the terminal.

----

In usr.tc user information is stored

