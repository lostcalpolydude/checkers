import base64

def long_to_base64(value):
   rval  = ''
   value = long(value)
   while value > 0:
      rval += chr(value & 255)
      value = value >> 8
   return base64.urlsafe_b64encode(rval)

def base64_to_long(str):
   rval = 0
   str = base64.urlsafe_b64decode(str)
   for i in range(0,len(str)):
      rval |= (ord(str[i]) << i*8)
   return long(rval)

def get_hash_bits(hash_long, offset, bits_per_offset):
   pos = offset * bits_per_offset
   maskval = (2**bits_per_offset) - 1
   mask = long(maskval << pos)
   return ((hash_long & mask) >> pos)

def set_hash_bits(hash_long, offset, bits_per_offset, val):
   pos = offset * bits_per_offset
   maskval = (2**bits_per_offset) - 1
   val &= maskval
   mask = ~long(maskval << pos)
   hash_long &= mask
   hash_long |= (val << pos)
   return hash_long
