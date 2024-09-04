# gdb-gef

<<<<<<< HEAD
=======
This file was contributed to by `deveynull` (also made the hello_world binary)

>>>>>>> 62e51517054901aa0b7fd1508d70dcb095961589
So throughout this project, we will be using a lot of different tools. The purpose of this module is to show you some of the basics of three of those tools. We will start with gdb-gef.

First off, gdb is a debugger (specifically the gnu debugger). Gef is an a gdb wrapper, designed  to give us some extended features (https://github.com/hugsy/gef). To install it, you can find the instructions on the github page. it's super simple.

A debugger is software that allows us to perform various types of analysis of a process as it's running, and alter it in a variety of different ways.

Now you can tell if you have it installed by just looking at gdb. For instance this is the look of gdb if you have gef installed:

```
$ gdb
GNU gdb (Ubuntu 8.2.91.20190405-0ubuntu3) 8.2.91.20190405-git
Copyright (C) 2019 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word".
GEF for linux ready, type `gef' to start, `gef config' to configure
75 commands loaded for GDB 8.2.91.20190405-git using Python engine 3.7
[*] 5 commands could not be loaded, run `gef missing` to know why.
gef➤  
```

If you don't have it installed this is what vanilla gdb looks like:

```
$    gdb
GNU gdb (Ubuntu 8.2.91.20190405-0ubuntu3) 8.2.91.20190405-git
Copyright (C) 2019 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word".
(gdb)
```

## Running

<<<<<<< HEAD
To run the binary `titan` in gdb:

```
gdb ./titan
GNU gdb (Ubuntu 8.2.91.20190405-0ubuntu3) 8.2.91.20190405-git
Copyright (C) 2019 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
=======
To run the binary `hello_world` in gdb:

```
gdb ./hello_world 
GNU gdb (Ubuntu 8.1-0ubuntu3) 8.1.0.20180409-git
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
>>>>>>> 62e51517054901aa0b7fd1508d70dcb095961589
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<<<<<<< HEAD
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
GEF for linux ready, type `gef' to start, `gef config' to configure
75 commands loaded for GDB 8.2.91.20190405-git using Python engine 3.7
[*] 5 commands could not be loaded, run `gef missing` to know why.
Reading symbols from ./titan...
(No debugging symbols found in ./titan)
gef➤  r
Starting program: /tmp/titan
hi
```

If you are running a process in gdb, and wish to drop to the debugger console, you can do so by pressing `Cotrol + C`:

```
gef➤  r
Starting program: /tmp/titan
hi
^C
Program received signal SIGINT, Interrupt.
0x00007ffff7ed6f81 in __GI___libc_read (fd=0x0, buf=0x555555559670, nbytes=0x400) at ../sysdeps/unix/sysv/linux/read.c:26
26    ../sysdeps/unix/sysv/linux/read.c: No such file or directory.
[ Legend: Modified register | Code | Heap | Stack | String ]
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── registers ────
$rax   : 0xfffffffffffffe00
$rbx   : 0x00007ffff7faea00  →  0x00000000fbad2288
$rcx   : 0x00007ffff7ed6f81  →  0x5777fffff0003d48 ("H="?)
$rdx   : 0x400             
$rsp   : 0x00007fffffffdef8  →  0x00007ffff7e59e50  →  <_IO_file_underflow+336> test rax, rax
$rbp   : 0xd68             
$rsi   : 0x0000555555559670  →  0x0000000000000000
$rdi   : 0x0               
$rip   : 0x00007ffff7ed6f81  →  0x5777fffff0003d48 ("H="?)
$r8    : 0x00007ffff7fb1580  →  0x0000000000000000
$r9    : 0x00007ffff7fb6500  →  0x00007ffff7fb6500  →  [loop detected]
$r10   : 0x00007ffff7faeca0  →  0x0000555555559a70  →  0x0000000000000000
$r11   : 0x246             
$r12   : 0x00007ffff7faf960  →  0x0000000000000000
$r13   : 0x00007ffff7fb0560  →  0x0000000000000000
$r14   : 0x00007ffff7faf848  →  0x00007ffff7faf760  →  0x00000000fbad2a84
$r15   : 0x00007ffff7fb0560  →  0x0000000000000000
$eflags: [ZERO carry PARITY adjust sign trap INTERRUPT direction overflow resume virtualx86 identification]
$cs: 0x0033 $ss: 0x002b $ds: 0x0000 $es: 0x0000 $fs: 0x0000 $gs: 0x0000
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── stack ────
0x00007fffffffdef8│+0x0000: 0x00007ffff7e59e50  →  <_IO_file_underflow+336> test rax, rax     ← $rsp
0x00007fffffffdf00│+0x0008: 0x00007ffff7faf960  →  0x0000000000000000
0x00007fffffffdf08│+0x0010: 0x00007ffff7faea00  →  0x00000000fbad2288
0x00007fffffffdf10│+0x0018: 0x00007ffff7fb0560  →  0x0000000000000000
0x00007fffffffdf18│+0x0020: 0x000000000000000a
0x00007fffffffdf20│+0x0028: 0x0000000000000000
0x00007fffffffdf28│+0x0030: 0x0000000000000008
0x00007fffffffdf30│+0x0038: 0x00007ffff7faea00  →  0x00000000fbad2288
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── code:x86:64 ────
   0x7ffff7ed6f75 <read+5>         or     eax, 0x85008b00
   0x7ffff7ed6f7a <read+10>        shl    BYTE PTR [rbp+0x13], 0x31
   0x7ffff7ed6f7e <read+14>        ror    BYTE PTR [rdi], 0x5
 → 0x7ffff7ed6f81 <read+17>        cmp    rax, 0xfffffffffffff000
   0x7ffff7ed6f87 <read+23>        ja     0x7ffff7ed6fe0 <__GI___libc_read+112>
   0x7ffff7ed6f89 <read+25>        ret    
   0x7ffff7ed6f8a <read+26>        nop    WORD PTR [rax+rax*1+0x0]
   0x7ffff7ed6f90 <read+32>        push   r12
   0x7ffff7ed6f92 <read+34>        mov    r12, rdx
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "titan", stopped, reason: SIGINT
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── trace ────
[#0] 0x7ffff7ed6f81 → __GI___libc_read(fd=0x0, buf=0x555555559670, nbytes=0x400)
[#1] 0x7ffff7e59e50 → _IO_new_file_underflow(fp=0x7ffff7faea00 <_IO_2_1_stdin_>)
[#2] 0x7ffff7e5b182 → __GI__IO_default_uflow(fp=0x7ffff7faea00 <_IO_2_1_stdin_>)
[#3] 0x7ffff7e4d1fa → __GI__IO_getline_info(fp=0x7ffff7faea00 <_IO_2_1_stdin_>, buf=0x7fffffffdfee "", n=0x8, delim=0xa, extract_delim=0x1, eof=0x0)
[#4] 0x7ffff7e4d2e8 → __GI__IO_getline(fp=0x7ffff7faea00 <_IO_2_1_stdin_>, buf=0x7fffffffdfee "", n=<optimized out>, delim=0xa, extract_delim=0x1)
[#5] 0x7ffff7e4c1ab → _IO_fgets(buf=0x7fffffffdfee "", n=<optimized out>, fp=0x7ffff7faea00 <_IO_2_1_stdin_>)
[#6] 0x555555555190 → main()
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
gef➤  
```

## Breakpoints

Let's take a look at the main function:

```
gef➤  disas main
Dump of assembler code for function main:
   0x0000000000401142 <+0>:    push   rbp
   0x0000000000401143 <+1>:    mov    rbp,rsp
   0x0000000000401146 <+4>:    sub    rsp,0x20
   0x000000000040114a <+8>:    mov    rax,QWORD PTR fs:0x28
   0x0000000000401153 <+17>:    mov    QWORD PTR [rbp-0x8],rax
   0x0000000000401157 <+21>:    xor    eax,eax
   0x0000000000401159 <+23>:    lea    rdi,[rip+0xea4]        # 0x402004
   0x0000000000401160 <+30>:    call   0x401030 <puts@plt>
   0x0000000000401165 <+35>:    mov    rdx,QWORD PTR [rip+0x2ed4]        # 0x404040 <stdin@@GLIBC_2.2.5>
   0x000000000040116c <+42>:    lea    rax,[rbp-0x12]
   0x0000000000401170 <+46>:    mov    esi,0x9
   0x0000000000401175 <+51>:    mov    rdi,rax
   0x0000000000401178 <+54>:    call   0x401050 <fgets@plt>
   0x000000000040117d <+59>:    nop
   0x000000000040117e <+60>:    mov    rax,QWORD PTR [rbp-0x8]
   0x0000000000401182 <+64>:    xor    rax,QWORD PTR fs:0x28
   0x000000000040118b <+73>:    je     0x401192 <main+80>
   0x000000000040118d <+75>:    call   0x401040 <__stack_chk_fail@plt>
   0x0000000000401192 <+80>:    leave  
   0x0000000000401193 <+81>:    ret    
End of assembler dump.
=======
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
GEF for linux ready, type `gef' to start, `gef config' to configure
75 commands loaded for GDB 8.1.0.20180409-git using Python engine 3.6
[*] 5 commands could not be loaded, run `gef missing` to know why.
Reading symbols from ./hello_world...(no debugging symbols found)...done.
gef➤  r
Starting program: /home/devey/nightmare/modules/02-intro_tooling/hello_world 
hello world!
[Inferior 1 (process 9133) exited normally]
```

In order to enter debugger mode, we can set breakpoints. Breakpoints are places in the program where GDB will know to stop execution to allow you to examine the contents of the stack. 
The most common breakpoint to set is on main, which we can set with 'break main' or 'b main'. Most GDB commands can be shortened. Check out this cheat sheet for more: <CHEATSHEET> 


```
gef➤  break main
Breakpoint 1 at 0x8048409
gef➤  r
Starting program: /home/devey/nightmare/modules/02-intro_tooling/hello_world 
[ Legend: Modified register | Code | Heap | Stack | String ]
────────────────────────────────────────────────────────────────────── registers ────
$eax   : 0xf7fb9dd8  →  0xffffd19c  →  0xffffd389  →  "CLUTTER_IM_MODULE=xim"
$ebx   : 0x0       
$ecx   : 0xffffd100  →  0x00000001
$edx   : 0xffffd124  →  0x00000000
$esp   : 0xffffd0e4  →  0xffffd100  →  0x00000001
$ebp   : 0xffffd0e8  →  0x00000000
$esi   : 0xf7fb8000  →  0x001d4d6c
$edi   : 0x0       
$eip   : 0x08048409  →  <main+14> sub esp, 0x4
$eflags: [zero carry PARITY adjust SIGN trap INTERRUPT direction overflow resume virtualx86 identification]
$cs: 0x0023 $ss: 0x002b $ds: 0x002b $es: 0x002b $fs: 0x0000 $gs: 0x0063 
────────────────────────────────────────────────────────────────────────── stack ────
0xffffd0e4│+0x0000: 0xffffd100  →  0x00000001	 ← $esp
0xffffd0e8│+0x0004: 0x00000000	 ← $ebp
0xffffd0ec│+0x0008: 0xf7dfbe81  →  <__libc_start_main+241> add esp, 0x10
0xffffd0f0│+0x000c: 0xf7fb8000  →  0x001d4d6c
0xffffd0f4│+0x0010: 0xf7fb8000  →  0x001d4d6c
0xffffd0f8│+0x0014: 0x00000000
0xffffd0fc│+0x0018: 0xf7dfbe81  →  <__libc_start_main+241> add esp, 0x10
0xffffd100│+0x001c: 0x00000001
──────────────────────────────────────────────────────────────────── code:x86:32 ────
    0x8048405 <main+10>        push   ebp
    0x8048406 <main+11>        mov    ebp, esp
    0x8048408 <main+13>        push   ecx
 →  0x8048409 <main+14>        sub    esp, 0x4
    0x804840c <main+17>        sub    esp, 0xc
    0x804840f <main+20>        push   0x80484b0
    0x8048414 <main+25>        call   0x80482d0 <puts@plt>
    0x8048419 <main+30>        add    esp, 0x10
    0x804841c <main+33>        mov    eax, 0x0
──────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "hello_world", stopped 0x8048409 in main (), reason: BREAKPOINT
────────────────────────────────────────────────────────────────────────── trace ────
[#0] 0x8048409 → main()
─────────────────────────────────────────────────────────────────────────────────────

Breakpoint 1, 0x08048409 in main ()
```


Now you can step through the function by typing 'nexti' until the program ends. 'nexti' will have you go instruction by intruction through the program, but will not step into function calls such as puts. 

Other ways to navigate a program are:
* 'next' - which will take you through one line of code, but will step over function calls such as puts. 
* 'step' - which will take you through one line of code, but will step into function calls
* 'stepi' - whch will take you through one instruction at a time, stepping into function calls

For each of these methods, work through the program after setting a breakpoint in main. Take specific care to see what step and stepi see after entering puts. Most of the time, because those are part of standard libraries, we don't need to step into anything.

## Breakpoints

Let's take a look at the main function using 'disassemble' or 'disass':

```
gef➤  disass main
Dump of assembler code for function main:
   0x080483fb <+0>:	lea    ecx,[esp+0x4]
   0x080483ff <+4>:	and    esp,0xfffffff0
   0x08048402 <+7>:	push   DWORD PTR [ecx-0x4]
   0x08048405 <+10>:	push   ebp
   0x08048406 <+11>:	mov    ebp,esp
   0x08048408 <+13>:	push   ecx
   0x08048409 <+14>:	sub    esp,0x4
   0x0804840c <+17>:	sub    esp,0xc
   0x0804840f <+20>:	push   0x80484b0
   0x08048414 <+25>:	call   0x80482d0 <puts@plt>
   0x08048419 <+30>:	add    esp,0x10
   0x0804841c <+33>:	mov    eax,0x0
   0x08048421 <+38>:	mov    ecx,DWORD PTR [ebp-0x4]
   0x08048424 <+41>:	leave  
   0x08048425 <+42>:	lea    esp,[ecx-0x4]
   0x08048428 <+45>:	ret    
End of assembler dump.

>>>>>>> 62e51517054901aa0b7fd1508d70dcb095961589
```

Let's say we wanted to break on the call to `puts`. We can do this by setting a breakpoint for that instruction.

Like this:
```
<<<<<<< HEAD
gef➤  b *main+30
Breakpoint 1 at 0x401160
=======
gef➤  b *main+25
Breakpoint 1 at 0x8048414
>>>>>>> 62e51517054901aa0b7fd1508d70dcb095961589
```

Or like this:
```
<<<<<<< HEAD
gef➤  b *0x401160
Note: breakpoint 1 also set at pc 0x401160.
Breakpoint 2 at 0x401160
=======
gef➤  b *0x08048414
Note: breakpoint 1 also set at pc 0x08048414
Breakpoint 2 at 0x08048414
>>>>>>> 62e51517054901aa0b7fd1508d70dcb095961589
```

When we run the binary and it tries to execute that instruction, the process will pause and drop us into the debugger console:

```
gef➤  r
<<<<<<< HEAD
Starting program: /tmp/titan

Breakpoint 1, 0x0000000000401160 in main ()
[ Legend: Modified register | Code | Heap | Stack | String ]
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── registers ────
$rax   : 0x0               
$rbx   : 0x0               
$rcx   : 0x00000000004011a0  →  <__libc_csu_init+0> push r15
$rdx   : 0x00007fffffffe0f8  →  0x00007fffffffe412  →  "SHELL=/bin/bash"
$rsp   : 0x00007fffffffdfe0  →  0x00000000004011a0  →  <__libc_csu_init+0> push r15
$rbp   : 0x00007fffffffe000  →  0x00000000004011a0  →  <__libc_csu_init+0> push r15
$rsi   : 0x00007fffffffe0e8  →  0x00007fffffffe407  →  "/tmp/titan"
$rdi   : 0x0000000000402004  →  0x3b031b0100006968 ("hi"?)
$rip   : 0x0000000000401160  →  <main+30> call 0x401030 <puts@plt>
$r8    : 0x00007ffff7fb0a40  →  0x0000000000000000
$r9    : 0x00007ffff7fb0a40  →  0x0000000000000000
$r10   : 0x1               
$r11   : 0x206             
$r12   : 0x0000000000401060  →  <_start+0> xor ebp, ebp
$r13   : 0x00007fffffffe0e0  →  0x0000000000000001
$r14   : 0x0               
$r15   : 0x0               
$eflags: [ZERO carry PARITY adjust sign trap INTERRUPT direction overflow resume virtualx86 identification]
$cs: 0x0033 $ss: 0x002b $ds: 0x0000 $es: 0x0000 $fs: 0x0000 $gs: 0x0000
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── stack ────
0x00007fffffffdfe0│+0x0000: 0x00000000004011a0  →  <__libc_csu_init+0> push r15     ← $rsp
0x00007fffffffdfe8│+0x0008: 0x0000000000401060  →  <_start+0> xor ebp, ebp
0x00007fffffffdff0│+0x0010: 0x00007fffffffe0e0  →  0x0000000000000001
0x00007fffffffdff8│+0x0018: 0x42586df821034f00
0x00007fffffffe000│+0x0020: 0x00000000004011a0  →  <__libc_csu_init+0> push r15     ← $rbp
0x00007fffffffe008│+0x0028: 0x00007ffff7df0b6b  →  <__libc_start_main+235> mov edi, eax
0x00007fffffffe010│+0x0030: 0x00007ffff7fab4d8  →  0x00007ffff7df0450  →  <init_cacheinfo+0> push r15
0x00007fffffffe018│+0x0038: 0x00007fffffffe0e8  →  0x00007fffffffe407  →  "/tmp/titan"
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── code:x86:64 ────
     0x401153 <main+17>        mov    QWORD PTR [rbp-0x8], rax
     0x401157 <main+21>        xor    eax, eax
     0x401159 <main+23>        lea    rdi, [rip+0xea4]        # 0x402004
 →   0x401160 <main+30>        call   0x401030 <puts@plt>
   ↳    0x401030 <puts@plt+0>     jmp    QWORD PTR [rip+0x2fe2]        # 0x404018 <puts@got.plt>
        0x401036 <puts@plt+6>     push   0x0
        0x40103b <puts@plt+11>    jmp    0x401020
        0x401040 <__stack_chk_fail@plt+0> jmp    QWORD PTR [rip+0x2fda]        # 0x404020 <__stack_chk_fail@got.plt>
        0x401046 <__stack_chk_fail@plt+6> push   0x1
        0x40104b <__stack_chk_fail@plt+11> jmp    0x401020
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── arguments (guessed) ────
puts@plt (
   $rdi = 0x0000000000402004 → 0x3b031b0100006968 ("hi"?),
   $rsi = 0x00007fffffffe0e8 → 0x00007fffffffe407 → "/tmp/titan",
   $rdx = 0x00007fffffffe0f8 → 0x00007fffffffe412 → "SHELL=/bin/bash"
)
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "titan", stopped, reason: BREAKPOINT
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── trace ────
[#0] 0x401160 → main()
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
gef➤  
=======
Starting program: /home/devey/nightmare/modules/02-intro_tooling/hello_world 
[ Legend: Modified register | Code | Heap | Stack | String ]
────────────────────────────────────────────────────────────────────── registers ────
$eax   : 0xf7fb9dd8  →  0xffffd19c  →  0xffffd389  →  "CLUTTER_IM_MODULE=xim"
$ebx   : 0x0       
$ecx   : 0xffffd100  →  0x00000001
$edx   : 0xffffd124  →  0x00000000
$esp   : 0xffffd0d0  →  0x080484b0  →  "hello world!"
$ebp   : 0xffffd0e8  →  0x00000000
$esi   : 0xf7fb8000  →  0x001d4d6c
$edi   : 0x0       
$eip   : 0x08048414  →  0xfffeb7e8  →  0x00000000
$eflags: [zero carry PARITY ADJUST SIGN trap INTERRUPT direction overflow resume virtualx86 identification]
$cs: 0x0023 $ss: 0x002b $ds: 0x002b $es: 0x002b $fs: 0x0000 $gs: 0x0063 
────────────────────────────────────────────────────────────────────────── stack ────
0xffffd0d0│+0x0000: 0x080484b0  →  "hello world!"	 ← $esp
0xffffd0d4│+0x0004: 0xffffd194  →  0xffffd34e  →  "/home/devey/nightmare/modules/02-intro_tooling/hel[...]"
0xffffd0d8│+0x0008: 0xffffd19c  →  0xffffd389  →  "CLUTTER_IM_MODULE=xim"
0xffffd0dc│+0x000c: 0x08048451  →  <__libc_csu_init+33> lea eax, [ebx-0xf8]
0xffffd0e0│+0x0010: 0xf7fe59b0  →   push ebp
0xffffd0e4│+0x0014: 0xffffd100  →  0x00000001
0xffffd0e8│+0x0018: 0x00000000	 ← $ebp
0xffffd0ec│+0x001c: 0xf7dfbe81  →  <__libc_start_main+241> add esp, 0x10
──────────────────────────────────────────────────────────────────── code:x86:32 ────
    0x8048409 <main+14>        sub    esp, 0x4
    0x804840c <main+17>        sub    esp, 0xc
    0x804840f <main+20>        push   0x80484b0
 →  0x8048414 <main+25>        call   0x80482d0 <puts@plt>
   ↳   0x80482d0 <puts@plt+0>     jmp    DWORD PTR ds:0x80496bc
       0x80482d6 <puts@plt+6>     push   0x0
       0x80482db <puts@plt+11>    jmp    0x80482c0
       0x80482e0 <__gmon_start__@plt+0> jmp    DWORD PTR ds:0x80496c0
       0x80482e6 <__gmon_start__@plt+6> push   0x8
       0x80482eb <__gmon_start__@plt+11> jmp    0x80482c0
──────────────────────────────────────────────────────────── arguments (guessed) ────
puts@plt (
   [sp + 0x0] = 0x080484b0 → "hello world!",
   [sp + 0x4] = 0xffffd194 → 0xffffd34e → "/home/devey/nightmare/modules/02-intro_tooling/hel[...]"
)
──────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "hello_world", stopped 0x8048414 in main (), reason: BREAKPOINT
────────────────────────────────────────────────────────────────────────── trace ────
[#0] 0x8048414 → main()
─────────────────────────────────────────────────────────────────────────────────────

Breakpoint 1, 0x08048414 in main ()
gef➤  

>>>>>>> 62e51517054901aa0b7fd1508d70dcb095961589
```

In the debugger console is where we can actually use the debugger to provide various types of analysis, and change things about the binary. For now let's keep looking at breakpoints. To show all breakpoints:

```
gef➤  info breakpoints
<<<<<<< HEAD
Num     Type           Disp Enb Address            What
1       breakpoint     keep y   0x0000000000401160 <main+30>
    breakpoint already hit 1 time
2       breakpoint     keep y   0x0000000000401170 <main+46>
```

=======
Num     Type           Disp Enb Address    What
1       breakpoint     keep y   0x08048414 <main+25>
	breakpoint already hit 1 time
2       breakpoint     keep y   0x08048414 <main+25>

```

or to be short, "info b" or "i b".

>>>>>>> 62e51517054901aa0b7fd1508d70dcb095961589
To delete a breakpoint Num `2`:

```
gef➤  delete 2
<<<<<<< HEAD
```
=======

```
or to be short "del 2" or "d 2".
>>>>>>> 62e51517054901aa0b7fd1508d70dcb095961589

We can also set breakpoints for functions like `puts`:

```
gef➤  b *puts
<<<<<<< HEAD
Breakpoint 1 at 0x401030
gef➤  r
Starting program: /tmp/titan

Breakpoint 1, __GI__IO_puts (str=0x402004 "hi") at ioputs.c:35
35    ioputs.c: No such file or directory.
[ Legend: Modified register | Code | Heap | Stack | String ]
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── registers ────
$rax   : 0x0               
$rbx   : 0x0               
$rcx   : 0x00000000004011a0  →  <__libc_csu_init+0> push r15
$rdx   : 0x00007fffffffe0f8  →  0x00007fffffffe412  →  "SHELL=/bin/bash"
$rsp   : 0x00007fffffffdfd8  →  0x0000000000401165  →  <main+35> mov rdx, QWORD PTR [rip+0x2ed4]        # 0x404040 <stdin@@GLIBC_2.2.5>
$rbp   : 0x00007fffffffe000  →  0x00000000004011a0  →  <__libc_csu_init+0> push r15
$rsi   : 0x00007fffffffe0e8  →  0x00007fffffffe407  →  "/tmp/titan"
$rdi   : 0x0000000000402004  →  0x3b031b0100006968 ("hi"?)
$rip   : 0x00007ffff7e4dcc0  →  <puts+0> push r14
$r8    : 0x00007ffff7fb0a40  →  0x0000000000000000
$r9    : 0x00007ffff7fb0a40  →  0x0000000000000000
$r10   : 0x3               
$r11   : 0x00007ffff7e4dcc0  →  <puts+0> push r14
$r12   : 0x0000000000401060  →  <_start+0> xor ebp, ebp
$r13   : 0x00007fffffffe0e0  →  0x0000000000000001
$r14   : 0x0               
$r15   : 0x0               
$eflags: [zero carry PARITY adjust sign trap INTERRUPT direction overflow resume virtualx86 identification]
$cs: 0x0033 $ss: 0x002b $ds: 0x0000 $es: 0x0000 $fs: 0x0000 $gs: 0x0000
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── stack ────
0x00007fffffffdfd8│+0x0000: 0x0000000000401165  →  <main+35> mov rdx, QWORD PTR [rip+0x2ed4]        # 0x404040 <stdin@@GLIBC_2.2.5>     ← $rsp
0x00007fffffffdfe0│+0x0008: 0x00000000004011a0  →  <__libc_csu_init+0> push r15
0x00007fffffffdfe8│+0x0010: 0x0000000000401060  →  <_start+0> xor ebp, ebp
0x00007fffffffdff0│+0x0018: 0x00007fffffffe0e0  →  0x0000000000000001
0x00007fffffffdff8│+0x0020: 0xf2a5b1c2e2ab0300
0x00007fffffffe000│+0x0028: 0x00000000004011a0  →  <__libc_csu_init+0> push r15     ← $rbp
0x00007fffffffe008│+0x0030: 0x00007ffff7df0b6b  →  <__libc_start_main+235> mov edi, eax
0x00007fffffffe010│+0x0038: 0x00007ffff7fab4d8  →  0x00007ffff7df0450  →  <init_cacheinfo+0> push r15
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── code:x86:64 ────
   0x7ffff7e4dcb1 <popen+145>      ret    
   0x7ffff7e4dcb2                  nop    WORD PTR cs:[rax+rax*1+0x0]
   0x7ffff7e4dcbc                  nop    DWORD PTR [rax+0x0]
 → 0x7ffff7e4dcc0 <puts+0>         push   r14
   0x7ffff7e4dcc2 <puts+2>         push   r13
   0x7ffff7e4dcc4 <puts+4>         mov    r13, rdi
   0x7ffff7e4dcc7 <puts+7>         push   r12
   0x7ffff7e4dcc9 <puts+9>         push   rbp
   0x7ffff7e4dcca <puts+10>        push   rbx
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "titan", stopped, reason: BREAKPOINT
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── trace ────
[#0] 0x7ffff7e4dcc0 → __GI__IO_puts(str=0x402004 "hi")
[#1] 0x401165 → main()
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
gef➤  
=======
Breakpoint 1 at 0x80482d0
gef➤  r
Starting program: /home/devey/nightmare/modules/02-intro_tooling/hello_world 
[ Legend: Modified register | Code | Heap | Stack | String ]
────────────────────────────────────────────────────────────────────── registers ────
$eax   : 0xf7fb9dd8  →  0xffffd19c  →  0xffffd389  →  "CLUTTER_IM_MODULE=xim"
$ebx   : 0x0       
$ecx   : 0xffffd100  →  0x00000001
$edx   : 0xffffd124  →  0x00000000
$esp   : 0xffffd0cc  →  0x08048419  →  <main+30> add esp, 0x10
$ebp   : 0xffffd0e8  →  0x00000000
$esi   : 0xf7fb8000  →  0x001d4d6c
$edi   : 0x0       
$eip   : 0xf7e4a360  →  <puts+0> push ebp
$eflags: [zero carry parity ADJUST SIGN trap INTERRUPT direction overflow resume virtualx86 identification]
$cs: 0x0023 $ss: 0x002b $ds: 0x002b $es: 0x002b $fs: 0x0000 $gs: 0x0063 
────────────────────────────────────────────────────────────────────────── stack ────
0xffffd0cc│+0x0000: 0x08048419  →  <main+30> add esp, 0x10	 ← $esp
0xffffd0d0│+0x0004: 0x080484b0  →  "hello world!"
0xffffd0d4│+0x0008: 0xffffd194  →  0xffffd34e  →  "/home/devey/nightmare/modules/02-intro_tooling/hel[...]"
0xffffd0d8│+0x000c: 0xffffd19c  →  0xffffd389  →  "CLUTTER_IM_MODULE=xim"
0xffffd0dc│+0x0010: 0x08048451  →  <__libc_csu_init+33> lea eax, [ebx-0xf8]
0xffffd0e0│+0x0014: 0xf7fe59b0  →   push ebp
0xffffd0e4│+0x0018: 0xffffd100  →  0x00000001
0xffffd0e8│+0x001c: 0x00000000	 ← $ebp
──────────────────────────────────────────────────────────────────── code:x86:32 ────
   0xf7e4a356 <popen+134>      call   0xf7dfb608 <free@plt>
   0xf7e4a35b <popen+139>      add    esp, 0x10
   0xf7e4a35e <popen+142>      jmp    0xf7e4a333 <popen+99>
 → 0xf7e4a360 <puts+0>         push   ebp
   0xf7e4a361 <puts+1>         mov    ebp, esp
   0xf7e4a363 <puts+3>         push   edi
   0xf7e4a364 <puts+4>         push   esi
   0xf7e4a365 <puts+5>         push   ebx
   0xf7e4a366 <puts+6>         call   0xf7f17c89
──────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "hello_world", stopped 0xf7e4a360 in puts (), reason: BREAKPOINT
────────────────────────────────────────────────────────────────────────── trace ────
[#0] 0xf7e4a360 → puts()
[#1] 0x8048419 → main()
─────────────────────────────────────────────────────────────────────────────────────

Breakpoint 1, 0xf7e4a360 in puts () from /lib32/libc.so.6

>>>>>>> 62e51517054901aa0b7fd1508d70dcb095961589
```

## Viewing Things

<<<<<<< HEAD
So one thing that gdb is really useful for is viewing the values of different things. Once we are dropped into a debugger while the process is viewing, let's view the contents of the `rdi` register:

```
Breakpoint 1, 0x0000000000401160 in main ()
[ Legend: Modified register | Code | Heap | Stack | String ]
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── registers ────
$rax   : 0x0               
$rbx   : 0x0               
$rcx   : 0x00000000004011a0  →  <__libc_csu_init+0> push r15
$rdx   : 0x00007fffffffe0f8  →  0x00007fffffffe412  →  "SHELL=/bin/bash"
$rsp   : 0x00007fffffffdfe0  →  0x00000000004011a0  →  <__libc_csu_init+0> push r15
$rbp   : 0x00007fffffffe000  →  0x00000000004011a0  →  <__libc_csu_init+0> push r15
$rsi   : 0x00007fffffffe0e8  →  0x00007fffffffe407  →  "/tmp/titan"
$rdi   : 0x0000000000402004  →  0x3b031b0100006968 ("hi"?)
$rip   : 0x0000000000401160  →  <main+30> call 0x401030 <puts@plt>
$r8    : 0x00007ffff7fb0a40  →  0x0000000000000000
$r9    : 0x00007ffff7fb0a40  →  0x0000000000000000
$r10   : 0x1               
$r11   : 0x206             
$r12   : 0x0000000000401060  →  <_start+0> xor ebp, ebp
$r13   : 0x00007fffffffe0e0  →  0x0000000000000001
$r14   : 0x0               
$r15   : 0x0               
$eflags: [ZERO carry PARITY adjust sign trap INTERRUPT direction overflow resume virtualx86 identification]
$cs: 0x0033 $ss: 0x002b $ds: 0x0000 $es: 0x0000 $fs: 0x0000 $gs: 0x0000
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── stack ────
0x00007fffffffdfe0│+0x0000: 0x00000000004011a0  →  <__libc_csu_init+0> push r15     ← $rsp
0x00007fffffffdfe8│+0x0008: 0x0000000000401060  →  <_start+0> xor ebp, ebp
0x00007fffffffdff0│+0x0010: 0x00007fffffffe0e0  →  0x0000000000000001
0x00007fffffffdff8│+0x0018: 0x0a17c82ca27b0d00
0x00007fffffffe000│+0x0020: 0x00000000004011a0  →  <__libc_csu_init+0> push r15     ← $rbp
0x00007fffffffe008│+0x0028: 0x00007ffff7df0b6b  →  <__libc_start_main+235> mov edi, eax
0x00007fffffffe010│+0x0030: 0x00007ffff7fab4d8  →  0x00007ffff7df0450  →  <init_cacheinfo+0> push r15
0x00007fffffffe018│+0x0038: 0x00007fffffffe0e8  →  0x00007fffffffe407  →  "/tmp/titan"
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── code:x86:64 ────
     0x401153 <main+17>        mov    QWORD PTR [rbp-0x8], rax
     0x401157 <main+21>        xor    eax, eax
     0x401159 <main+23>        lea    rdi, [rip+0xea4]        # 0x402004
 →   0x401160 <main+30>        call   0x401030 <puts@plt>
   ↳    0x401030 <puts@plt+0>     jmp    QWORD PTR [rip+0x2fe2]        # 0x404018 <puts@got.plt>
        0x401036 <puts@plt+6>     push   0x0
        0x40103b <puts@plt+11>    jmp    0x401020
        0x401040 <__stack_chk_fail@plt+0> jmp    QWORD PTR [rip+0x2fda]        # 0x404020 <__stack_chk_fail@got.plt>
        0x401046 <__stack_chk_fail@plt+6> push   0x1
        0x40104b <__stack_chk_fail@plt+11> jmp    0x401020
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── arguments (guessed) ────
puts@plt (
   $rdi = 0x0000000000402004 → 0x3b031b0100006968 ("hi"?),
   $rsi = 0x00007fffffffe0e8 → 0x00007fffffffe407 → "/tmp/titan",
   $rdx = 0x00007fffffffe0f8 → 0x00007fffffffe412 → "SHELL=/bin/bash"
)
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "titan", stopped, reason: BREAKPOINT
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── trace ────
[#0] 0x401160 → main()
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
gef➤  p $rdi
$1 = 0x402004
```

So we can see that the register `rdi` holds the value `0x402004`, which is a pointer. Let's see what it points to:

```
gef➤  x/g 0x402004
0x402004:    0x3b031b0100006968
gef➤  x/s 0x402004
0x402004:    "hi"
```

So we can see that it points to the string `hi`, which will be printed by `puts` (since `puts` takes a single argument which is a char pointer). One thing in gdb when you examine things with `x`, you can specify what you want to examine it as. Possible things include as a string `x/s`, as a qword `x/g`, or as a dword `x/w`.
=======
So one thing that gdb is really useful for is viewing the values of different things. Once we are dropped into a debugger while the process is viewing, let's view the contents of the `esp` register. To get there we will break on main, run, and then advance three instructions: 

```
gef➤  break main 
gef➤  run
gef➤  nexti
gef➤  nexti
[ Legend: Modified register | Code | Heap | Stack | String ]
────────────────────────────────────────────────────────────────────── registers ────
$eax   : 0xf7fb9dd8  →  0xffffd19c  →  0xffffd389  →  "CLUTTER_IM_MODULE=xim"
$ebx   : 0x0       
$ecx   : 0xffffd100  →  0x00000001
$edx   : 0xffffd124  →  0x00000000
$esp   : 0xffffd0d4  →  0xffffd194  →  0xffffd34e  →  "/home/devey/nightmare/modules/02-intro_tooling/hel[...]"
$ebp   : 0xffffd0e8  →  0x00000000
$esi   : 0xf7fb8000  →  0x001d4d6c
$edi   : 0x0       
$eip   : 0x0804840f  →  <main+20> push 0x80484b0
$eflags: [zero carry PARITY ADJUST SIGN trap INTERRUPT direction overflow resume virtualx86 identification]
$cs: 0x0023 $ss: 0x002b $ds: 0x002b $es: 0x002b $fs: 0x0000 $gs: 0x0063 
────────────────────────────────────────────────────────────────────────── stack ────
0xffffd0d4│+0x0000: 0xffffd194  →  0xffffd34e  →  "/home/devey/nightmare/modules/02-intro_tooling/hel[...]"	 ← $esp
0xffffd0d8│+0x0004: 0xffffd19c  →  0xffffd389  →  "CLUTTER_IM_MODULE=xim"
0xffffd0dc│+0x0008: 0x08048451  →  <__libc_csu_init+33> lea eax, [ebx-0xf8]
0xffffd0e0│+0x000c: 0xf7fe59b0  →   push ebp
0xffffd0e4│+0x0010: 0xffffd100  →  0x00000001
0xffffd0e8│+0x0014: 0x00000000	 ← $ebp
0xffffd0ec│+0x0018: 0xf7dfbe81  →  <__libc_start_main+241> add esp, 0x10
0xffffd0f0│+0x001c: 0xf7fb8000  →  0x001d4d6c
──────────────────────────────────────────────────────────────────── code:x86:32 ────
    0x8048407 <main+12>        in     eax, 0x51
    0x8048409 <main+14>        sub    esp, 0x4
    0x804840c <main+17>        sub    esp, 0xc
 →  0x804840f <main+20>        push   0x80484b0
    0x8048414 <main+25>        call   0x80482d0 <puts@plt>
    0x8048419 <main+30>        add    esp, 0x10
    0x804841c <main+33>        mov    eax, 0x0
    0x8048421 <main+38>        mov    ecx, DWORD PTR [ebp-0x4]
    0x8048424 <main+41>        leave  
──────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "hello_world", stopped 0x804840f in main (), reason: SINGLE STEP
────────────────────────────────────────────────────────────────────────── trace ────
[#0] 0x804840f → main()
─────────────────────────────────────────────────────────────────────────────────────
0x0804840f in main ()
gef➤  p 0x80484b0
$1 = 0x80484b0
gef➤  x/10c 0x80484b0
0x80484b0:	0x68	0x65	0x6c	0x6c	0x6f	0x20	0x77	0x6f
0x80484b8:	0x72	0x6c
gef➤  x/s 0x80484b0
0x80484b0:	"hello world!"

gef➤  

```

We can see that the register `esp` holds the value `0xffffd0d0`, which is a pointer. Let's see what it points to:

```
gef➤  x/a 0xffffd0d0
0xffffd0d0:	0x80484b0
gef➤  x/10c 0x80484b0
0x80484b0:	0x68	0x65	0x6c	0x6c	0x6f	0x20	0x77	0x6f
0x80484b8:	0x72	0x6c
gef➤  x/s 0x80484b0
0x80484b0:	"hello world!"
```

So we can see that it points to the string `hello world!`, which will be printed by `puts` (since `puts` takes a single argument which is a char pointer). One thing in gdb when you examine things with `x`, you can specify what you want to examine it as. Possible things include as an address `x/a`, a number of characters `x/10c` string `x/s`, as a qword `x/g`, or as a dword `x/w`.
>>>>>>> 62e51517054901aa0b7fd1508d70dcb095961589

let's view the contents of all of the registers:

```
gef➤  info registers
<<<<<<< HEAD
rax            0x0                 0x0
rbx            0x0                 0x0
rcx            0x4011a0            0x4011a0
rdx            0x7fffffffe0f8      0x7fffffffe0f8
rsi            0x7fffffffe0e8      0x7fffffffe0e8
rdi            0x402004            0x402004
rbp            0x7fffffffe000      0x7fffffffe000
rsp            0x7fffffffdfe0      0x7fffffffdfe0
r8             0x7ffff7fb0a40      0x7ffff7fb0a40
r9             0x7ffff7fb0a40      0x7ffff7fb0a40
r10            0x1                 0x1
r11            0x206               0x206
r12            0x401060            0x401060
r13            0x7fffffffe0e0      0x7fffffffe0e0
r14            0x0                 0x0
r15            0x0                 0x0
rip            0x401160            0x401160 <main+30>
eflags         0x246               [ PF ZF IF ]
cs             0x33                0x33
ss             0x2b                0x2b
ds             0x0                 0x0
es             0x0                 0x0
fs             0x0                 0x0
gs             0x0                 0x0
=======
eax            0xf7fb9dd8	0xf7fb9dd8
ecx            0xffffd100	0xffffd100
edx            0xffffd124	0xffffd124
ebx            0x0	0x0
esp            0xffffd0d0	0xffffd0d0
ebp            0xffffd0e8	0xffffd0e8
esi            0xf7fb8000	0xf7fb8000
edi            0x0	0x0
eip            0x8048414	0x8048414 <main+25>
eflags         0x296	[ PF AF SF IF ]
cs             0x23	0x23
ss             0x2b	0x2b
ds             0x2b	0x2b
es             0x2b	0x2b
fs             0x0	0x0
gs             0x63	0x63

>>>>>>> 62e51517054901aa0b7fd1508d70dcb095961589
```

Now let's view the stack frame:

```
gef➤  info frame
<<<<<<< HEAD
Stack level 0, frame at 0x7fffffffe010:
 rip = 0x401160 in main; saved rip = 0x7ffff7df0b6b
 Arglist at 0x7fffffffe000, args:
 Locals at 0x7fffffffe000, Previous frame's sp is 0x7fffffffe010
 Saved registers:
  rbp at 0x7fffffffe000, rip at 0x7fffffffe008
=======
Stack level 0, frame at 0xffffd100:
 eip = 0x8048414 in main; saved eip = 0xf7dfbe81
 Arglist at 0xffffd0e8, args: 
 Locals at 0xffffd0e8, Previous frame's sp is 0xffffd100
 Saved registers:
  ebp at 0xffffd0e8, eip at 0xffffd0fc

>>>>>>> 62e51517054901aa0b7fd1508d70dcb095961589
```

Now let's view the disassembly for the main function:

```
<<<<<<< HEAD
gef➤  disas main
Dump of assembler code for function main:
   0x0000000000401142 <+0>:    push   rbp
   0x0000000000401143 <+1>:    mov    rbp,rsp
   0x0000000000401146 <+4>:    sub    rsp,0x20
   0x000000000040114a <+8>:    mov    rax,QWORD PTR fs:0x28
   0x0000000000401153 <+17>:    mov    QWORD PTR [rbp-0x8],rax
   0x0000000000401157 <+21>:    xor    eax,eax
   0x0000000000401159 <+23>:    lea    rdi,[rip+0xea4]        # 0x402004
=> 0x0000000000401160 <+30>:    call   0x401030 <puts@plt>
   0x0000000000401165 <+35>:    mov    rdx,QWORD PTR [rip+0x2ed4]        # 0x404040 <stdin@@GLIBC_2.2.5>
   0x000000000040116c <+42>:    lea    rax,[rbp-0x12]
   0x0000000000401170 <+46>:    mov    esi,0x9
   0x0000000000401175 <+51>:    mov    rdi,rax
   0x0000000000401178 <+54>:    call   0x401050 <fgets@plt>
   0x000000000040117d <+59>:    nop
   0x000000000040117e <+60>:    mov    rax,QWORD PTR [rbp-0x8]
   0x0000000000401182 <+64>:    xor    rax,QWORD PTR fs:0x28
   0x000000000040118b <+73>:    je     0x401192 <main+80>
   0x000000000040118d <+75>:    call   0x401040 <__stack_chk_fail@plt>
   0x0000000000401192 <+80>:    leave  
   0x0000000000401193 <+81>:    ret    
End of assembler dump.
=======
gef➤  disass main
Dump of assembler code for function main:
   0x080483fb <+0>:	lea    ecx,[esp+0x4]
   0x080483ff <+4>:	and    esp,0xfffffff0
   0x08048402 <+7>:	push   DWORD PTR [ecx-0x4]
   0x08048405 <+10>:	push   ebp
   0x08048406 <+11>:	mov    ebp,esp
   0x08048408 <+13>:	push   ecx
   0x08048409 <+14>:	sub    esp,0x4
   0x0804840c <+17>:	sub    esp,0xc
   0x0804840f <+20>:	push   0x80484b0
=> 0x08048414 <+25>:	call   0x80482d0 <puts@plt>
   0x08048419 <+30>:	add    esp,0x10
   0x0804841c <+33>:	mov    eax,0x0
   0x08048421 <+38>:	mov    ecx,DWORD PTR [ebp-0x4]
   0x08048424 <+41>:	leave  
   0x08048425 <+42>:	lea    esp,[ecx-0x4]
   0x08048428 <+45>:	ret    
End of assembler dump.

>>>>>>> 62e51517054901aa0b7fd1508d70dcb095961589
```

## Changing Values

<<<<<<< HEAD
Let's say we wanted to change the contents of the `rdi` register:

```
gef➤  p $rdi
$2 = 0x402004
gef➤  set $rdi = 0x0
gef➤  p $rdi
$3 = 0x0
```

Now let's say we wanted to change the value stored at the memory address `0x402004` to `0xfacade`:

```
gef➤  x/g 0x402004
0x402004:    0x3b031b0100006968
gef➤  set *0x402004 = 0xfacade
gef➤  x/g 0x402004
0x402004:    0x3b031b0100facade
```

Let's say we wanted to jump directly to an instruction like `0x40117d`, and skip all instructions in between:

```
gef➤  j *0x40117d
Continuing at 0x40117d.
```
=======
As you can see, we are at the instruction for puts. 

Let's say we wanted to change the contents of what will be printed. Importantly, in many programs your ability to do this is dependent on the size of the string you are trying to replace. If you overwrite it with something that is too large, you run the risk of overwriting other memory and breaking the program. There are plenty of workarounds but this is rarely applicable from a bin-ex perspective. 

```
gef➤  set {char [12]} 0x080484b0 = "hello venus"
gef➤  x/s 0x080484b0
0x80484b0:	"hello venus"
gef➤  nexti
hello venus
[ Legend: Modified register | Code | Heap | Stack | String ]
────────────────────────────────────────────────────────────────────── registers ────
$eax   : 0xc       
$ebx   : 0x0       
$ecx   : 0x0804a160  →  "hello venus\n"
$edx   : 0xf7fb9890  →  0x00000000
$esp   : 0xffffd0d0  →  0x080484b0  →  "hello venus"
$ebp   : 0xffffd0e8  →  0x00000000
$esi   : 0xf7fb8000  →  0x001d4d6c
$edi   : 0x0       
$eip   : 0x08048419  →  <main+30> add esp, 0x10
$eflags: [ZERO carry PARITY adjust sign trap INTERRUPT direction overflow resume virtualx86 identification]
$cs: 0x0023 $ss: 0x002b $ds: 0x002b $es: 0x002b $fs: 0x0000 $gs: 0x0063 
────────────────────────────────────────────────────────────────────────── stack ────
0xffffd0d0│+0x0000: 0x080484b0  →  "hello venus"	 ← $esp
0xffffd0d4│+0x0004: 0xffffd194  →  0xffffd34e  →  "/home/devey/nightmare/modules/02-intro_tooling/hel[...]"
0xffffd0d8│+0x0008: 0xffffd19c  →  0xffffd389  →  "CLUTTER_IM_MODULE=xim"
0xffffd0dc│+0x000c: 0x08048451  →  <__libc_csu_init+33> lea eax, [ebx-0xf8]
0xffffd0e0│+0x0010: 0xf7fe59b0  →   push ebp
0xffffd0e4│+0x0014: 0xffffd100  →  0x00000001
0xffffd0e8│+0x0018: 0x00000000	 ← $ebp
0xffffd0ec│+0x001c: 0xf7dfbe81  →  <__libc_start_main+241> add esp, 0x10
──────────────────────────────────────────────────────────────────── code:x86:32 ────
    0x804840c <main+17>        sub    esp, 0xc
    0x804840f <main+20>        push   0x80484b0
    0x8048414 <main+25>        call   0x80482d0 <puts@plt>
 →  0x8048419 <main+30>        add    esp, 0x10
    0x804841c <main+33>        mov    eax, 0x0
    0x8048421 <main+38>        mov    ecx, DWORD PTR [ebp-0x4]
    0x8048424 <main+41>        leave  
    0x8048425 <main+42>        lea    esp, [ecx-0x4]
    0x8048428 <main+45>        ret    
──────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "hello_world", stopped 0x8048419 in main (), reason: SINGLE STEP
────────────────────────────────────────────────────────────────────────── trace ────
[#0] 0x8048419 → main()
─────────────────────────────────────────────────────────────────────────────────────
0x08048419 in main ()

```

Now let's say we wanted to change the value stored at the memory address `0x08048451` to `0xfacade`:

```
gef➤  x/g 0x08048451
0x8048451 <__libc_csu_init+33>:	0xff08838d
gef➤  set *0x08048451 = 0xfacade
gef➤  x/g 0x08048451
0x8048451 <__libc_csu_init+33>:	0xfacade

```

Let's say we wanted to jump directly to an instruction like `0x08048451`, and skip all instructions in between:

```
gef➤  j *0x08048451
Continuing at 0x0x08048451.
```

That was a lot, keep referring to this, your notes, and GDB cheatsheets as you go along. 

>>>>>>> 62e51517054901aa0b7fd1508d70dcb095961589
