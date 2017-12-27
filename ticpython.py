import os
import ctypes
from ctypes import *

#Modifying sys.path doesn't affect where windows searches for DLLs, so instead we have to append to the environment path.
os.environ['PATH'] = os.environ['PATH'] + 'C:/msys64/mingw64/bin'.replace('/','\\')+';'

#Load tic library
libtic = windll.LoadLibrary('libpololu-tic-1')

#Initialize functions and specify ctypes argtypes:
tic_list_connected_devices = libtic.tic_list_connected_devices
tic_device_get_serial_number = libtic.tic_device_get_serial_number
tic_error_get_message = libtic.tic_error_get_message
tic_error_free = libtic.tic_error_free

#Specify arguments and return types so that ctypes takes care of conversions
tic_list_connected_devices.argtypes = [POINTER(POINTER(POINTER(c_void_p))),POINTER(c_size_t)]
tic_list_connected_devices.restype = c_void_p

tic_device_get_serial_number.argtypes = [POINTER(c_void_p),]
tic_device_get_serial_number.restype = c_char_p

tic_error_get_message.argtypes = [POINTER(c_void_p),]
tic_error_get_message.restype = c_char_p

tic_error_free.argtypes = [POINTER(c_void_p),]
tic_error_free.restype = None

#Initialize empty ctypes variables to pass to function:
devcount = c_size_t()
mem = POINTER(POINTER(c_void_p))()

#Call function (1 tic device connected to computer)
terr = tic_list_connected_devices(byref(mem),byref(devcount))

#Verify function worked by checking serial number and devcount (serial number agrees with output of ticgui)

devcount
#returns: c_ulonglong(1)

tic_device_get_serial_number(mem[0])
#returns: b'00201645'


tic_error_get_message(terr)
#returns b'No error.'

tic_error_free(terr)

#In this case, terr was actually 'None' because list_connected_devices returned a null pointer indicating no error.