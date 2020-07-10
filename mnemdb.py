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
    parser.add_argument("-s","--substring",action="store_true",help="match for substring of mnemonic")
    
    args = parser.parse_args()

    with open(mnemdb_path,"r") as f:
        db = json.load(f)
    
    if args.v:
        db_key = 'x86-64'
    else:
        db_key = 'x86-64-brief'

    if args.substring:
        entries = [e for e in db[db_key] if args.mnemonic.lower() in e["mnem"].lower()]
    else:
        entries = [e for e in db[db_key] if e["mnem"].lower()==args.mnemonic.lower()]

    if len(entries)==0:
        print("Unknown mnemonic '%s'"%(args.mnemonic))
        return -1

    if args.v:
        # print only description in verbose mode
        print(entries[0]['description'])
    else:
        # print mnemonic and shot description in default mode
        for e in entries:
            print(e["mnem"]+"\t"+e["description"])

if __name__=="__main__":
    main()
