#!/usr/bin/python3
#
#Autor: Sc0rp10n

import re
import os
import sys
import time
import requests
from os import path
from colorama import Fore
from alive_progress import alive_bar

evil_ascii = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡌⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡌⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⡀⢣⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⢀⠃⢘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢃⠐⠀⠑⢔⠊⠁⠀⠀⠀⢩⠑⠢⣀⢀⠮⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡈⢒⡄⠀⢀⢻⠀⠀⠀⡠⠃⢆⠐⣻⠁⠀⡀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣷⡺⢽⠕⡪⡃⣀⠤⠊⠀⠀⡌⠢⠫⣢⡤⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡜⡤⡆⠣⠱⡭⠭⠴⠦⡬⠔⡓⣬⠵⠤⡽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⡧⢠⠘⠢⠥⠶⣚⠼⠀⡷⢭⡮⣻⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⢁⠀⡓⠤⠀⢠⢒⡀⠐⠰⢁⢀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⢹⣮⡄⠀⠀⠁⠤⡤⠋⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠀⠀⢽⡏⣹⣧⣤⣴⣬⢺⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⡀⠀⢿⢿⡿⠻⠿⢟⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⡀⠀⠈⠁⢉⠉⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠤⣤⠜⠤⠔
"""

aws_banner = """
                  (      (         (            (       (     
   (     (  (     )\ )   )\ )  (   )\ )   (     )\ )    )\ )  
   )\    )\))(   (()/(  (()/(  )\ (()/(   )\   (()/((  (()/(  
((((_)( ((_)()\ ) /(_))  /(_)(((_) /(_)((((_)(  /(_))\  /(_)) 
 )\ _ )\_(())\_)((_))   (_)) )\___(_))  )\ _ )\(_))((_)(_))   
 (_)_\(_\ \((_)/ / __|  / __((/ __| _ \ (_)_\(_| _ | __| _ \  
  / _ \  \ \/\/ /\__ \  \__ \| (__|   /  / _ \ |  _| _||   /  
 /_/ \_\  \_/\_/ |___/  |___/ \___|_|_\ /_/ \_\|_| |___|_|_\ 
               
                Autor: Sc0rp10n     


Python Tool for automatic and full file download of open AWS Buckets.
"""

instructions = """
[*]Instructions:

    python3 AwsScraper.py <Bucket Base Url>

    [*]Optional for specific file extensions:
    
    python3 AwsScraper.py <Bucket Base Url> <File Type>

    [*]Example:

        python3 AwsScraper.py https://sc0rp10n.s3.amazonaws.com pdf
"""

def DirectoryCreation(bucketname):
    basename_extract = bucketname.split('.')
    basename_cleaning = basename_extract[0].split('//')
    if path.isdir('./Results/' + basename_cleaning[1]) == False:
	    os.system('mkdir ./Results/' + basename_cleaning[1])
	    print(Fore.GREEN + '[*]Creating output folder under ./Results')
    elif path.isdir('./Results/' + basename_cleaning[1]) == True:
	    print(Fore.GREEN + '[*]Output folder already created. Continuing with program execution...')
		
    return  './Results/' + basename_cleaning[1] + '/'

def SpecificExtensionDirectory(bucketname):
    basename_extract = bucketname.split('.')
    basename_cleaning = basename_extract[0].split('//')
    if path.isdir('./Results/' + basename_cleaning[1] + '/' + str(sys.argv[2])) == True:
        print('[*]Specific extension directory already created. Continuing with program execution...')
    elif path.isdir('./Results/' + basename_cleaning[1] + '/' + str(sys.argv[2])) == False:
        comando = """mkdir ./Results/""" + basename_cleaning[1] + "/" + str(sys.argv[2])
        os.system(comando)
        print('[*]Creating file extension output folder under ./Results/' + basename_cleaning[1])

    return './Results/' + basename_cleaning[1] + '/' + sys.argv[2] + '/'


def KeyNameExtractNoFileType(web_text):
	## Format Section
	first_conversion = """\n<Key>"""
	second_conversion = """</Key>\n"""
	new_spaces = web_text.replace('<Key>', first_conversion).replace('</Key>', second_conversion)
	cleaning_list = []
	## Filenames by Regex
	key_regex = """\<Key\>.+\<\/Key\>"""
	filenames = re.findall(key_regex, new_spaces)
	## Escaped replacer values
	key1 = """<Key>"""
	key2 = """</Key>"""
	## Appending clean values to new list
	for i in range(len(filenames)):
	    intrusion = cleaning_list.append(filenames[i-1].replace(key1, '').replace(key2, ''))
	    
	return cleaning_list

def KeyNameExtractFileType(web_text, filetype):
	## Format Section
	first_conversion = """\n<Key>"""
	second_conversion = """</Key>\n"""
	new_spaces = web_text.replace('<Key>', first_conversion).replace('</Key>', second_conversion)
	cleaning_list = []
	## Filenames by Regex
	key_regex = """\<Key\>.+""" + "." + str(filetype) + """\<\/Key\>"""
	filenames = re.findall(key_regex, new_spaces)
	## Escaped replacer values
	key1 = """<Key>"""
	key2 = """</Key>"""
	## Appending clean values to new list
	for i in range(len(filenames)):
	    intrusion = cleaning_list.append(filenames[i-1].replace(key1, '').replace(key2, ''))

	return cleaning_list

def FileDownloader(filenames, directory):
    with alive_bar(len(filenames), bar = 'filling', spinner = 'pulse', spinner_length = 30) as bar:
        for i in range(len(filenames)):
            clean_filename = filenames[i - 1].split('/')[-1]
            if(sys.argv[1][-1] == '/' and filenames[i - 1][0] == '/'):
                temp = list(filenames[i-1])
                temp[-1] = ''
                working_uri = "".join(temp)
                command = """wget -q """ + '"' + sys.argv[1] + working_uri + '"' + " -O " + '"' + str(directory) + clean_filename + '"'
                os.system(command)
            elif(sys.argv[1][-1] == '/' and filenames[i - 1][0] != '/'):
                command = """wget -q """ + '"' + sys.argv[1] + filenames[i -1] + '"' + " -O " + '"' + str(directory) + clean_filename + '"'
                os.system(command)
            elif(sys.argv[1][-1] != '/' and filenames[i - 1][0] != '/'):
                temp = list(sys.argv[1])
                temp.append('/')
                working_url = "".join(temp)
                command = """wget -q """ + '"'  + working_url + filenames[i - 1] + '"' + " -O " + '"' + str(directory) + clean_filename + '"'
                os.system(command)
            elif(sys.argv[1][-1] != '/' and filenames[i -1][0] == '/'):
                command = """wget -q """ + '"' + sys.argv[1] + filenames[i - 1] + '"' + " -O " + '"' + str(directory) + clean_filename + '"'
                os.system(command)
            else:
                print(Fore.RED + '[*]There is a problem with your arguments, please double check your writing.')
                print(Fore.RED + '[*]Exiting()')
                exit()

            bar()

        
    return 0

os.system("clear")
print(Fore.RED + evil_ascii)
print(Fore.RED + aws_banner)

if(len(sys.argv) == 1):
    print(Fore.GREEN + instructions)
    exit()
elif(len(sys.argv) == 2):
    basepath = DirectoryCreation(sys.argv[1])
    ## Alive_bar
    print(Fore.GREEN +  '[*]Requesting information from AWS Bucket...')
    with alive_bar(100, bar = 'filling' ,spinner = 'pulse', spinner_length = 30) as bar:
        for i in range(100):
            time.sleep(0.02)
            if(i == 50):
                req = requests.get(sys.argv[1])
                bar()
            else:
                bar()
                continue	
    filenames = KeyNameExtractNoFileType(req.text)
    print(Fore.GREEN + '[*]Downloading Files...')
    FileDownloader(filenames, basepath)
elif(len(sys.argv) == 3):
    basename = DirectoryCreation(sys.argv[1])
    full_path = SpecificExtensionDirectory(sys.argv[1])
    ## Alive Bar
    print(Fore.GREEN +  '[*]Requesting information from AWS Bucket...')
    with alive_bar(100, bar = 'filling' ,spinner = 'pulse', spinner_length = 30) as bar:
        for i in range(100):
            time.sleep(0.02)
            if(i == 50):
                req = requests.get(sys.argv[1])
                bar()
            else:
                bar()
                continue
    
    print(Fore.GREEN + '\n[*]Identifying files with specified extension...')
    filenames = KeyNameExtractFileType(req.text, sys.argv[2])
    print(Fore.GREEN + '[*]Downloading Files...')
    FileDownloader(filenames, full_path)

print(Fore.GREEN + '\n[*]Files downloaded correctly :)')
