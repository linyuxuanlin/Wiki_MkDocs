## Project Organization

A Visual Basic project is organized around three primary types of files: **Forms**, **Modules**, and **Classes**. Forms normally contain interactive UI (i.e. TextBox, Button, Picture).

## C Language Concepts in Visual Basic

### Data Types

The Visual Basic data types are:

| Type                                     | Length                   | Comment                                                                                                                                                                                                          |
| ---------------------------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Byte                                     | 1 byte                   | `0` to `255`                                                                                                                                                                                                     |
| Boolean                                  | 2 bytes                  | `True` or `False`                                                                                                                                                                                                |
| Integer                                  | 2 bytes                  | `-32,768` to `32,767`                                                                                                                                                                                            |
| Long (long int)                          | 4 bytes                  | `-2,147,483,648` to `2,147,483,647`                                                                                                                                                                              |
| Single (single-precision floating-point) | 4 bytes                  | `-3.402823E38` to `-1.401298E-45`; `1.401298E-45` to `3.402823E38`                                                                                                                                               |
| Double (double-precision floating-point) | 8 bytes                  | `-1.79769313486231E308` to `-4.94065645841247E-324`; `4.94065645841247E-324` to `1.79769313486232E308`                                                                                                           |
| Currency (scaled integer)                | 8 bytes                  | `-922,337,203,685,477.5808` to `922,337,203,685,477.5807`                                                                                                                                                        |
| Decimal                                  | 14 bytes                 | `+/-79,228,162,514,264,337,593,543,950,335` with no decimal point; `+/-7.9228162514264337593543950335` with 28 places to the right of the decimal; smallest non-zero number is +/-0.0000000000000000000000000001 |
| Date                                     | 8 bytes                  | `January 1, 100` to `December 31, 9999`                                                                                                                                                                          |
| Object                                   | 4 bytes                  | Any Object reference                                                                                                                                                                                             |
| String (variable-length)                 | 10 bytes + string length | `0` to approximately `2 billion`                                                                                                                                                                                 |
| String (fixed-length)                    | Length of string         | `1` to approximately `65,400`                                                                                                                                                                                    |
| Variant                                  | 16 bytes                 | /                                                                                                                                                                                                                |

Compared to C lang, VB lacks the concept of `unsigned int` and `unsigned long`.

#### The Variant Type

**Variant** type is capable of holding any of the specific data types, including arrays.

#### The Boolean Type

**Booleans** can be assigned or tested for the pre-defined values `True` and `False`. `False` is defined to have the value `0`, and `True` is defined to be a unary Not False that is `-1`.

VB evaluates logical expressions according to the same rule as C, non-
zero is `True` and zero is `False`. But **never** get in the habit of thinking that `True` has the value `1`.

#### The Object Type and Pointers

**Object** type is frequently used in VB program.

The **pointer** is not explicitly present in the VB language. But in fact, variables whose type is Object are, references (a.k.a. pointers) to objects.

Both will be introduce in the following chapters.

#### Type Conversion and Casting

There is a rich set of type conversion functions for the
fundamental types in VB:

- `CByte` : Convert to a byte
- `CCur` : Convert to a currency
- `CDate` : Convert to a date
- `CDbl` : Convert to a double
- `CDec` : Convert to a decimal
- `CInt` : Convert to an integer
- `CLng` : Convert to a long
- `CSng` : Convert to a single
- `CStr` : Convert to a string
- `CVar` : Convert to a variant

Also there are several additional math functions that manipulate numbers:

- `Fix` : Truncate
- `Int` : Truncate, with different handling of negative numbers than Fix
- `Round` : Round, to a selectable number of decimal places
- `\`: Perform integer division. (The regular division operator performs a floating point division)

We can also try out type conversion in the IDE's Immediate Window before writing into program, which may avoid some mismatch errors.

### Variables

#### Variable Declaration

Variable declarations are **optional** in VB. But we can prevent VB from auto-declaring variant variables if we don't like this feature, by adding the following construct at the top of every file:

```vbscript
Option Explicit
```

It forces VB to complain about variables that haven't been declared. We can also set the value to `True` in `Tools` - `Options` - `Editor` - `Require Variable Declaration` to cause `Option Explicit` to be inserted automatically in new files.

Variables are declared with the **Dim** (dimension) keyword as follows:

```vbscript
Dim x As Integer
```

Noted that module-level variables are suggested to declare at the top of the module. The feature of `Option Explicit` only requires you to dim the variable, but does not require the type (and the type is assumed to be variant).

And be careful that VB does not have a way to declare multiple variables of the same type. Each variable must be separately declared and typed. For example, `Dim x, y As Integer` will creates a variant variable `x` and an integer variable `y`.

#### Variable Scope

Variables which declared at the top of a module are **global** to that module, also **global** to the program. Variables which declared in the body of a function/subroutine, are **private** to that procedure.

We can create project-global variables by using the **Public** keyword rather than Dim when you declare the variable. And in contrast, we can create a module scope variable by using the **Private** keyword.

```vbscript
Public g_var As Integer
Private p_var As Integer
```

Noted that **Dim** can be omitted in both usage. The `extern` keyword has no equivalent in VB, rather in C lang.

In summary, we can use Public and Private for all module-level declarations, and use Dim for all procedure-level declarations.

### Arrays

VB allows static/dynamic arrays of any type and with any number of dimensions. Arrays can be resized at runtime.

#### Declaration of Arrays

The syntax of for declaring an unsized array is as follows:

```vbscript
Dim x() As Long 'undimensioned
```

Sizing and resizing of the array can be done at runtime with the **ReDim** function. We can ReDim with the `Preserve` attribute in order to preserve the array content while making it larger. The `Erase` statement can be used to clear a fixed array of any type, also release storage of dynamically ReDim'd arrays.

VB has a flexible syntax for describing how we want to index an array:

```vbscript
Dim x(5) As Long 'dimension an array of 6 elements
Dim x(1 To 5) As Long '5 elements from 1 to 5, more prefer
Dim y(100 To 200) As String 'legal index values range from 100 to 200
```

#### Multiple Dimension Arrays

We can declare an array to have as many dimensions. For example, a
declaration for a 2 dimension array of Longs:

```vbscript
Dim x(1 To 5, 1 To 10) As Long
```

#### Variant Arrays

