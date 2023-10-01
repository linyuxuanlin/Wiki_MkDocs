# BookJourney - Second-hand Book Mall Mini Program

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/书程小驿.jpg)

Project Repository: [**linyuxuanlin/BookJourney**](https://github.com/linyuxuanlin/BookJourney)

Demo (Scan the QR code with WeChat to experience):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/1.jpg)

## Background

A friend wanted to do some side business selling second-hand books on WeChat Moments, so he asked me to create a WeChat mini program. As I had nothing to do during the summer break, I decided to practice my skills. The requirement was to create a mall-like mini program that regularly updates new book information for buyers to choose from.

## Development

I didn't want to reinvent the wheel, so I found a good open-source mall-like mini program project: [wechat-app-mall](https://github.com/EastWorld/wechat-app-mall). I modified and added my own desired styles based on it (global search is very useful). The default style of this open-source mini program didn't match my aesthetic taste. What I needed was a simple page that could focus users' attention on the content to be displayed. After many iterations, the style basically met my requirements.

In terms of functionality, I removed a series of messy features related to bargaining and sharing rewards, and only kept the core functions.

Since I wasn't responsible for adding new products later, the backend product editor had to be a graphical interface. BookJourney uses the backend of [API Factory](https://www.it120.cc/), which eliminates the need to build a server and makes it easy for team members to add new products. However, free users have storage limitations.

## Pitfalls to Avoid

During the development of BookJourney, we encountered many challenges. For example, the issue of payment. Common sense told me to integrate WeChat Pay for easy ordering, but WeChat has removed the personal registration window for WeChat Pay in mini-programs (although this is also for user fund security). The only way was to register a company, but first, I needed a company. Further research showed that registering a company was not easy. I needed to find an accounting firm to act as an agent, have an office address, a red contract, and be audited by a bank manager. The application process took nearly two to three months, and the cost was close to a thousand yuan, not including various miscellaneous fees. The solution was to change the order button to contact customer service directly. Users only needed to take a screenshot of the "shopping cart" page and send it directly to the team member responsible for customer service to place an order.

## FAQ

Q: Why is it called BookJourney?  
A: Originally, it had a nice Chinese name called "Shu Cheng Xiao Yi," but when registering the mini-program, I found that it was already taken, so I had to compromise.

Q: Did you make any money?  
A: Total profit income: ¥16.66...

## Conclusion

After time has proven, this was a failed project.

In the early stages, we did not conduct thorough market research or understand the needs of users. We only created a product that we thought was cool. In the future, when working on projects, we need to pay attention not only to technology but also to the market and understand what kind of products the market needs.

## References and Acknowledgments

- [EastWorld / wechat-app-mall](https://github.com/EastWorld/wechat-app-mall)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.