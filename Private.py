
class MStruct():
    def __init__(self):
        __sVar = 13
        

class MStruct2():
    def __init__(self):
        _sVar = 13
        pass
    @property
    def sVar(self):
        return self._sVar*2
    @sVar.setter
    def sVar(self, v):
        print(f'set _sVar: {v}')
        self._sVar = v
if __name__ == "__main__":
 s = MStruct()
 try :
  print(s.__sVar)
 except AttributeError:
    print("__sVar not found")

 try:
     print(f"_sVar: {MStruct2()._sVar}")
 except AttributeError as err:
      print( str ( err ) )
 s = MStruct2()
 s.sVar = 12
 print(s.sVar)
