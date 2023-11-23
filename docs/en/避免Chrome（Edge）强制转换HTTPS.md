# Avoid Chrome (Edge) Forced HTTPS Conversion

Some websites can only be accessed using HTTP, but sometimes the browser forcibly converts them to HTTPS, resulting in access errors. The following steps will show you how to disable the browser's automatic conversion.

## Steps

Enter the following link in the address bar and press Enter:

- Chrome: `chrome://net-internals/#hsts`
- Edge: `edge://net-internals/#hsts`

In the "Delete domain security policies" section, enter the links that you do not want to be automatically converted. For example, if you want to prevent `wiki-power.com` from being forcibly converted to HTTPS, enter `wiki-power.com` and click "Delete" to remove it.

Then enter the following link in the address bar and press Enter:

- Chrome: `chrome://flags/#edge-automatic-https`
- Edge: `edge://flags/#edge-automatic-https`

Change the "Automatic HTTPS" option from "Default" to "Disabled" and restart the browser.

## References and Acknowledgements

- [Edge or Google Chrome automatically converts HTTP URLs to HTTPS, manual modification to HTTP is ineffective](https://blog.csdn.net/Thinker001/article/details/117717690)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.