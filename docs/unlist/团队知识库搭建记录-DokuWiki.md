---
id: 团队知识库搭建记录-DokuWiki
title: 团队知识库搭建记录 - DokuWiki
---


对比：

- MoinMoin Wiki
- FosWiki
- xwiki
- mm-wiki
- MinDoc



> 文章作者：**Power Lin**
> 原文地址：<https://wiki-power.com>  
> 版权声明：文章采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议，转载请注明出处。

## 拓展

- discussion plugin
- Markdowku
- MathJax plugin
- Pagelist Plugin
- simplenavi plugin
- Wrap Plugin
- Indexmenu Plugin：索引目录

模板

- vector template

## 命名空间与文章

DokuWiki 的文章数据在 `dokuwiki/data/pages` 目录下。命名空间相当于文件夹，`.txt` 文件相当于单篇文章。

中文目录不能正常显示的解决方法：

1. 进入 `DokuWiki` 目录下的 `/inc` 文件夹，打开 `pageutils.php` 文件，将如下两行注释：

   ```
   // $file = urlencode($file);
   // $file = str_replace('%2F','/',$file);
   ```

2. 将如下一行代码注释，并添加另外一行：

   ```
   // return urldecode($file);
   return $file;
   ```

## 新增文章

1. 搜索安装插件：`Add New Page Plugin`
2. 网址后缀 id 改为 `sidebar` 访问
3. 创建页面，写入 `{{NEWPAGE}}`

## 删除文章

把文章内容删空，页面就自动删除了。没有文章的命名空间也会被自动移除

## 移动文章 / 修改名字

1. 搜索安装插件：`Move Plugin`
2. 在右侧工具栏 - `页面重命名`

## 定制

### 删除页面内的编辑按钮

`inc/html.php` 中搜索

```
return "<div class='secedit editbutton_" . $data['target'] .
                   " editbutton_" . $secid . "'>" .
       html_btn('secedit', $ID, '',
                array_merge(array('do'  => 'edit',
                                  'rev' => $INFO['lastmod'],
                                  'summary' => '['.$name.'] '), $data),
                'post', $name) . '</div>';
```

注释掉。

## 问题及解决

### 上传的文件与扩展名不符

修改 `inc/media.php` ：

```
if(substr($mime,0,6) == 'image/'){
$info = getimagesize($file);
if($mime == 'image/gif' && $info[2] != 1){
msg(sprintf('php function getimagesize(%s) does not think this is an image/gif file (info[2]=%d) even though %s is the mime type',$file,$info[2],$mime));
return 0;
}elseif($mime == 'image/jpeg' && $info[2] != 2){
msg(sprintf('php function getimagesize(%s) does not think this is an image/jpeg file (info[2]=%d) even though %s is the mime type',$file,$info[2],$mime));
return 0;
}elseif($mime == 'image/png' && $info[2] != 3){
msg(sprintf('php function getimagesize(%s) does not think this is an image/png file (info[2]=%d) even though %s is the mime type',$file,$info[2],$mime));
return 0;
}

This function used to return -1 if the info[2] didn't return the right type. Now I just return 0 and show a msg. The debug messages printed out show

php function getimagesize(/srv/www/www.ini.unizh.ch/tmp/phpQu74yf) does not think this is an image/jpeg file (info[2]=0) even though image/jpeg is the mime type
```

### 批量导入用户出现乱码

解决方法：使用 utf8 编码的 .csv 文件


## 参考与致谢

- [dokuwiki 学习（一）—— 增加页面命名空间](https://blog.csdn.net/wszll_Alex/article/details/80246721)
- [dokuwiki 学习（二）—— 新增页面（文章）](https://blog.csdn.net/wszll_Alex/article/details/80246836)
- [dokuwiki 学习（三）—— 删除页面（文章）](https://blog.csdn.net/wszll_Alex/article/details/80252098)
- [dokuwiki 学习（四）—— 移动页面（文章）](https://blog.csdn.net/wszll_Alex/article/details/80252132)
- [dokuwiki 插件的常用配置及其他 Tips](https://leekwen.blog.csdn.net/article/details/54907445?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.control)
- [自定义 DokuWiki](https://wiki.gimo.me/wiki/customize)
- [Upload doesn't match extension - DokuWiki User Forum](https://forum.dokuwiki.org/d/1297-upload-doesn-t-match-extension/3)
- [dokuwiki 学习（六）—— 增加媒体命名空间](https://blog.csdn.net/wszll_Alex/article/details/80252201)
