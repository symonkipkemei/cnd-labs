![CodingNomads Logo](https://codingnomads.co/wp-content/uploads/2018/08/CN_Logo_Retina.png)
## python 101 - summary notes by [Symon Kipkemei](https://github.com/symonkipkemei):
- [Click here to get started](#click)
- [Course logistics](#course)
- [Learning something new](#learn)
- [Build something](#build)
- [Set up your machine](#set)
- [Introduction to programming](#intro)
- [Variables and types](#var)
- [Strings And Texth](#str)
- [Operators And Booleans](#ope)
- [Conditionals And Loops](#con)
- [User Input And String Formatting](#user)
- [Modules And Automation](#mod)
- [Version Control](#ver)



<h1 id = "click">1. Click here to get started</h1>

- Access to codingnomads forum
- Download python 101 labs

<h1 id = "course">2. Course logistics</h1>

- course progression
- Be at your computer
- keep a notebook
- communicate with us ( work on this)
- course logistics
  - muscle memory
  - Length of lessons
  - code block examples
- Learning resources
   - Text documentation
   - videos
   - Links
   - Quizzes
   - Assignments
   - Resources
   - projects
   - Feedback
- Grading
  - without mentorship
  - with community (interact more with the community)


<h1 id = "learn">3. Learning something new</h1>

- Growth mindset course
- Online communities (No man is an island)
     - codingnomads forum (joined)
     - stackoverflow (joined)
     - Twitter ( joined)
     - Dev.to ( joined, be more active)
     - Reddit ( should be your base for growth comment on communities, share your work)
- Podcasts and youtube channel
     - Talk python to me (join)
     - Real python ( join)
     - Python for everybody

     - Sentdex 
     - AI Sweigart
     - Corey schafer
- Coding nomads Forum
    - Asking good questions ( read through)
    - code formating
    ``` 
    Hello there , this is called a fenced code block
    ```
    - [Markdown Tutorial](https://www.markdowntutorial.com/)
    - [Asking goood questions](https://forum.codingnomads.co/t/how-to-ask-a-question/30)
    - [Formatting your code](https://forum.codingnomads.co/t/how-to-format-your-code/27)

- Job Outlook
  - Realistic salary expectations, your earning are directly proportional to your level of experience
  - Learning never stops
  - Increase your value


<h1 id = "build">4. Build something</h1>

  - Guess My number
  - play the game
  - programming concepts

<h1 id = "set">5. Set up your machine</h1>

   - hardware specifications
   - Operating system (Course built on unix sysytem)
       - [Setting up WSL](https://forum.codingnomads.co/t/developing-on-windows-with-wsl-2/791)

   - Software programs ( Vscode)
   - Installation test
      -  ``` 
         python3 --version 
         ```
   - A little bit of fun
      - Enter interactive mode of the python interpreter
        ```
        python3
        import this
        exit()
        ```

   - The python intepreter
     - Run and evaluate code line by line
     - its also known as (REPLs) Read-evaluate-print-loop
     - Once intepreter is closed code is gone.
     - IDE (Integrated development environment) solves this

   - VS code
      - Write, navigate & execute

   - The python console
      - a.K.a python console, python shell, python intepreter
   - Python scripts
      - procedural programming ( from top to bottom)
      - create python script ( add extension.py)
      - Run the script with command, terminal must point to the folder where the script is saved
       ```
       python3 <name of the script.py>
       ```
      - Run the script with button
   - Create your folder structure
   - Get your lab exercises



<h1 id = "intro">6. Introduction to programming</h1>

- A match made in heaven
    - computers are Precise, fast and don't mind repetition ( my take; all things that are repetitive in nature can be automized)
    - Humans are good in ideas and conceptualizing solutuions
    - A much made in heaven, we need a common language.
- Scripts and scripting
- Automate something.
- Pseudocode
  - organized thoughts
  - in between your idea and a functional code
- Code comments and dicriptiveness
```
# at the beginning of the line to make it a code comment
```
- Why code comments
  - exclusively for human beings
  - Undesrtand
  - Maintain
  - Improve
  - Extend
  - Debug
- How to write code comments (improve on this)
  - Rationale: Comments Tell You Why code was written in the way it was, rather than how the code does something or what it does.
  - Human-Focus: Code comments, as well as code style, are for humans only. But that doesn't make them less important!
  - Descriptiveness: What the code does, and how it accomplishes it, should be self-explanatory through well-written code and descriptively named variables

- Additional resources 
   - [Zentut:python comments](https://www.pythontutorial.net/python-basics/python-comments/)
   - [DigitalOcean:  How to Write Comments in Python 3](https://www.digitalocean.com/community/tutorials/how-to-write-comments-in-python-3)

- Pass Keyword
  - Placeholder when building code
  - Unlike code comments, python reads it and unadertsnads that it shouldn't do anything
- The print Function
  - display
  - print out
  - inspect/debug
- Scripts vs console
  


<h1 id = "var">7. Variables and types</h1>

- python variables
  - name of a value
  - reference that points to a value
- Variable assignment
   - ``` assignment operator = ```
- variables rules and conventions
  - Start With a Character and not a numbet
  - Don't Use Spaces
  - Avoid Reserved Keywords

- Coventions ( Best practice)
  - Use Lower-Case
  - Use Descriptive Names
  - Use Snake Case
- Multiple variable assignment
- Reserved Keywords
  ```
  python3
  help("keywords")
  ```
- Learn about individual keywords
  ```
  python3
  help("False")
  ```
- Aditional Resource
 [The 35 Words you need to Python.](https://yawpitchroll.com/posts/the-35-words-you-need-to-python/)

- Variables updates
  -  Dynamic typing
  -  Duck typing
- Data types
- Type checking
   - check the type of data ina variable
   ```
   type(num)
   ```
- Type operations
  - Integers
  - strings
  - float
  - booleans
  - lists
  - dictionaries

- [Built-in types](https://docs.python.org/3/library/stdtypes.html#built-in-types)

- Nothingness
 - Their is adifference between 0 and Nothing
 - ```
   Nothing = None
   ```
 
 <h1 id = "num">8. Numbers and math</h1>

- integers and Floats
- python calculator on REPL
- calculating with variables
- Arthietic operators
- Type conversion
  - Implicit ( done by python)
   - Divisions that produce a reminder 
   - Calculation that involve `` int `` and ``float``
   - Insertions of variables into f-strings

  - Explicit (done by you)
    - Input from a user that is gathered with ``` input() ``` always arrives as a text value, needs to be explicitly converted to integers/float


 <h1 id = "str">9. Strings And Text Data</h1>

- text is wrapped in quotes
- python sees text as a sequence of characters
      - python breaks texts into the smallest of their units.
      - 
- counting characters
```
len()
```
- string concatenation (joining characters to form a string)
- Error message
- String Indexing
- Zero based numbering 
- Accessing Characters Through Indices (positive indexing)
     ```
     0 1 2 3 4
     ---------
     h e l l o
  ```
  - brackets as tweezers
  ```
  greeting = "hello"
  greeting[0]  # h
  greeting[4]  # o
  ```
- Accessing Characters Backwards (negative indexing)
  - each string is also indexed from the end, starting with -1
  ```
  -5 -4 -3 -2 -1
   --------------
   h  e  l  l  o
  ```
- Slicing 
   - string slicing syntax
   ```
   s = "plumage"
   s[0:4]  # plum
   Start: You pass in the index of the first character you want to be part of your resulting word
   Separator: You place a colon (:) as a separator
   End: You add the index of the character one after the last one that you want to be part of your new string
   ```

   - syntax shortcut
   ```
   s = "plumage"
   s[:4]
   s[4:]
   define the end or the start index and python will slice all the way to the end
   ```
   - Specifying Strides
   ```
   s = "plumage"
   s[0:4:2]  # pu
   ```

   - Reverse a string
   ```
   s = "plumage"
   s[::-1]
   ```

- String Methods
  ``` I am calling a method on an object. ```
  [atring Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

- String are immutable
  Strings are immutable. You can't change a string, but you can create new strings and re-assign them to the original variable, effectively replacing the old string value with the new one.

- Searching and Finding

   - Finding Sub-Strings
   ```
   "mytext.txt".endswith("txt")  # True
   "mypage.php".endswith("txt")  # False

   ```
  

 <h1 id = "ope">10. Operators And Booleans</h1>

   operators are symbols with specific meaning that allow you to bring values in context with each other.
   1. Assignment Operator:Makes a symbol refer to a value
   2. Arithmetic Operators:Do arithmetic calculations
   3. Membership Operator:Checks whether an element is part of a collection
   3. Relational/Comparision Operators: Compare two or more values to each other
   4. Logical Operators: Compare values on the basis of logic
   5. Identity Operator : Finds out whether two values point to the same object in memory

- Assignment Operator``` (=)```
The assignment operator is used to assign values to variables. Its symbol is a single equals sign (=).
    - Chained Assignment
    - Shorthand Assignment

- Arthimetic operators
```
+	Addition	2 + 2	4
-	Subtraction	4 - 2	2
*	Multiplication	2 * 2	4
/	Division	10 / 5	2.0
%	Modulo	3 % 2	1 (performs a division and returns the remainder)
//	Floor division	5 // 2	2( performs divison but discards the remainder)
**	Exponent	3**2	9
```
-  Membership Operator ```(in)```
allows you to quickly check whether an element is part of a collection.


- Boolean Values
   - represent their own datatype (bool) in Python.
   - Boolean values in Python are capitalized


- Relational Operators
```
<	Less than	1 < 2	True
<=	Less than or equal to	1 <= 1	True
>	Greater than	2 > 1	True
>=	Greater than or equal to	2 >= 2	True
==	Equal to	2 == 2	True
!=	Not equal to	2 != 1	True

```

- Logical /conditional operators ``` ( and, or , not )```
```
and	True if both Booleans are True	True and True	True
or	True if either of the operands is True	True or False	True
not	True if the Boolean is False, False if Boolean is True	not False	True

```

- Identity Operators

```
is: Returns True if the variables on the left and right side of is point to the same object
is not: Returns True if the variables on the left and right side of is not do not point to the same object

```

The comparison operator == checks for the same values, and the identity operator is checks for whether they are the same object in memory.

- Operator precedence

```
Operators	Description
**	Exponentiation
*, /, %, //	Multiplication, division, modulo, floor division
+, -	Addition and subtraction
<=, <, >, >=	Comparison operators
==, !=	Equality operators
=, %=, /=, //=, -=, +=, *=, **=	Assignment operators
is, is not	Identity operators
in, not in	Membership operators
not, or, and	Logical operators

```


- Parentheses ``()``
If you ever feel unsure about what the operator precedence will be in an expression, then you can use parentheses to make
 sure it gets evaluated as you want it to

 <h1 id = "con">11. Conditionals and  Loops</h1>


- The if statatment
  - if, else, elif
- Flag variable
  ```
   flag = True

   if flag == True:
       print("yay!")
   The concept of using the state of a Boolean value to decide what to do in a conditional statement is sometimes called a flag
   ```
- The if - elif - else Construct
- Order Of Execution
- Looping
 allow you to repeat lines of code according to certain conditions
- For loop
  Loops through an iterable
- The Range Function
  Helps define how many times a loop should run
- Nested loops


 <h1 id = "user">12. User Input and string Formatting</h1>

- the input function
- the input prompt
- User input conversion
- The while loop
- Anatomy of a while loop
- The exit condition
- Looping keyword
  - break
  - continue
- String Formatting
   - F strings
   - str.format()
- String Mini-language
  - string Formatting Mini-language
   ```
   message = "you move me!"
   print(f"{message:>20}")
  ```
  - Character escaping
  - String Concatenation using Parentheses

<h1 id = "mod">13. Modules and Automation</h1>

- Modules and Packages
   - python's standard Library
   - code import
   - Code Namespaces
- Work with File paths
  - work with File paths
  - Interact with your file system

- Find your current location/working directory
 ```
 import pathlib
pathlib.Path().cwd()
 ```

- List Folder contents
    - list all files
    - ``` .iterdir() to create a collection of all the file paths of the files that are inside of the current working directory ```
    ```
    import pathlib
    path = pathlib.Path().cwd

    for filepath in path.iterdir():
        print(filepath)
    ```
    - display only file names (.name is an attribute of any pathlib.Path object)
    ```
    import pathlib

    path = pathlib.Path().cwd()

    for filepath in path.iterdir():
        print(filepath.name)
    ```
    - create a specific path object
    
    ```
    import pathlib
    pathlib.Path("/home/symon_kipkemei")
    ```

    - Filter by File extension
    ```
    import pathlib

    desktop = pathlib.Path('/home/symon_kipkemei')

    for filepath in desktop.iterdir():
         print(filepath.suffix)
    ```

    - Create A new path for the New Folder
    ```
     import pathlib
     new_path = pathlib.Path('/home/symon_kipkemei/screenshots')
     new_path.mkdir(exist_ok=True)  
    ```
    - Create path for each files
    ```
    new_filepath = new_path.joinpath(filepath.name)
    ```


    - Move files
    ```
    oldpath.replace(newpath)
    ```


<h1 id = "ver">14. Version Control</h1>

- Introduction to version control
  - Time-travel
  - Explore
  - Read history

-  Commit A file to version control
  - Git repositories
     - top level folder where anything inside will be tracked
  - Initializing a new git folder

  ``` git init ```

  - Add files to your git repo (which files should be bundled together) a.k.a staging area
  ``` git add README.md ```

  - checking updates and what's going on
  ``` git status ```

  - commiting ( give the bundle a name and register in the git version tracker) A snapshot in the history of your project
  ``` git commit -m "commit message" ```
  - addding many files at the same time
  ``` git add . ```

- Github
  - cloud storage for our git repositories
  - Connecting Your Local Git Repo to a GitHub Remote Repo
      - adding a remote repository
      - ``` git remote -v ` Monitors remotes
      - add remote
      ```
      git remote add origin https://github.com/<YOUR GITHUB USERNAME>/<folder.git>
      ```
      - where origin is the default name for git remotes
      - Pushing to github
      ```
      git push -u origin master
      ```

- Project documentation
   - How to write a good readme














 

