# Delete a folder in a GitHub repository

## Problem

When uploading a local repository to GitHub, you may forget to ignore a certain folder and push it to the remote repository. How can you delete the folder in the GitHub repository while keeping it in your local repository?

## Solution

```shell
git pull origin master        # First, pull the project from the remote repository
dir                           # Check which folders exist
git rm -r --cached target     # Delete the folder named "target"
git commit -m 'Deleted target'  # Add a description of the operation and commit
```

## Reference and Acknowledgement

- [Delete a folder in GitHub](https://blog.csdn.net/wudinaniya/article/details/77508229)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.