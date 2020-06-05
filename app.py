from . import html5


class HelloWorld(html5.Div):
	def __init__(self):
		super(HelloWorld, self).__init__()
		self.fromHTML("""
			<h1>Hello World</h1>
			<ul class="is-list" [name]="myList">
					<li>One</li>
					<li>Two</li>
					<li>Three</li>
			</ul>
		""")
		self.sinkEvent("onClick")

	def onClick(self, e):
		for li in self.myList.children():
			if html5.utils.doesEventHitWidgetOrChildren(e, li):
				html5.ext.Alert(li.element.innerHTML)
