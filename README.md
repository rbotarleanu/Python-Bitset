
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Python-BitSet](#python-bitset)
  - [Description](#description)
  - [Methods](#methods)
      - [BitSet(n_bits)](#bitsetn_bits)
      - [set([position], [value=1])](#setposition-value1)
      - [reset([position])](#resetposition)
      - [flip([position])](#flipposition)
      - [\_\_getitem\_\_(position)](#__getitem__position)
  - [Example](#example)

<!-- /code_chunk_output -->

# Python-BitSet

## Description
Lightweight implementation of a C++ like "bitset" class, which provides a
memory efficient method of storing bit data.

## Methods

#### BitSet(n_bits)
- constructs a bitset with a capacity of n_bits.

#### set([position], [value=1])
- set all bits to 1 if no argument is provided.
- set the bit at *position* to *value*

#### reset([position])
- set all bits to 0 if no argument is provided.
- set the bit at *position* to 0.

#### flip([position])
- Flips the value of the bit at position.
- If position is -1, all bits are flipped.

#### \_\_getitem\_\_(position)
- overloads the "[]" operator and allows for selecting the value of a bit at
a position.

## Example

```python
bs = BitSet(7)  # 0000000
bs.set()  # 1111111
bs.flip()  # 0000000
bs.set(0, 1)  # 1000000
bs.set(5, 1)  # 1000010
bs.flip(3)  # 1001010
bit_value = bs[3]  # 1
```