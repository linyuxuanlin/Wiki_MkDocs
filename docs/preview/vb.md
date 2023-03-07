## Project Organization

A Visual Basic project is organized around three primary types of files: **Forms**, **Modules**, and **Classes**. Forms normally contain interactive UI (i.e. TextBox, Button, Picture).

## Data Types

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


