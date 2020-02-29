class informationManger:
    def __init__(self):
        # Info Variables ↓
        self.developerName: str
        self.developerEmail: str
        self.logoCreditName: str
        self.logoCreditEmail: str
        self.icons8Credit: str
        self.applicationVersion: str
        self.sourceCodeLink: str

        # Tooltip Variables ↓
        self.developerNameTooltip: str
        self.developerEmailTooltip: str
        self.logoCreditNameTooltip: str
        self.logoCreditEmailTooltip: str
        self.icons8CreditTooltip: str
        self.applicationVersionTooltip: str
        self.sourceCodeLinkTooltip: str

        # Version ↓
        self.version: str = '3.0'

        # Setting up variables ↓
        self.__info()
        self.__toolTip()

    def __info(self):
        self.developerName = """<html><head/><body><p><span style=" font-size:10pt; 
        font-weight:600;">Developer:</span><a href="https://github.com/Rizwan-Hasan/"><span style="text-decoration: 
        none; font-size:10pt; color:#0000ff;"> Rizwan Hasan</span></a></p></body></html> """

        self.developerEmail = """<html><head/><body><p><span style=" font-size:10pt; font-weight:600;">Email: 
                </span><a href="mailto:rizwan.hasan486@gmail.com"><span style="text-decoration: none; font-size:10pt; 
                color:#0000ff;">rizwan.hasan486@gmail.com</span></a></p></body></html>"""

        self.logoCreditName = """<html><head/><body><p><span style=" font-size:10pt; font-weight:600;">Logo 
                credit: </span><a href="https://github.com/skinan"><span style="text-decoration: none; font-size:10pt; 
                color:#0000ff;">Sakib Khan Inan</span></a></p></body></html>"""

        self.logoCreditEmail = """<html><head/><body><p><span style=" font-size:10pt; font-weight:600;">Email: 
                </span><a href="mailto:sakib.khaninan@hotmail.com"><span style="text-decoration: none; font-size:10pt; 
                color:#0000ff;">sakib.khaninan@hotmail.com</span></a></p></body></html>"""

        self.icons8Credit = """<html><head/><body><p><span style=" font-size:10pt; font-weight:600;">Icons 
                credit: </span><a href="https://icons8.com"><span style="text-decoration: none; font-size:10pt; 
                color:#0000ff;">Icons8</span></a></p></body></html>"""

        self.applicationVersion = """<html><head/><body><p align="center"><span style=" font-size:22pt; 
        font-weight:600;">{0}</span></p></body></html>""".format(self.version)

        self.sourceCodeLink = """<html><head/><body><p align="center"><a 
        href="https://github.com/Rizwan-Hasan/Free-Hash-Checker"><img 
        src=":/github/github.png"/></a></p></body></html>"""

    def __toolTip(self):
        self.developerNameTooltip = 'https://github.com/Rizwan-Hasan'
        self.developerEmailTooltip = 'rizwan.hasan486@gmail.com'
        self.logoCreditNameTooltip = 'https://github.com/skinan'
        self.logoCreditEmailTooltip = 'sakib.khaninan@hotmail.com'
        self.icons8CreditTooltip = 'https://icons8.com'
        self.applicationVersionTooltip = self.version
        self.sourceCodeLinkTooltip = 'https://github.com/Rizwan-Hasan/Free-Hash-Checker'
