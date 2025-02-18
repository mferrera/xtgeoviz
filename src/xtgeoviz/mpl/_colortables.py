# -*- coding: utf-8 -*-
"""Module for color tables."""

import logging
import os
import random

logger = logging.getLogger(__name__)


def random40():
    """Random but fixed color table with 40 entries, mostly for testing."""

    ctable = [
        (0.83345071168299956, 0.2382011018575051, 0.6457693086399422),
        (0.541018453798349, 0.48038587236806063, 0.9151873938263322),
        (0.10882072036344093, 0.8838633180878654, 0.5133890790690832),
        (0.0021118859288566, 0.23207523745480785, 0.87105494758907984),
        (0.9167955510272826, 0.06636986706409276, 0.2085761696435795),
        (0.95445330127180916, 0.92537092140778787, 0.5643674283342163),
        (0.1118142610865344, 0.8753812704140146, 0.882396282596847),
        (0.9169300859386396, 0.94501442557231312, 0.01407158657305927),
        (0.878693250908883, 0.11222139418674728, 0.6167801456569036),
        (0.5256939400784498, 0.11435373675297966, 0.48354476358995946),
        (0.48340383516545826, 0.6410572769763058, 0.29403657486119683),
        (0.311139625063827, 0.9263058894491734, 0.7287039866021682),
        (0.8598753478111007, 0.9018735026443733, 0.6313058592961296),
        (0.43793800204923883, 0.2921469762701936, 0.2098830453305408),
        (0.7381272212655949, 0.1156423111704514, 0.2452716196308139),
        (0.21717885649022806, 0.3046216797738889, 0.6714686237358712),
        (0.0070595461262333, 0.714345667698068, 0.34723053474857124),
        (0.9745984699708928, 0.4730239548162848, 0.15007860849878418),
        (0.6833692521550699, 0.4228448482259841, 0.0044103854819418364),
        (0.5691320165209793, 0.08796666338494852, 0.8035539289654177),
        (0.34042801546149426, 0.47713419001045765, 0.20879105326096692),
        (0.3085826005434883, 0.5079488187213768, 0.4608596310424611),
        (0.9396543635576965, 0.0064011918231481335, 0.2812656314040958),
        (0.5217398018516609, 0.2575024696206665, 0.4677374482174591),
        (0.42127435507233524, 0.8568338738437583, 0.7638805644700677),
        (0.09602707599420568, 0.3864069927590945, 0.6039576328011579),
        (0.16897839817549498, 0.7065043632174942, 0.8423968298858847),
        (0.2986608595521294, 0.6791125573730088, 0.5589263091038545),
        (0.445032995863182, 0.3024296426041809, 0.887087647343199),
        (0.40061174588633763, 0.8547027289892815, 0.822969921567935),
        (0.6547824166299984, 0.9159072024952073, 0.5999250835064326),
        (0.6234796486190842, 0.9312014083676132, 0.2705486337045906),
        (0.46405899784500193, 0.5740384701517647, 0.6154775367548058),
        (0.5479496115847091, 0.607922568141698, 0.48482790495317296),
        (0.950508478466332, 0.15137736802206792, 0.277696533485587),
        (0.27606819502763125, 0.7150787664103754, 0.9004516278146157),
        (0.41462932348169335, 0.1546152675658281, 0.6024802500176701),
        (0.26316035181248487, 0.9924296950259774, 0.012858089574406706),
        (0.6058186938654891, 0.8263245802609571, 0.5632477188449058),
        (0.18715791502874501, 0.8748052205404021, 0.43694647042971213),
    ]

    return ctable


def randomc(nlen):
    """Get a truly random color table with nlen entries."""

    ctable = []
    for _ic in range(nlen):
        red = random.uniform(0, 1)
        green = random.uniform(0, 1)
        blue = random.uniform(0, 1)
        ctable.append((red, green, blue))

    return ctable


def xtgeocolors():
    """Get the XTGeo color table which is basic inherited from old IRAP."""

    ctable = [
        (0.500, 0.500, 0.500),  # CGM colour 0 is "dummy" grey
        (0.000, 0.000, 0.000),
        (1.000, 0.000, 0.000),
        (0.000, 1.000, 0.000),
        (0.000, 0.000, 1.000),
        (0.000, 1.000, 1.000),
        (1.000, 0.408, 0.729),
        (1.000, 1.000, 0.000),
        (0.800, 0.196, 0.600),
        (1.000, 0.800, 0.498),
        (1.000, 0.000, 1.000),
        (0.576, 0.859, 0.439),
        (0.498, 1.000, 0.000),
        (0.800, 0.498, 0.196),
        (0.498, 0.000, 1.000),
        (1.000, 0.498, 0.000),
        (0.918, 0.678, 0.918),
        (0.000, 0.000, 0.000),
        (0.059, 0.059, 0.059),
        (0.129, 0.129, 0.129),
        (0.200, 0.200, 0.200),
        (0.259, 0.259, 0.259),
        (0.322, 0.322, 0.322),
        (0.388, 0.388, 0.388),
        (0.471, 0.471, 0.471),
        (0.541, 0.541, 0.541),
        (0.612, 0.612, 0.612),
        (0.671, 0.671, 0.671),
        (0.729, 0.729, 0.729),
        (0.788, 0.788, 0.788),
        (0.851, 0.851, 0.851),
        (0.929, 0.929, 0.929),
        (1.000, 1.000, 1.000),
        (0.000, 0.000, 0.000),
        (0.141, 0.000, 0.000),
        (0.282, 0.000, 0.000),
        (0.424, 0.000, 0.000),
        (0.565, 0.000, 0.000),
        (0.706, 0.000, 0.000),
        (0.847, 0.000, 0.000),
        (0.988, 0.000, 0.000),
        (0.988, 0.122, 0.122),
        (0.988, 0.243, 0.243),
        (0.988, 0.365, 0.365),
        (0.988, 0.486, 0.486),
        (0.988, 0.608, 0.608),
        (0.988, 0.729, 0.729),
        (0.988, 0.851, 0.851),
        (0.988, 0.973, 0.973),
        (0.000, 0.000, 0.000),
        (0.000, 0.141, 0.000),
        (0.000, 0.282, 0.000),
        (0.000, 0.424, 0.000),
        (0.000, 0.565, 0.000),
        (0.000, 0.706, 0.000),
        (0.000, 0.847, 0.000),
        (0.000, 0.988, 0.000),
        (0.122, 0.988, 0.122),
        (0.243, 0.988, 0.243),
        (0.365, 0.988, 0.365),
        (0.486, 0.988, 0.486),
        (0.608, 0.988, 0.608),
        (0.729, 0.988, 0.729),
        (0.851, 0.988, 0.851),
        (0.973, 0.988, 0.973),
        (0.000, 0.000, 0.000),
        (0.000, 0.000, 0.141),
        (0.000, 0.000, 0.282),
        (0.000, 0.000, 0.424),
        (0.000, 0.000, 0.565),
        (0.000, 0.000, 0.706),
        (0.000, 0.000, 0.847),
        (0.000, 0.000, 0.988),
        (0.122, 0.122, 0.988),
        (0.243, 0.243, 0.988),
        (0.365, 0.365, 0.988),
        (0.486, 0.486, 0.988),
        (0.608, 0.608, 0.988),
        (0.729, 0.729, 0.988),
        (0.851, 0.851, 0.988),
        (0.973, 0.973, 0.988),
        (0.000, 0.000, 0.000),
        (0.141, 0.141, 0.000),
        (0.282, 0.282, 0.000),
        (0.424, 0.424, 0.000),
        (0.565, 0.565, 0.000),
        (0.706, 0.706, 0.000),
        (0.847, 0.847, 0.000),
        (0.988, 0.988, 0.000),
        (0.988, 0.988, 0.122),
        (0.988, 0.988, 0.243),
        (0.988, 0.988, 0.365),
        (0.988, 0.988, 0.486),
        (0.988, 0.988, 0.608),
        (0.988, 0.988, 0.729),
        (0.988, 0.988, 0.851),
        (0.988, 0.988, 0.973),
        (0.298, 0.298, 1.000),
        (0.549, 0.298, 1.000),
        (0.749, 0.298, 1.000),
        (0.867, 0.298, 1.000),
        (0.929, 0.298, 1.000),
        (1.000, 0.298, 1.000),
        (1.000, 0.298, 0.929),
        (1.000, 0.298, 0.867),
        (1.000, 0.298, 0.749),
        (1.000, 0.298, 0.549),
        (1.000, 0.298, 0.298),
        (1.000, 0.549, 0.298),
        (1.000, 0.749, 0.298),
        (1.000, 0.867, 0.298),
        (1.000, 0.929, 0.298),
        (1.000, 1.000, 0.298),
        (0.929, 1.000, 0.298),
        (0.867, 1.000, 0.298),
        (0.749, 1.000, 0.298),
        (0.549, 1.000, 0.298),
        (0.298, 1.000, 0.298),
        (0.298, 1.000, 0.549),
        (0.298, 1.000, 0.749),
        (0.298, 1.000, 0.867),
        (0.298, 1.000, 0.929),
        (0.298, 1.000, 1.000),
        (0.298, 0.929, 1.000),
        (0.298, 0.867, 1.000),
        (0.298, 0.749, 1.000),
        (0.298, 0.549, 1.000),
        (1.000, 1.000, 1.000),
        (1.000, 1.000, 1.000),
        (0.208, 0.208, 0.698),
        (0.384, 0.208, 0.698),
        (0.522, 0.208, 0.698),
        (0.608, 0.208, 0.698),
        (0.651, 0.208, 0.698),
        (0.698, 0.208, 0.698),
        (0.698, 0.208, 0.651),
        (0.698, 0.208, 0.608),
        (0.698, 0.208, 0.522),
        (0.698, 0.208, 0.384),
        (0.698, 0.208, 0.208),
        (0.698, 0.384, 0.208),
        (0.698, 0.522, 0.208),
        (0.698, 0.608, 0.208),
        (0.698, 0.651, 0.208),
        (0.698, 0.698, 0.208),
        (0.651, 0.698, 0.208),
        (0.608, 0.698, 0.208),
        (0.522, 0.698, 0.208),
        (0.384, 0.698, 0.208),
        (0.208, 0.698, 0.208),
        (0.208, 0.698, 0.384),
        (0.208, 0.698, 0.522),
        (0.208, 0.698, 0.608),
        (0.208, 0.698, 0.651),
        (0.208, 0.698, 0.698),
        (0.208, 0.651, 0.698),
        (0.208, 0.608, 0.698),
        (0.208, 0.522, 0.698),
        (0.208, 0.384, 0.698),
        (1.000, 1.000, 1.000),
        (1.000, 1.000, 1.000),
        (0.008, 0.008, 1.000),
        (0.122, 0.008, 1.000),
        (0.247, 0.008, 1.000),
        (0.373, 0.008, 1.000),
        (0.498, 0.008, 1.000),
        (0.624, 0.008, 1.000),
        (0.749, 0.008, 1.000),
        (0.875, 0.008, 1.000),
        (1.000, 0.008, 1.000),
        (1.000, 0.008, 0.875),
        (1.000, 0.008, 0.749),
        (1.000, 0.008, 0.624),
        (1.000, 0.008, 0.498),
        (1.000, 0.008, 0.373),
        (1.000, 0.008, 0.247),
        (1.000, 0.008, 0.122),
        (1.000, 0.008, 0.008),
        (1.000, 0.122, 0.008),
        (1.000, 0.247, 0.008),
        (1.000, 0.373, 0.008),
        (1.000, 0.498, 0.008),
        (1.000, 0.624, 0.008),
        (1.000, 0.749, 0.008),
        (1.000, 0.875, 0.008),
        (1.000, 1.000, 0.008),
        (0.875, 1.000, 0.008),
        (0.749, 1.000, 0.008),
        (0.624, 1.000, 0.008),
        (0.498, 1.000, 0.008),
        (0.373, 1.000, 0.008),
        (0.247, 1.000, 0.008),
        (0.122, 1.000, 0.008),
        (0.008, 1.000, 0.008),
        (0.008, 1.000, 0.122),
        (0.008, 1.000, 0.247),
        (0.008, 1.000, 0.373),
        (0.008, 1.000, 0.498),
        (0.008, 1.000, 0.624),
        (0.008, 1.000, 0.749),
        (0.008, 1.000, 0.875),
        (0.008, 1.000, 1.000),
        (0.008, 0.875, 1.000),
        (0.008, 0.749, 1.000),
        (0.008, 0.624, 1.000),
        (0.008, 0.498, 1.000),
        (0.008, 0.373, 1.000),
        (0.008, 0.247, 1.000),
        (0.008, 0.122, 1.000),
        (0.000, 1.000, 0.000),
        (0.000, 1.000, 0.039),
        (0.000, 1.000, 0.078),
        (0.000, 1.000, 0.118),
        (0.000, 1.000, 0.157),
        (0.000, 1.000, 0.196),
        (0.000, 1.000, 0.235),
        (0.000, 1.000, 0.275),
        (0.000, 1.000, 0.314),
        (0.000, 1.000, 0.353),
        (0.000, 1.000, 0.392),
        (0.000, 1.000, 0.431),
        (0.000, 1.000, 0.471),
        (0.000, 1.000, 0.510),
        (0.000, 1.000, 0.549),
        (0.000, 1.000, 0.588),
        (0.000, 1.000, 0.627),
        (0.000, 1.000, 0.667),
        (0.000, 1.000, 0.706),
        (0.000, 1.000, 0.745),
        (0.000, 1.000, 0.784),
        (0.000, 1.000, 0.824),
        (1.000, 0.000, 1.000),
        (1.000, 0.039, 1.000),
        (1.000, 0.078, 1.000),
        (1.000, 0.118, 1.000),
        (1.000, 0.157, 1.000),
        (1.000, 0.196, 1.000),
        (1.000, 0.235, 1.000),
        (1.000, 0.275, 1.000),
        (1.000, 0.314, 1.000),
        (1.000, 0.353, 1.000),
        (1.000, 0.392, 1.000),
        (1.000, 0.431, 1.000),
        (1.000, 0.471, 1.000),
        (1.000, 0.510, 1.000),
        (1.000, 0.549, 1.000),
        (1.000, 0.588, 1.000),
        (1.000, 0.627, 1.000),
        (1.000, 0.667, 1.000),
        (1.000, 0.706, 1.000),
        (1.000, 0.745, 1.000),
        (1.000, 0.784, 1.000),
        (1.000, 0.824, 1.000),
        (1.000, 0.863, 1.000),
        (1.000, 1.000, 1.000),
        (1.000, 1.000, 1.000),
    ]

    return ctable


def colorsfromfile(fname, fformat="rms"):
    """Read a color table from a file."""

    logger.info("Default style is %s", fformat)
    ctable = []

    if not os.path.isfile(fname):
        raise IOError(f"Color file not found: {fname}")

    with open(fname, "r", encoding="utf-8") as fc:
        for line in fc:
            if line.startswith("ColorMap.color("):
                _key, _eq, rgb1, rgb2, rgb3 = line.split()
                ctable.append((float(rgb1), float(rgb2), float(rgb3)))

    return ctable
