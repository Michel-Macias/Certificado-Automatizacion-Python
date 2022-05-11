# Modulo OS de Python


```python
import os
```

### Usamos la función dir() para que nos muestre todos los metodos de los que disponemos para este modulo OS


```python
print(dir(os))
```

    ['CLD_CONTINUED', 'CLD_DUMPED', 'CLD_EXITED', 'CLD_TRAPPED', 'DirEntry', 'EX_CANTCREAT', 'EX_CONFIG', 'EX_DATAERR', 'EX_IOERR', 'EX_NOHOST', 'EX_NOINPUT', 'EX_NOPERM', 'EX_NOUSER', 'EX_OK', 'EX_OSERR', 'EX_OSFILE', 'EX_PROTOCOL', 'EX_SOFTWARE', 'EX_TEMPFAIL', 'EX_UNAVAILABLE', 'EX_USAGE', 'F_LOCK', 'F_OK', 'F_TEST', 'F_TLOCK', 'F_ULOCK', 'GRND_NONBLOCK', 'GRND_RANDOM', 'MFD_ALLOW_SEALING', 'MFD_CLOEXEC', 'MFD_HUGETLB', 'MFD_HUGE_16GB', 'MFD_HUGE_16MB', 'MFD_HUGE_1GB', 'MFD_HUGE_1MB', 'MFD_HUGE_256MB', 'MFD_HUGE_2GB', 'MFD_HUGE_2MB', 'MFD_HUGE_32MB', 'MFD_HUGE_512KB', 'MFD_HUGE_512MB', 'MFD_HUGE_64KB', 'MFD_HUGE_8MB', 'MFD_HUGE_MASK', 'MFD_HUGE_SHIFT', 'MutableMapping', 'NGROUPS_MAX', 'O_ACCMODE', 'O_APPEND', 'O_ASYNC', 'O_CLOEXEC', 'O_CREAT', 'O_DIRECT', 'O_DIRECTORY', 'O_DSYNC', 'O_EXCL', 'O_LARGEFILE', 'O_NDELAY', 'O_NOATIME', 'O_NOCTTY', 'O_NOFOLLOW', 'O_NONBLOCK', 'O_PATH', 'O_RDONLY', 'O_RDWR', 'O_RSYNC', 'O_SYNC', 'O_TMPFILE', 'O_TRUNC', 'O_WRONLY', 'POSIX_FADV_DONTNEED', 'POSIX_FADV_NOREUSE', 'POSIX_FADV_NORMAL', 'POSIX_FADV_RANDOM', 'POSIX_FADV_SEQUENTIAL', 'POSIX_FADV_WILLNEED', 'POSIX_SPAWN_CLOSE', 'POSIX_SPAWN_DUP2', 'POSIX_SPAWN_OPEN', 'PRIO_PGRP', 'PRIO_PROCESS', 'PRIO_USER', 'P_ALL', 'P_NOWAIT', 'P_NOWAITO', 'P_PGID', 'P_PID', 'P_WAIT', 'PathLike', 'RTLD_DEEPBIND', 'RTLD_GLOBAL', 'RTLD_LAZY', 'RTLD_LOCAL', 'RTLD_NODELETE', 'RTLD_NOLOAD', 'RTLD_NOW', 'RWF_DSYNC', 'RWF_HIPRI', 'RWF_NOWAIT', 'RWF_SYNC', 'R_OK', 'SCHED_BATCH', 'SCHED_FIFO', 'SCHED_IDLE', 'SCHED_OTHER', 'SCHED_RESET_ON_FORK', 'SCHED_RR', 'SEEK_CUR', 'SEEK_DATA', 'SEEK_END', 'SEEK_HOLE', 'SEEK_SET', 'ST_APPEND', 'ST_MANDLOCK', 'ST_NOATIME', 'ST_NODEV', 'ST_NODIRATIME', 'ST_NOEXEC', 'ST_NOSUID', 'ST_RDONLY', 'ST_RELATIME', 'ST_SYNCHRONOUS', 'ST_WRITE', 'TMP_MAX', 'WCONTINUED', 'WCOREDUMP', 'WEXITED', 'WEXITSTATUS', 'WIFCONTINUED', 'WIFEXITED', 'WIFSIGNALED', 'WIFSTOPPED', 'WNOHANG', 'WNOWAIT', 'WSTOPPED', 'WSTOPSIG', 'WTERMSIG', 'WUNTRACED', 'W_OK', 'XATTR_CREATE', 'XATTR_REPLACE', 'XATTR_SIZE_MAX', 'X_OK', '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_check_methods', '_execvpe', '_exists', '_exit', '_fspath', '_fwalk', '_get_exports_list', '_putenv', '_spawnvef', '_unsetenv', '_wrap_close', 'abc', 'abort', 'access', 'altsep', 'chdir', 'chmod', 'chown', 'chroot', 'close', 'closerange', 'confstr', 'confstr_names', 'copy_file_range', 'cpu_count', 'ctermid', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'environb', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fchdir', 'fchmod', 'fchown', 'fdatasync', 'fdopen', 'fork', 'forkpty', 'fpathconf', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fstatvfs', 'fsync', 'ftruncate', 'fwalk', 'get_blocking', 'get_exec_path', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getegid', 'getenv', 'getenvb', 'geteuid', 'getgid', 'getgrouplist', 'getgroups', 'getloadavg', 'getlogin', 'getpgid', 'getpgrp', 'getpid', 'getppid', 'getpriority', 'getrandom', 'getresgid', 'getresuid', 'getsid', 'getuid', 'getxattr', 'initgroups', 'isatty', 'kill', 'killpg', 'lchown', 'linesep', 'link', 'listdir', 'listxattr', 'lockf', 'lseek', 'lstat', 'major', 'makedev', 'makedirs', 'memfd_create', 'minor', 'mkdir', 'mkfifo', 'mknod', 'name', 'nice', 'open', 'openpty', 'pardir', 'path', 'pathconf', 'pathconf_names', 'pathsep', 'pipe', 'pipe2', 'popen', 'posix_fadvise', 'posix_fallocate', 'posix_spawn', 'posix_spawnp', 'pread', 'preadv', 'putenv', 'pwrite', 'pwritev', 'read', 'readlink', 'readv', 'register_at_fork', 'remove', 'removedirs', 'removexattr', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sched_get_priority_max', 'sched_get_priority_min', 'sched_getaffinity', 'sched_getparam', 'sched_getscheduler', 'sched_param', 'sched_rr_get_interval', 'sched_setaffinity', 'sched_setparam', 'sched_setscheduler', 'sched_yield', 'sendfile', 'sep', 'set_blocking', 'set_inheritable', 'setegid', 'seteuid', 'setgid', 'setgroups', 'setpgid', 'setpgrp', 'setpriority', 'setregid', 'setresgid', 'setresuid', 'setreuid', 'setsid', 'setuid', 'setxattr', 'spawnl', 'spawnle', 'spawnlp', 'spawnlpe', 'spawnv', 'spawnve', 'spawnvp', 'spawnvpe', 'st', 'stat', 'stat_result', 'statvfs', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sync', 'sys', 'sysconf', 'sysconf_names', 'system', 'tcgetpgrp', 'tcsetpgrp', 'terminal_size', 'times', 'times_result', 'truncate', 'ttyname', 'umask', 'uname', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'wait', 'wait3', 'wait4', 'waitid', 'waitid_result', 'waitpid', 'walk', 'write', 'writev']


### get_exec_path()---> lista de str con los path que contienen ejecutables


```python
print(dir(os.get_exec_path))
```

    ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']



```python
print(os.get_exec_path())
```

    ['/home/michelle/.local/bin', '/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin', '/usr/games', '/usr/local/games', '/snap/bin']


## getsize()

#### Función .getsize() nos devuelve el tamaño en bits (int)


```python
print('OS.CHDIR()')
print(dir(os.chdir))
print('------------------------------------------------------------------------------------------------------------------')
print('OS.PATH.GETSIZE()')
print(dir(os.path.getsize))
```

    OS.CHDIR()
    ['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']
    ------------------------------------------------------------------------------------------------------------------
    OS.PATH.GETSIZE()
    ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']



```python
os.chdir('/home/michelle/FORMACION/GOOGLE/CuadernosJupyter/')
os.path.getsize('strings.py')
```




    2613



## getmtime()

#### getmtime() nos devuelve en segundos la fecha desde el 1 de enero de 1970, en la que se hizo la ultima modificacion en el file. El formato de salida es en un 'timestamp' que es una marca de tiempo de Unix.


```python
print(dir(os.path.getmtime))
```

    ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']



```python
os.path.getmtime('strings.py')
```




    1651346238.0074563



# Modulo datetime en Python

### Hacemos uso de este modulo para pasar a formato entendible por los humanos el 'timestamp' devuelto por getmtime()


```python
import datetime
```


```python
print(dir(datetime))
```

    ['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']


### Podemos ver a traves de help() la documentacion de cada modulo y función


```python
help(datetime)
```

    Help on module datetime:
    
    NAME
        datetime - Fast implementation of the datetime type.
    
    MODULE REFERENCE
        https://docs.python.org/3.8/library/datetime
        
        The following documentation is automatically generated from the Python
        source files.  It may be incomplete, incorrect or include features that
        are considered implementation detail and may vary between Python
        implementations.  When in doubt, consult the module reference at the
        location listed above.
    
    CLASSES
        builtins.object
            date
                datetime
            time
            timedelta
            tzinfo
                timezone
        
        class date(builtins.object)
         |  date(year, month, day) --> date object
         |  
         |  Methods defined here:
         |  
         |  __add__(self, value, /)
         |      Return self+value.
         |  
         |  __eq__(self, value, /)
         |      Return self==value.
         |  
         |  __format__(...)
         |      Formats self with strftime.
         |  
         |  __ge__(self, value, /)
         |      Return self>=value.
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __gt__(self, value, /)
         |      Return self>value.
         |  
         |  __hash__(self, /)
         |      Return hash(self).
         |  
         |  __le__(self, value, /)
         |      Return self<=value.
         |  
         |  __lt__(self, value, /)
         |      Return self<value.
         |  
         |  __ne__(self, value, /)
         |      Return self!=value.
         |  
         |  __radd__(self, value, /)
         |      Return value+self.
         |  
         |  __reduce__(...)
         |      __reduce__() -> (cls, state)
         |  
         |  __repr__(self, /)
         |      Return repr(self).
         |  
         |  __rsub__(self, value, /)
         |      Return value-self.
         |  
         |  __str__(self, /)
         |      Return str(self).
         |  
         |  __sub__(self, value, /)
         |      Return self-value.
         |  
         |  ctime(...)
         |      Return ctime() style string.
         |  
         |  isocalendar(...)
         |      Return a 3-tuple containing ISO year, week number, and weekday.
         |  
         |  isoformat(...)
         |      Return string in ISO 8601 format, YYYY-MM-DD.
         |  
         |  isoweekday(...)
         |      Return the day of the week represented by the date.
         |      Monday == 1 ... Sunday == 7
         |  
         |  replace(...)
         |      Return date with new specified fields.
         |  
         |  strftime(...)
         |      format -> strftime() style string.
         |  
         |  timetuple(...)
         |      Return time tuple, compatible with time.localtime().
         |  
         |  toordinal(...)
         |      Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.
         |  
         |  weekday(...)
         |      Return the day of the week represented by the date.
         |      Monday == 0 ... Sunday == 6
         |  
         |  ----------------------------------------------------------------------
         |  Class methods defined here:
         |  
         |  fromisocalendar(...) from builtins.type
         |      int, int, int -> Construct a date from the ISO year, week number and weekday.
         |      
         |      This is the inverse of the date.isocalendar() function
         |  
         |  fromisoformat(...) from builtins.type
         |      str -> Construct a date from the output of date.isoformat()
         |  
         |  fromordinal(...) from builtins.type
         |      int -> date corresponding to a proleptic Gregorian ordinal.
         |  
         |  fromtimestamp(timestamp, /) from builtins.type
         |      Create a date from a POSIX timestamp.
         |      
         |      The timestamp is a number, e.g. created via time.time(), that is interpreted
         |      as local time.
         |  
         |  today(...) from builtins.type
         |      Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).
         |  
         |  ----------------------------------------------------------------------
         |  Static methods defined here:
         |  
         |  __new__(*args, **kwargs) from builtins.type
         |      Create and return a new object.  See help(type) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  day
         |  
         |  month
         |  
         |  year
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  max = datetime.date(9999, 12, 31)
         |  
         |  min = datetime.date(1, 1, 1)
         |  
         |  resolution = datetime.timedelta(days=1)
        
        class datetime(date)
         |  datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
         |  
         |  The year, month and day arguments are required. tzinfo may be None, or an
         |  instance of a tzinfo subclass. The remaining arguments may be ints.
         |  
         |  Method resolution order:
         |      datetime
         |      date
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __add__(self, value, /)
         |      Return self+value.
         |  
         |  __eq__(self, value, /)
         |      Return self==value.
         |  
         |  __ge__(self, value, /)
         |      Return self>=value.
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __gt__(self, value, /)
         |      Return self>value.
         |  
         |  __hash__(self, /)
         |      Return hash(self).
         |  
         |  __le__(self, value, /)
         |      Return self<=value.
         |  
         |  __lt__(self, value, /)
         |      Return self<value.
         |  
         |  __ne__(self, value, /)
         |      Return self!=value.
         |  
         |  __radd__(self, value, /)
         |      Return value+self.
         |  
         |  __reduce__(...)
         |      __reduce__() -> (cls, state)
         |  
         |  __reduce_ex__(...)
         |      __reduce_ex__(proto) -> (cls, state)
         |  
         |  __repr__(self, /)
         |      Return repr(self).
         |  
         |  __rsub__(self, value, /)
         |      Return value-self.
         |  
         |  __str__(self, /)
         |      Return str(self).
         |  
         |  __sub__(self, value, /)
         |      Return self-value.
         |  
         |  astimezone(...)
         |      tz -> convert to local time in new timezone tz
         |  
         |  ctime(...)
         |      Return ctime() style string.
         |  
         |  date(...)
         |      Return date object with same year, month and day.
         |  
         |  dst(...)
         |      Return self.tzinfo.dst(self).
         |  
         |  isoformat(...)
         |      [sep] -> string in ISO 8601 format, YYYY-MM-DDT[HH[:MM[:SS[.mmm[uuu]]]]][+HH:MM].
         |      sep is used to separate the year from the time, and defaults to 'T'.
         |      The optional argument timespec specifies the number of additional terms
         |      of the time to include. Valid options are 'auto', 'hours', 'minutes',
         |      'seconds', 'milliseconds' and 'microseconds'.
         |  
         |  replace(...)
         |      Return datetime with new specified fields.
         |  
         |  time(...)
         |      Return time object with same time but with tzinfo=None.
         |  
         |  timestamp(...)
         |      Return POSIX timestamp as float.
         |  
         |  timetuple(...)
         |      Return time tuple, compatible with time.localtime().
         |  
         |  timetz(...)
         |      Return time object with same time and tzinfo.
         |  
         |  tzname(...)
         |      Return self.tzinfo.tzname(self).
         |  
         |  utcoffset(...)
         |      Return self.tzinfo.utcoffset(self).
         |  
         |  utctimetuple(...)
         |      Return UTC time tuple, compatible with time.localtime().
         |  
         |  ----------------------------------------------------------------------
         |  Class methods defined here:
         |  
         |  combine(...) from builtins.type
         |      date, time -> datetime with same date and time fields
         |  
         |  fromisoformat(...) from builtins.type
         |      string -> datetime from datetime.isoformat() output
         |  
         |  fromtimestamp(...) from builtins.type
         |      timestamp[, tz] -> tz's local time from POSIX timestamp.
         |  
         |  now(tz=None) from builtins.type
         |      Returns new datetime object representing current time local to tz.
         |      
         |        tz
         |          Timezone object.
         |      
         |      If no tz is specified, uses local timezone.
         |  
         |  strptime(...) from builtins.type
         |      string, format -> new datetime parsed from a string (like time.strptime()).
         |  
         |  utcfromtimestamp(...) from builtins.type
         |      Construct a naive UTC datetime from a POSIX timestamp.
         |  
         |  utcnow(...) from builtins.type
         |      Return a new datetime representing UTC day and time.
         |  
         |  ----------------------------------------------------------------------
         |  Static methods defined here:
         |  
         |  __new__(*args, **kwargs) from builtins.type
         |      Create and return a new object.  See help(type) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  fold
         |  
         |  hour
         |  
         |  microsecond
         |  
         |  minute
         |  
         |  second
         |  
         |  tzinfo
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  max = datetime.datetime(9999, 12, 31, 23, 59, 59, 999999)
         |  
         |  min = datetime.datetime(1, 1, 1, 0, 0)
         |  
         |  resolution = datetime.timedelta(microseconds=1)
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from date:
         |  
         |  __format__(...)
         |      Formats self with strftime.
         |  
         |  isocalendar(...)
         |      Return a 3-tuple containing ISO year, week number, and weekday.
         |  
         |  isoweekday(...)
         |      Return the day of the week represented by the date.
         |      Monday == 1 ... Sunday == 7
         |  
         |  strftime(...)
         |      format -> strftime() style string.
         |  
         |  toordinal(...)
         |      Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.
         |  
         |  weekday(...)
         |      Return the day of the week represented by the date.
         |      Monday == 0 ... Sunday == 6
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from date:
         |  
         |  fromisocalendar(...) from builtins.type
         |      int, int, int -> Construct a date from the ISO year, week number and weekday.
         |      
         |      This is the inverse of the date.isocalendar() function
         |  
         |  fromordinal(...) from builtins.type
         |      int -> date corresponding to a proleptic Gregorian ordinal.
         |  
         |  today(...) from builtins.type
         |      Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors inherited from date:
         |  
         |  day
         |  
         |  month
         |  
         |  year
        
        class time(builtins.object)
         |  time([hour[, minute[, second[, microsecond[, tzinfo]]]]]) --> a time object
         |  
         |  All arguments are optional. tzinfo may be None, or an instance of
         |  a tzinfo subclass. The remaining arguments may be ints.
         |  
         |  Methods defined here:
         |  
         |  __eq__(self, value, /)
         |      Return self==value.
         |  
         |  __format__(...)
         |      Formats self with strftime.
         |  
         |  __ge__(self, value, /)
         |      Return self>=value.
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __gt__(self, value, /)
         |      Return self>value.
         |  
         |  __hash__(self, /)
         |      Return hash(self).
         |  
         |  __le__(self, value, /)
         |      Return self<=value.
         |  
         |  __lt__(self, value, /)
         |      Return self<value.
         |  
         |  __ne__(self, value, /)
         |      Return self!=value.
         |  
         |  __reduce__(...)
         |      __reduce__() -> (cls, state)
         |  
         |  __reduce_ex__(...)
         |      __reduce_ex__(proto) -> (cls, state)
         |  
         |  __repr__(self, /)
         |      Return repr(self).
         |  
         |  __str__(self, /)
         |      Return str(self).
         |  
         |  dst(...)
         |      Return self.tzinfo.dst(self).
         |  
         |  isoformat(...)
         |      Return string in ISO 8601 format, [HH[:MM[:SS[.mmm[uuu]]]]][+HH:MM].
         |      
         |      The optional argument timespec specifies the number of additional terms
         |      of the time to include. Valid options are 'auto', 'hours', 'minutes',
         |      'seconds', 'milliseconds' and 'microseconds'.
         |  
         |  replace(...)
         |      Return time with new specified fields.
         |  
         |  strftime(...)
         |      format -> strftime() style string.
         |  
         |  tzname(...)
         |      Return self.tzinfo.tzname(self).
         |  
         |  utcoffset(...)
         |      Return self.tzinfo.utcoffset(self).
         |  
         |  ----------------------------------------------------------------------
         |  Class methods defined here:
         |  
         |  fromisoformat(...) from builtins.type
         |      string -> time from time.isoformat() output
         |  
         |  ----------------------------------------------------------------------
         |  Static methods defined here:
         |  
         |  __new__(*args, **kwargs) from builtins.type
         |      Create and return a new object.  See help(type) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  fold
         |  
         |  hour
         |  
         |  microsecond
         |  
         |  minute
         |  
         |  second
         |  
         |  tzinfo
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  max = datetime.time(23, 59, 59, 999999)
         |  
         |  min = datetime.time(0, 0)
         |  
         |  resolution = datetime.timedelta(microseconds=1)
        
        class timedelta(builtins.object)
         |  Difference between two datetime values.
         |  
         |  timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
         |  
         |  All arguments are optional and default to 0.
         |  Arguments may be integers or floats, and may be positive or negative.
         |  
         |  Methods defined here:
         |  
         |  __abs__(self, /)
         |      abs(self)
         |  
         |  __add__(self, value, /)
         |      Return self+value.
         |  
         |  __bool__(self, /)
         |      self != 0
         |  
         |  __divmod__(self, value, /)
         |      Return divmod(self, value).
         |  
         |  __eq__(self, value, /)
         |      Return self==value.
         |  
         |  __floordiv__(self, value, /)
         |      Return self//value.
         |  
         |  __ge__(self, value, /)
         |      Return self>=value.
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __gt__(self, value, /)
         |      Return self>value.
         |  
         |  __hash__(self, /)
         |      Return hash(self).
         |  
         |  __le__(self, value, /)
         |      Return self<=value.
         |  
         |  __lt__(self, value, /)
         |      Return self<value.
         |  
         |  __mod__(self, value, /)
         |      Return self%value.
         |  
         |  __mul__(self, value, /)
         |      Return self*value.
         |  
         |  __ne__(self, value, /)
         |      Return self!=value.
         |  
         |  __neg__(self, /)
         |      -self
         |  
         |  __pos__(self, /)
         |      +self
         |  
         |  __radd__(self, value, /)
         |      Return value+self.
         |  
         |  __rdivmod__(self, value, /)
         |      Return divmod(value, self).
         |  
         |  __reduce__(...)
         |      __reduce__() -> (cls, state)
         |  
         |  __repr__(self, /)
         |      Return repr(self).
         |  
         |  __rfloordiv__(self, value, /)
         |      Return value//self.
         |  
         |  __rmod__(self, value, /)
         |      Return value%self.
         |  
         |  __rmul__(self, value, /)
         |      Return value*self.
         |  
         |  __rsub__(self, value, /)
         |      Return value-self.
         |  
         |  __rtruediv__(self, value, /)
         |      Return value/self.
         |  
         |  __str__(self, /)
         |      Return str(self).
         |  
         |  __sub__(self, value, /)
         |      Return self-value.
         |  
         |  __truediv__(self, value, /)
         |      Return self/value.
         |  
         |  total_seconds(...)
         |      Total seconds in the duration.
         |  
         |  ----------------------------------------------------------------------
         |  Static methods defined here:
         |  
         |  __new__(*args, **kwargs) from builtins.type
         |      Create and return a new object.  See help(type) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  days
         |      Number of days.
         |  
         |  microseconds
         |      Number of microseconds (>= 0 and less than 1 second).
         |  
         |  seconds
         |      Number of seconds (>= 0 and less than 1 day).
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  max = datetime.timedelta(days=999999999, seconds=86399, microseconds=9...
         |  
         |  min = datetime.timedelta(days=-999999999)
         |  
         |  resolution = datetime.timedelta(microseconds=1)
        
        class timezone(tzinfo)
         |  Fixed offset from UTC implementation of tzinfo.
         |  
         |  Method resolution order:
         |      timezone
         |      tzinfo
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __eq__(self, value, /)
         |      Return self==value.
         |  
         |  __ge__(self, value, /)
         |      Return self>=value.
         |  
         |  __getinitargs__(...)
         |      pickle support
         |  
         |  __gt__(self, value, /)
         |      Return self>value.
         |  
         |  __hash__(self, /)
         |      Return hash(self).
         |  
         |  __le__(self, value, /)
         |      Return self<=value.
         |  
         |  __lt__(self, value, /)
         |      Return self<value.
         |  
         |  __ne__(self, value, /)
         |      Return self!=value.
         |  
         |  __repr__(self, /)
         |      Return repr(self).
         |  
         |  __str__(self, /)
         |      Return str(self).
         |  
         |  dst(...)
         |      Return None.
         |  
         |  fromutc(...)
         |      datetime in UTC -> datetime in local time.
         |  
         |  tzname(...)
         |      If name is specified when timezone is created, returns the name.  Otherwise returns offset as 'UTC(+|-)HH:MM'.
         |  
         |  utcoffset(...)
         |      Return fixed offset.
         |  
         |  ----------------------------------------------------------------------
         |  Static methods defined here:
         |  
         |  __new__(*args, **kwargs) from builtins.type
         |      Create and return a new object.  See help(type) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  max = datetime.timezone(datetime.timedelta(seconds=86340))
         |  
         |  min = datetime.timezone(datetime.timedelta(days=-1, seconds=60))
         |  
         |  utc = datetime.timezone.utc
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from tzinfo:
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __reduce__(...)
         |      -> (cls, state)
        
        class tzinfo(builtins.object)
         |  Abstract base class for time zone info objects.
         |  
         |  Methods defined here:
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __reduce__(...)
         |      -> (cls, state)
         |  
         |  dst(...)
         |      datetime -> DST offset as timedelta positive east of UTC.
         |  
         |  fromutc(...)
         |      datetime in UTC -> datetime in local time.
         |  
         |  tzname(...)
         |      datetime -> string name of time zone.
         |  
         |  utcoffset(...)
         |      datetime -> timedelta showing offset from UTC, negative values indicating West of UTC
         |  
         |  ----------------------------------------------------------------------
         |  Static methods defined here:
         |  
         |  __new__(*args, **kwargs) from builtins.type
         |      Create and return a new object.  See help(type) for accurate signature.
    
    DATA
        MAXYEAR = 9999
        MINYEAR = 1
        datetime_CAPI = <capsule object "datetime.datetime_CAPI">
    
    FILE
        /usr/lib/python3.8/datetime.py
    
    



```python
help(os.path.getmtime)
```

    Help on function getmtime in module genericpath:
    
    getmtime(filename)
        Return the last modification time of a file, reported by os.stat().
    



```python
timestamp = os.path.getmtime('strings.py')
a = os.path.getatime('herencia.py')
print(timestamp)
print(a)
```

    1651346238.0074563
    1652217555.0204172



```python
print(dir(datetime.datetime))
```

    ['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold', 'fromisocalendar', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']



```python
help('datetime.datetime.fromtimestamp')
```

    Help on built-in function fromtimestamp in datetime.datetime:
    
    datetime.datetime.fromtimestamp = fromtimestamp(...) method of builtins.type instance
        timestamp[, tz] -> tz's local time from POSIX timestamp.
    



```python
fecha = datetime.datetime.fromtimestamp(timestamp)
fecha_a = datetime.datetime.fromtimestamp(a)
print(f'La fecha del timestamp es : {fecha}')
print(f'La fecha de fecha_a es : {fecha_a}')
```

    La fecha del timestamp es : 2022-04-30 21:17:18.007456
    La fecha de fecha_a es : 2022-05-10 23:19:15.020417


## exists()

#### .exists() nos devuelve True si existe el file


```python
help(os.path.exists)
```

    Help on function exists in module genericpath:
    
    exists(path)
        Test whether a path exists.  Returns False for broken symbolic links
    



```python
os.path.exists('strings.py')
```




    True



### Continuamos con abspath() que nos devuelve la ruta absoluta de un file


```python
print(dir(os.path))
```

    ['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_get_sep', '_joinrealpath', '_varprog', '_varprogb', 'abspath', 'altsep', 'basename', 'commonpath', 'commonprefix', 'curdir', 'defpath', 'devnull', 'dirname', 'exists', 'expanduser', 'expandvars', 'extsep', 'genericpath', 'getatime', 'getctime', 'getmtime', 'getsize', 'isabs', 'isdir', 'isfile', 'islink', 'ismount', 'join', 'lexists', 'normcase', 'normpath', 'os', 'pardir', 'pathsep', 'realpath', 'relpath', 'samefile', 'sameopenfile', 'samestat', 'sep', 'split', 'splitdrive', 'splitext', 'stat', 'supports_unicode_filenames', 'sys']



```python
help('os.path.abspath')
```

    Help on function abspath in os.path:
    
    os.path.abspath = abspath(path)
        Return an absolute path.
    



```python
ruta = os.path.abspath('herencia.py')
print(f'Ruta absoluta del file: {ruta}')
```

    Ruta absoluta del file: /home/michelle/FORMACION/GOOGLE/CuadernosJupyter/herencia.py


### getcwd() nos muestra el path actual
### chdir(ruta del directorio) nos cambia al directorio pasado


```python
help('os.getcwd')
```

    Help on built-in function getcwd in os:
    
    os.getcwd = getcwd()
        Return a unicode string representing the current working directory.
    



```python
os.getcwd()
```




    '/home/michelle/FORMACION/GOOGLE/CuadernosJupyter'




```python
try:
    os.mkdir('Modulo_OS')
except FileExistsError:
    print('Ya existe una carpeta con este nombre')
```

    Ya existe una carpeta con este nombre


### mkdir() nos crea un directorio que le pasamos como argumento str, si existe arroja error

### usamos un try: except con el error que nos arroja para no colgar el programa


```python
help('os.mkdir')
```

    Help on built-in function mkdir in os:
    
    os.mkdir = mkdir(path, mode=511, *, dir_fd=None)
        Create a directory.
        
        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.
        
        The mode argument is ignored on Windows.
    



```python
help('os.chdir')
```

    Help on built-in function chdir in os:
    
    os.chdir = chdir(path)
        Change the current working directory to the specified path.
        
        path may always be specified as a string.
        On some platforms, path may also be specified as an open file descriptor.
          If this functionality is unavailable, using it raises an exception.
    



```python
os.chdir('/home/michelle/FORMACION/GOOGLE/CuadernosJupyter/')
os.getcwd()
```




    '/home/michelle/FORMACION/GOOGLE/CuadernosJupyter'



## os.walk() ---> Muy util para listar cada folder con sus subfolders y files


```python
help('os.walk')
```

    Help on function walk in os:
    
    os.walk = walk(top, topdown=True, onerror=None, followlinks=False)
        Directory tree generator.
        
        For each directory in the directory tree rooted at top (including top
        itself, but excluding '.' and '..'), yields a 3-tuple
        
            dirpath, dirnames, filenames
        
        dirpath is a string, the path to the directory.  dirnames is a list of
        the names of the subdirectories in dirpath (excluding '.' and '..').
        filenames is a list of the names of the non-directory files in dirpath.
        Note that the names in the lists are just names, with no path components.
        To get a full path (which begins with top) to a file or directory in
        dirpath, do os.path.join(dirpath, name).
        
        If optional arg 'topdown' is true or not specified, the triple for a
        directory is generated before the triples for any of its subdirectories
        (directories are generated top down).  If topdown is false, the triple
        for a directory is generated after the triples for all of its
        subdirectories (directories are generated bottom up).
        
        When topdown is true, the caller can modify the dirnames list in-place
        (e.g., via del or slice assignment), and walk will only recurse into the
        subdirectories whose names remain in dirnames; this can be used to prune the
        search, or to impose a specific order of visiting.  Modifying dirnames when
        topdown is false has no effect on the behavior of os.walk(), since the
        directories in dirnames have already been generated by the time dirnames
        itself is generated. No matter the value of topdown, the list of
        subdirectories is retrieved before the tuples for the directory and its
        subdirectories are generated.
        
        By default errors from the os.scandir() call are ignored.  If
        optional arg 'onerror' is specified, it should be a function; it
        will be called with one argument, an OSError instance.  It can
        report the error to continue with the walk, or raise the exception
        to abort the walk.  Note that the filename is available as the
        filename attribute of the exception object.
        
        By default, os.walk does not follow symbolic links to subdirectories on
        systems that support them.  In order to get this functionality, set the
        optional argument 'followlinks' to true.
        
        Caution:  if you pass a relative pathname for top, don't change the
        current working directory between resumptions of walk.  walk never
        changes the current directory, and assumes that the client doesn't
        either.
        
        Example:
        
        import os
        from os.path import join, getsize
        for root, dirs, files in os.walk('python/Lib/email'):
            print(root, "consumes", end="")
            print(sum(getsize(join(root, name)) for name in files), end="")
            print("bytes in", len(files), "non-directory files")
            if 'CVS' in dirs:
                dirs.remove('CVS')  # don't visit CVS directories
    



```python
'''os.chdir('/home/michelle/')
os.getcwd()

for dirpath, dirnames, filenames in os.walk('/home/michelle/'):
    print('Ruta al directorio: ',dirpath)
    print('----------------------------------')
    print('Nombres de directorio: ',dirnames)
    print('----------------------------------')
    print('Nombres de archivo: ',filenames)
    print('----------------------------------')
    print()
'''   
```




    "os.chdir('/home/michelle/')\nos.getcwd()\n\nfor dirpath, dirnames, filenames in os.walk('/home/michelle/'):\n    print('Ruta al directorio: ',dirpath)\n    print('----------------------------------')\n    print('Nombres de directorio: ',dirnames)\n    print('----------------------------------')\n    print('Nombres de archivo: ',filenames)\n    print('----------------------------------')\n    print()\n"



## NOTA ----->>
#### Mirar el archivo arbol_del_sistema.txt creado con el script de python en la misma carpeta

### os.path.join() ----> nos devuelve un path a partir de un path y un file


```python
help('os.path.join')
```

    Help on function join in os.path:
    
    os.path.join = join(a, *p)
        Join two or more pathname components, inserting '/' as needed.
        If any component is an absolute path, all previous path components
        will be discarded.  An empty last part will result in a path that
        ends with a separator.
    



```python
print(os.environ.get('HOME'))# Nos pasa el path de la variable de entorno HOME
path_home = os.environ.get('HOME')
print(path_home)
```

    /home/michelle
    /home/michelle



```python
file_path = os.path.join(path_home, 'test.txt') # Dos argumentos
print(file_path)
```

    /home/michelle/test.txt



```python
help('os.path.basename')
```

    Help on function basename in os.path:
    
    os.path.basename = basename(p)
        Returns the final component of a pathname
    



```python
# Para analizar por separado las dos partes del path
nombre_file = os.path.basename(file_path)
directorio_file = os.path.dirname(file_path)
print(f'El archivo se llama --> {nombre_file} y el directorio --> {directorio_file}')
```

    El archivo se llama --> test.txt y el directorio --> /home/michelle



```python
help('os.path.split')
```

    Help on function split in os.path:
    
    os.path.split = split(p)
        Split a pathname.  Returns tuple "(head, tail)" where "tail" is
        everything after the final slash.  Either part may be empty.
    



```python
# os.path.split() nos devuelve una tupla con dos str
completo_ruta_tupla = os.path.split(file_path)
print(completo_ruta_tupla)
print(type(completo_ruta_tupla))
```

    ('/home/michelle', 'test.txt')
    <class 'tuple'>



```python
# Vamos a seguir con otras funciones de este modulo. Acuérdate de mirar con dir(funcion) --> para ver las funciones
# y con help('string nombre funcion') --> para ayuda del intérprete

print(os.path.isdir('/home/michelle/FORMACION/GOOGLE/CuadernosJupyter/'))
print(os.path.isdir('/home/michelle/FORMACION/GOOGLE/CuadernosJupyter23/'))
print(os.path.isfile('/home/michelle/FORMACION/GOOGLE/CuadernosJupyter/'))
print(os.path.isfile('/home/michelle/FORMACION/GOOGLE/CuadernosJupyter/strings.py'))
# os.path.isdir() & os.path.isfile() devuelve booleano. Comprueba si es un directorio o file en el sistema
```

    True
    False
    False
    True



```python
# os.path.splitex() nos devuelve la extension del file
os.path.splitext('/home/michelle/FORMACION/GOOGLE/CuadernosJupyter/strings.py')[0] # entrecorchetes la posicion de la extension
```




    '/home/michelle/FORMACION/GOOGLE/CuadernosJupyter/strings'




```python
help('os.path.splitext')
```

    Help on function splitext in os.path:
    
    os.path.splitext = splitext(p)
        Split the extension from a pathname.
        
        Extension is everything from the last dot to the end, ignoring
        leading dots.  Returns "(root, ext)"; ext may be empty.
    


# DESPEDIDA Y CIERRE
### Aquí se acaba el repaso al modulo OS de Python. Espero te ayude el repaso
