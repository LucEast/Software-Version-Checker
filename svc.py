#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import queue
import base64
import webbrowser
import configparser
from sys import platform
from threading import Thread

try:
    from tabulate import tabulate
except:
    print('Install tabulate with "pip3 install tabulate"')
    quit()
try:
    import grequests
except:
    print('Install qrequests with "pip3 install grequests"')
    quit()
try:
    from tkinter import *
    from tkinter import messagebox
except:
    print('Install tkinter with "sudo apt install python3-tk"')
    quit()
try:
    from bs4 import BeautifulSoup
except:
    print('Install BeautifulSoup with "pip3 install beautifulsoup4"')
    quit()
try:
    from tkscrolledframe import ScrolledFrame
except:
    print('Install tkScrolledFrame with "pip3 install tkScrolledFrame"')
    quit()

if os.path.isfile('current_versions.ini') == False:
    default_config = '''[CURRENT]
gui = Display all
seven_zip
aim = 
aleapp = 
atola = 
autopsy = 
avml = 
axiom = 
bec = 
blacklight = 
caine = 
cyberchef = 
deft = 
eift = 
encase = 
exiftool = 
ez_amcacheparser = 
ez_appcompatcacheparser = 
ez_bstrings = 
ez_evtxex = 
ez_jlecmd = 
ez_jumplistex = 
ez_lecmd = 
ez_mftecmd = 
ez_mftexplorer = 
ez_pecmd = 
ez_rbcmd = 
ez_recentfilecacheparser = 
ez_registryex = 
ez_sdbex = 
ez_shellbagex = 
ez_timelineex = 
ez_vscmount = 
ez_wxtcmd = 
fec = 
forensicexplorer = 
ffn = 
fresponse = 
ftk = 
ftkimager = 
hashcat = 
hstex = 
ileapp = 
irec = 
ive = 
kali = 
kape = 
lime = 
macquisition = 
mobiledit = 
mountimagepro = 
netanalysis = 
nirsoft = 
nsrl = 
osf = 
oxygen = 
paraben = 
passware = 
physicalanalyzer = 
sleuthkit = 
tzworks = 
ufed4pc = 
usbdetective = 
veracrypt = 
xamn = 
xways = 
'''

    try:
        configfile = open('current_versions.ini', 'w')
        configfile.write(default_config)
        configfile.close()
    except:
        print('Can\'t save the config file. Please check your permissions.')
        quit()
    first_run = True
else:
    first_run = False

config = configparser.ConfigParser()
config.read('current_versions.ini')

mt_queue = queue.Queue()
response = []

used_tools = []
used_tools_counter = 1

try:
    parsers_url = ['https://raw.githubusercontent.com/LucEast/Software-Version-Checker/main/parsers.ini',
                   'https://api.github.com/repos/LucEast/Software-Version-Checker/commits?path=parsers.ini']
    parsers_get = (grequests.get(u) for u in parsers_url)
    parsers_responses = grequests.map(parsers_get)
    for idx, r in enumerate(parsers_responses):
        if idx == 0:
            if r.status_code == 200:
                parsersfile = open('parsers.ini', 'wb')
                parsersfile.write(r.content)
                parsersfile.close()
                r.close()
            else:
                print(
                    'Couldn\'t download parser definitions. Please check your Internet connection.')
                # quit()
        if idx == 1:
            soup = r.content.decode('utf-8')
            parsers_date = str(
                soup[soup.find('"date":"') + 8:soup.find('T', soup.find('"date":"') + 8)])
            first_message = soup.find('"message":"') + 11
            parsers_changes = str(
                soup[first_message:soup.find('",', first_message)])
            parsers_previous_changes = str(soup[soup.find(
                '"message":"', first_message) + 11:soup.find('",', soup.find('"message":"', first_message) + 11)])
except:
    print('Couldn\'t download parser definitions. Please check your Internet connection.')
    # quit()

parsers = configparser.ConfigParser()
parsers.read('parsers.ini')

seven_zip_parser = (
    parsers['PARSERS']['seven_zip_parser']).replace('\\t', '\t')
aim_parser = (parsers['PARSERS']['aim_parser']).replace('\\t', '\t')
aleapp_parser = (parsers['PARSERS']['aleapp_parser']).replace('\\t', '\t')
atola_parser = (parsers['PARSERS']['atola_parser']).replace('\\t', '\t')
autopsy_parser = (parsers['PARSERS']['autopsy_parser']).replace('\\t', '\t')
avml_parser = (parsers['PARSERS']['avml_parser']).replace('\\t', '\t')
axiom_parser = (parsers['PARSERS']['axiom_parser']).replace('\\t', '\t')
bec_parser = (parsers['PARSERS']['bec_parser']).replace('\\t', '\t')
blacklight_parser = (
    parsers['PARSERS']['blacklight_parser']).replace('\\t', '\t')
caine_parser = (parsers['PARSERS']['caine_parser']).replace('\\t', '\t')
cyberchef_parser = (
    parsers['PARSERS']['cyberchef_parser']).replace('\\t', '\t')
deft_parser = (parsers['PARSERS']['deft_parser']).replace('\\t', '\t')
eift_parser = (parsers['PARSERS']['eift_parser']).replace('\\t', '\t')
encase_parser = (parsers['PARSERS']['encase_parser']).replace('\\t', '\t')
exiftool_parser = (parsers['PARSERS']['exiftool_parser']).replace('\\t', '\t')
ez_amcacheparser_parser = (
    parsers['PARSERS']['ez_amcacheparser_parser']).replace('\\t', '\t')
ez_appcompatcacheparser_parser = (
    parsers['PARSERS']['ez_appcompatcacheparser_parser']).replace('\\t', '\t')
ez_bstrings_parser = (
    parsers['PARSERS']['ez_bstrings_parser']).replace('\\t', '\t')
ez_evtxex_parser = (
    parsers['PARSERS']['ez_evtxex_parser']).replace('\\t', '\t')
ez_jlecmd_parser = (
    parsers['PARSERS']['ez_jlecmd_parser']).replace('\\t', '\t')
ez_jumplistex_parser = (
    parsers['PARSERS']['ez_jumplistex_parser']).replace('\\t', '\t')
ez_lecmd_parser = (parsers['PARSERS']['ez_lecmd_parser']).replace('\\t', '\t')
ez_mftecmd_parser = (
    parsers['PARSERS']['ez_mftecmd_parser']).replace('\\t', '\t')
ez_mftexplorer_parser = (
    parsers['PARSERS']['ez_mftexplorer_parser']).replace('\\t', '\t')
ez_pecmd_parser = (parsers['PARSERS']['ez_pecmd_parser']).replace('\\t', '\t')
ez_rbcmd_parser = (parsers['PARSERS']['ez_rbcmd_parser']).replace('\\t', '\t')
ez_recentfilecacheparser_parser = (
    parsers['PARSERS']['ez_recentfilecacheparser_parser']).replace('\\t', '\t')
ez_registryex_parser = (
    parsers['PARSERS']['ez_registryex_parser']).replace('\\t', '\t')
ez_sdbex_parser = (parsers['PARSERS']['ez_sdbex_parser']).replace('\\t', '\t')
ez_shellbagex_parser = (
    parsers['PARSERS']['ez_shellbagex_parser']).replace('\\t', '\t')
ez_timelineex_parser = (
    parsers['PARSERS']['ez_timelineex_parser']).replace('\\t', '\t')
ez_vscmount_parser = (
    parsers['PARSERS']['ez_vscmount_parser']).replace('\\t', '\t')
ez_wxtcmd_parser = (
    parsers['PARSERS']['ez_wxtcmd_parser']).replace('\\t', '\t')
fec_parser = (parsers['PARSERS']['fec_parser']).replace('\\t', '\t')
forensicexplorer_parser = (
    parsers['PARSERS']['forensicexplorer_parser']).replace('\\t', '\t')
ffn_parser = (parsers['PARSERS']['ffn_parser']).replace('\\t', '\t')
fresponse_parser = (
    parsers['PARSERS']['fresponse_parser']).replace('\\t', '\t')
ftk_parser = (parsers['PARSERS']['ftk_parser']).replace('\\t', '\t')
ftkimager_parser = (
    parsers['PARSERS']['ftkimager_parser']).replace('\\t', '\t')
hashcat_parser = (parsers['PARSERS']['hashcat_parser']).replace('\\t', '\t')
hstex_parser = (parsers['PARSERS']['hstex_parser']).replace('\\t', '\t')
ileapp_parser = (parsers['PARSERS']['ileapp_parser']).replace('\\t', '\t')
irec_parser = (parsers['PARSERS']['irec_parser']).replace('\\t', '\t')
ive_parser = (parsers['PARSERS']['ive_parser']).replace('\\t', '\t')
kali_parser = (parsers['PARSERS']['kali_parser']).replace('\\t', '\t')
kape_parser = (parsers['PARSERS']['kape_parser']).replace('\\t', '\t')
lime_parser = (parsers['PARSERS']['lime_parser']).replace('\\t', '\t')
macquisition_parser = (
    parsers['PARSERS']['macquisition_parser']).replace('\\t', '\t')
mobiledit_parser = (
    parsers['PARSERS']['mobiledit_parser']).replace('\\t', '\t')
mountimagepro_parser = (
    parsers['PARSERS']['mountimagepro_parser']).replace('\\t', '\t')
mysql_connector_odbc_parser = (
    parsers['PARSERS']['mysql_connector_odbc_parser']).replace('\\t', '\t')
netanalysis_parser = (
    parsers['PARSERS']['netanalysis_parser']).replace('\\t', '\t')
nirsoft_parser = (parsers['PARSERS']['nirsoft_parser']).replace('\\t', '\t')
nsrl_parser = (parsers['PARSERS']['nsrl_parser']).replace('\\t', '\t')
osf_parser = (parsers['PARSERS']['osf_parser']).replace('\\t', '\t')
oxygen_parser = (parsers['PARSERS']['oxygen_parser']).replace('\\t', '\t')
paraben_parser = (parsers['PARSERS']['paraben_parser']).replace('\\t', '\t')
passware_parser = (parsers['PARSERS']['passware_parser']).replace('\\t', '\t')
physicalanalyzer_parser = (
    parsers['PARSERS']['physicalanalyzer_parser']).replace('\\t', '\t')
sleuthkit_parser = (
    parsers['PARSERS']['sleuthkit_parser']).replace('\\t', '\t')
tzworks_parser = (parsers['PARSERS']['tzworks_parser']).replace('\\t', '\t')
ufed4pc_parser = (parsers['PARSERS']['ufed4pc_parser']).replace('\\t', '\t')
usbdetective_parser = (
    parsers['PARSERS']['usbdetective_parser']).replace('\\t', '\t')
veracrypt_parser = (
    parsers['PARSERS']['veracrypt_parser']).replace('\\t', '\t')
xamn_parser = (parsers['PARSERS']['xamn_parser']).replace('\\t', '\t')
xways_parser = (parsers['PARSERS']['xways_parser']).replace('\\t', '\t')


def spinning_cursor():
    while True:
        for cursor in '|/–\\':
            yield cursor


def build_gui(fieldname, displayname, url):
    code = compile('''
try:
	current = config['CURRENT'][\'''' + fieldname + '''\']
except:
	current = ''
if (gui == 'Display all' or current != ''):
	''' + fieldname + ''' = Label(inner_frame, text = \'''' + displayname + '''\', font = ('TkDefaultFont', fontsize), padx = 5)
	''' + fieldname + '''.grid(column = 0, row = rowID, sticky = W)
	''' + fieldname + '''_current = Entry(inner_frame, font = ('TkDefaultFont', fontsize), width = 8)
	''' + fieldname + '''_current.grid(column = 1, row = rowID, sticky = N+S+E+W)
	''' + fieldname + '''_current.insert(0, current)
	''' + fieldname + '''_latest = Entry(inner_frame, font = ('TkDefaultFont', fontsize), width = 8, state = 'readonly')
	''' + fieldname + '''_latest.grid(column = 2, row = rowID, sticky = N+S+E+W)
	''' + fieldname + '''_update = Label(inner_frame, text = '', font = ('TkDefaultFont', fontsize))
	''' + fieldname + '''_update.grid(column = 3, row = rowID, sticky = W)
	''' + fieldname + '''_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new(\'''' + url + '''\'))
	widget_order.append(''' + fieldname + '''_current)
	used_tools.append(\'''' + fieldname + '''\')
	rowID += 1
''', '<string>', 'exec')
    exec(code, globals(), globals())


def update_gui(fieldname, parsing):
    code = compile('''
global response
global used_tools_counter
try:
	current = ''' + fieldname + '''_current.get()
except:
	current = ''
if (gui == 'Display all' or current != ''):
	try:
''' + parsing + '''
	except:
		version = 'Error'
		''' + fieldname + '''_latest.configure(readonlybackground = 'red')
try:
	''' + fieldname + '''_latest.configure(state = 'normal')
	''' + fieldname + '''_latest.delete(0, END)
	''' + fieldname + '''_latest.insert(0, version)
	''' + fieldname + '''_latest.configure(state = 'readonly')
	if ''' + fieldname + '''_current.get() == ''' + fieldname + '''_latest.get():
		''' + fieldname + '''_latest.configure(readonlybackground = 'limegreen')
		''' + fieldname + '''_update.configure(text = '', cursor = '')
	elif ((''' + fieldname + '''_current.get() != '') and (''' + fieldname + '''_latest.get() != 'Error')):
		''' + fieldname + '''_latest.configure(readonlybackground = 'orange')
		''' + fieldname + '''_update.configure(text = 'Update', fg = 'blue', cursor = 'hand2')
	used_tools_counter += 1
except:
	pass
''', '<string>', 'exec')
    exec(code, globals(), globals())


def gather_used_tools(fieldname):
    code = compile('''
try:
	current = config['CURRENT'][\'''' + fieldname + '''\']
except:
	current = ''
if (current != ''):
	used_tools.append(\'''' + fieldname + '''\')
''', '<string>', 'exec')
    exec(code, globals(), globals())


def update_cli(fieldname, displayname, parsing):
    code = compile('''
try:
	current = config['CURRENT'][\'''' + fieldname + '''\']
except:
	current = ''
if (current != ''):
	try:
''' + parsing + '''
	except:
		version = 'Error'
	if ((current == version) or (version == 'Error')):
		table.append([\'''' + displayname + '''\', current, version, ''])
	else:
		table.append([\'''' + displayname + '''\', current, version, 'Update available!'])
	used_tools_counter += 1
''', '<string>', 'exec')
    exec(code, globals(), globals())


def crawl():
    ua_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    }

    all_urls = {'svc':	parsers['URLS']['svc'],
                'seven_zip':	parsers['URLS']['seven_zip'],
                'aim':	parsers['URLS']['aim'],
                'aleapp':	parsers['URLS']['aleapp'],
                'atola':	parsers['URLS']['atola'],
                'autopsy':	parsers['URLS']['autopsy'],
                'avml':	parsers['URLS']['avml'],
                'axiom':	parsers['URLS']['axiom'],
                'bec':	parsers['URLS']['bec'],
                'blacklight':	parsers['URLS']['blacklight'],
                'caine':	parsers['URLS']['caine'],
                'cyberchef':	parsers['URLS']['cyberchef'],
                'deft':	parsers['URLS']['deft'],
                'eift':	parsers['URLS']['eift'],
                'encase':	parsers['URLS']['encase'],
                'exiftool':	parsers['URLS']['exiftool'],
                'ez_amcacheparser':	parsers['URLS']['ez_amcacheparser'],
                'ez_appcompatcacheparser':	parsers['URLS']['ez_appcompatcacheparser'],
                'ez_bstrings':	parsers['URLS']['ez_bstrings'],
                'ez_evtxex':	parsers['URLS']['ez_evtxex'],
                'ez_jlecmd':	parsers['URLS']['ez_jlecmd'],
                'ez_jumplistex':	parsers['URLS']['ez_jumplistex'],
                'ez_lecmd':	parsers['URLS']['ez_lecmd'],
                'ez_mftecmd':	parsers['URLS']['ez_mftecmd'],
                'ez_mftexplorer':	parsers['URLS']['ez_mftexplorer'],
                'ez_pecmd':	parsers['URLS']['ez_pecmd'],
                'ez_rbcmd':	parsers['URLS']['ez_rbcmd'],
                'ez_recentfilecacheparser':	parsers['URLS']['ez_recentfilecacheparser'],
                'ez_registryex':	parsers['URLS']['ez_registryex'],
                'ez_sdbex':	parsers['URLS']['ez_sdbex'],
                'ez_shellbagex':	parsers['URLS']['ez_shellbagex'],
                'ez_timelineex':	parsers['URLS']['ez_timelineex'],
                'ez_vscmount':	parsers['URLS']['ez_vscmount'],
                'ez_wxtcmd':	parsers['URLS']['ez_wxtcmd'],
                'fec':	parsers['URLS']['fec'],
                'forensicexplorer':	parsers['URLS']['forensicexplorer'],
                'ffn':	parsers['URLS']['ffn'],
                'fresponse':	parsers['URLS']['fresponse'],
                'ftk':	parsers['URLS']['ftk'],
                'ftkimager':	parsers['URLS']['ftkimager'],
                'hashcat':	parsers['URLS']['hashcat'],
                'hstex':	parsers['URLS']['hstex'],
                'ileapp':	parsers['URLS']['ileapp'],
                'irec':	parsers['URLS']['irec'],
                'ive':	parsers['URLS']['ive'],
                'kali':	parsers['URLS']['kali'],
                'kape':	parsers['URLS']['kape'],
                'lime':	parsers['URLS']['lime'],
                'macquisition':	parsers['URLS']['macquisition'],
                'mobiledit':	parsers['URLS']['mobiledit'],
                'mountimagepro':	parsers['URLS']['mountimagepro'],
                'mysql_connector_odbc':	parsers['URLS']['mysql_connector_odbc'],
                'netanalysis':	parsers['URLS']['netanalysis'],
                'nirsoft':	parsers['URLS']['nirsoft'],
                'nsrl':	parsers['URLS']['nsrl'],
                'osf':	parsers['URLS']['osf'],
                'oxygen':	parsers['URLS']['oxygen'],
                'paraben':	parsers['URLS']['paraben'],
                'passware':	parsers['URLS']['passware'],
                'physicalanalyzer':	parsers['URLS']['physicalanalyzer'],
                'sleuthkit':	parsers['URLS']['sleuthkit'],
                'tzworks':	parsers['URLS']['tzworks'],
                'ufed4pc':	parsers['URLS']['ufed4pc'],
                'usbdetective':	parsers['URLS']['usbdetective'],
                'veracrypt':	parsers['URLS']['veracrypt'],
                'xamn':	parsers['URLS']['xamn'],
                'xways':	parsers['URLS']['xways']
                }

    urls = []
    urls.append(all_urls['svc'])
    for tool in used_tools:
        urls.append(all_urls[tool])

    mt_queue.put(grequests.map(
        (grequests.get(u, headers=ua_headers) for u in urls)))


def refresh_gui():
    global response
    global used_tools_counter
    used_tools_counter = 1

    current_save.configure(state='disabled')
    gui_toggle.configure(state='disabled')
    for widget in widget_order:
        widget.configure(state='disabled')

    thread = Thread(target=crawl)
    thread.start()

    while(thread.is_alive()):
        current_save.configure(text='Checking for updates·..')
        root.update()
        time.sleep(0.15)
        current_save.configure(text='Checking for updates.·.')
        root.update()
        time.sleep(0.15)
        current_save.configure(text='Checking for updates..·')
        root.update()
        time.sleep(0.15)
        current_save.configure(text='Checking for updates...')
        for _ in range(10):
            root.update()
            time.sleep(0.15)

    response = mt_queue.get()

    update_gui('seven_zip', seven_zip_parser)
    update_gui('aim', aim_parser)
    update_gui('aleapp', aleapp_parser)
    update_gui('atola', atola_parser)
    update_gui('autopsy', autopsy_parser)
    update_gui('avml', avml_parser)
    update_gui('axiom', axiom_parser)
    update_gui('bec', bec_parser)
    update_gui('blacklight', blacklight_parser)
    update_gui('caine', caine_parser)
    update_gui('cyberchef', cyberchef_parser)
    update_gui('deft', deft_parser)
    update_gui('eift', eift_parser)
    update_gui('encase', encase_parser)
    update_gui('exiftool', exiftool_parser)
    update_gui('ez_amcacheparser', ez_amcacheparser_parser)
    update_gui('ez_appcompatcacheparser', ez_appcompatcacheparser_parser)
    update_gui('ez_bstrings', ez_bstrings_parser)
    update_gui('ez_evtxex', ez_evtxex_parser)
    update_gui('ez_jlecmd', ez_jlecmd_parser)
    update_gui('ez_jumplistex', ez_jumplistex_parser)
    update_gui('ez_lecmd', ez_lecmd_parser)
    update_gui('ez_mftecmd', ez_mftecmd_parser)
    update_gui('ez_mftexplorer', ez_mftexplorer_parser)
    update_gui('ez_pecmd', ez_pecmd_parser)
    update_gui('ez_rbcmd', ez_rbcmd_parser)
    update_gui('ez_recentfilecacheparser', ez_recentfilecacheparser_parser)
    update_gui('ez_registryex', ez_registryex_parser)
    update_gui('ez_sdbex', ez_sdbex_parser)
    update_gui('ez_shellbagex', ez_shellbagex_parser)
    update_gui('ez_timelineex', ez_timelineex_parser)
    update_gui('ez_vscmount', ez_vscmount_parser)
    update_gui('ez_wxtcmd', ez_wxtcmd_parser)
    update_gui('fec', fec_parser)
    update_gui('forensicexplorer', forensicexplorer_parser)
    update_gui('ffn', ffn_parser)
    update_gui('fresponse', fresponse_parser)
    update_gui('ftk', ftk_parser)
    update_gui('ftkimager', ftkimager_parser)
    update_gui('hashcat', hashcat_parser)
    update_gui('hstex', hstex_parser)
    update_gui('ileapp', ileapp_parser)
    update_gui('irec', irec_parser)
    update_gui('ive', ive_parser)
    update_gui('kali', kali_parser)
    update_gui('kape', kape_parser)
    update_gui('lime', lime_parser)
    update_gui('macquisition', macquisition_parser)
    update_gui('mobiledit', mobiledit_parser)
    update_gui('mountimagepro', mountimagepro_parser)
    update_gui('mysql_connector_odbc', mysql_connector_odbc_parser)
    update_gui('netanalysis', netanalysis_parser)
    update_gui('nirsoft', nirsoft_parser)
    update_gui('nsrl', nsrl_parser)
    update_gui('osf', osf_parser)
    update_gui('oxygen', oxygen_parser)
    update_gui('paraben', paraben_parser)
    update_gui('passware', passware_parser)
    update_gui('physicalanalyzer', physicalanalyzer_parser)
    update_gui('sleuthkit', sleuthkit_parser)
    update_gui('tzworks', tzworks_parser)
    update_gui('ufed4pc', ufed4pc_parser)
    update_gui('usbdetective', usbdetective_parser)
    update_gui('veracrypt', veracrypt_parser)
    update_gui('xamn', xamn_parser)
    update_gui('xways', xways_parser)

    # Software Version Checker
    try:
        soup = BeautifulSoup(response[0].text, 'html.parser')
        version = soup.find(
            'div', {'class': 'release-header'}).select_one('a').text.strip()
        version = version.replace('v', '')
    except:
        version = '1.16'
    if version != '1.16':
        about.configure(text='Update SVC', fg='blue', cursor='hand2')
        about.bind('<ButtonRelease-1>', lambda e: webbrowser.open_new(
            'https://github.com/LucEast/Software-Version-Checker/releases/latest'))

    current_save.configure(text='Save', state='normal')
    gui_toggle.configure(state='normal')

    for widget in widget_order:
        widget.configure(state='normal')


def run_cli():
    global response
    table_headers = ['Tool', 'Current Version', 'Latest Version', 'Update?']

    gather_used_tools('seven_zip')
    gather_used_tools('aim')
    gather_used_tools('aleapp')
    gather_used_tools('atola')
    gather_used_tools('autopsy')
    gather_used_tools('avml')
    gather_used_tools('axiom')
    gather_used_tools('bec')
    gather_used_tools('blacklight')
    gather_used_tools('caine')
    gather_used_tools('cyberchef')
    gather_used_tools('deft')
    gather_used_tools('eift')
    gather_used_tools('encase')
    gather_used_tools('exiftool')
    gather_used_tools('ez_amcacheparser')
    gather_used_tools('ez_appcompatcacheparser')
    gather_used_tools('ez_bstrings')
    gather_used_tools('ez_evtxex')
    gather_used_tools('ez_jlecmd')
    gather_used_tools('ez_jumplistex')
    gather_used_tools('ez_lecmd')
    gather_used_tools('ez_mftecmd')
    gather_used_tools('ez_mftexplorer')
    gather_used_tools('ez_pecmd')
    gather_used_tools('ez_rbcmd')
    gather_used_tools('ez_recentfilecacheparser')
    gather_used_tools('ez_registryex')
    gather_used_tools('ez_sdbex')
    gather_used_tools('ez_shellbagex')
    gather_used_tools('ez_timelineex')
    gather_used_tools('ez_vscmount')
    gather_used_tools('ez_wxtcmd')
    gather_used_tools('fec')
    gather_used_tools('forensicexplorer')
    gather_used_tools('ffn')
    gather_used_tools('fresponse')
    gather_used_tools('ftk')
    gather_used_tools('ftkimager')
    gather_used_tools('hashcat')
    gather_used_tools('hstex')
    gather_used_tools('ileapp')
    gather_used_tools('irec')
    gather_used_tools('ive')
    gather_used_tools('kali')
    gather_used_tools('kape')
    gather_used_tools('lime')
    gather_used_tools('macquisition')
    gather_used_tools('mobiledit')
    gather_used_tools('mountimagepro')
    gather_used_tools('mysql_connector_odbc')
    gather_used_tools('netanalysis')
    gather_used_tools('nirsoft')
    gather_used_tools('nsrl')
    gather_used_tools('osf')
    gather_used_tools('oxygen')
    gather_used_tools('paraben')
    gather_used_tools('passware')
    gather_used_tools('physicalanalyzer')
    gather_used_tools('sleuthkit')
    gather_used_tools('tzworks')
    gather_used_tools('ufed4pc')
    gather_used_tools('usbdetective')
    gather_used_tools('veracrypt')
    gather_used_tools('xamn')
    gather_used_tools('xways')

    thread = Thread(target=crawl)
    thread.start()

    spinner = spinning_cursor()
    sys.stdout.write('Checking for updates ')
    while(thread.is_alive()):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')
    sys.stdout.write('\b' * 21)

    response = mt_queue.get()

    update_cli('seven_zip', '7zip', seven_zip_parser)
    update_cli('aim', 'AIM', aim_parser)
    update_cli('aleapp', 'ALEAPP', aleapp_parser)
    update_cli('atola', 'Atola TaskForce', atola_parser)
    update_cli('autopsy', 'Autopsy', autopsy_parser)
    update_cli('avml', 'AVML', avml_parser)
    update_cli('axiom', 'AXIOM', axiom_parser)
    update_cli('bec', 'BEC', bec_parser)
    update_cli('blacklight', 'BlackLight', blacklight_parser)
    update_cli('caine', 'CAINE', caine_parser)
    update_cli('cyberchef', 'CyberChef', cyberchef_parser)
    update_cli('deft', 'DEFT', deft_parser)
    update_cli('eift', 'EIFT', eift_parser)
    update_cli('encase', 'Encase', encase_parser)
    update_cli('exiftool', 'ExifTool', exiftool_parser)
    update_cli('ez_amcacheparser', 'EZ AmcacheParser', ez_amcacheparser_parser)
    update_cli('ez_appcompatcacheparser', 'EZ AppCompatCacheParser',
               ez_appcompatcacheparser_parser)
    update_cli('ez_bstrings', 'EZ bstrings', ez_bstrings_parser)
    update_cli('ez_evtxex', 'EZ Evtx Explorer/EvtxECmd', ez_evtxex_parser)
    update_cli('ez_jlecmd', 'EZ JLECmd', ez_jlecmd_parser)
    update_cli('ez_jumplistex', 'EZ JumpList Explorer', ez_jumplistex_parser)
    update_cli('ez_lecmd', 'EZ LECmd', ez_lecmd_parser)
    update_cli('ez_mftecmd', 'EZ MFTECmd', ez_mftecmd_parser)
    update_cli('ez_mftexplorer', 'EZ MFTExplorer', ez_mftexplorer_parser)
    update_cli('ez_pecmd', 'EZ PECmd', ez_pecmd_parser)
    update_cli('ez_rbcmd', 'EZ RBCmd', ez_rbcmd_parser)
    update_cli('ez_recentfilecacheparser', 'EZ RecentFileCacheParser',
               ez_recentfilecacheparser_parser)
    update_cli('ez_registryex', 'EZ Registry Explorer/RECmd',
               ez_registryex_parser)
    update_cli('ez_sdbex', 'EZ SDB Explorer', ez_sdbex_parser)
    update_cli('ez_shellbagex', 'EZ ShellBags Explorer', ez_shellbagex_parser)
    update_cli('ez_timelineex', 'EZ Timeline Explorer', ez_timelineex_parser)
    update_cli('ez_vscmount', 'EZ VSCMount', ez_vscmount_parser)
    update_cli('ez_wxtcmd', 'EZ WxTCmd', ez_wxtcmd_parser)
    update_cli('fec', 'Forensic Email Collector', fec_parser)
    update_cli('forensicexplorer', 'Forensic Explorer',
               forensicexplorer_parser)
    update_cli('ffn', 'Forensic Falcon Neo', ffn_parser)
    update_cli('fresponse', 'F-Response', fresponse_parser)
    update_cli('ftk', 'FTK', ftk_parser)
    update_cli('ftkimager', 'FTK Imager', ftkimager_parser)
    update_cli('hashcat', 'hashcat', hashcat_parser)
    update_cli('hstex', 'HstEx', hstex_parser)
    update_cli('ileapp', 'iLEAPP', ileapp_parser)
    update_cli('irec', 'IREC', irec_parser)
    update_cli('ive', 'iVe', ive_parser)
    update_cli('kali', 'Kali', kali_parser)
    update_cli('kape', 'KAPE', kape_parser)
    update_cli('lime', 'LiME', lime_parser)
    update_cli('macquisition', 'MacQuisition', macquisition_parser)
    update_cli('mobiledit', 'MobilEdit', mobiledit_parser)
    update_cli('mountimagepro', 'Mount Image Pro', mountimagepro_parser)
    update_cli('mysql_connector_odbc', 'MySql Connector ODBC',
               mysql_connector_odbc_parser)
    update_cli('netanalysis', 'NetAnalysis', netanalysis_parser)
    update_cli('nirsoft', 'NirSoft Launcher', nirsoft_parser)
    update_cli('nsrl', 'NSRL hash set', nsrl_parser)
    update_cli('osf', 'OSForensics', osf_parser)
    update_cli('oxygen', 'Oxygen Forensic', oxygen_parser)
    update_cli('paraben', 'Paraben E3', paraben_parser)
    update_cli('passware', 'Passware', passware_parser)
    update_cli('physicalanalyzer', 'Physical Analyzer',
               physicalanalyzer_parser)
    update_cli('sleuthkit', 'The Sleuth Kit', sleuthkit_parser)
    update_cli('tzworks', 'TZWorks', tzworks_parser)
    update_cli('ufed4pc', 'UFED 4PC', ufed4pc_parser)
    update_cli('usbdetective', 'USB Detective', usbdetective_parser)
    update_cli('veracrypt', 'VeraCrypt', veracrypt_parser)
    update_cli('xamn', 'XAMN', xamn_parser)
    update_cli('xways', 'X-Ways', xways_parser)

    print(tabulate(table, headers=table_headers, disable_numparse=True))

    # Software Version Checker
    try:
        soup = BeautifulSoup(response[0].text, 'html.parser')
        version = soup.find(
            'div', {'class': 'release-header'}).select_one('a').text.strip()
        version = version.replace('v', '')
    except:
        version = '1.16'
    if (version == '1.16'):
        pass
    else:
        print('')
        print('SVC update available!')


def save():
    config['CURRENT']['gui'] = gui_option.get()
    for tool in used_tools:
        code = compile('''
config['CURRENT'][\'''' + tool + '''\'] = ''' + tool + '''_current.get()
''', '<string>', 'exec')
        exec(code, globals(), globals())

    with open('current_versions.ini', 'w') as configfile:
        config.write(configfile)

    refresh_gui()
    current_save.configure(text='Current versions saved', state='normal')
    gui_toggle.configure(state='normal')


def about_box():
    messagebox.showinfo('About', 'Software Version Checker v1.0\n\n\
Latest parsers.ini update on: ' + parsers_date + '\n\
Latest changes: ' + parsers_changes + '\n\
Previous changes: ' + parsers_previous_changes + '\n\n\
Tool\'s homepage:\nhttps://github.com/LucEast/Software-Version-Checker')


def get_max_height():
    helper = Tk()
    helper.attributes('-alpha', 0)
    if os.name == 'nt':
        helper.state('zoomed')
        helper.update()
        usable_height = helper.winfo_height()
    else:
        usable_height = helper.winfo_screenheight()
    helper.destroy()
    return usable_height


try:
    if (config['CURRENT']['gui'] == '1' or config['CURRENT']['gui'] == 'Display all'):
        gui = 'Display all'
    elif config['CURRENT']['gui'] == 'Display used':
        gui = 'Display used'
    else:
        gui = 'CLI mode'
except:
    gui = 'Display all'

if gui != 'CLI mode':
    root = Tk()
    root.attributes('-alpha', 0)
    root.title('Software Version Checker')

    sf = ScrolledFrame(root, scrollbars='vertical')
    sf.pack(side='top', expand=True, fill='both')
    sf.bind_scroll_wheel(root)
    inner_frame = sf.display_widget(Frame)

    icon = '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'  # https://thenounproject.com/term/update/2827723/
    try:
        icon = base64.b64decode(icon)
        icon = PhotoImage(data=icon)
        root.tk.call('wm', 'iconphoto', root._w, icon)
    except:
        pass

    if os.name == 'nt':
        fontsize = 9
    elif platform == 'darwin':
        fontsize = 12
    else:
        fontsize = 10

    rowID = 0
    tool = Label(inner_frame, text='Tool', font=(
        'TkDefaultFont', fontsize, 'underline'), padx=5, pady=3)
    tool.grid(column=0, row=rowID, sticky=W)
    current = Label(inner_frame, text='Current Version', font=(
        'TkDefaultFont', fontsize, 'underline'), pady=3)
    current.grid(column=1, row=rowID)
    latest = Label(inner_frame, text='Latest Version', font=(
        'TkDefaultFont', fontsize, 'underline'), pady=3)
    latest.grid(column=2, row=rowID)
    latest = Label(inner_frame, text='Update', font=(
        'TkDefaultFont', fontsize, 'underline'), pady=3)
    latest.grid(column=3, row=rowID, padx=(0, 10), sticky=W)
    rowID += 1

    widget_order = []

    build_gui('seven_zip', '7zip', 'https://www.7-zip.org/download.html')
    build_gui('aim', 'AIM', 'https://arsenalrecon.com/downloads/')
    build_gui('aleapp', 'ALEAPP', 'https://github.com/abrignoni/ALEAPP')
    build_gui('atola', 'Atola TaskForce',
              'https://atola.com/products/taskforce/download.html')
    build_gui('autopsy', 'Autopsy',
              'https://github.com/sleuthkit/autopsy/releases/latest')
    build_gui('avml', 'AVML', 'https://github.com/microsoft/avml/releases/latest')
    build_gui('axiom', 'AXIOM', 'https://www.magnetforensics.com/downloadaxiom/')
    build_gui('bec', 'BEC', 'https://belkasoft.com/get')
    build_gui('blacklight', 'BlackLight',
              'https://www.blackbagtech.com/downloads/')
    build_gui('caine', 'CAINE', 'https://www.caine-live.net/')
    build_gui('cyberchef', 'CyberChef',
              'https://github.com/gchq/CyberChef/releases/latest')
    build_gui('deft', 'DEFT', 'http://na.mirror.garr.it/mirrors/deft/zero/')
    build_gui('eift', 'EIFT', 'https://www.elcomsoft.com/eift.html')
    build_gui('encase', 'EnCase',
              'https://www.guidancesoftware.com/encase-forensic')
    build_gui('exiftool', 'ExifTool',
              'https://owl.phy.queensu.ca/~phil/exiftool/')
    build_gui('ez_amcacheparser', 'EZ AmcacheParser',
              'https://ericzimmerman.github.io/#!index.md')
    build_gui('ez_appcompatcacheparser', 'EZ AppCompatCacheParser',
              'https://ericzimmerman.github.io/#!index.md')
    build_gui('ez_bstrings', 'EZ bstrings',
              'https://ericzimmerman.github.io/#!index.md')
    build_gui('ez_evtxex', 'EZ Evtx Explorer/EvtxECmd',
              'https://ericzimmerman.github.io/#!index.md')
    build_gui('ez_jlecmd', 'EZ JLECmd',
              'https://ericzimmerman.github.io/#!index.md')
    build_gui('ez_jumplistex', 'EZ JumpList Explorer',
              'https://ericzimmerman.github.io/#!index.md')
    build_gui('ez_lecmd', 'EZ LECmd',
              'https://ericzimmerman.github.io/#!index.md')
    build_gui('ez_mftecmd', 'EZ MFTECmd',
              'https://ericzimmerman.github.io/#!index.md')
    build_gui('ez_mftexplorer', 'EZ MFTExplorer',
              'https://ericzimmerman.github.io/#!index.md')
    build_gui('ez_pecmd', 'EZ PECmd',
              'https://ericzimmerman.github.io/#!index.md')
    build_gui('ez_rbcmd', 'EZ RBCmd',
              'https://ericzimmerman.github.io/#!index.md')
    build_gui('ez_recentfilecacheparser', 'EZ RecentFileCacheParser',
              'https://ericzimmerman.github.io/#!index.md')
    build_gui('ez_registryex', 'EZ Registry Explorer/RECmd',
              'https://ericzimmerman.github.io/#!index.md')
    build_gui('ez_sdbex', 'EZ SDB Explorer',
              'https://ericzimmerman.github.io/#!index.md')
    build_gui('ez_shellbagex', 'EZ ShellBags Explorer',
              'https://ericzimmerman.github.io/#!index.md')
    build_gui('ez_timelineex', 'EZ Timeline Explorer',
              'https://ericzimmerman.github.io/#!index.md')
    build_gui('ez_vscmount', 'EZ VSCMount',
              'https://ericzimmerman.github.io/#!index.md')
    build_gui('ez_wxtcmd', 'EZ WxTCmd',
              'https://ericzimmerman.github.io/#!index.md')
    build_gui('fec', 'Forensic Email Collector',
              'http://www.metaspike.com/fec-change-log/')
    build_gui('forensicexplorer', 'Forensic Explorer',
              'http://www.forensicexplorer.com/download.php')
    build_gui('ffn', 'Forensic Falcon Neo',
              'https://www.logicube.com/knowledge/forensic-falcon-neo/')
    build_gui('fresponse', 'F-Response',
              'https://www.f-response.com/support/downloads')
    build_gui('ftk', 'FTK', 'https://accessdata.com/product-download')
    build_gui('ftkimager', 'FTK Imager',
              'https://accessdata.com/product-download')
    build_gui('hashcat', 'hashcat', 'https://hashcat.net/beta/')
    build_gui('hstex', 'HstEx',
              'https://www.digital-detective.net/start/hstex-quick-start/')
    build_gui('ileapp', 'iLEAPP', 'https://github.com/abrignoni/iLEAPP')
    build_gui('irec', 'IREC', 'https://binalyze.com/products/irec/release-notes/')
    build_gui('ive', 'iVe', 'https://berla.co/customer-support/')
    build_gui('kali', 'Kali', 'https://www.kali.org/downloads/')
    build_gui('kape', 'KAPE',
              'https://ericzimmerman.github.io/KapeDocs/#!Pages\\0.-Changelog.md')
    build_gui('lime', 'LiME',
              'https://github.com/504ensicsLabs/LiME/releases/latest')
    build_gui('macquisition', 'MacQuisition',
              'https://www.blackbagtech.com/downloads/')
    build_gui('mobiledit', 'MobilEdit', 'https://www.mobiledit.com/downloads')
    build_gui('mountimagepro', 'Mount Image Pro',
              'http://www.forensicexplorer.com/download.php')
    build_gui('mysql_connector_odbc', 'MySql Connector ODBC',
              'https://dev.mysql.com/downloads/connector/odbc/')
    build_gui('netanalysis', 'NetAnalysis',
              'https://www.digital-detective.net/start/netanalysis-quick-start/')
    build_gui('nirsoft', 'NirSoft Launcher',
              'https://launcher.nirsoft.net/downloads/index.html')
    build_gui('nsrl', 'NSRL hash set',
              'https://www.nist.gov/itl/ssd/software-quality-group/national-software-reference-library-nsrl/nsrl-download/current-rds')
    build_gui('osf', 'OSForensics',
              'https://www.osforensics.com/download.html')
    build_gui('oxygen', 'Oxygen Forensic',
              'http://www.oxygen-forensic.com/download/whatsnew/OFD/WhatsNew.html')
    build_gui('paraben', 'Paraben E3',
              'https://paraben.com/paraben-downloads/')
    build_gui('passware', 'Passware',
              'https://www.passware.com/kit-forensic/whatsnew/')
    build_gui('physicalanalyzer', 'Physical Analyzer',
              'https://www.cellebrite.com/en/support/product-releases/')
    build_gui('sleuthkit', 'The Sleuth Kit',
              'https://github.com/sleuthkit/sleuthkit/releases/latest')
    build_gui('tzworks', 'TZWorks', 'https://tzworks.net/download_links.php')
    build_gui('ufed4pc', 'UFED 4PC',
              'https://www.cellebrite.com/en/support/product-releases/')
    build_gui('usbdetective', 'USB Detective',
              'https://usbdetective.com/release-notes/')
    build_gui('veracrypt', 'VeraCrypt',
              'https://www.veracrypt.fr/en/Downloads.html')
    build_gui('xamn', 'XAMN', 'https://www.msab.com/downloads/')
    build_gui('xways', 'X-Ways', 'http://www.x-ways.net/winhex/license.html')

    gui_option = StringVar()
    gui_option.set(gui)
    gui_toggle = OptionMenu(inner_frame, gui_option,
                            'Display all', 'Display used', 'CLI mode')

    current_save = Button(inner_frame, text='Save', command=save)
    current_save.grid(column=1, row=rowID, columnspan=2,
                      sticky=E+W, pady=(7, 7))

    pixel = PhotoImage(width=1, height=1)
    if os.name == 'nt':
        gui_toggle.config(image=pixel, height=14, compound='c')
        gui_toggle.grid(column=0, row=rowID, sticky=N +
                        S+W, padx=(5, 0), pady=(7, 7))
        current_save.config(image=pixel, height=18, compound='c')
    elif platform == 'darwin':
        gui_toggle.config(image=pixel, height=18, compound='c')
        gui_toggle.grid(column=0, row=rowID, sticky=N +
                        S+W, padx=(4, 0), pady=(5, 7))
        current_save.config(image=pixel, height=14, compound='c')
    else:
        gui_toggle.config(image=pixel, height=16, compound='c')
        gui_toggle.grid(column=0, row=rowID, sticky=N +
                        S+W, padx=(4, 0), pady=(7, 7))
        current_save.config(image=pixel, height=16, compound='c')

    about = Label(inner_frame, text='    ?', font=(
        'TkDefaultFont', fontsize), fg='grey', cursor='hand2')
    about.grid(column=3, row=rowID, pady=(7, 7), sticky=W)
    about.bind('<ButtonRelease-1>', lambda e: about_box())

    root.update()
    max_heigth = get_max_height()

    if (inner_frame.winfo_height() > (max_heigth - 100)) and max_heigth != 200:
        sf.configure(height=max_heigth - 100,
                     width=inner_frame.winfo_width() + 20)
        root.resizable(False, True)
    else:
        sf.configure(height=inner_frame.winfo_height(),
                     width=inner_frame.winfo_width() + 20)
        root.resizable(False, True)

    root.attributes('-alpha', 1)
    root.lift()
    root.attributes('-topmost', True)
    root.attributes('-topmost', False)

    if first_run != True:
        refresh_gui()
    else:
        messagebox.showinfo('Welcome', 'A new config file has been created.\n\n\
Please populate your current tool versions,\nchoose a display mode, and click Save.')

    for widget in widget_order:
        widget.lift()

    while True:
        try:
            root.mainloop()
            break
        except UnicodeDecodeError:
            pass
else:
    table = []
    run_cli()
