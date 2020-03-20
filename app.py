from . import html5


class HelloWorld(html5.Div):
	def __init__(self):
		super().__init__("""
			<h1 [name]="title">Hello </h1>
		""")

		self.title.appendChild("World")
