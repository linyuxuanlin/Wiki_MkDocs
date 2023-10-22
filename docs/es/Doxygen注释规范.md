# Normas de Comentarios Doxygen

## Expansión de la Anotación de Encabezado de Archivo

```c
/****************************************************************************
 *   Copyright (C) 2018 por Comentario C de Doxygen                         *
 *                                                                          *
 *   Este archivo es parte de Box.                                          *
 *                                                                          *
 *   Box es software libre: puedes redistribuirlo y/o modificarlo           *
 *   bajo los términos de la Licencia Pública General Menor de GNU tal     *
 *   como fue publicada por la Fundación de Software Libre, en su versión  *
 *   3 de la Licencia, o (a tu elección) cualquier versión posterior.       *
 *                                                                          *
 *   Box se distribuye con la esperanza de que sea útil,                   *
 *   pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de        *
 *   COMERCIABILIDAD o IDONEIDAD PARA UN PROPÓSITO PARTICULAR. Consulta la  *
 *   Licencia Pública General Menor de GNU para obtener más detalles.      *
 *                                                                          *
 *   Deberías haber recibido una copia de la Licencia Pública General Menor *
 *   de GNU junto con Box. Si no la has recibido, consulta                  *
 *   <http://www.gnu.org/licenses/>.                                        *
 ****************************************************************************/

/**
 * @file doxygen_c.h
 * @autor alguien
 * @fecha 2018.1.4
 * @brief Documentación de las normas de comentarios de archivos C para Doxygen, con capacidad de salto de línea,
 * todos los breves son iguales.
 *
 * @details Explicación detallada de este documento y su interpretación, con capacidad de salto de línea,
 * todos los detalles son iguales.
 */

#include "header.h"
```

## Expansión de la Anotación de Tipos de Estructuras y Enumeraciones

```c
/**
 * @brief Descripción concisa
 *
 * @details Descripción detallada
 */
typedef enum BoxEnum_enum {
  BOXENUM_FIRST,  /**< Alguna documentación para el primero. */
  BOXENUM_SECOND, /**< Alguna documentación para el segundo. */
  BOXENUM_ETC     /**< Etc. */
} BoxEnum;
```

## Desglose de Comentarios de Encabezado de Función

```c
/**
 * @brief Descripción breve de la función, puede ocupar varias líneas
 *
 * @details Explicación detallada y completa de la función, también puede ocupar varias líneas
 *
 * @note Contenido de las observaciones
 *
 * @param index Texto explicativo
 * @param cent Texto explicativo
 *
 * @return Descripción del valor devuelto por la función
 * @retval 1 Éxito en la prueba
 * @retval -1 Fallo en la prueba
 */
bool Test(int index, char *cent);
```

## Desglose de Comentarios de Variables

```c
int element = 0; /**< Descripción breve de la variable */
```

```
/**
 * @brief Descripción breve de la variable
 *
 * @details Explicación detallada de la variable
 */
unsigned int variable = 0;
```

## Desglose de Comentarios de Macros

```c
/**
 * @brief Descripción breve del macro
 *
 * @details Explicación detallada del macro
 */
#define variable 10
```

## Referencias y Agradecimientos

- [Normas de Comentarios Breves en C basadas en Doxygen](https://www.liuguogy.com/archives/doxygen-c-brief-annotation.html)
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.