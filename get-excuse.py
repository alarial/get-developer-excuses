__author__ = 'panda'
import urllib2
import sgmllib


class MyParser(sgmllib.SGMLParser):
    """Simple parser class"""

    def parse(self, s):
        """Parse the string 's'."""

        self.feed(s)
        self.close()

    def __init__(self, verbose=0):
        """Initialize object and pass 'verbose' to superclass"""

        sgmllib.SGMLParser.__init__(self, verbose)
        self.hyperlinks = []
        self.descriptions = []
        self.inside_a_element = 0

    def start_a(self, attributes):
        """Process hyperlink and its attributes"""

        for name, value in attributes:
            if name == "href":
                self.hyperlinks.append(value)
                self.inside_a_element = 1
    def end_a(self):
        """Capture the end of hyperlink tag"""

        self.inside_a_element = 0

    def get_hyperlinks(self):
        """Return list of hyperlinks"""

        return self.hyperlinks

    def get_descriptions(self):
        """Return list of descriptions"""

        return self.descriptions

    def handle_data(self, data):
        """Handle text data"""

        if self.inside_a_element:
            self.descriptions.append(data)

url = 'http://www.programmerexcuses.com/'
response = urllib2.urlopen(url)
html = response.read()
response.close()

myparser = MyParser()
myparser.parse(html)

# See what we get
#print myparser.get_hyperlinks()
print myparser.get_descriptions()
