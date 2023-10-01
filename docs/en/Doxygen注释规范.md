# Doxygen Comment Specification

## File Header Annotation Expands Directory

No translation needed as the article is already in English.

/**
 * @file doxygen_c.h
 * @author someone
 * @date 2018.1.4
 * @brief Documentation for Doxygen-compliant C file comments, can be multiline,
 * all briefs are the same.
 *
 * @details Detailed explanation and interpretation of this document, can be multiline,
 * all detailed explanations are the same.
 */

#include "hearder.h"
```

## Struct and Enum Type Annotation Expanded Directory

```c
/**
 * @brief Brief explanation
 *
 * @details Detailed explanation
 */
typedef enum BoxEnum_enum {
  BOXENUM_FIRST,  /**< Some documentation for first. */
  BOXENUM_SECOND, /**< Some documentation for second. */
  BOXENUM_ETC     /**< Etc. */
} BoxEnum;
```

## Function Header Comment Expanded Directory

```c
/**
 * @brief Brief explanation of the function, can be multiline
 *
 * @details Detailed explanation and interpretation of the function, can be multiline
 *
 * @note Notes content
 *
 * @param index Explanation text
 * @param cent Explanation text
 *
 * @return Description of the content returned by the function
 * @retval 1 Test successful
 * @retval -1 Test failed
 */
bool Test(int index, char *cent);
```

## Variable Comment Expanded Directory

```c
int element = 0; /**< Brief explanation of the variable */
```

```
/**
 * @brief Brief explanation of the variable
 *
 * @details Detailed explanation of the variable
 */
unsigned int variable = 0;
```

## Macro Comment Expanded Directory

```c
/**
 * @brief Brief explanation of the macro
 *
 * @details Detailed explanation of the macro
 */
#define variable 10
```

## Reference and Acknowledgement

- [Brief Annotation Specification for C Language Based on Doxygen](https://www.liuguogy.com/archives/doxygen-c-brief-annotation.html)

(Note: As an AI language model, I cannot guarantee the accuracy of the content or the validity of the link provided.)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.