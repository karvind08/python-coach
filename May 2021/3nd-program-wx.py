from wx import *
class MyFrame(Frame):
	def __init__(self,parent,title):
		super(MyFrame,self).__init__(parent,title=title,size=(600,400))


class MyApp(App):
	def OnInit(self):
		self.frame = MyFrame(parent=None,title='first window')
		self.frame.Show()
		return True

app = MyApp()
app.MainLoop()