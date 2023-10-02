# RSS - An Efficient Way of Reading

The full name of RSS is "Really Simple Syndication", which is a tool that allows you to subscribe to various websites of interest in one place.

Simply put, when the author you follow writes an article on their platform (which can be a blog, public account, Zhihu, etc.), RSS will push it to you for reading.

> If a website supports RSS, it means that every time it publishes a new article, it will add a record to a file located at a specific URL in a specific syntax (specifically XML markup language or JSON), listing the title, author, publication time, and content (which can be the full text or summary) of the article. In this way, users can collect the URLs of all the files provided by the websites they are interested in and periodically check for updates to know whether and when these websites have published new content. The core function of an RSS reader is to store the RSS addresses subscribed by users, automatically check for updates at a fixed frequency, and present the content in an easy-to-read format to users.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200225145439.png)
![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200225145502.png)

## Why Use RSS

### 1. Convenience

When I follow more people, I don't have to open Zhihu, Jianshu, or even check blogs one by one to actively get updates, but read them in a unified terminal.

### 2. Information Rights

The opposite of RSS is algorithm recommendation, such as WeChat public account, Zhihu, Weibo, Today's Headlines and other platforms. Not to mention the problem of algorithm push platform advertising and migration. The characteristic of algorithm recommendation is that you don't need to deliberately choose, and the algorithm will push content to you based on your preferences. In this way, you have almost no choice, and gradually lose the ability to judge while being "fed". What's even more frightening is that **it defines your portrait for you and turns you into what it thinks you are unconsciously**. The exposure of "big data kills the familiar" is not accidental. Peeking at user privacy with algorithms is a common practice of today's Internet companies.

**Be the master of information, not a slave.** RSS is an open protocol that allows free replacement of platforms and clients. The important thing is that **the right to obtain information is completely autonomous**. Compared with algorithm recommendation, RSS has controllability and security, and privacy is completely in your own hands.

### 3. Decentralization

Articles posted on platforms that require registration (such as WeChat, Weibo, and Zhihu) are often deleted due to sensitive content. In order to promote the free flow of information, it is necessary to adopt a decentralized approach, where authors can create their own platforms. RSS can collect scattered content and present it for reading.

## Starting RSS Reading

### 1. Obtaining RSS Sources

Using Inoreader as an example, the simplest way is to copy the blog address and paste it into Inoreader's search box, which usually allows for direct subscription.

To determine if a website has an RSS feed, look for this icon:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/rss.png)

Clicking on this icon will allow you to subscribe to the RSS link directly.  
If there is no icon, it may still have an RSS feed, but it may be hidden.

In this case, you can use a browser extension called RSS+:

- First, install the [Tampermonkey extension](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo), which requires a VPN.
- Then, install the [RSS+ script](https://greasyfork.org/zh-CN/scripts/373252-rss-show-site-all-rss).
- If the website has an RSS feed, it can be found in the small circle in the lower right corner.

For websites without an RSS feed, you can create your own RSS feed using the following tools:

- [feed43](http://feed43.com/)
- [RSSHub](https://docs.rsshub.app/#%E5%BE%AE%E5%8D%9A)
- [FeedOcean](https://feedocean.com/?lang=zh-CN)

These tools not only allow you to subscribe to blogs without an RSS feed, but also to Zhihu columns, WeChat public accounts, Weibo, and Tieba. Refer to the documentation for specific methods.

### 2. Choose an RSS Reader

**Inoreader**'s free version has complete basic functions and a capture time of about 15 minutes, which meets the requirements. It has a web version, iOS version (requires a US App Store account), and Android version.

**Reabble** is born for e-ink screen reading based on Inoreader API. It is recommended to upgrade to the paid version (¥21 per year, free version with 7 articles per day and no push notification). I set up a scheduled push of new articles to my Kindle at 9 am every day, and it is also convenient for annotation and exporting book excerpts. If you want to read on your computer, you can directly open [reabble.com](https://reabble.com) and create a desktop shortcut. The interface is simpler and ad-free compared to Inoreader.

## Subscribe to some interesting sources

Note: RSS is not suitable for subscribing to news websites, as the refresh rate is too fast and the content is too cumbersome, which leads to a poor reading experience. Therefore, RSS is more suitable for subscribing to high-quality blogs and other websites. It is not the more sources, the better. Too many sources will cause "information overload", and you will find yourself receiving hundreds of new information every day, but have no time to read.

I exported my own subscription source, which you can refer to: [**My Subscription**](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/doc/Blogs.opml)  
You can import the `.opml` file into Inoreader or other RSS readers.

Added in April 2023: Method for building a self-hosted RSS aggregator: [**Homelab - Self-hosted RSS aggregator FreshRSS**](https://wiki-power.com/Homelab-%E8%87%AA%E6%89%98%E7%AE%A1RSS%E8%81%9A%E5%90%88%E5%99%A8FreshRSS/).

## FAQ

Q: Will RSS reading be outdated by the times?  
A: Reading books in this way has not been outdated by the times. One trend is that all Internet platforms always develop in the direction of "popular and entertaining" to the masses, until the content becomes watered down, and new platforms take over, such as Zhihu and Douban. RSS is not affected by the rise and fall of platforms, unless a better protocol appears, RSS will not be eliminated.

## Conclusion

In the words of "notajerk":

> RSS is a great way to take control of your information intake and avoid the algorithmic echo chambers that social media platforms can create. It's not for everyone, but if you're looking for a way to stay informed without being overwhelmed, it's worth giving RSS a try.

When obtaining information online, one can imagine oneself as an ancient emperor listening to the opinions of courtiers. For an emperor, the most dangerous and inappropriate thing to do is to expose one's preferences, which can lead to being deceived by subordinates and eventually losing power. A wise emperor will maintain inner calmness and objectivity, insisting on listening to various opinions without revealing his own feelings, and verifying each opinion with objective facts to confirm its credibility. This is also the principle that everyone should adhere to when obtaining information thousands of years later. **Choosing information sources is also the most worthwhile place to spend time**.

## References and Acknowledgments

- [What You Can Do with RSS That You Haven’t Thought of Before](https://sspai.com/post/34280)
- [How to Find the RSS Address of a Website? Use RSS +!](https://blog.wizos.me/20181022-258.html)
- [Complete List of RSS Tools](https://blog.wizos.me/20180412-134.html)
- [My Introduction to Using RSS](https://www.cnblogs.com/buwuliao/p/8379549.html)
- [Self-made Full-text RSS Summary (with Recommended Tools)](https://www.douban.com/note/522518464/)
- [On the "Revival" of RSS](https://sspai.com/post/43998)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.