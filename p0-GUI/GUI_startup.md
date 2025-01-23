---
meta:
    author: Austin Reid
    topic: Shakedown GUI project
    course: TN Tech PHYS4130
    term: Spring 2025
---

- [The Assignment](#the-assignment)
  * [Program specification:](#program-specification-)
  * [Possible libraries/languages](#possible-libraries-languages)
  * [The Writeup](#the-writeup)
    + [Languages, Libraries, Lessons Learned](#languages--libraries--lessons-learned)
    + [Questions](#questions)
    + [Attribution](#attribution)
    + [Timekeeping](#timekeeping)
- [The Submission](#the-submission)
  * [Code directory](#code-directory)
  * [Writeup directory](#writeup-directory)

# The Assignment

I've written a minimal program specification and writeup request below.
Please complete both: With full attribution and logged prompts, you may use AI on the programming task. I do not recommend it. You may _not_ use generative AI on the writeup.

> [!IMPORTANT]
> Commit your work by 1pm on Thursday, Jan 23

## Program specification:
Write a program incorporating the following:
 - Two figure axes
 - three buttons
 - two text boxes.
One button should save the text box values to a file, another button should load a text file to the boxes. The third button should do something with the values in the text boxes, and update at least one of the figures.

This program does not need to be "beautiful", so don't spend time making the interface pixel-perfect. It should be clear, though, with appropriately labeled buttons and documented code.

## Possible libraries/language

 1. Python, MatPlotLib, and Textual:
    - https://textual.textualize.io/
 1. Python & MatPlotLib
    - https://matplotlib.org/stable/gallery/widgets/buttons.html
    - https://matplotlib.org/stable/gallery/widgets/textbox.html
 1. C++ (or Python) & wxwidgets
    - https://docs.wxwidgets.org/3.0/classwx_button.html
 1. Pygame? Maybe. Could be fun.
 1. Python or WebAssembly + Web GUI framework: There are a lot of these. I don't know much about them, but if you have one you know or would like to learn, knock yourself out.

## The Writeup

Please include a single page markdown (.md) file[^1] with the following sections:

### Languages, Libraries, Lessons Learned
What language did you use for your submission? Is it the same one you started using?
If not, why'd you change?

What libraries did you use in your submission?
Were any of them remarkable?
Great to use, super annoying to use, etc? 

### Questions

#### Without looking anything up, answer the following
 1. Do you know what it means to "target compilation for WebAssembly?"

#### Use the internet to answer the following correctly and succinctly
 2. What purpose does a "debounce" serve in a user interface? Did you have to "debounce" your buttons in this gui? Why or why not?
 3. What is Fitts's Law? What relevance does it have for a scientific user interface?

### Attribution
What resources did you use on this assignment? People, websites, books, etc.

### Timekeeping
How long did you spend on this assignment? If you didn't keep an accurate log, an estimate is fine.

# The Submission
> [!IMPORTANT]
> Your submissions for this project should be located within this project's directory. You'll have a lot of different "code" and "writeup" directories before all is said and done!

Your contribution should be contained in a directory that is your GitHub username, with subfolders for code and writeup. Turn it in with a pull request.

## Code directory
A directory titled "code" that contains your program files and makefile (if used), or a ReadMe.md file that gives sufficiently detailed instructions for me to build and execute your code.

## Writeup directory
A directory titled "writeup" containing
 1. your writeup .md file and
 2. a screenshot of the GUI as it's running
 3. *ONLY REQUIRED WITH GENERATIVE AI:* A file titled genAI.md, containing the queries and responses from the AI tool you used. You **MUST** list the following details:
    1. the AI model you used (If you used multiple, indicate which one returned which prompt)
    2. The prompts you supplied
    3. The model's response to the prompt
    4. What part of the generated code you used
    5. What's wrong with the generated code

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

[^1]: Up to 500 words, but this is not a strict limit
