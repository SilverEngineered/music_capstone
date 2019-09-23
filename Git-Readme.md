
# Step-To-Step Git Instructions to Make Changes
1. Supposed you have already had your git setup properly
2. Make sure your local repo is updated with master.

    ` git pull origin master`
3. Create and move to a **new branch**

    ` git branch new-sample-branch`

    ` git checkout new-sample-branch`
4. Now that you are on your own feature branch, make whatever changes you want!
5. Once you complete your feature, **add, commit and push** your change to Github. If you do everything correctly, you would see your change in Github branch: new-sample-branch
    
    `git add .`

    `git commit -a`

    `git push origin new-sample-branch`
6. Push changes to **qa** branch for testing

    `git pull origin qa`

    `git checkout origin/qa`

    `git merge new-sample-branch`

    `git push origin qa`
7. Once you finished all testing in qa branch, create a **Pull Request** to the master branch by going to your banch on Github, and submitting a new Pull Request.
8. People will make comments and updates will need to be made (usually multiple times), from there you will need to fix your code, push to new-sample-branch and qa and test again before the code is merged. So repeat step 4-6.
9. Hopefully someone will finally approve your code and merge your code into master branch. Congratulations!
