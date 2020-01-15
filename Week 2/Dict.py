import json,os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--key", help="display a square of a given number",type=str)
parser.add_argument("--val", help="display a square of a given number",type=int)
args = parser.parse_args()
arg= [args.key,arg.val]
arg = input()
with open("storage2.data","r") as f:
    if os.stat("storage2.data").st_size == 0:
        dicts={}
    else:
         dicts = json.load(f)
with open("storage2.data", "w") as f:
    if (len(arg)==1) and (arg[0] in dicts):
        print(dicts[arg[0]])
    elif (len(arg)==1) and (arg[0] not in dicts):
        print("Don't have '{}' key".format(arg[0]))
    if (len(arg) == 2):
        if arg[0] in dicts:
            dicts[arg[0]]= dicts[arg[0]]+", "+arg[1]
        else:
            dicts[arg[0]] = arg[1]
    json.dump(dicts, f)
