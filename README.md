## Shell Shortcuts

Link to [Shell Shortcuts](terminal.md)
## Convert format in pandoc
pandoc -f latex -t markdown <file.tex> > <out.md>
## Pushing Changes from Desktop to Remote Repository

Follow these steps to push changes from your local desktop environment to a remote repository on GitHub.

### 1. Obtain Repository URL

First, obtain the URL of the repository to which you want to push your changes. For example:
```bash
https://github.com/rajeshphy/Private.git
```

### 2. Set Up Remote Origin

Use the following command to set up the remote repository as the origin:
```bash
git remote add origin https://github.com/rajeshphy/Private.git
```

### 3. Fetch and Rebase Changes

Ensure your local repository is synchronized with the remote repository by fetching and rebasing the changes:
```bash
git pull --rebase origin main
```

This step helps in integrating the latest changes from the remote repository while keeping your local changes on top.

### 4. Push Changes to Remote

Finally, push your local changes to the remote repository with the following command:
```bash
git push -u origin main
```

### Additional Note: Authentication

If prompted for a username and password, use your GitHub username for the username field. For the password, generate a personal access token from the Developer Settings on GitHub. This token will serve as your password for authentication.

Note: Ensure you keep your access token secure and do not share it openly.

Now, your changes should be successfully pushed to the remote repository on GitHub.
