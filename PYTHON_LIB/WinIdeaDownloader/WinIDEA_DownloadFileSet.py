from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import configparser
import isystem as ic
import os
import os.path

#====================================================================================================================

inifile = "C:/Users/leemi4/Desktop/My PythonScript/WinIDEA_DownloadFileSet/WinIDEA_DownloadFileSet.ini"
sandboxdir = "D:/00.Sandboxes/HKMC"

def sandboxdirUpdater(str):
    global sandboxdir
    sandboxdir = os.path.dirname(str)

#====================================================================================================================

root = Tk()
root.title("winIDEA Downloader")
root.geometry("1240x670")

#====================================================================================================================

def Callback_MasterBootButton():
    print(sandboxdir)
    name= filedialog.askopenfilename(initialdir=sandboxdir);
    sandboxdirUpdater(name)
    list = MasterBootComboBox['value'] 
    if not name in list:
        if list == "":
            list = (name,)
        else:
            list =  list + (name,)
        newlist = ';'.join(list)
        config.set("MasterBoot", "list", newlist)
        with open(inifile, 'w') as configfile:
            config.write(configfile)
        MasterBootComboBox['value'] = list
    MasterBootComboBox.current(list.index(name))

yposition = 10    
MasterBootButton = Button(root, height=2, width=15, text='Master Boot', command=Callback_MasterBootButton)
MasterBootButton.place(x=10, y=yposition)
box_value = StringVar()
MasterBootComboBox = ttk.Combobox(root, textvariable=box_value, height=10, width=180)
MasterBootComboBox.place(x=130, y=yposition)

def Callback_SlaveBootButton():
    print(sandboxdir)
    name= filedialog.askopenfilename(initialdir=sandboxdir);
    sandboxdirUpdater(name)
    list = SlaveBootComboBox['value'] 
    if not name in list:
        if list == "":
            list = (name,)
        else:
            list =  list + (name,)
        newlist = ';'.join(list)
        config.set("SlaveBoot", "list", newlist)
        with open(inifile, 'w') as configfile:
            config.write(configfile)
        SlaveBootComboBox['value'] = list
    SlaveBootComboBox.current(list.index(name))

yposition = 40 + yposition
SlaveBootButton = Button(root, height=2, width=15, text='Slave Boot', command=Callback_SlaveBootButton)
SlaveBootButton.place(x=10, y=yposition)
box_value = StringVar()
SlaveBootComboBox = ttk.Combobox(root, textvariable=box_value, height=10, width=180)
SlaveBootComboBox.place(x=130, y=yposition)


def Callback_HtsmButton():
    print(sandboxdir)
    name= filedialog.askopenfilename(initialdir=sandboxdir);
    sandboxdirUpdater(name)
    list = HtsmComboBox['value'] 
    if not name in list:
        if list == "":
            list = (name,)
        else:
            list =  list + (name,)
        newlist = ';'.join(list)
        config.set("Htsm", "list", newlist)
        with open(inifile, 'w') as configfile:
            config.write(configfile)
        HtsmComboBox['value'] = list
    HtsmComboBox.current(list.index(name))

yposition = 40 + yposition
HtsmButton = Button(root, height=2, width=15, text='Htsm', command=Callback_HtsmButton)
HtsmButton.place(x=10, y=yposition)
box_value = StringVar()
HtsmComboBox = ttk.Combobox(root, textvariable=box_value, height=10, width=180)
HtsmComboBox.place(x=130, y=yposition)


def Callback_HtsmValidButton():
    print(sandboxdir)
    name= filedialog.askopenfilename(initialdir=sandboxdir);
    sandboxdirUpdater(name)
    list = HtsmValidComboBox['value'] 
    if not name in list:
        if list == "":
            list = (name,)
        else:
            list =  list + (name,)
        newlist = ';'.join(list)
        config.set("HtsmValid", "list", newlist)
        with open(inifile, 'w') as configfile:
            config.write(configfile)
        HtsmValidComboBox['value'] = list
    HtsmValidComboBox.current(list.index(name))

yposition = 40 + yposition
HtsmValidButton = Button(root, height=2, width=15, text='Htsm Valid', command=Callback_HtsmValidButton)
HtsmValidButton.place(x=10, y=yposition)
box_value = StringVar()
HtsmValidComboBox = ttk.Combobox(root, textvariable=box_value, height=10, width=180)
HtsmValidComboBox.place(x=130, y=yposition)


def Callback_AppButton():
    print(sandboxdir)
    name= filedialog.askopenfilename(initialdir=sandboxdir);
    sandboxdirUpdater(name)
    list = AppComboBox['value'] 
    if not name in list:
        if list == "":
            list = (name,)
        else:
            list =  list + (name,)
        newlist = ';'.join(list)
        config.set("App", "list", newlist)
        with open(inifile, 'w') as configfile:
            config.write(configfile)
        AppComboBox['value'] = list
    AppComboBox.current(list.index(name))

yposition = 40 + yposition
AppButton = Button(root, height=2, width=15, text='App', command=Callback_AppButton)
AppButton.place(x=10, y=yposition)
box_value = StringVar()
AppComboBox = ttk.Combobox(root, textvariable=box_value, height=10, width=180)
AppComboBox.place(x=130, y=yposition)


def Callback_AppValidButton():
    print(sandboxdir)
    name= filedialog.askopenfilename(initialdir=sandboxdir);
    sandboxdirUpdater(name)
    list = AppValidComboBox['value'] 
    if not name in list:
        if list == "":
            list = (name,)
        else:
            list =  list + (name,)
        newlist = ';'.join(list)
        config.set("AppValid", "list", newlist)
        with open(inifile, 'w') as configfile:
            config.write(configfile)
        AppValidComboBox['value'] = list
    AppValidComboBox.current(list.index(name))

yposition = 40 + yposition
AppValidButton = Button(root, height=2, width=15, text='App Valid', command=Callback_AppValidButton)
AppValidButton.place(x=10, y=yposition)
box_value = StringVar()
AppValidComboBox = ttk.Combobox(root, textvariable=box_value, height=10, width=180)
AppValidComboBox.place(x=130, y=yposition)


def Callback_DatasetButton():
    print(sandboxdir)
    name= filedialog.askopenfilename(initialdir=sandboxdir);
    sandboxdirUpdater(name)
    list = DatasetComboBox['value'] 
    if not name in list:
        if list == "":
            list = (name,)
        else:
            list =  list + (name,)
        newlist = ';'.join(list)
        config.set("Dataset", "list", newlist)
        with open(inifile, 'w') as configfile:
            config.write(configfile)
        DatasetComboBox['value'] = list
    DatasetComboBox.current(list.index(name))

yposition = 40 + yposition
DatasetButton = Button(root, height=2, width=15, text='Dataset', command=Callback_DatasetButton)
DatasetButton.place(x=10, y=yposition)
box_value = StringVar()
DatasetComboBox = ttk.Combobox(root, textvariable=box_value, height=10, width=180)
DatasetComboBox.place(x=130, y=yposition)


def Callback_DatasetValidButton():
    print(sandboxdir)
    name= filedialog.askopenfilename(initialdir=sandboxdir);
    sandboxdirUpdater(name)
    list = DatasetValidComboBox['value'] 
    if not name in list:
        if list == "":
            list = (name,)
        else:
            list =  list + (name,)
        newlist = ';'.join(list)
        config.set("DatasetValid", "list", newlist)
        with open(inifile, 'w') as configfile:
            config.write(configfile)
        DatasetValidComboBox['value'] = list
    DatasetValidComboBox.current(list.index(name))

yposition = 40 + yposition
DatasetValidButton = Button(root, height=2, width=15, text='Dataset Valid', command=Callback_DatasetValidButton)
DatasetValidButton.place(x=10, y=yposition)
box_value = StringVar()
DatasetValidComboBox = ttk.Combobox(root, textvariable=box_value, height=10, width=180)
DatasetValidComboBox.place(x=130, y=yposition)


def Callback_OtpMasterButton():
    print(sandboxdir)
    name= filedialog.askopenfilename(initialdir=sandboxdir);
    sandboxdirUpdater(name)
    list = OtpMasterComboBox['value'] 
    if not name in list:
        if list == "":
            list = (name,)
        else:
            list =  list + (name,)
        newlist = ';'.join(list)
        config.set("OtpMaster", "list", newlist)
        with open(inifile, 'w') as configfile:
            config.write(configfile)
        OtpMasterComboBox['value'] = list
    OtpMasterComboBox.current(list.index(name))

yposition = 40 + yposition
OtpMasterButton = Button(root, height=2, width=15, text='Otp Master', command=Callback_OtpMasterButton)
OtpMasterButton.place(x=10, y=yposition)
box_value = StringVar()
OtpMasterComboBox = ttk.Combobox(root, textvariable=box_value, height=10, width=180)
OtpMasterComboBox.place(x=130, y=yposition)


def Callback_OtpSlaveButton():
    print(sandboxdir)
    name= filedialog.askopenfilename(initialdir=sandboxdir);
    sandboxdirUpdater(name)
    list = OtpSlaveComboBox['value'] 
    if not name in list:
        if list == "":
            list = (name,)
        else:
            list =  list + (name,)
        newlist = ';'.join(list)
        config.set("OtpSlave", "list", newlist)
        with open(inifile, 'w') as configfile:
            config.write(configfile)
        OtpSlaveComboBox['value'] = list
    OtpSlaveComboBox.current(list.index(name))

yposition = 40 + yposition
OtpSlaveButton = Button(root, height=2, width=15, text='Otp Slave', command=Callback_OtpSlaveButton)
OtpSlaveButton.place(x=10, y=yposition)
box_value = StringVar()
OtpSlaveComboBox = ttk.Combobox(root, textvariable=box_value, height=10, width=180)
OtpSlaveComboBox.place(x=130, y=yposition)


def Callback_CalibButton():
    print(sandboxdir)
    name= filedialog.askopenfilename(initialdir=sandboxdir);
    sandboxdirUpdater(name)
    list = CalibComboBox['value'] 
    if not name in list:
        if list == "":
            list = (name,)
        else:
            list =  list + (name,)
        newlist = ';'.join(list)
        config.set("Calib", "list", newlist)
        with open(inifile, 'w') as configfile:
            config.write(configfile)
        CalibComboBox['value'] = list
    CalibComboBox.current(list.index(name))

yposition = 40 + yposition
CalibButton = Button(root, height=2, width=15, text='Calib', command=Callback_CalibButton)
CalibButton.place(x=10, y=yposition)
box_value = StringVar()
CalibComboBox = ttk.Combobox(root, textvariable=box_value, height=10, width=180)
CalibComboBox.place(x=130, y=yposition)


def Callback_UcbButton():
    print(sandboxdir)
    name= filedialog.askopenfilename(initialdir=sandboxdir);
    sandboxdirUpdater(name)
    list = UcbComboBox['value'] 
    if not name in list:
        if list == "":
            list = (name,)
        else:
            list =  list + (name,)
        newlist = ';'.join(list)
        config.set("Ucb", "list", newlist)
        with open(inifile, 'w') as configfile:
            config.write(configfile)
        UcbComboBox['value'] = list
    UcbComboBox.current(list.index(name))

yposition = 40 + yposition
UcbButton = Button(root, height=2, width=15, text='Ucb', command=Callback_UcbButton)
UcbButton.place(x=10, y=yposition)
box_value = StringVar()
UcbComboBox = ttk.Combobox(root, textvariable=box_value, height=10, width=180)
UcbComboBox.place(x=130, y=yposition)

def Callback_MasterFullFlashButton():
    print(sandboxdir)
    name= filedialog.askopenfilename(initialdir=sandboxdir);
    sandboxdirUpdater(name)
    list = MasterFullFlashComboBox['value'] 
    if not name in list:
        if list == "":
            list = (name,)
        else:
            list =  list + (name,)
        newlist = ';'.join(list)
        config.set("MasterFullFlash", "list", newlist)
        with open(inifile, 'w') as configfile:
            config.write(configfile)
        MasterFullFlashComboBox['value'] = list
    MasterFullFlashComboBox.current(list.index(name))

yposition = 40 + yposition
MasterFullFlashButton = Button(root, height=2, width=15, text='MasterFullFlash', command=Callback_MasterFullFlashButton)
MasterFullFlashButton.place(x=10, y=yposition)
box_value = StringVar()
MasterFullFlashComboBox = ttk.Combobox(root, textvariable=box_value, height=10, width=180)
MasterFullFlashComboBox.place(x=130, y=yposition)


def Callback_SlaveFullFlashButton():
    print(sandboxdir)
    name= filedialog.askopenfilename(initialdir=sandboxdir);
    sandboxdirUpdater(name)
    list = SlaveFullFlashComboBox['value'] 
    if not name in list:
        if list == "":
            list = (name,)
        else:
            list =  list + (name,)
        newlist = ';'.join(list)
        config.set("SlaveFullFlash", "list", newlist)
        with open(inifile, 'w') as configfile:
            config.write(configfile)
        SlaveFullFlashComboBox['value'] = list
    SlaveFullFlashComboBox.current(list.index(name))

yposition = 40 + yposition
SlaveFullFlashButton = Button(root, height=2, width=15, text='SlaveFullFlash', command=Callback_SlaveFullFlashButton)
SlaveFullFlashButton.place(x=10, y=yposition)
box_value = StringVar()
SlaveFullFlashComboBox = ttk.Combobox(root, textvariable=box_value, height=10, width=180)
SlaveFullFlashComboBox.place(x=130, y=yposition)

#====================================================================================================================

config = configparser.ConfigParser()
config.read(inifile)

inistr = config.get("MasterBoot", "list")
inituple = tuple(inistr.split(';'))
MasterBootComboBox['value'] = inituple

inistr = config.get("SlaveBoot", "list")
inituple = tuple(inistr.split(';'))
SlaveBootComboBox['value'] = inituple

inistr = config.get("Htsm", "list")
inituple = tuple(inistr.split(';'))
HtsmComboBox['value'] = inituple

inistr = config.get("HtsmValid", "list")
inituple = tuple(inistr.split(';'))
HtsmValidComboBox['value'] = inituple

inistr = config.get("App", "list")
inituple = tuple(inistr.split(';'))
AppComboBox['value'] = inituple

inistr = config.get("AppValid", "list")
inituple = tuple(inistr.split(';'))
AppValidComboBox['value'] = inituple

inistr = config.get("Dataset", "list")
inituple = tuple(inistr.split(';'))
DatasetComboBox['value'] = inituple

inistr = config.get("DatasetValid", "list")
inituple = tuple(inistr.split(';'))
DatasetValidComboBox['value'] = inituple

inistr = config.get("OtpMaster", "list")
inituple = tuple(inistr.split(';'))
OtpMasterComboBox['value'] = inituple

inistr = config.get("OtpSlave", "list")
inituple = tuple(inistr.split(';'))
OtpSlaveComboBox['value'] = inituple

inistr = config.get("Calib", "list")
inituple = tuple(inistr.split(';'))
CalibComboBox['value'] = inituple

inistr = config.get("Ucb", "list")
inituple = tuple(inistr.split(';'))
UcbComboBox['value'] = inituple

inistr = config.get("MasterFullFlash", "list")
inituple = tuple(inistr.split(';'))
MasterFullFlashComboBox['value'] = inituple

inistr = config.get("SlaveFullFlash", "list")
inituple = tuple(inistr.split(';'))
SlaveFullFlashComboBox['value'] = inituple

#====================================================================================================================

def Callback_MasterWrite():
    try:
        connectionMgr = ic.ConnectionMgr()
        connectionMgr.connectMRU('')  

        #data = ic.CDataController(connectionMgr)
        #data.eraseFlash()

        s3downloadConfig = ic.CDownloadConfiguration()
        if(s3downloadConfig != None):
          s3downloadConfig.setCodeOffset(0);
          s3downloadConfig.setSymbolsOffset(0);
          s3downloadConfig.setDownloadFileFormat(ic.CDownloadConfiguration.ftMotorolaS);
          s3downloadConfig.setUsedInFullDownload(True);

        elfdownloadConfig = ic.CDownloadConfiguration()
        if(elfdownloadConfig != None):
          elfdownloadConfig.setCodeOffset(0);
          elfdownloadConfig.setSymbolsOffset(0);
          elfdownloadConfig.setDownloadFileFormat(ic.CDownloadConfiguration.ftELF);
          elfdownloadConfig.setUsedInFullDownload(True);

        loader = ic.CLoaderController(connectionMgr)
        if(loader != None):
          loader.clearDownloadList(ic.CLoaderController.DLIST_PRIMARY);
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, MasterBootComboBox.get(), '')
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, HtsmComboBox.get(), '')
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, HtsmValidComboBox.get(), '')
          if "elf" not in AppComboBox.get():
            loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, AppComboBox.get(), '')
          else:
            loader.addToDownloadList(elfdownloadConfig, ic.CLoaderController.DLIST_PRIMARY, AppComboBox.get(), '')
            loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, AppComboBox.get().replace("elf", "s3"), '')
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, AppValidComboBox.get(), '')
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, DatasetComboBox.get(), '')
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, DatasetValidComboBox.get(), '')
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, OtpMasterComboBox.get(), '')
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, CalibComboBox.get(), '')
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, UcbComboBox.get(), '')
          loader.download();
        pass
    except Exception as e:
        raise e

yposition = 40 + yposition
MasterWriteButton = Button(root, height=2, width=15, text='Master Write', command=Callback_MasterWrite)
MasterWriteButton.place(x=600, y=yposition)

def Callback_SlaveWrite():
    try:
        connectionMgr = ic.ConnectionMgr()
        connectionMgr.connectMRU('')  

        #data = ic.CDataController(connectionMgr)
        #data.eraseFlash()

        s3downloadConfig = ic.CDownloadConfiguration()
        if(s3downloadConfig != None):
          s3downloadConfig.setCodeOffset(0);
          s3downloadConfig.setSymbolsOffset(0);
          s3downloadConfig.setDownloadFileFormat(ic.CDownloadConfiguration.ftMotorolaS);
          s3downloadConfig.setUsedInFullDownload(True);

        elfdownloadConfig = ic.CDownloadConfiguration()
        if(elfdownloadConfig != None):
          elfdownloadConfig.setCodeOffset(0);
          elfdownloadConfig.setSymbolsOffset(0);
          elfdownloadConfig.setDownloadFileFormat(ic.CDownloadConfiguration.ftELF);
          elfdownloadConfig.setUsedInFullDownload(True);

        loader = ic.CLoaderController(connectionMgr)
        if(loader != None):
          loader.clearDownloadList(ic.CLoaderController.DLIST_PRIMARY);
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, SlaveBootComboBox.get(), '')
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, HtsmComboBox.get(), '')
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, HtsmValidComboBox.get(), '')
          if "elf" not in AppComboBox.get():
            loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, AppComboBox.get(), '')
          else:
            loader.addToDownloadList(elfdownloadConfig, ic.CLoaderController.DLIST_PRIMARY, AppComboBox.get(), '')
            loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, AppComboBox.get().replace("elf", "s3"), '')
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, AppValidComboBox.get(), '')
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, AppValidComboBox.get(), '')
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, DatasetComboBox.get(), '')
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, DatasetValidComboBox.get(), '')
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, OtpSlaveComboBox.get(), '')
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, CalibComboBox.get(), '')
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, UcbComboBox.get(), '')
          loader.download();
        pass
    except Exception as e:
        raise e

SlaveWriteButton = Button(root, height=2, width=15, text='Slave Write', command=Callback_SlaveWrite)
SlaveWriteButton.place(x=720, y=yposition)

def Callback_MasterFullFlashWrite():
    try:
        connectionMgr = ic.ConnectionMgr()
        connectionMgr.connectMRU('')  

        #data = ic.CDataController(connectionMgr)
        #data.eraseFlash()

        s3downloadConfig = ic.CDownloadConfiguration()
        if(s3downloadConfig != None):
          s3downloadConfig.setCodeOffset(0);
          s3downloadConfig.setSymbolsOffset(0);
          s3downloadConfig.setDownloadFileFormat(ic.CDownloadConfiguration.ftMotorolaS);
          s3downloadConfig.setUsedInFullDownload(True);

        elfdownloadConfig = ic.CDownloadConfiguration()
        if(elfdownloadConfig != None):
          elfdownloadConfig.setCodeOffset(0);
          elfdownloadConfig.setSymbolsOffset(0);
          elfdownloadConfig.setDownloadFileFormat(ic.CDownloadConfiguration.ftELF);
          elfdownloadConfig.setUsedInFullDownload(True);

        loader = ic.CLoaderController(connectionMgr)
        if(loader != None):
          loader.clearDownloadList(ic.CLoaderController.DLIST_PRIMARY);
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, MasterFullFlashComboBox.get(), '')
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, HtsmComboBox.get(), '')
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, HtsmValidComboBox.get(), '')
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, OtpMasterComboBox.get(), '')
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, CalibComboBox.get(), '')
          loader.download();
        pass
    except Exception as e:
        raise e

SlaveWriteButton = Button(root, height=2, width=20, text='Master FullFlash Write', command=Callback_MasterFullFlashWrite)
SlaveWriteButton.place(x=850, y=yposition)

def Callback_SlaveFullFlashWrite():
    try:
        connectionMgr = ic.ConnectionMgr()
        connectionMgr.connectMRU('')  

        #data = ic.CDataController(connectionMgr)
        #data.eraseFlash()

        s3downloadConfig = ic.CDownloadConfiguration()
        if(s3downloadConfig != None):
          s3downloadConfig.setCodeOffset(0);
          s3downloadConfig.setSymbolsOffset(0);
          s3downloadConfig.setDownloadFileFormat(ic.CDownloadConfiguration.ftMotorolaS);
          s3downloadConfig.setUsedInFullDownload(True);

        loader = ic.CLoaderController(connectionMgr)
        if(loader != None):
          loader.clearDownloadList(ic.CLoaderController.DLIST_PRIMARY);
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, SlaveFullFlashComboBox.get(), '')
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, HtsmComboBox.get(), '')
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, HtsmValidComboBox.get(), '')
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, OtpSlaveComboBox.get(), '')
          loader.addToDownloadList(s3downloadConfig, ic.CLoaderController.DLIST_PRIMARY, CalibComboBox.get(), '')
          loader.download();
        pass
    except Exception as e:
        raise e

SlaveWriteButton = Button(root, height=2, width=20, text='Master FullFlash Write', command=Callback_SlaveFullFlashWrite)
SlaveWriteButton.place(x=1005, y=yposition)

#====================================================================================================================

root.mainloop()  
