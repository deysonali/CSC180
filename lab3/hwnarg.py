import sys

FIN=""
FOUT=""
nargs=len(sys.argv)
skip=False
for i in range(1,nargs):
   if not skip:
      arg=sys.argv[i]
      if arg == "--n":
         if i != nargs-1:
            FIN=sys.argv[i+1]
            skip=True
      elif arg == "--word":
         if i != nargs-1:
            FOUT=sys.argv[i+1]
            skip=True
      else:
         print "ERR: unknown arg:",arg
   else:
      skip=False

for i in range(0,int(FIN)):
	print FOUT


