# Avoid Chrome (Edge) Forced HTTPS Conversion

Some websites can only be accessed through http, but sometimes the browser will force the conversion to https, resulting in access errors. The following steps will show how to disable the browser's automatic conversion.

## Steps

Enter the link in the address bar and press enter:

- Chrome: `chrome://net-internals/#hsts`
- Edge: `edge://net-internals/#hsts`

In the `Delete domain security policies` section, enter the links that you do not want to be automatically converted. For example, if I want `wiki-power.com` to not be forced to use https, then I will enter `wiki-power.com` and click `Delete` to remove it.

Then enter the link in the address bar and press enter:

- Chrome: `chrome://flags/#edge-automatic-https`
- Edge: `edge://flags/#edge-automatic-https`

Change the `Default` option of `Automatic HTTPS` to `Disabled` and restart the browser.

## References and Acknowledgements

- [Edge or Google browser automatically converts http URLs to https, manual modification to http is invalid](https://blog.csdn.net/Thinker001/article/details/117717690)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.