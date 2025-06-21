import webbrowser
import tkinter as tk
from tkinter import ttk, messagebox
from termcolor import colored
import customtkinter
col = colored
import subprocess
import wget
import os
import getpass
import shutil
import sys
import pygame
import hashlib
from pygame import mixer
from urllib import request
from PIL import ImageTk, Image
import urllib
import io
import requests
import readline
from pytube import YouTube

os.system('title malehTerminal')
os.system('cls')

mixer.init()
pausedmusic = False
version = '1.9'
update_available = False

if os.path.exists(f'{os.path.expanduser("~")}/AppData/malehTerminal/settings.txt'):
    try:
        with open(f'{os.path.expanduser("~")}/AppData/malehTerminal/settings.txt', 'r') as f:
            USER_COLOR, DIR_COLOR, SUCCESS_COLOR, ERROR_COLOR, PROMPT_STYLE = f.read().split('\n')
            f.close()
    except:
        pass
else:
    USER_COLOR = 'green'
    DIR_COLOR = 'blue'
    SUCCESS_COLOR = 'green'
    ERROR_COLOR = 'red'
    PROMPT_STYLE = 'one-line'

def error(text):
    global ERROR_COLOR
    return col(text, ERROR_COLOR)

def success(text):
    global SUCCESS_COLOR
    return col(text, SUCCESS_COLOR)

def get_path(text):
    result = []
    start_index = text.find('"')
    
    while start_index != -1:
        end_index = text.find('"', start_index + 1)
        if end_index != -1:
            result.append(text[start_index + 1:end_index])
            print(start_index+1, end_index)
        else:
            break
        start_index = text.find('"', end_index + 1)
    
    return result

url = "https://malehterminal.netlify.app/version.txt"
file = request.urlopen(url)
for line in file:
    decoded_line = line.decode("utf-8").strip()
    if decoded_line == str(version):
        update_available = False
    else:
        update_available = True
        print(error('A new malehTerminal update is available\nDownload it at https://malehterminal.netlify.app'))

commands = ['help',
'rm',
'ls',
'cd',
'echo',
'unzip',
'zip',
'whoami',
'pwd',
'mv',
'desktop',
'cp',
'opendir',
'settings',
'open',
'cat',
'touch',
'rmdir',
'mkdir',
'clear',
'wget',
'exit',
'calculate',
'mp3',
'malehterminal',
'plugins',
'project123',
'cmdlist',
'browser',
'webhook',
'ytdownload']

commands_explanation = {'help':'Shows how commands work',
'rm':'Remove a file',
'ls':'List all items in a directory',
'cd':'Change current directory',
'echo':'Print entered text',
'unzip':'Unpack a zip file',
'zip':'Create a zip file',
'whoami':'Print current username',
'pwd':'Print current working directory',
'mv':'Move a file or directory',
'desktop':'Change to desktop directory',
'cp':'Copy a file or directory',
'opendir':'Open a directory in your explorer',
'settings':'Open Settings menu',
'open':'Open a file in notepad.exe',
'cat':'Read content of a file',
'touch':'Create a file',
'rmdir':'Remove a directory',
'mkdir':'Create a directory',
'clear':'Clear the command prompt',
'wget':'Install items from web',
'exit':'Close the command prompt',
'calculate':'Calculate calculations using malehTerminal',
'mp3':'Play a mp3 music file',
'malehterminal':'Show informations about malehTerminal',
'project123':'HIDDEN',
'cmdlist':'Show all commands',
'webhook':'Send files to a webhook using discord webhooks',
'ytdownload':'Download youtube videos in mp3, mp4 and many more file formats'}

commands_usage = {'help':'Usage: help <command>',
'rm':'Usage: rm <target>',
'ls':'Usage: ls <target>\nLeave <target> empty so list current directory',
'cd':'Usage: cd <path>\nLeave <path> empty to change directory to user directory',
'echo':'Usage: echo <text>\nSpecial text: $SHELL, $USER',
'unzip':'Usage: unzip <target>',
'zip':'Usage: zip <target> <output-name>\nYou can leave <output-name> empty',
'whoami':'Usage: whoami',
'pwd':'Usage: pwd',
'mv':'Usage: mv <target> <where-to-move>',
'desktop':'Usage: desktop',
'cp':'Usage: cp <target> <where-to-copy>',
'opendir':'Usage: opendir <target>\nLeave <target> empty to open current directory',
'settings':'Usage: settings',
'open':'Usage: open <target>',
'cat':'Usage: cat <target>',
'touch':'Usage: touch <name>',
'rmdir':'Usage: rmdir <target>',
'mkdir':'Usage: mkdir <name>',
'clear':'Usage: clear',
'wget':'Usage: wget <url> <output-path>\nYou can leave <output-path> empty',
'exit':'Usage: exit',
'calculate':'Usage: calculate <calculation>',
'mp3':'Usage: mp3 play <path-to-mp3>\nUsage: mp3 pause - Pause current song\nUsage: mp3 unpause - Unpause current song\nUsage: mp3 volume <0-100> - Change volume',
'malehterminal':'Usage: malehterminal',
'project123':'HIDDEN',
'cmdlist':'cmdlist',
'webhook':'Usage: webhook <file> <webhook-url>',
'ytdownload':'Usage: ytdownload <url> <format> <output-path>\nYou can leave <output-path> empty'}

plugin_names = ['YouTube Downloader','Terminal customization','YouTube Downloader','Terminal customization','YouTube Downloader','Terminal customization','YouTube Downloader','Terminal customization','YouTube Downloader','Terminal customization','YouTube Downloader','Terminal customization','YouTube Downloader','Terminal customization','YouTube Downloader','Terminal customization']
plugin_versions = {'YouTube Downloader':'1.0','Terminal customization':'1.1'}
plugin_authors = {'YouTube Downloader':'maleh','Terminal customization':'maleh'}
plugin_descriptions = {'YouTube Downloader':None,'Terminal customization':None}
plugin_imglinks = {'YouTube Downloader':'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/YouTube_social_red_circle_%282017%29.svg/2048px-YouTube_social_red_circle_%282017%29.svg.png'
                   ,'Terminal customization':'https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/GNOME_Terminal_icon_2019.svg/1024px-GNOME_Terminal_icon_2019.svg.png'}
    

def load_image(url, x=25, y=25):
    raw_data = urllib.request.urlopen(url).read()
    im = Image.open(io.BytesIO(raw_data)).resize((x,y))
    image = ImageTk.PhotoImage(im)
    return image

class CreatePlugin:
    def __init__(self, win, name, version, author, description, img_link, x, y):
        frame = customtkinter.CTkFrame(master=win, width=266, height=70, cursor='hand2')
        frame.place(x=x, y=y)
        img = load_image(str(img_link), x=50, y=50)
        l1=customtkinter.CTkLabel(master=frame, image=img, text=' ', font=('Consolas',13), cursor='hand2')
        l1.place(rely=.5, anchor=customtkinter.CENTER, x=35)
        l2=customtkinter.CTkLabel(master=frame, text=str(name), font=('Consolas',13), cursor='hand2')
        l2.place(y=1, x=73)
        l3=customtkinter.CTkLabel(master=frame, text=f'Version {str(version)} by {str(author)}', font=('Consolas',11), cursor='hand2')
        l3.place(y=27, x=73)
        frame.bind('<Button-1>', lambda e:print('hey'))
        l1.bind('<Button-1>', lambda e:print('hey'))
        l2.bind('<Button-1>', lambda e:print('hey'))
        l3.bind('<Button-1>', lambda e:print('hey'))

project123_access = False

class Commands:
    global cmdargs, fullcmd
    def webhook_cmd():
        def send_file(file_path, url):             
            with open(file_path, "rb") as filetosend:
                files = {'file': filetosend}
                r = requests.post(url, files=files)
                r.text
                filetosend.close()
        try:
            file_path = get_path(fullcmd)
            webhookurl = get_path(fullcmd, arg=1)
            if os.path.exists(file_path):
                if os.path.isfile(file_path):
                    try:
                        send_file(file_path, webhookurl)
                        print(success('Successfully sent file'))
                    except requests.exceptions.MissingSchema:
                           print(error('The webhook was not found'))
                    except:
                        print(error('There was an error while sending file'))
                else:
                    print(error("The entered path isn't a file"))
            else:
                print(error("The file does not exist"))
        except IndexError:
            print(error(commands_usage["webhook"]))
        except:
            print(error('There was an error'))
    def browser_cmd():
        try:
            url = get_path(fullcmd)
            webbrowser.open(url)
            print(success(f'Successfully opened {str(url)}'))
        except IndexError:
            print(error(commands_usage['browser']))
        except:
            print(error('There was an error'))
    def cmdlist_cmd():
        for cmd in commands:
            print(cmd)
    def project123_cmd():
        global project123_access
        try:
            cmd = cmdargs[1]
            if cmd.lower() == 'login':
                if project123_access == True:
                    print('You are already logged in\nTo logout use: project123 logout')
                else:
                    pwd = getpass.getpass('To use this command you need to enter a password: ')
                    pwd_hash = hashlib.sha256(pwd.encode()).hexdigest()
                    data = request.urlopen('https://project123-maleh-lugga.netlify.app/malehterminal_pwd.txt')
                    for line in data:
                        decoded_line = line.decode("utf-8").strip()
                        if decoded_line == pwd_hash:
                            print(success('Successfully logged in\nYou are now able to use project123 commands\nTo logout use: project123 logout'))
                            project123_access = True
                        else:
                            print(error('The entered password is wrong'))
            elif cmd.lower() == 'help':
                if project123_access == True:
                    pass
                else:
                    print(error('You have no permission to use this command'))
            elif cmd.lower() == 'logout':
                if project123_access == True:
                    project123_access = False
                    print(success('Successfully logged out'))
                else:
                    print(error('You are not logged in'))
        except IndexError:
            print(error(commands_usage['project123']))
        except:
            print(error('Error'))
    def malehterminal_cmd():
        try:
            if update_available:
                print(f'{error("A new update is available!")}\nmalehTerminal v{str(version)}\nMade by maleh with python\nhttps://malehterminal.netlify.app') 
            else:
                print(f'malehTerminal v{str(version)}\nMade by maleh with python\nhttps://malehterminal.netlify.app')
        except:
            pass
    def plugins_cmd():
        try:
            window1 = customtkinter.CTk()
            window1.title('malehTerminal Plugins')
            window1.resizable(False, False)
            window1.geometry('1092x600')

            topframe = customtkinter.CTkFrame(master=window1, width=1083, height=50)
            topframe.place(x=5, y=5)
            
            logoimage = ImageTk.PhotoImage(Image.open(f'{os.path.expanduser("~")}/AppData/Roaming/malehTerminal/images/icon.png'))
            window1.call('wm', 'iconphoto', window1._w, logoimage)
            logoimage = ImageTk.PhotoImage(Image.open(f'{os.path.expanduser("~")}/AppData/Roaming/malehTerminal/images/icon.png').resize((25,25)))
            customtkinter.CTkLabel(master=topframe, image=logoimage, text=' malehTerminal Plugins', compound=customtkinter.LEFT, font=('Consolas',16)).place(x=15,y=10)
            x = 5
            y = 60
            for plugin in plugin_names:
                CreatePlugin(win=window1, name=str(plugin), version=str(plugin_versions[plugin]), author=str(plugin_authors[plugin]), description=str(plugin_descriptions[plugin]), img_link=str(plugin_imglinks[plugin]), x=x, y=y)
                x+=272
                if x>=900:
                    x=5
                    y+=75

            window1.mainloop()
        except:
            pass
    def help_cmd():
        try:
            cmd = cmdargs[1]
            if cmd.lower() in commands:
                print(f'Help for {cmd.lower()}:\n{commands_explanation[cmd.lower()]}\n{commands_usage[cmd.lower()]}')
            else:
                print(error(f'help: No command named {cmd.lower()}'))
        except IndexError:
            print(error(commands_usage['help']))
        except:
            print(error('Error'))
    def mp3_cmd():
        global pausedmusic
        try:
            arg = cmdargs[1]
            if arg.lower() == 'play':
                try:
                    path = get_path(fullcmd, arg=1)
                except:
                    pass
                if os.path.exists(path):
                    if path.endswith('.mp3'):
                        try:
                            mixer.music.unload()
                            mixer.music.unpause()
                            mixer.music.load(path)
                            mixer.music.play()
                            pausedmusic = False
                            print(success(f'Now playing: {os.path.basename(path)}'))
                        except:
                            print(error('mp3: There was an error while playing the file'))    
                    else:
                        print(error('mp3: Target is not a mp3 file'))
                else:
                    print(error('mp3: No such file or directory'))
            elif arg.lower() == 'pause':
                if pausedmusic == False:
                    pausedmusic = True
                    mixer.music.pause()
                    print(success('Music is now paused'))
                else:
                    print(error('Music is already paused'))
            elif arg.lower() == 'unpause':
                if pausedmusic == True:
                    pausedmusic = False
                    mixer.music.unpause()
                    print(success('Music is now unpaused'))
                else:
                    print(error('Music is not paused'))
            elif arg.lower() == 'volume':
                try:
                    volume = int(cmdargs[2])
                    if volume in range(0,101):
                        if volume in range(0,10):
                            volume2 = float('0.0'+cmdargs[2])
                        elif volume == 100:
                            volume2 = 1
                        else:
                            volume2 = float('0.'+cmdargs[2])
                        mixer.music.set_volume(volume2)
                        print(success(f'Volume was set to {str(volume)}'))
                    else:
                        print(error(commands_usage['mp3']))
                except:
                    print(error(commands_usage['mp3']))
            else:
                print(error(commands_usage['mp3']))
        except:
            print(error(commands_usage['mp3']))
        #except:
         #   print('error')
    def rm_cmd():
        try:
            path = get_path(fullcmd)[0]
            try:
                if os.path.exists(path):
                    os.remove(path)
                    print(success('Successfully removed'))
                else:
                    print(error("The path does not exist"))
            except:
                print(error('Permission denied'))
        except IndexError:
            print(error(commands_usage['rm']))
    def ls_cmd():
        try:
            path = get_path(fullcmd)
            if os.path.exists(path):
                listd = os.listdir(path)
                list1 = []
                for i in listd:
                    i = i.replace(i, col(i, 'cyan'))
                    list1.append(i)
                current=''
                for x in list1:
                    if x==list1[0]:
                        current=str(x)
                    else:
                        current = f'{current}     {str(x)}'
                print(current)
            else:
                print(error('ls: No such file or directory'))
        except IndexError:
            listd = os.listdir(os.getcwd())
            list1 = []
            for i in listd:
                i = i.replace(i, col(i, 'cyan'))
                list1.append(i)
            current=''
            for x in list1:
                if x==list1[0]:
                    current=str(x)
                else:
                    current = f'{current}     {str(x)}'
            print(current)
        except:
            print(error('Error'))
    def echo_cmd():
        try:
            text = cmdargs[1]
            text = fullcmd[5::]
            if text.lower() == '$shell':
                print('malehTerminal')
            elif text.lower() == '$user':
                print(getpass.getuser())
            else:
                print(text)
        except:
            print(error(commands_usage['echo']))
    def unzip_cmd():
        try:
            target = get_path(fullcmd)
            if os.path.exists(target):
                extensions = ['.tar.gz', '.bz2', '.zip']
                x = False
                for extension in extensions:
                    if target.endswith(extension):
                        x = True
                if x:
                    shutil.unpack_archive(target, dir)
                else:
                    print(error('unzip: Target is not a zip file'))
            else:
                print(error('unzip: No such file or directory'))
        except:
            print(error(commands_usage['unzip']))
    def zip_cmd():
        try:
            target = get_path(fullcmd)
            if os.path.exists(target):
                try:
                    name = get_path(fullcmd, arg=1)
                except:
                    name = os.path.basename(get_path(fullcmd))
                shutil.make_archive(name, format='zip', root_dir='.', base_dir=target)
            else:
                print(error('zip: No such file or directory'))
        except:
            print(error(commands_usage['zip']))
    def whoami_cmd():
        print(getpass.getuser())
    def pwd_cmd():
        print(dir)
    def mv_cmd():
        try:
            file = get_path(fullcmd)
            new_file = get_path(fullcmd, arg=1)
            print(file, new_file)
            if os.path.exists(file):
                try:
                    os.rename(file, new_file)
                    print(success(f'Successfully moved'))
                except:
                    print(error('Permission denied'))
        except:
            print(error(commands_usage['mv']))
    def desktop_cmd():
        os.chdir(os.path.expanduser('~') + '/Desktop')
    def cp_cmd():
        try:
            first_file = get_path(fullcmd)
            second_file = get_path(fullcmd, arg=1)
            if os.path.exists(first_file) and os.path.isfile(first_file):
                try:
                    if os.path.exists(second_file):
                        pass
                    else:
                        with open(second_file, 'w') as f:
                            f.close()
                    with open(first_file, 'r') as f:
                        content = f.read()
                        f.close()
                    with open(second_file, 'w') as f:
                        f.write(content)
                        f.close()
                    print(success(f'Successfully copied content from {first_file} to {second_file}'))
                except:
                    print(error('Permission denied'))
            else:
                print(error('cp: No such file or directory'))
        except:
            print(error(commands_usage['cp']))
    def play_cmd():
        pygame.mixer.init()
    def opendir_cmd():
        try:
            directory = get_path(fullcmd)
            if os.path.exists(directory):
                subprocess.Popen(f'explorer {directory}')
            else:
                print(error('opendir: No such file or directory'))
        except:
            directory = os.getcwd()
            subprocess.Popen(f'explorer {directory}')
    def settings_cmd():
        def dragonwin(event):
            x = root.winfo_pointerx() - root._offsetx
            y = root.winfo_pointery() - root._offsety
            root.geometry(f"+{x}+{y}")
        def clickonwin(event):
            root._offsetx = root.winfo_pointerx() - root.winfo_rootx()
            root._offsety = root.winfo_pointery() - root.winfo_rooty()
        def change_color(value):
            global USER_COLOR, DIR_COLOR, SUCCESS_COLOR, ERROR_COLOR, PROMPT_STYLE
            USER_COLOR = varname.get().lower()
            DIR_COLOR = vardir.get().lower()
            SUCCESS_COLOR = varsuccess.get().lower()
            ERROR_COLOR = varerror.get().lower()
            PROMPT_STYLE = varstyle.get().lower()
            try:
                if os.path.exists(f'{os.path.expanduser("~")}/AppData/malehTerminal/settings.txt'):
                    with open(f'{os.path.expanduser("~")}/AppData/malehTerminal/settings.txt', 'w') as f:
                        f.write(f'{USER_COLOR}\n{DIR_COLOR}\n{SUCCESS_COLOR}\n{ERROR_COLOR}\n{PROMPT_STYLE}')
                        f.close()
                else:
                    if os.path.exists(f'{os.path.expanduser("~")}/AppData/malehTerminal'):
                        pass
                    else:
                        os.mkdir(f'{os.path.expanduser("~")}/AppData/malehTerminal')
                    with open(f'{os.path.expanduser("~")}/AppData/malehTerminal/settings.txt', 'w') as f:
                        f.write(f'{USER_COLOR}\n{DIR_COLOR}\n{SUCCESS_COLOR}\n{ERROR_COLOR}\n{PROMPT_STYLE}')
                        f.close()
            except:
                pass
        root = customtkinter.CTk()
        root.overrideredirect(True)
        root._offsetx = 0
        root._offsety = 0
        root.title('malehTerminal Settings - by maleh')
        root.geometry('600x400')
        root.resizable(False, False)
        color_list = ['Cyan','Red','Blue','Yellow','Green', 'Grey', 'Magenta', 'White']
        style_list = ['One-Line','Two-Line']
            
        varname = tk.StringVar()
        vardir = tk.StringVar()
        varsuccess = tk.StringVar()
        varerror = tk.StringVar()
        varstyle = tk.StringVar()

        root.configure(background='#545454')

        varname.set(USER_COLOR.capitalize())
        vardir.set(DIR_COLOR.capitalize())
        varsuccess.set(SUCCESS_COLOR.capitalize())
        varerror.set(ERROR_COLOR.capitalize())
        varstyle.set(PROMPT_STYLE.capitalize())

        label = tk.Label(master=root, text='Settings', font=('Consolas',15)).place(x=10, y=10)
        customtkinter.CTkButton(master=root, text='Save & Close', font=('Consolas',13), command=lambda: root.destroy(), cursor='hand2').place(x=450, y=10)
        customtkinter.CTkLabel(master=root, text='Name color:').place(x=230, y=100, anchor=tk.CENTER)
        customtkinter.CTkLabel(master=root, text='Directory color:').place(x=230, y=150, anchor=tk.CENTER)
        customtkinter.CTkLabel(master=root, text='Success color:').place(x=230, y=200, anchor=tk.CENTER)
        customtkinter.CTkLabel(master=root, text='Error color:').place(x=230, y=250, anchor=tk.CENTER)
        customtkinter.CTkLabel(master=root, text='Prompt style:').place(x=230, y=300, anchor=tk.CENTER)

        nameop = ttk.OptionMenu(root, varname, USER_COLOR, command=change_color, *color_list)
        nameop.configure(width=10)
        nameop.place(x=350, y=100, anchor=tk.CENTER)
        dirop = ttk.OptionMenu(root, vardir, DIR_COLOR, command=change_color, *color_list)
        dirop.configure(width=10)
        dirop.place(x=350, y=150, anchor=tk.CENTER)
        successop = ttk.OptionMenu(root, varsuccess, SUCCESS_COLOR, command=change_color, *color_list)
        successop.configure(width=10)
        successop.place(x=350, y=200, anchor=tk.CENTER)
        errorop = ttk.OptionMenu(root, varerror, ERROR_COLOR, command=change_color, *color_list)
        errorop.configure(width=10)
        errorop.place(x=350, y=250, anchor=tk.CENTER)
        styleop = ttk.OptionMenu(root, varstyle, PROMPT_STYLE, command=change_color, *style_list)
        styleop.configure(width=10)
        styleop.place(x=350, y=300, anchor=tk.CENTER)
            
        root.bind('<Button-1>',clickonwin)
        root.bind('<B1-Motion>',dragonwin)
        for child in root.winfo_children():
            try:
                try:
                    child.config(fg='white', bg='#545454', activeforeground='white', activebackground='#545454')
                except:
                    child.config(fg='white', bg='#545454')
            except:
                pass
        root.mainloop()
    def open_cmd():
        try:
            file = get_path(fullcmd)
            if os.path.exists(file):
                if os.path.isfile(file):
                    try:
                        os.system(f'notepad.exe {file}')
                    except:
                        print(error('open: Error'))
                else:
                    print(error('open: Path is not a file'))
            else:
                print(error('open: No such file or directory'))
        except IndexError:
            print(error(commands_usage['open']))
    def ytdownload_cmd():
        try:
            format = cmdargs[1]
            url = cmdargs[2]
            print(format, url)
            try:
                out_path = out_path = get_path(fullcmd, arg=3)
            except:
                out_path = os.getcwd()
            if(format.lower() == "audio"):
                yt = YouTube(url)
                video = yt.streams.filter(only_audio=True).first() 
                out_file = video.download(output_path=out_path) 
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
                print(success("Successfully downloaded " + new_file))
            elif(format.lower() == "video"):
                yt = YouTube(url)
                video = yt.streams.filter(only_audio=False).first() 
                out_file = video.download(output_path=out_path) 
                base, ext = os.path.splitext(out_file) 
                new_file = base + '.mp4'
                os.rename(out_file, new_file)
                print(success("Successfully downloaded " + new_file))
        except IndexError:
            print(error(commands_usage['ytdownload']))
    def cat_cmd():
        try:
            path = get_path(fullcmd)
            if os.path.exists(path):
                if os.path.isfile(path):
                    try:
                        with open(path, 'r') as f:
                            content = f.read()
                            f.close()
                        print(content)
                    except:
                        print(error('cat: There was an error.\nMaybe the entered path isnt a file'))
                else:
                    print(error('cat: Path is not a file'))
            else:
                print(error('cat: No such file or directory'))
        except IndexError:
            print(error(commands_usage['cat']))
    def touch_cmd():
        try:
            file = get_path(fullcmd)
            if os.path.exists(file):
                print(error('touch: File already exists'))
            else:
                try:
                    with open(file, 'w') as f:
                        f.close()
                    print(success('Successfully created file'))
                except:
                    print(error('touch: Error'))
        except IndexError:
            print(error(commands_usage['touch']))
    def rmdir_cmd():
        try:
            path = get_path(fullcmd)
            if os.path.exists(path):
                if len(os.listdir(path)) == 0:
                    try:
                        os.rmdir(path)
                        print(success('Successfully removed directory'))
                    except:
                        print(error('Permission denied'))
                else:
                    a = input('The directory you want to delete contains files\nDo you still want to delete it? [Y/N]')
                    if a.lower() == 'y':
                        try:
                            shutil.rmtree(path)
                            print(success('Successfully removed directory'))
                        except:
                            print(error('Permission denied'))
                    else:
                        pass
            else:
                print(error('rmdir: No such file or directory'))
        except IndexError:
            print(error(commands_usage['rmdir']))
    def mkdir_cmd():
        try:
            path = get_path(fullcmd)
            if os.path.exists(path):
                print(error('mkdir: Directory already exists'))
            else:
                try:
                    os.mkdir(path)
                    print(success('Successfully created directory'))
                except:
                    print(error('Permission denied'))
        except IndexError:
            print(error(commands_usage['mkdir']))
    def clear_cmd():
        os.system('cls')
    def wget_cmd():
        try:
            url = get_path(fullcmd)
            try:
                out_path = get_path(fullcmd, arg=1)
                if os.path.exists(out_path):
                    try:
                        wget.download(url=url, out=out_path)
                        print(success('\nSuccessfully downloaded'))
                    except:
                        print(error('wget: URL does not exist'))
                else:
                    print(error('wget: No such file or directory'))
            except IndexError:
                try:
                    wget.download(url=url, out=dir)
                    print(success('\nSuccessfully downloaded'))
                except:
                    print(error('wget: URL does not exist'))
        except IndexError:
            print(error(commands_usage['wget']))
    def exit_cmd():
        sys.exit()
    def cd_cmd():
        try:
            new_path = get_path(fullcmd)
            if os.path.exists(new_path):
                os.chdir(new_path)
            else:
                print(error('cd: No such file or directory'))
        except IndexError:
            os.chdir(os.path.expanduser("~"))
    def calculate_cmd():
        try:
            calculation = cmdargs[1]
            calculation = fullcmd[10::]
            print(eval(calculation))
        except SyntaxError:
            print(error('calculate: There was an error'))
        except:
            print(error(commands_usage['calculate']))

def getprompt(username, directory):
    global PROMPT_STYLE, USER_COLOR, DIR_COLOR
    if PROMPT_STYLE == 'one-line':
        return f'{col(username, USER_COLOR)} {col(directory, DIR_COLOR)}$ '
    elif PROMPT_STYLE == 'two-line':
        return f'┌──({col(username, USER_COLOR)})-[{col(directory, DIR_COLOR)}]\n└─$ '
    else:
        return 'Error'

def completer(text, state):
    all_items = [".", ".."]
    for i in os.listdir(os.getcwd()):
        all_items.append(i)
    matches = [item for item in all_items if item.startswith(text)]
    if state < len(matches):
        if " " in matches[state]:
            return '"' + matches[state] + '"'
        return matches[state]
    else:
        return None

def input_autocompletion(prompt):
    readline.set_completer(completer)
    readline.parse_and_bind("tab: complete")
    return input(prompt)

while True:
    dir = os.getcwd()
    prompt = getprompt(getpass.getuser(), dir)
    fullcmd = input_autocompletion(prompt)
    if fullcmd.strip() == '':
        continue
    cmdargs = fullcmd.split()
    command = cmdargs[0]

    if command.lower() in commands:
        command = f'Commands.' + command.lower() + '_cmd'
        eval(command + "()")
    else:
        try:
            subprocess.call(fullcmd)
        except:
            print(error(command + ': command not found'))