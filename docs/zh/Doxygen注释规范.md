---
id: Doxygen注释规范
title: Doxygen 注释规范
---

## 文件头标注展开目录

```c
/****************************************************************************
 *   Copyright (C) 2018 by Doxygen C Comment                                *
 *                                                                          *
 *   This file is part of Box.                                              *
 *                                                                          *
 *   Box is free software: you can redistribute it and/or modify it         *
 *   under the terms of the GNU Lesser General Public License as published  *
 *   by the Free Software Foundation, either version 3 of the License, or   *
 *   (at your option) any later version.                                    *
 *                                                                          *
 *   Box is distributed in the hope that it will be useful,                 *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of         *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          *
 *   GNU Lesser General Public License for more details.                    *
 *                                                                          *
 *   You should have received a copy of the GNU Lesser General Public       *
 *   License along with Box.  If not, see <http://www.gnu.org/licenses/>.   *
 ****************************************************************************/

/**
 * @file doxygen_c.h
 * @author someone
 * @date 2018.1.4
 * @brief doxygen 规范的 C 文件注释规范文档，可以换行，
 * 所有 brief 同
 *
 * @details 对该文档的详细说明和解释，可以换行，
 * 所有详细说明同
 */

#include "hearder.h"
```

## 结构体、枚举类型标注展开目录

```c
/**
 * @brief 简要说明
 *
 * @details 详细说明
 */
typedef enum BoxEnum_enum {
  BOXENUM_FIRST,  /**< Some documentation for first. */
  BOXENUM_SECOND, /**< Some documentation for second. */
  BOXENUM_ETC     /**< Etc. */
} BoxEnum;
```

## 函数头注释展开目录

```c
/**
 * @brief 函数简要说明，可以换行
 *
 * @details 对函数的详细说明和解释，可以换行
 *
 * @note 注意事项内容
 *
 * @param index 说明文字
 * @param cent 说明文字
 *
 * @return 描述函数返回的内容
 * @retval 1 测试成功
 * @retval -1 测试失败
 */
bool Test(int index, char *cent);
```

## 变量注释展开目录

```c
int element = 0; /**< 变量简单说明 */
```

```
/**
 * @brief 变量简要说明
 *
 * @details 变量详细说明
 */
unsigned int variable = 0;
```

## 宏注释展开目录

```c
/**
 * @brief 宏简要说明
 *
 * @details 宏详细说明
 */
#define variable 10
```

## 参考与致谢

- [基于 Doxygen 的 C 语言简要注释规范](https://www.liuguogy.com/archives/doxygen-c-brief-annotation.html)
