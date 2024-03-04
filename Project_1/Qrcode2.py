
import pyqrcode

url = "https://github.com/Karan-dvlpr07"
X_Dvlpr = pyqrcode.create(url)
X_Dvlpr.svg("Git.Svg",scale=10)