# Deleting a Specific Folder in a GitHub Repository

## Problem Background

While uploading a local repository to GitHub, you may have forgotten to exclude a particular folder and inadvertently pushed it to the remote repository. How can you remove this folder from the GitHub repository while retaining it in your local directory?

## Solution

```shell
git pull origin master        # First, pull the content from the remote repository
dir                           # List the available folders in your local directory
git rm -r --cached target     # Delete the folder named 'target'
git commit -m 'Removed target folder'  # Provide a descriptive commit message and commit the changes
```

## References and Acknowledgments

- [How to Delete a Specific Folder in GitHub](https://blog.csdn.net/wudinaniya/article/details/77508229)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.