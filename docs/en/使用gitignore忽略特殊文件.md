# Using gitignore to Exclude Specific Files

There are certain files that we do not want to include in Git version control, and we also do not want them to constantly appear in the untracked list, such as `node_modules`, some development dependencies, compilation logs, and so on.

In such cases, we can create a `.gitignore` file to list the items that need to be ignored.

## Guidelines

- Empty lines or lines starting with the comment symbol `#` will be ignored.
- Standard glob pattern matching is used.
- If a matching pattern ends with a forward slash (/), it indicates that directories should be ignored.
- To exclude files and directories except for specific patterns, you can prefix the pattern with `!` to negate it.

## Examples

```gitignore
# This line is a comment and will be ignored by Git

# Ignore all files with the .a extension
*.a

# Do not ignore lib.a
!lib.a

# Ignore the TODO file in the root directory
/TODO

# Ignore the build folder
build/

# Ignore all txt files under the doc directory (excluding subdirectories)
doc/*.txt

# Ignore all txt files under the doc directory (including all subdirectories)
doc/**/*.txt
```

## References and Acknowledgments

- [zxhfighter/git-ignore.md](https://gist.github.com/zxhfighter/6320b9a08698bb8703ee)
- [github/gitignore](https://github.com/github/gitignore)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.