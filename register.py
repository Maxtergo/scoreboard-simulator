# register.py - the file define the table for register status
# Class Register holds status od 11 registers

REG_STATUS_HEADER = \
"\
\n                              REGISTER STATUS\
\n---------------------------------------------------------------------------------------------------------------------------\
\n              F0        F2        F4        F6        F8        F10        F12        F14        F16        F18        F20\
\n---------------------------------------------------------------------------------------------------------------------------"


class ReGister:
  def __init__(self):
    self.f0=self.f2=self.f4=self.f6=self.f8=self.f10=None;

  def write_back(self,regname,func_unit):
    if(regname=="F0"):
      self.f0=func_unit;
    if(regname=="F2"):
      self.f2=func_unit;
    if(regname=="F4"):
      self.f4=func_unit;
    if(regname=="F6"):
      self.f6=func_unit;
    if(regname=="F8"):
      self.f8=func_unit;
    if(regname=="F10"):
      self.f10=func_unit;
    if(regname=="F12"):
      self.f2=func_unit;
    if(regname=="F14"):
      self.f4=func_unit;
    if(regname=="F16"):
      self.f6=func_unit;
    if(regname=="F18"):
      self.f8=func_unit;
    if(regname=="F20"):
      self.f10=func_unit;

  def __str__(self):
    return "FU    %10s%10s%10s%10s%10s%10s"%(self.f0,self.f2,self.f4,self.f6,self.f8,self.f10)

