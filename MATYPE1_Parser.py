# The MATYPE byte is broken up into bits.
# This parser will get the information from the byte


class MATYPE1_MASK:
    def __init__(self):
        self._MATYPE_BITS = 8
        self._TS_GS_BIT_POSITION = 0
        self._TS_GS_BITS = 2
        self._TS_GS_MASK = int('11000000', 2)

        self._SIS_MIS_BIT_POSITION = 2
        self._SIS_MIS_BITS = 1
        self._SIS_MIS_MASK = int('00100000', 2)

        self._CCM_ACM_BIT_POSITION = 3
        self._CCM_ACM_BITS = 1
        self._CCM_ACM_MASK = int('00010000', 2)

        self._ISSYI_BIT_POSITION = 4
        self._ISSYI_BITS = 1
        self._ISSYI_MASK = int('00001000', 2)

        self._NPD_BIT_POSITION = 5
        self._NPD_BITS = 1
        self._NPD_MASK = int('00000100', 2)

        self._RO_BIT_POSITION = 6
        self._RO_BITS = 2
        self._RO_MASK = int('00000011', 2)
    
    def mask_bits(self, number, number_bits, mask, bit_position, number_of_bits):
        return (mask & number) >> (number_bits - bit_position - number_of_bits)

    def get_TS_GS(self, MATYPE_INT):
        return self._mask_bits(MATYPE_INT, self._MATYPE_BITS, self._TS_GS_MASK, self._TS_GS_BIT_POSITION, self._TS_GS_BITS)
    
    def get_SIS_MIS(self, MATYPE_INT):
        return self._mask_bits(MATYPE_INT, self._MATYPE_BITS, self._SIS_MIS_MASK, self._SIS_MIS_BIT_POSITION, self._SIS_MIS_BITS)
    
    def get_CCM_ACM(self, MATYPE_INT):
        return self._mask_bits(MATYPE_INT, self._MATYPE_BITS, self._CCM_ACM_MASK, self._CCM_ACM_BIT_POSITION, self._CCM_ACM_BITS)
    
    def get_ISSYI(self, MATYPE_INT):
        return self._mask_bits(MATYPE_INT, self._MATYPE_BITS, self._CCM_ACM_MASK, self._CCM_ACM_BIT_POSITION, self._CCM_ACM_BITS)
    
    def get_NPD(self, MATYPE_INT):
        return self._mask_bits(MATYPE_INT, self._MATYPE_BITS, self._NPD_MASK, self._NPD_BIT_POSITION, self._NPD_BITS)
    
    def get_RO(self, MATYPE_INT):
        return self._mask_bits(MATYPE_INT, self._MATYPE_BITS, self._RO_MASK, self._RO_BIT_POSITION, self._RO_BITS)
    
    