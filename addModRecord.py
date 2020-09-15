# addModRecord.py

import commonDlgs
import logic
import wx

########################################################################
class AddModRecDialog(wx.Dialog):
    """
    Add / Modify Record dialog
    """

    #----------------------------------------------------------------------
    def __init__(self, row=None, title="Add", addRecord=True):
        """Constructor"""
        wx.Dialog.__init__(self, None, title="%s Contact" % title)
        self.addRecord = addRecord
        self.selectedRow = row
        if row:
           # bTitle = self.selectedRow.title
            fName = self.selectedRow.first_name
            lName = self.selectedRow.last_name
            mail = self.selectedRow.mail
            contact_number = self.selectedRow.contact_number
        else:
            fName = lName = mail = contact_number = ""
        size = (80, -1)
        font = wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD) 
       
        
        # create the sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
       # authorSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
                
        # create some widgets
        lbl = wx.StaticText(self, label="New Contact")
        lbl.SetFont(font)
        mainSizer.Add(lbl, 0, wx.CENTER)
        
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD) 
        first_nameLbl = wx.StaticText(self, label="First Name:", size=size)
        first_nameLbl.SetFont(font)
        self.first_nameTxt = wx.TextCtrl(self, value=fName)
        mainSizer.Add(self.rowBuilder([first_nameLbl, self.first_nameTxt]), 
                      0, wx.EXPAND)
       
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD) 
        last_nameLbl = wx.StaticText(self, label="Last Name:", size=size)
        last_nameLbl.SetFont(font)
        self.last_nameTxt = wx.TextCtrl(self, value=lName)
        mainSizer.Add(self.rowBuilder([last_nameLbl, self.last_nameTxt]), 
                      0, wx.EXPAND)
        
        mailLbl = wx.StaticText(self, label="E-mail:", size=size)
        mailLbl.SetFont(font)
        self.mailTxt = wx.TextCtrl(self, value=mail)
        mainSizer.Add(self.rowBuilder([mailLbl, self.mailTxt]),
                      0, wx.EXPAND)
        

        contact_numberLbl = wx.StaticText(self, label="Contact Number:", size=size)
        contact_numberLbl.SetFont(font)
        self.contact_numberTxt = wx.TextCtrl(self, value=contact_number)
        mainSizer.Add(self.rowBuilder([contact_numberLbl, self.contact_numberTxt]),
                      0, wx.EXPAND)
        
      
        okBtn = wx.Button(self, label="OK")
        okBtn.Bind(wx.EVT_BUTTON, self.onRecord)
        btnSizer.Add(okBtn, 0, wx.ALL, 5)
        cancelBtn = wx.Button(self, label="Close")
        cancelBtn.Bind(wx.EVT_BUTTON, self.onClose)
        btnSizer.Add(cancelBtn, 0, wx.ALL, 5)
        
        mainSizer.Add(btnSizer, 0, wx.CENTER)
        self.SetSizer(mainSizer)
        mainSizer.Fit(self)
        
    #----------------------------------------------------------------------
    def getData(self):
      
        personDict = {}
                        
        fName = self.first_nameTxt.GetValue()
        lName = self.last_nameTxt.GetValue()
        mail = self.mailTxt.GetValue()
        contact_number = self.contact_numberTxt.GetValue()
        
        if fName == "" or mail == "" or contact_number == "":
            commonDlgs.showMessageDlg("First Name or E-mail or Contact Number are Required!",
                                      "Error")
            return
       
        personDict["first_name"] = fName
        personDict["last_name"] = lName
        personDict["mail"] = mail
        personDict["contact_number"] = contact_number
        
        return personDict
            
    #----------------------------------------------------------------------
    def onAdd(self):
        """
        Add the record to the database
        """
        personDict = self.getData()
        data = ({"person":personDict})
        logic.addRecord(data)
        
        # show dialog upon completion
        commonDlgs.showMessageDlg("Contact Added",
                                  "Success!", wx.ICON_INFORMATION)
        
        # clear dialog so we can add another book
        for child in self.GetChildren():
            if isinstance(child, wx.TextCtrl):
                child.SetValue("")
        
    #----------------------------------------------------------------------
    def onClose(self, event):
        """
        Cancel the dialog
        """
        self.Destroy()
        
    #----------------------------------------------------------------------
    def onEdit(self):
        """"""
        personDict = self.getData()
        logic.editRecord(self.selectedRow.mail, personDict)
        commonDlgs.showMessageDlg("Contact Edited Successfully!", "Success",
                                  wx.ICON_INFORMATION)
        self.Destroy()
        
    #----------------------------------------------------------------------
    def onRecord(self, event):
        """"""
        if self.addRecord:
            self.onAdd()
        else:
            self.onEdit()
        
    #----------------------------------------------------------------------
    def rowBuilder(self, widgets):
        """"""
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        lbl, txt = widgets
        sizer.Add(lbl, 0, wx.ALL, 5)
        sizer.Add(txt, 1, wx.EXPAND|wx.ALL, 5)
        return sizer
            
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    dlg = AddRecDialog()
    dlg.ShowModal()
    app.MainLoop()
