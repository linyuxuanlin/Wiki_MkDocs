# Doxygen Commenting Guidelines

## File Header Annotation and Directory Expansion

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
 * @brief Document outlining the Doxygen conventions for C file comments. 
 *        Line breaks are acceptable. All brief descriptions should follow
 *        the same format.
 *
 * @details Detailed explanation and description of this document. Line
 * breaks are acceptable. All detailed explanations should follow the same
 * format.
 */

#include "header.h"
```

## Structs and Enum Type Annotation and Directory Expansion

```c
/**
 * @brief Brief Explanation
 *
 * @details Detailed Explanation
 */
typedef enum BoxEnum_enum {
  BOXENUM_FIRST,  /**< Some documentation for the first item. */
  BOXENUM_SECOND, /**< Some documentation for the second item. */
  BOXENUM_ETC     /**< Etc. */
} BoxEnum;
```

## Function Header Comment Expansion

```c
/**
 * @brief A concise description of the function. This can be multiline.
 *
 * @details Detailed explanation and description of the function, which can be multiline as well.
 *
 * @note Notes and important considerations about the function.
 *
 * @param index An explanation for the 'index' parameter.
 * @param cent An explanation for the 'cent' parameter.
 *
 * @return Description of what the function returns.
 * @retval 1 Successful test
 * @retval -1 Test failed
 */
bool Test(int index, char *cent);
```

## Variable Comment Expansion

```c
int element = 0; /**< A brief description of the variable. */
```

```c
/**
 * @brief A concise explanation of the variable.
 *
 * @details Detailed explanation of the variable.
 */
unsigned int variable = 0;
```

## Macro Comment Expansion

```c
/**
 * @brief A brief explanation of the macro.
 *
 * @details Detailed explanation of the macro.
 */
#define variable 10
```

## References and Acknowledgments

- [C Language Brief Comment Guidelines Based on Doxygen](https://www.liuguogy.com/archives/doxygen-c-brief-annotation.html)
```

Please let me know if you need any further assistance.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.