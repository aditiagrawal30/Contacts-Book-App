import addModRecord
import commonDlgs
import logic
import wx
from ObjectListView import ObjectListView, ColumnDefn

########################################################################
class ContactPanel(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        try:
            self.personResults = logic.getAllRecords()
        except:
            self.personResults = []

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        searchSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD) 
        
        # create the search related widgets
        cat = ["First name", "E-Mail", "Contact Number"]
        searchByLbl = wx.StaticText(self, label="Search By:")
        searchByLbl.SetFont(font)
        searchSizer.Add(searchByLbl, 0, wx.ALL, 5)
        
        self.categories = wx.ComboBox(self, value="First Name", choices=cat)
        searchSizer.Add(self.categories, 0, wx.ALL, 5)
        
        self.search = wx.SearchCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.search.Bind(wx.EVT_TEXT_ENTER, self.onSearch)
        searchSizer.Add(self.search, 0, wx.ALL, 5)
        
        self.personResultsOlv = ObjectListView(self, style=wx.LC_REPORT
                                                        |wx.SUNKEN_BORDER)
        self.personResultsOlv.SetEmptyListMsg("No Details Found")
        self.setBooks()
        
        # create the button row
        addRecordBtn = wx.Button(self, label="Add")
        addRecordBtn.Bind(wx.EVT_BUTTON, self.onAddRecord)
        btnSizer.Add(addRecordBtn, 0, wx.ALL, 5)
        
        editRecordBtn = wx.Button(self, label="Edit")
        editRecordBtn.Bind(wx.EVT_BUTTON, self.onEditRecord)
        btnSizer.Add(editRecordBtn, 0, wx.ALL, 5)
        
        deleteRecordBtn = wx.Button(self, label="Delete")
        deleteRecordBtn.Bind(wx.EVT_BUTTON, self.onDelete)
        btnSizer.Add(deleteRecordBtn, 0, wx.ALL, 5)
        
        showAllBtn = wx.Button(self, label="Show All")
        showAllBtn.Bind(wx.EVT_BUTTON, self.onShowAllRecord)
        btnSizer.Add(showAllBtn, 0, wx.ALL, 5)
        
        mainSizer.Add(searchSizer)
        mainSizer.Add(self.personResultsOlv, 1, wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(btnSizer, 0, wx.CENTER)
        self.SetSizer(mainSizer)
        
    #----------------------------------------------------------------------
    def onAddRecord(self, event):
        """
        Add a record to the database
        """
        dlg = addModRecord.AddModRecDialog()
        dlg.ShowModal()
        dlg.Destroy()
        self.showAllRecords()
        
    #----------------------------------------------------------------------
    def onEditRecord(self, event):
        """
        Edit a record
        """
        selectedRow = self.personResultsOlv.GetSelectedObject()
        if selectedRow == None:
            commonDlgs.showMessageDlg("No row selected!", "Error")
            return
        dlg = addModRecord.AddModRecDialog(selectedRow, title="Modify",
                                           addRecord=False)
        dlg.ShowModal()
        dlg.Destroy()
        self.showAllRecords()
        
    #----------------------------------------------------------------------
    def onDelete(self, event):
        """
        Delete a record
        """
        selectedRow = self.personResultsOlv.GetSelectedObject()
        if selectedRow == None:
            commonDlgs.showMessageDlg("No row selected!", "Error")
            return
        logic.deleteRecord(selectedRow.mail)
        self.showAllRecords()
        
    #----------------------------------------------------------------------
    def onSearch(self, event):
        """
        Searches database based on the user's filter choice and keyword
        """
        filterChoice = self.categories.GetValue()
        keyword = self.search.GetValue()
        print ("%s %s" % (filterChoice, keyword))
        self.personResults = logic.searchRecords(filterChoice, keyword)
        self.setBooks()
        
    #----------------------------------------------------------------------
    def onShowAllRecord(self, event):
        """
        Updates the record list to show all of them
        """
        self.showAllRecords()
        
    #----------------------------------------------------------------------
    def setBooks(self):
        self.personResultsOlv.SetColumns([
            ColumnDefn("First Name", "left", 150, "first_name"),
            ColumnDefn("Last Name", "left", 150, "last_name"),
            ColumnDefn("E-Mail", "right", 200, "mail"),
            ColumnDefn("Contact Number", "left", 150, "contact_number")
        ])
        self.personResultsOlv.SetObjects(self.personResults)
        self.SetBackgroundColour('sky blue')
        


    #----------------------------------------------------------------------
    def showAllRecords(self):
        """
        Show all records in the object list view control
        """
        self.personResults = logic.getAllRecords()
        self.setBooks()
        
########################################################################
class ContactFrame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Contact Book",
                          size=(600, 500))
        self.colors()
        panel = ContactPanel(self)
        self.Show()
        
    def colors(self):
        self.SetBackgroundColour('sky blue')
        
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    frame = ContactFrame()
    app.MainLoop()
