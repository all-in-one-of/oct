#!/usr/bin/env python
# coding=utf-8

from __future__ import with_statement #only needed for maya 2008 & 2009


def FKNC_Optimize_run():
    import FKNC_OpTools
    FKNC_OpTools.FKNC_Optimize()

def FKNC_SelectRoot():
    import FKNC_OpTools
    FKNC_OpTools.SelectRootFolder()

def FKNC_DeleteAndOptize():
    import FKNC_OpTools
    FKNC_OpTools.DeleteConAndOptimize()