#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 10:49:41 2018

@author: ericgrant
"""

import pandas as pd

def rename_cols(df, renames):
    if renames != {}:
        df.rename(columns=renames, inplace=True)

def format_date_cols(df, col_list, tf = None, un = None):
    if col_list != {}:
            for col in col_list:
                df[col] = pd.to_datetime(df[col], format=tf, unit=un)

def format_int_col(df, col_list):
    if col_list != {}:
        for col in col_list: df[col] = pd.to_numeric(df[col], downcast='integer')

def format_int8_col(df, col_list):
    if col_list != {}:
        for col in col_list: df[col] = df[col].astype('int8')

def format_int32_col(df, col_list):
    if col_list != {}:
        for col in col_list: df[col] = df[col].astype('int32')

def format_flt_col(df, col_list):
    if col_list != {}:
        for col in col_list: df[col] = pd.to_numeric(df[col], downcast='float')

def format_str_col(df, col_list):
    if col_list != {}:
        for col in col_list: df[col] = df[col].apply(str)

def format_bool_col(df, col_list):
    if col_list != {}:
        for col in col_list: df[col] = df[col].astype(bool)

def display_cols(df):
    print (df.dtypes)
    for key, val in df.iterrows():
        print (key)
        print (val)