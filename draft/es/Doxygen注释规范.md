# Normas de comentarios Doxygen

## Encabezado de archivo con índice desplegable

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
 * @author alguien
 * @date 2018.1.4
 * @brief Normas de comentarios de archivos C con Doxygen, pueden haber saltos de línea,
 * todos los resúmenes son iguales.
 *
 * @details Descripción detallada y explicación de este documento, pueden haber saltos de línea,
 * todas las descripciones detalladas son iguales.
 */

#include "header.h"
```

## Encabezado de estructuras y tipos de enumeración con índice desplegable

```c
/**
 * @brief Breve descripción
 *
 * @details Descripción detallada
 */
typedef enum BoxEnum_enum {
  BOXENUM_FIRST,  /**< Alguna documentación para el primero. */
  BOXENUM_SECOND, /**< Alguna documentación para el segundo. */
  BOXENUM_ETC     /**< Etc. */
} BoxEnum;
```

## Desglose de comentarios de encabezado de función

```c
/**
 * @brief Descripción breve de la función, puede ser en varias líneas
 *
 * @details Descripción detallada y explicación de la función, puede ser en varias líneas
 *
 * @note Contenido de notas importantes
 *
 * @param index Texto explicativo
 * @param cent Texto explicativo
 *
 * @return Descripción del contenido devuelto por la función
 * @retval 1 Prueba exitosa
 * @retval -1 Prueba fallida
 */
bool Test(int index, char *cent);
```

## Desglose de comentarios de variables

```c
int element = 0; /**< Breve descripción de la variable */
```

```
/**
 * @brief Descripción breve de la variable
 *
 * @details Descripción detallada de la variable
 */
unsigned int variable = 0;
```

## Desglose de comentarios de macros

```c
/**
 * @brief Breve descripción de la macro
 *
 * @details Descripción detallada de la macro
 */
#define variable 10
```

## Referencias y agradecimientos

- [Especificación de comentarios breves de C con Doxygen](https://www.liuguogy.com/archives/doxygen-c-brief-annotation.html)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.