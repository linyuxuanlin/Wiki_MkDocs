# BookJourney - Secondhand Bookstore Mini Program

![BookJourney](https://media.wiki-power.com/img/书程小驿.jpg)

Project Repository: [**linyuxuanlin/BookJourney**](https://github.com/linyuxuanlin/BookJourney)

Demo (Scan with WeChat):

![Demo](https://media.wiki-power.com/img/1.jpg)

## Background

A friend wanted to explore a side business of selling secondhand books on WeChat Moments, so they asked me to create a WeChat mini program for them. With some free time during the summer break, I decided to take on the project. The requirement was to develop a marketplace-style mini program that would regularly list new book information for buyers to browse and select.

## Development

I didn't want to reinvent the wheel, and I discovered a promising open-source project for a mall-style mini program: [wechat-app-mall](https://github.com/EastWorld/wechat-app-mall). I decided to build upon it, making modifications and adding the styles I envisioned (global search was quite handy). The default styles of this open-source mini program didn't align with my aesthetic preferences. What I aimed for was a clean, focused presentation of content on simple pages. After numerous iterations, the styles were brought in line with my vision.

In terms of functionality, I removed various features related to bargaining and reward sharing that seemed convoluted and retained only the core functions.

Since I wouldn't be responsible for adding new products later, the backend product editing needed to be a graphical interface. BookJourney utilizes the backend provided by [api factory](https://www.it120.cc/), eliminating the need for setting up our own server, and making it convenient for team members to list new products. However, this comes with storage limitations for free users.

## Pitfalls

Developing BookJourney came with its share of challenges. For instance, the issue of payments. Common sense suggested integrating WeChat Pay for user convenience, but WeChat had cut off the WeChat Pay option for individual registered mini programs (possibly due to security concerns). The only way was to register a business account, but that required having a registered company. Further investigation revealed that registering a company was not a straightforward task. It involved hiring an accounting firm, having a physical office address, signing redacted contracts, undergoing bank manager reviews, taking nearly two to three months, incurring costs of around a thousand yuan, not to mention various miscellaneous charges. The solution was to replace the "Place Order" button with "Contact Customer Service." Users could now simply take a screenshot of their "Shopping Cart" page and send it to the customer service team member responsible for placing orders.

## FAQ

Q: Why is it called BookJourney?  
A: Originally, it had a nice Chinese name, "书程小驿." However, during the mini program registration process, I discovered that the name was already taken, so I had to compromise.

Q: Did it make any money?  
A: Total profit income: ¥16.66...

## Conclusion

With the benefit of hindsight, this was a failed project.

In the initial stages, I didn't conduct thorough market research, failed to understand user needs, and instead created a product I thought was cool. In the future, when undertaking projects, it's crucial to focus not only on technology but also on the market, to understand what kind of products the market demands.

## References and Acknowledgments

- [EastWorld / wechat-app-mall](https://github.com/EastWorld/wechat-app-mall)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
