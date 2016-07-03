'''
Group: Eva Gerlitz, Anna-Lena Popkes, Pascal Wenker, Kanil Patel, Nico Lutz

Exercise: 1.3: Implement Connect Four
'''

import kivy
kivy.require('1.8.0')
from kivy.app import App
from Connect import *


__version__ = '1.0'


class ConnectApp(App):

	def build(self):
		
		return ConnectFourGrid(cols=7,rows=6)

if __name__ == '__main__':
	ConnectApp().run()