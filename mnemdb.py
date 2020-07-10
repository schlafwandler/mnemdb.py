#!/usr/bin/env python
import json
import argparse
import sys

# mnemdb from the x64dbg project
# https://github.com/x64dbg/x64dbg/blob/development/bin/mnemdb.json
mnemdb_path = sys.path[0] + "/" + "mnemdb.json"

def main():
    parser = argparse.ArgumentParser(description="Displays information about x86-64 assembler mnemonics.")
    parser.add_argument("mnemonic",help="mnemonic to display information about")
    parser.add_argument("-v",action="store_true",help="selects verbose text (use with less)")
    
    args = parser.parse_args()

    with open(mnemdb_path,"r") as f:
        db = json.load(f)
    
    if args.v:
        db_key = 'x86-64'
    else:
        db_key = 'x86-64-brief'

    entries = [e for e in db[db_key] if e["mnem"].lower()==args.mnemonic.lower()]

    if len(entries)==0:
        print("Unknown mnemonic '%s'"%(args.mnemonic))
        return -1

    print(entries[0]['description'])

if __name__=="__main__":
    main()
