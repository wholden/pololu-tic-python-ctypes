# pololu-tic-python-ctypes

Exploring the possibility of using ctypes and Python to control Pololu Tic stepper motor drivers (https://github.com/pololu/pololu-tic-software).  This was a quick attempt and was mainly a learning exercise to figure out how to interface ctypes with a DLL from a c-library.

#### Main lessons learned:
- To load DLLs, modifying sys.path doesn't work.  The environment path has to be modified.  In particular, if DLLs need to access other DLLs in the same folder, specifying the path in LoadLibrary is also insufficient, because it can't locate the other DLL.
  - solution: ```os.environ['PATH'] = os.environ['PATH'] + 'C:/msys64/mingw64/bin'.replace('/','\\')+';'```
- In ctypes, reading the documentation (https://docs.python.org/3/library/ctypes.html) makes you think (at least it made me think) that you have to specify a structure completely to be able to pass it into a c-library function.  This is not true.  
  - If you want to be able to access the members of the structure, you have to specify them as ```_fields_```.  
  - If you just need to pass generic pointers to structures with unknown contents, you can use a ```c_void_p``` in place of the structure.  Although it's probably better to just create an empty ctypes Structure class.
