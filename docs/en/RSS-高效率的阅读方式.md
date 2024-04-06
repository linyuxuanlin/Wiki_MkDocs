# RSS - An Efficient Way to Read

RSS stands for "Really Simple Syndication" and is a tool that allows you to subscribe to various websites of interest in one place.

In simple terms, when the authors you follow write an article on their platform (which could be a blog, public account, or a platform like Zhihu), RSS will push it to me for reading.

> When a website supports RSS, it means that every time it publishes a new article, it adds a record in a file located at a specific URL with a specific syntax (specifically in XML markup language or JSON). This record includes the article's title, author, publication time, and content (which can be the full text or a summary). In this way, users can collect the URLs of these files provided by all the websites they are interested in and periodically check for updates in the content of these files. The core function of an RSS reader is to store the RSS addresses subscribed by the user, automatically check for updates at a fixed frequency, and present the content in a readable format to the user.

![RSS Example 1](https://media.wiki-power.com/img/20200225145439.png)
![RSS Example 2](https://media.wiki-power.com/img/20200225145502.png)

## Why Use RSS

### 1. Convenience

As I start following more people, I don't have to individually visit platforms like Zhihu, Jian Shu, or even check blogs for updates. I can read everything in one unified terminal.

### 2. Information Control

RSS stands in contrast to algorithmic recommendations found on platforms like WeChat Public Accounts, Zhihu, Weibo, and Toutiao, to name a few. Leaving aside the issues of excessive advertising and the inconvenience of migration, algorithmic recommendations rely on your preferences to push content to you. Consequently, you have little room for choice and gradually lose the ability to make judgments while being continuously "fed" information. What's even more concerning is that these algorithms define your online persona and transform you into what they think you are. The revelation of "big data price discrimination" is no accident. Peering into user privacy through algorithms is a common practice among today's internet companies.

**Be the master of your information, not a slave.** RSS is an open protocol that allows freedom to switch between platforms and clients. Crucially, it empowers you with full control over your information. Compared to algorithmic recommendations, RSS provides controllability and a sense of security, with privacy firmly in your hands.

### 3. Decentralization

Articles posted on platforms requiring registration (such as Public Accounts, Weibo, Zhihu, etc.) are often deleted due to sensitive content. To ensure the free flow of information, we need to embrace a decentralized approach, where authors create their own platforms. RSS collects scattered content and presents it for your reading pleasure.

## Getting Started with RSS Reading

### 1. Acquiring RSS Sources

Using Inoreader as an example, the simplest method is to copy the blog's URL and paste it into Inoreader's search box, where you can usually subscribe directly.

To determine if a website has an RSS feed, look for this symbol when you visit:

![RSS Symbol](https://media.wiki-power.com/img/rss.png)

If you see this symbol, you can click on it to directly subscribe to the RSS link. If the symbol is absent, it may still have an RSS feed, but it might be hidden.

In such cases, you can use a browser extension called RSS+:

- First, install the [Tampermonkey extension](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo) (requires VPN access).
- Then, install the [RSS+ script](https://greasyfork.org/zh-CN/scripts/373252-rss-show-site-all-rss).
- At this point, if the website has an RSS feed, you can find it in the small circle in the lower right corner.

For websites without RSS, you can create your own RSS feed using these recommended tools:

- [feed43](http://feed43.com/)
- [RSSHub](https://docs.rsshub.app/#%E5%BE%AE%E5%8D%9A)
- [FeedOcean](https://feedocean.com/?lang=zh-CN)

These tools not only allow you to subscribe to blogs without RSS feeds but also directly subscribe to Zhihu columns, public accounts, Weibo, and forums, among others. For specific instructions, refer to the documentation.

### 2. Choose an RSS Reader

**Inoreader** offers a comprehensive set of features in its free version, with a fetching time of approximately 15 minutes, which meets the requirements. It is available in a web version, as well as on iOS (requires a US App Store account) and Android.

**Reabble**, built on the Inoreader API, is designed for e-ink screen reading. I recommend upgrading to the paid version (annual fee of ¥21), as the free version allows only 7 articles per day and does not support push notifications. I have set it up to send new articles to my Kindle for reading at 9 AM daily, making it convenient for annotations and exporting highlights. If you prefer reading on your computer, you can directly access [reabble.com](https://reabble.com) and create a desktop shortcut. The interface is cleaner and free of ads compared to Inoreader.

## Subscribing to Interesting Sources

Note: RSS is not ideal for subscribing to news websites as they update too frequently, leading to a cumbersome reading experience. Therefore, RSS is better suited for subscribing to high-quality blogs and similar websites. More is not necessarily better when it comes to subscriptions; it's best to keep them focused. Subscribing to too many sources can result in information overload, with hundreds of new updates every day that you may not have time to read.

I have exported my own subscription sources, which you can reference here: [**My Subscriptions**](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/doc/Blogs.opml). You can import the `.opml` file into Inoreader or other RSS readers.

Supplement as of April 2023: A guide on setting up a self-hosted RSS aggregator can be found here: [**Homelab - Self-Hosted RSS Aggregator FreshRSS**](https://wiki-power.com/Homelab-%E8%87%AA%E6%89%98%E7%AE%A1RSS%E8%81%9A%E5%90%88%E5%99%A8FreshRSS/).

## FAQ

Q: Will RSS reading become obsolete?
A: Reading, in this form, has not become obsolete. A common trend with internet platforms is to cater to mass preferences until the content becomes diluted, and new platforms replace them, as seen with platforms like Zhihu and Douban. However, RSS remains unaffected by the rise and fall of platforms unless a better protocol emerges. Therefore, RSS is not likely to become obsolete.

## Conclusion

To conclude, I'd like to quote "[notajerk](https://sspai.com/user/701048/updates)":

> When gathering information online, one can imagine themselves as an ancient emperor seeking counsel from advisors. For an emperor, the most dangerous and ill-advised action is to reveal personal preferences, which forms the basis for advisors to manipulate and eventually usurp power. A wise emperor maintains inner equanimity (objectivity), solicits opinions from various sources without disclosing personal sentiments, and verifies each opinion against objective facts to confirm their credibility. This is a principle that every person should uphold when obtaining information even thousands of years later. **Choosing sources of information is where time is most wisely spent.**

## References and Acknowledgments

- [What You Can Do with RSS That You Haven't Thought Of](https://sspai.com/post/34280)
- [How to Find a Website's RSS Address? Use RSS+!](https://blog.wizos.me/20181022-258.html)
- [Comprehensive List of RSS Tools](https://blog.wizos.me/20180412-134.html)
- [My RSS Usage Guide](https://www.cnblogs.com/buwuliao/p/8379549.html)
- [Homemade Full-Text RSS Compilation (Includes Recommended Tools)](https://www.douban.com/note/522518464/)
- [The "Revival" of RSS](https://sspai.com/post/43998)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
