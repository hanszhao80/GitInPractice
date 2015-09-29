#-*- coding:utf-8 –*-
import argparse

parser = argparse.ArgumentParser()
#加入参数简写
parser.add_argument('-v', '--verbose', help="increase output verbosity",
                   action='store_true')
args = parser.parse_args()
if args.verbose:
    print "verbose turned on"
