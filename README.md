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

### When error is encountered: RPC failed; HTTP 400 curl 22
If you encounter an error while pushing changes to the remote repository, you can try increasing the buffer size for HTTP post requests using the following command:
```bash
git config --global http.postBuffer 524288000
```

### Install git-filter-repo (if needed)

```bash
brew install git-filter-repo
```

### Remove a file from git history

```bash
git filter-repo --path Folder-Inside-Repo/ABC --invert-paths
```



### Additional Note: Authentication

If prompted for a username and password, use your GitHub username for the username field. For the password, generate a personal access token from the Developer Settings on GitHub. This token will serve as your password for authentication.

Note: Ensure you keep your access token secure and do not share it openly.

Now, your changes should be successfully pushed to the remote repository on GitHub.
