marks = 14
# there are very few number methods

# as_integer_ratio() 
print(marks.as_integer_ratio()) # return the ratio of the number with its denominator in Tuple form (We will talk about tuple later )
# The as_integer_ratio() method is typically used with numeric types like floats. It's a useful method when you need to represent a floating-point number as a ratio of two integers. the float is written like this 5.556


# conjugate()

 # return the complex conjugate of the complex number like
complexd = 4-3j

print(complexd.conjugate()) # return the complex conjugate of the complex number like 

# fromhex()
# Example using float.fromhex()
hex_str = "0x1.47ae147ae147ap+0"  # Hexadecimal representation of a float
float_val = float.fromhex(hex_str) # fromhex() return a new data so you can store it in any variable
print(float_val)  # Output: 3.141592653589793

# NOTE IMPORTANT : PLEASE LEARN IMMUTABLE AND MUTABLE DATATYPES IN THE NEXT FOLDER

# marks.hex() return a hexadecimal representation of the floating point number

print(marks.hex()) # return a hexadecimal representation of the floating point number


#marks.imag returns the imaginary part of the complex number

print(complexd.imag) # return the imaginary part of the complex number


# marks.is_integer() return True if the the data is number and false if not

# [NOTE : THE MARKS CAN BE ANY NUMBER DATA TYPE WITH ANOTHER NAME LIKE superman = 56 , hero = 0]


# marks.real returns the real part of the complex number

print(complexd.real) # return the real part 
marks.bit_count() # return the bit count 
marks.bit_length() # return the bit length 
marks.to_bytes() # return the bytes 

# YOU CAN LEARN MORE BY GOOGLING


# math library
# math library in python is very used

import math # importing math library
print(math.pi) # return the PI value
print(math.e) # # Print the value of the mathematical constant 'e' , # Output: 2.718281828459045

print(math.sin(math.pi/2))
print(math.cos(math.pi/2))

# more methods in math library
