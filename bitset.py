from math import ceil


class BitSet:
    """
    A lightweight bitset class which can hold a fixed-size idx of bits in a
    memory-efficient manner.

    Methods
    -------
    set(position=-1, value=1)
        Set either all bits (when position is -1) or a certain bit
        (position>=0) to value.
    
    reset(position=-1)
        Set all bits (when position is -1) or the position bit to 0.

    flip(position=-1)
        Flips the value of the bit at *position*. If *position* is -1, all bits
        are flipped.
    
    Example
    -------

        bs = BitSet(7)  # 0000000
        bs.set()  # 1111111
        bs.flip()  # 0000000
        bs.set(0, 1)  # 1000000
        bs.set(5, 1)  # 1000010
        bs.flip(3)  # 1001010
        bit_value = bs[3]  # 1
    """

    __INT_SIZE = 32
    __ALL_SET = (1 << 32) - 1
    __ALL_CLEAR = 0

    def __init__(self, n_bits):
        self.n_bits = n_bits
        self.__bits = [self.__ALL_CLEAR
                       for _ in range(self.__idx_of_idxs_needed(n_bits))]

    def __number_of_integers_needed(self, n_bits):
        """
        Computes the number of integers required to store n_bits.

        Parameters
        ----------
        n_bits: int
            the number of bits to be stored.
        """

        return int(ceil(n_bits / self.__INT_SIZE))

    def __index_bit_in_bitset(self, position):
        """
        Computes the index in the bitset array that holds the *position* bit.

        Parameters
        ----------
        position: int
            the position of the bit in the bitset.

        Returns
        -------
        tuple
            the index of the corresponding idx in the bitset array and the
            index of the bit in that idx.
        """
        return divmod(position, self.__INT_SIZE)

    def __clear(self, idx, bit):
        """
        Clears the value of the *bit* bit of the *idx* integer.

        Parameters
        ----------
        idx: int
            index of the integer in the array holding the bits.
        bit: int
            index of the bit of that integer
        """
        if bit < 0 or bit > self.n_bits:
            raise ValueError("Bit position should not exceed BitSet capacity.")
        self.__bits[idx] &= ~(1 << bit)

    def __set(self, idx, bit):
        """
        Sets the value of the *bit* bit of the *idx* integer.

        Parameters
        ----------
        idx: int
            index of the integer in the array holding the bits.
        bit: int
            index of the bit of that integer
        """
        if bit < 0 or bit > self.n_bits:
            raise ValueError("Bit position should not exceed BitSet capacity.")

        self.__bits[idx] |= (1 << bit)

    def __flip(self, idx, bit):
        """
        Flips the value of the *bit* bit of the *idx* integer. As such, 0
        becomes 1 and vice-versa.

        Parameters
        ----------
        idx: int
            index of the integer in the array holding the bits.
        bit: int
            index of the bit of that integer
        """
        if bit < 0 or bit > self.n_bits:
            raise ValueError("Bit position should not exceed BitSet capacity.")

        self.__bits[idx] ^= (1 << bit)

    def __get(self, idx, bit):
        """
        Gets the value of the *bit* bit of the *idx* integer.

        Parameters
        ----------
        idx: int
            index of the integer in the array holding the bits.
        bit: int
            index of the bit of that integer
        """
        if bit < 0 or bit > self.n_bits:
            raise ValueError("Bit position should not exceed BitSet capacity.")

        return int(self.__bits[idx] & (1 << bit) > 0)

    def set(self, position=-1, value=1):
        """
        Sets the bit at *position* to *value*.
        If *position* is -1, all bits are set to *value*.

        Parameters
        ----------
        position: int
            the position at which to perform the set operation.
        value: int
            the value to use when setting the bit.
        """

        if position == -1:
            mask = self.__ALL_SET if value == 1 else self.__ALL_CLEAR
            for i in range(len(self.__bits)):
                self.__bits[i] = mask
        else:
            idx, bit = self.__index_bit_in_bitset(position)
            if bit < 0 or bit > self.n_bits:
                raise ValueError("Bit position should not exceed BitSet "
                                 "capacity.")

            if value == 1:
                self.__set(idx, bit)
            else:
                self.__clear(idx, bit)

    def reset(self, position=-1):
        """
        Resets the bit at *position* to 0.
        If *position* is -1, all bits are set to 0.

        Parameters
        ----------
        position: int
            the position at which to perform the set operation.
        """

        self.set(position, value=0)

    def __flip_all(self):
        """
        Flips the values of all bits in the bitset.
        """
        for i in range(len(self.__bits)):
            self.__bits[i] ^= self.__ALL_SET

    def flip(self, position=-1):
        """
        Flips the bit at *position* such that 0 becomes 1 and vice-versa.
        If *position* is -1, all bits are flippsed.

        Parameters
        ----------
        position: int
            the position at which to perform the set operation.
        """

        if position == -1:
            self.__flip_all()
            return 

        idx, bit = self.__index_bit_in_bitset(position)
        if bit < 0 or bit > self.n_bits:
            raise ValueError("Bit position should not exceed BitSet capacity.")

        self.__flip(idx, bit)

    def __getitem__(self, position):
        idx, bit = self.__index_bit_in_bitset(position)
        if bit < 0 or bit > self.n_bits:
            raise ValueError("Bit position should not exceed BitSet capacity.")

        return self.__get(idx, bit)

    def __int_to_bitstring(self, idx):
        """
        Converts the integer at position idx to a string of 0's and 1's.

        Parameters
        ----------
        idx: int
            an index in the __bits array.
        
        Returns
        -------
        str
            a string of 1's and 0's
        """
        bitstring = ""
        for i in range(0, self.__INT_SIZE):
            if idx == len(self.__bits) - 1 and \
                    i >= self.n_bits % self.__INT_SIZE:
                break
            bitstring += str(self.__get(idx, i))
        
        return bitstring[:self.n_bits]

    def __str__(self):
        s = ""

        for i in range(len(self.__bits)):
            s += self.__int_to_bitstring(i)

        return s
