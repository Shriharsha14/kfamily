import wx
import mounika
import choti
import puppy
import revanth

# Dictionary to map names to modules
details_mapping = {
    "Mounika": mounika,
    "Choti": choti,
    "Puppy": puppy,
    "Revanth": revanth
}

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Details Viewer')
        panel = wx.Panel(self)

        # ComboBox for selecting the file
        self.combo = wx.ComboBox(panel, choices=list(details_mapping.keys()), style=wx.CB_READONLY)
        self.combo.SetSelection(0)  # Set default selection to the first item

        # Button to display details
        self.button = wx.Button(panel, label='Show Details')
        self.button.Bind(wx.EVT_BUTTON, self.on_show_details)

        # Text box to display details
        self.details_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY, size=(400, 200))

        # Layout using sizers
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.combo, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(self.button, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(self.details_text, 1, wx.ALL | wx.EXPAND, 5)

        panel.SetSizer(sizer)
        self.Show()

    def on_show_details(self, event):
        # Get the selected name
        selected_name = self.combo.GetValue()
        details = details_mapping[selected_name]
        
        # Format the details to display
        output = (f"Age: {details.age}\n"
                  f"School: {details.school}\n"
                  f"College: {details.college}\n"
                  f"Graduation: {details.graduation}\n")
        
        # Update the text box with details
        self.details_text.SetValue(output)

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
