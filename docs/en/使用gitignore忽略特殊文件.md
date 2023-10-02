# Using gitignore to ignore special files

There are some files that we do not want to include in Git version control, nor do we want them to always appear in the untracked list, such as node_modules, some development dependencies, compilation logs, and so on.

In this case, we can create a `.gitignore` file and list the items that need to be ignored.

## Specification

- Empty lines or lines starting with the comment symbol `#` will be ignored
- Standard glob pattern matching
- Matching patterns followed by a backslash (/) indicate that the directory should be ignored
- To ignore files and directories other than the specified patterns, add `!` before the pattern to negate it

## Example

```gitignore
# This line is a comment and will be ignored by Git

# Ignore all .a files
*.a

# Do not ignore lib.a
!lib.a

# Ignore the TODO file in the root directory
/TODO

# Ignore the build folder
build/

# Ignore all txt files in the doc directory (excluding subdirectories)
doc/*.txt

# Ignore all txt files in the doc directory (including all subdirectories)
doc/**/*.txt
```

## Reference and Acknowledgement

- [zxhfighter/git-ignore.md](https://gist.github.com/zxhfighter/6320b9a08698bb8703ee)
- [github/gitignore](https://github.com/github/gitignore)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.