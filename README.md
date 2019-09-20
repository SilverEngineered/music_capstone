# Music Capstone Coding Guidline


## Source Control Infrastructure
For this project, we will be Git for source control with a feature branch style of source control. 

### Git
Git is the largest source control software out there. This is a good refresher https://rogerdudler.github.io/git-guide/ I would recommend brushing up on.

### Feature Branch
We will be using feature branches to organize our code, meaning no work will be done in the main branch of the repo, everything will be done in feature branches that will eventually be merged into the stable master branch. We will also have an experimental testing branch (semi-stable) that we will merge features into to test before making the merge to master. I have outlined the path of creating and publishing code below (I imagine this is something that will be referred to a lot at first).

### Pushing Code


#### I want to create a new feature
1.)  Branch off from Master's latest stable release (LSR) with a branch using this convention feature/{type_of_feature}/{name_of_feature}.

ex. feature/machine_learning/midi_extraction_algorithm

2.)  Document in a ReadMe where this code will be located and what its purpose will be. 📘

3.)  Write the perfect code you know how to write!

#### My BEAUTIFUL code is written, now what?
1.)   Merge your branch into the Experimental Branch titled "testing".

2.)  Test the interactions with the other latest semi-stable features, if something breaks, fix the code and come back to this step.

#### My BEAUTIFUL code is tested, now what?
1.)   Submit a PR (Pull request) to merge your code into Master to create another LSR with a description of what feature you added.

2.) 1 of 2 things will happen here.
A.) Your request will be approved by somebody (any 1 other person)
B.)  A reviewer will (again, any 1 other person) have something to say about the code or have questions about it in which case respond to these questions/concerns and update the PR.

3.) Merge and Close the feature Branch

🎉🥳🎉 Congradulations!!! You have just added a cool new feature to our codebase


## Repo Structure

There exists 4 folders under the top level Repo where all code and assets, besides the main.py script will be contained. 

**NO FEATURE BRANCH SHOULD AFFECT CODE IN MULTIPLE FOLDERS.**

### The different folders

#### /UI

Contains all code relating to UI design

#### /ML

This folder will contain all code related to different machine learning algorithms and "smart processing" of data

#### /IO
Contains all code for Hardware input and output, including but not limited to getting Midi data from the keyboard in addition to turning on specific lights.

#### /Utils
Contains extra utility code that is necessary for preprocessing data in addition to web scraping and fetching songs, in addition to working with local data

#### /Resources
Contains only non-code resources such as a few necessary or example MP3's or some assets required by the UI

## General Rules of Thumb

- Document everything with Python Docs 
Helpful link: https://realpython.com/documenting-python-code/

- Do not push any large data that is not essential to the basic code running correctly

- If there is any confusion on how to do something that is not outlined in this document, get an opinion from the whole group, do not assume any  liberties not outlined here.

- Commit and push code regularly to your feature branch

- Do not push any unstable code to Master, and if a bug is found, create a hot fix or ask somebody to create a hot fix

- When in doubt about software engineering principles consult https://agilemanifesto.org

- Include useful commit messages


