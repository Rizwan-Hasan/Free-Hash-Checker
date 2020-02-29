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

        # Setting information ↓
        self.__info()

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
        font-weight:600;">0.0</span></p></body></html>"""

        self.sourceCodeLink = """<html><head/><body><p align="center"><a 
        href="https://github.com/Rizwan-Hasan/Free-Hash-Checker"><img 
        src=":/github/github.png"/></a></p></body></html>"""
