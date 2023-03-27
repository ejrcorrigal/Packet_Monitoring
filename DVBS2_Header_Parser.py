# This will contain the DVBS2 UDP packet header parsing
# Look on page 3-4 of the attached DVB pdf attached in this repo for a good description of the Baseband Header (BBHEADER) description

# DVBS2 BBHEADER contains the following:
#   BBHEADER is 10-bytes long
#   The first byte corresponds to the MATYPE-1:
#       Within this byte contains info about general 
#       -TS/GS field (2-bits): Transport Stream Input or Generic Stream Input (packetised or continuous)
#       -SIS/MIS field (1 bit): Single Input Stream of Multiple Input stream
#       -CCM/ACM feild (1-bit): Constant COding and Modulation or Adaptive Coding and Modulation (VCM is signaled as ACM)
#       -ISSYI (1-bit): (Input Stream Synchronization Indicator) Not active in our case.
#       -NPD (1-bit): Null-Packet deletion active/not active.  Always non active in out case.
#       -RO (2-bits): Transmission Roll-off factor (alpha).  Three values are possible among 0.35, 0.25, and 0.2.
#   The second byte corrseponds to the MATYPE-2:
#       If SIS/MIS = Multiple Input Stream, then the second byte=Input Stream Identifier (ISI); else second byte reserved.
#   The third and fourth bytes corresponds to UPL: User packet Length in bits [0, 65535]
#   The fifth and sixth bytes correspond to the DFL: Data Field Length.  There is a link between the DFL and the chosen code rate.
#   The seventh byte corresponds to SYNC: Copy of the User Packet Sync-byte, not used in generic continuous stream mode.
#   The eighth and ninth byte correspond to the SYNCD: Distance in bits from the beginning of the DATA FIELD and the first UserPacket from this frame (first bit of the CRC-8). 
#   The last byte corresponds to CRC-8: not ised for generic continuous stream.
#
# The BBHEADER transmission order is byte by byte from the MSB of the TS/GS field.

class DVBS2_Packet_Parser:
    def __init__(self):
        self._BBHEADER_BYTES = 10

        self._MATYPE1_BYTE_POSITION = 0
        self._MATYPE1_BYTES = 1

        self._MATYPE2_BYTE_POSITION = 1
        self._MATYPE2_BYTES = 1

        self._UPL_BYTE_POSITION = 2
        self._UPL_BYTES = 2

        self._DFL_BYTE_POSITION = 4
        self._DFL_BYTES = 2

        self._SYNC_BYTE_POSITION = 6
        self._SYNC_BYTES = 1

        self._SYNCD_BYTE_POSITION = 7
        self._SYNCD_BYTES = 2

        self._CRC8_BYTE_POSITION = 9
        self._CRC8_BYTES = 1

    def get_specified_bytes(self, byte_array, start_byte, number_of_bytes):
        end_index = start_byte + number_of_bytes - 1:
        output = False
        if end_index <= len(byte_array):
                output = byte_array[start_byte:start_byte + number_of_bytes]
        return output
    
    def get_BBHEADER_and_payload(self, packet_bytes):
        BBHEADER_byte_array = False
        payload_byte_array = False
        
        BBHEADER_byte_array = packet_bytes[0: self._BBHEADER_BYTES]
        payload_byte_array = packet_bytes[self._BBHEADER_BYTES:]

        return BBHEADER_byte_array, payload_byte_array

    def get_BBHEADER_MATYPE1(self, BBHEADER):
        return self.get_specified_bytes(BBHEADER, self._MATYPE1_BYTE_POSITION, self._MATYPE1_BYTES)
    
    def get_BBHEADER_MATYPE2(self, BBHEADER):
        return self.get_specified_bytes(BBHEADER, self._MATYPE2_BYTE_POSITION, self._MATYPE2_BYTES)
    
    def get_BBHEADER_UPL(self, BBHEADER):
        return self.get_specified_bytes(BBHEADER, self._UPL_BYTE_POSITION, self._UPL_BYTES)
    
    def get_BBHEADER_DFL(self, BBHEADER):
        return self.get_specified_bytes(BBHEADER, self._DFL_BYTE_POSITION, self._DFL_BYTES)
    
    def get_BBHEADER_SYNC(self, BBHEADER):
        return self.get_specified_bytes(BBHEADER, self._SYNC_BYTE_POSITION, self._SYNC_BYTES)
    
    def get_BBHEADER_SYNCD(self, BBHEADER):
        return self.get_specified_bytes(BBHEADER, self._SYNCD_BYTE_POSITION, self._SYNCD_BYTES)
    
    def get_CRC8(self, BBHEADER):
        return self.get_specified_bytes(BBHEADER, self._CRC8_BYTE_POSITION, self._CRC8_BYTES)
    

