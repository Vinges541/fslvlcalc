import argparse
import logging
parser = argparse.ArgumentParser(
    description="Photos sorting using their timestamps and camera's model name")
parser.add_argument(
    'game', choices=['dss', 'ds1', 'ds2', 'bb', 'ds3', 'ssdt', 'er'])
parser.add_argument('current_level', type=int)
parser.add_argument('desired_level', type=int)
args = parser.parse_args()

if args.current_level < 1:
    logging.critical("Wrong current level!")
    exit(-1)


def dss(curr_lvl, des_lvl):
    raise NotImplementedError


def ds1(curr_lvl, des_lvl):
    raise NotImplementedError


def ds2(curr_lvl, des_lvl):
    raise NotImplementedError


def bb(curr_lvl, des_lvl):
    raise NotImplementedError


def ds3(curr_lvl, des_lvl):
    curr_lvl: int = args.current_level + 1
    des_lvl: int = args.desired_level
    needed_souls = 0

    while curr_lvl <= des_lvl:
        c = curr_lvl
        b = curr_lvl * curr_lvl
        a = b * curr_lvl

        if curr_lvl >= 12:
            a *= 0.02
            b *= 3.06
            c *= 105.6
            needed_souls += round(a + b + c) - 895
        elif curr_lvl >= 1 and curr_lvl < 12:
            a *= 0.0068
            b *= 0.06
            c *= 17.1
            needed_souls += round(a + b + c) + 639

        curr_lvl += 1
    return needed_souls


def ssdt(curr_lvl, des_lvl):
    raise NotImplementedError


def er(curr_lvl, des_lvl):
    raise NotImplementedError


lcalc = [dss, ds1, ds2, bb, ds3, ssdt, er]
dcalc = {func.__name__: func for func in lcalc}


needed_souls = dcalc[args.game](args.current_level, args.desired_level)
print(f"You need {needed_souls:,} souls")
