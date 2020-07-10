# mnemdb.py
A simple command line interface to [mnemdb.json](https://github.com/x64dbg/x64dbg/blob/development/bin/mnemdb.json)
from [x64dbg](https://x64dbg.com/).

## Usage
### Help
```
$ ./mnemdb.py -h
usage: mnemdb.py [-h] [-v] [-s] mnemonic

Displays information about x86-64 assembler mnemonics.

positional arguments:
  mnemonic         mnemonic to display information about

optional arguments:
  -h, --help       show this help message and exit
  -v               selects verbose text (use with less)
  -s, --substring  match for substring of mnemonic
```
### Simple search
```
$ ./mnemdb.py mov
mov	moves data from src to dst
```
### Substring search
```
$ ./mnemdb.py -s mov
bndmov	move bounds
cmova	conditional move - above/not below nor equal (cf=0 and zf=0)
cmovae	conditional move - above or equal/not below/not carry (cf=0)
cmovb	conditional move - below/not above nor equal/carry (cf=1)
cmovbe	conditional move - below or equal/not above (cf=1 or zf=1)
cmovc	conditional move - carry/below/not above or equal (cf=1)
cmove	conditional move - equal/zero (zf=1)
[ ... ]
```
### Verbose mode
```
$ ./mnemdb.py -v mov
MOV-Move
 Opcode              Instruction           Op/   64-Bit   Compat/ Description
                                           En    Mode     Leg Mode
 88 /r               MOV r/m8,r8           MR    Valid    Valid    Move r8 to r/m8.
 REX + 88 /r         MOV r/m8***,r8***     MR    Valid    N.E.     Move r8 to r/m8.
 89 /r               MOV r/m16,r16         MR    Valid    Valid    Move r16 to r/m16.
 89 /r               MOV r/m32,r32         MR    Valid    Valid    Move r32 to r/m32.
 REX.W + 89 /r       MOV r/m64,r64         MR    Valid    N.E.     Move r64 to r/m64.
 8A /r               MOV r8,r/m8           RM    Valid    Valid    Move r/m8 to r8.
[ ... ]
```
A large terminal window and/or piping to `less` is recommended.
