# How to Write a Practical VS Code Extension from Scratch (Work in Progress)

VS Code is a practical editor with a robust extension ecosystem that allows users to freely install or publish extensions to enhance the software's functionality.

This article originates from personal needs, focusing on the development of a practical kanban tool extension, detailing how to write and publish your own VS Code extension from scratch.

## Identifying Needs

When you have a need, the first step is to search for extensions that meet your requirements in the VS Code Extension Marketplace, without reinventing the wheel. Only when you find that existing applications do not meet your needs or lack the desired features should you consider developing an extension yourself.

In this example, I wanted a kanban tool that could instantly render my Markdown documents into a concise kanban view, allowing me to overview all tasks at hand. However, existing kanban-related extensions either do not work with Markdown format or fail to provide real-time updates to the kanban preview page, and some are not concise enough. In short, none of them meet my needs. So, I decided to create my own.

## Setting Up the Framework

The first step in extension development is to ensure that VS Code and Node.js are installed locally. Then, use npm to install Yeoman and VS Code Extension Generator to quickly generate the scaffold for extension development:

```
npm install -g yo generator-code
```

After installation, run the following command to create a new extension:

```
yo code
```

When prompted to choose the extension type, you can select "New Extension (TypeScript)" or choose another type based on personal preference.

In the auto-generated framework, there are two important files with the following names and purposes:

- src/extension.ts: The main entry point and logic implementation of the extension.
- package.json: Defines the extension's metadata and dependencies.

## Developing the Extension

## Testing the Extension

Press `F5` in VS Code to run and debug the extension. In this example, opening a Markdown file in the Debug window allows testing if the extension can render a kanban page.

## Packaging and Publishing the Extension

To package the extension, you need to install the `vsce` tool:

```
npm install -g vsce
```

Then, use `vsce package` to package the extension.

(Work in Progress)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.