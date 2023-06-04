import json
import os
import time
from datetime import datetime

class Jadwal:
    
    def __init__(self, nama: str, desc: str, jam:int, hari:int, tanggal:str):
        self.nama = nama
        self.desc = desc
        self.jam = jam
        self.hari = hari
        self.tanggal = tanggal

def getListJadwal() -> list:
    _directory = os.getcwd()+r"\app\file_jadwal\listjadwal.txt"

    _listjadwal_file = open(_directory,"r")
    
    return _listjadwal_file.read().splitlines() # Return List

def getJadwal(filename:str) -> Jadwal:
    _directory = os.getcwd()+r"\app\file_jadwal"
    _filename = f"\{filename}"
    _directory = _directory + _filename
    
    _jadwalInfo_file = open(_directory,"r")
    _jadwalInfo = json.loads(_jadwalInfo_file.read())
    
    _jadwal = Jadwal(_jadwalInfo['jadwalNama'], _jadwalInfo['jadwalDesc'],_jadwalInfo['jadwalJam'],_jadwalInfo['jadwalHari'],_jadwalInfo['jadwalTanggal'])
    
    return _jadwal # Return Jadwal.class

def getCurrentWeekday() -> int:
    _weekday = time.strftime("%w")
    _weekday = int(_weekday)
    return _weekday

def getCurrentHour() -> int:
    _hour = time.strftime('%H')
    _hour = int(_hour)
    return _hour

def getStrDay(day: int) -> str:
    _daydict = {
    "1":"senin",
    "2":"selasa",
    "3":"rabu",
    "4":"kamis",
    "5":"jumat",
    "6":"sabtu",
    "0":"minggu"
    }
    return _daydict[f'{str(day)}']

def getWeekdayByDate(date: str) -> int:
    _date = date
    _date = datetime.strptime(_date, '%Y-%m-%d')
    
    return int(_date.strftime('%w'))

def sortJadwal(unsorted_jadwal: list) -> list:
    return sorted(unsorted_jadwal, key=lambda jadwal: jadwal.jam)
