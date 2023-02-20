#!/usr/bin/env python

import hashlib
import getpass
import os
import argparse
import json
import subprocess

class Config:
    def __init__(self):
        config_path = os.path.expanduser("~/.config/password-nostore/config")
        config_dictionary = {}
        if os.path.isfile(config_path):
            config_file = open(config_path,"r")
            for line in config_file:
                (key, value) = line.split('=')
                config_dictionary[key.strip()] = value.strip()
        self.dictionary = config_dictionary
    
    def get_default_iteration(self):
        if "use_default_iterations" in self.dictionary and "default_add_iterations" in self.dictionary:
            if self.dictionary["default_add_iterations"].isnumeric() \
                and self.dictionary["use_default_iterations"] in ["y", "Y", "yes", "Yes", "YES", "True", "true", "TRUE"]:
                return int(self.dictionary["default_add_iterations"])
        return "none"
    
            
def hashing_password(conc_str: str, iterations: int):
    hashedpassword_hex = hashlib.sha256(conc_str.encode('utf-8'))
    for i in range(1, iterations):
        hashedpassword_hex = hashlib.sha256(hashedpassword_hex.hexdigest().encode('utf-8'))
    hashedpassword = hashedpassword_hex.hexdigest()
    return(hashedpassword)

def ask_info_form(account_info: dict):
    if 'target' not in account_info:
        account_info['target'] = input('Input target or url: ')
    if 'username' not in account_info:
        account_info['username'] = input('Input username: ')
    if 'additional_iterations' not in account_info:
        if config.get_default_iteration() != 'none':
            account_info['additional_iterations'] = config.get_default_iteration()
        else:
            input_add_iterations = input('Enter the number of additional iterations (default is 100000): ')
            if input_add_iterations != '' and input_add_iterations.isnumeric():
                account_info['additional_iterations'] = int(input_add_iterations)
            else:
                account_info['additional_iterations'] = 0
    password = getpass.getpass('Input password (the input is not visible): ')
    returned_dict = {'account_info': account_info, 'password': password}
    return returned_dict

def ask_what_to_save(account_info: dict):
    what_to_save = input("What from this data you want to save to file? \n [1]target [2]username [3]additional iterations [4]length [5]all of them: ")
    if '5' in what_to_save:
        return account_info
    else:
        save_info = {}
        if '1' in what_to_save:
            save_info['target'] = account_info['target']
        if '2' in what_to_save:
            save_info['username'] = account_info['username']
        if '3' in what_to_save:
            save_info['additional_iterations'] = account_info['additional_iterations']
        if '4' in what_to_save:
            if 'length' in account_info:
                save_info['length'] = account_info['length']
            else:
                print('length is not defined')
        return save_info

def main():
    account_info = {}
    if args.length:
        account_info['length'] = args.length
    file_path = args.file
    if args.save == True:
        ask_overwrite = 'Y'
        if os.path.isfile(file_path):
            ask_overwrite = input('File already exist. Do you want to overwrite your file?: [y/N] ')
    else:
        if os.path.isfile(file_path):
            with open(file_path) as account_file:
                account_info = json.loads(account_file.read())
    result = ask_info_form(account_info)
    account_info = result['account_info']
    password = result['password']
    conc_str  = account_info['target'] + account_info['username'] + password
    iterations = account_info['additional_iterations'] + def_iterations
    if args.save == True:
        account_info_save = ask_what_to_save(account_info)
        if ask_overwrite in ["y", "Y", "yes", "Yes", "YES", "True", "true", "TRUE"]:
            if not os.path.isfile(file_path):
                file_path_list = file_path.split("/")
                file_path_filename = file_path_list[-1]
                file_path_list.pop(-1)
                file_path = './'
                for folder in file_path_list:
                    file_path = file_path + folder + '/'
                if not os.path.isdir(file_path):
                    os.makedirs(file_path)
                file_path = file_path + file_path_filename
            with open(file_path, "w") as account_file:
                account_file.write(json.dumps(account_info_save))
        else:
            print("File not saved")
    hashed_password = hashing_password(conc_str,iterations)
    if 'length' in account_info:
        hashed_password = hashed_password[:account_info['length']]
    if args.clipboard == False:
        print(hashed_password)
    else:
        import clipboard
        clipboard.copy(hashed_password)
        print("Our password copied to clipboard!")

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='Load file with info', type=str, default='')
parser.add_argument('-s', '--save', help='Add to storage', action='store_true', default=False)
parser.add_argument('-c', '--clipboard', help='Copy password to clipboard instead on std::out', action='store_true', default=False)
parser.add_argument('-l', '--length', help='set lenght to hashed password', type=int)
args = parser.parse_args()
config = Config()
def_iterations = 100000

if __name__ == "__main__":
    main()
