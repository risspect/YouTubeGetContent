import json, os
from urllib import request

# PEWARNAAN
#============================================================

merah = '\033[91;1m'
kuning = '\033[93;1m'
hijau = '\033[92;1m'
biru = '\033[94;1m'
putih = '\033[97;1m'

# KEGABUTAN SAYA
#============================================================

os.system("clear")
logo = """
%s __  ________%s______%s______
%s \ \/ /_  __/%s ____/%s ____/
%s  \  / / / %s/ / __%s/ /
%s  / / / / %s/ /_/ /%s /___
%s /_/ /_/  %s\____/%s\____/

%sCreator : %sRisna Fadillah
%sVersion : %s1.0 BETA
%sWebsite : %shttps://risnfd.asia
%sEmail   : %semail@risnfd.asia /
          risnafadillah08@gmail.com

%sSend feedback to my email.
%s-------------------------->
""" % (merah, kuning, hijau, merah, kuning, hijau, merah, kuning, hijau, merah, kuning, hijau, merah, kuning, hijau, kuning, hijau, kuning, hijau, kuning, hijau, kuning, hijau, hijau, kuning)

# PROSES SCRAPING JSON DARI WEB API
#============================================================

print(logo)
link = input("%sLink or ID Video: %s" % (biru,putih))
vidID = link.replace("https://youtu.be/","")
apiKey = 'AIzaSyB9vMirJtOk1-Jd6hUyDeGrCXYN_SbCfI8'

url = "https://www.googleapis.com/youtube/v3/videos?part=snippet&id=" + vidID + "&fields=items(id%2Csnippet)&key=" + apiKey
response = request.urlopen(url)
data = json.loads(response.read())

ul = "https://www.googleapis.com/youtube/v3/videos?part=contentDetails&id=" + vidID + "&fields=items&key=" + apiKey
rs = request.urlopen(ul)
dt = json.loads(rs.read())

ur = "https://www.googleapis.com/youtube/v3/videos?part=statistics&id=" + vidID + "&fields=items&key=" + apiKey
rp = request.urlopen(ur)
dat = json.loads(rp.read())
# PROSES MENAMPILKAN DATA DARI .JSON
#============================================================

os.system("clear")
print(logo)
for r in data['items']:
            print(f"💡" + hijau + "Channel Name   : " + putih + r['snippet']['channelTitle'])
            print(f"💡" + hijau + "Video Title    : " + putih + r['snippet']['title'])
for s in dt['items']:
            print(f"💡" + hijau + "Video Duration : " + putih + s['contentDetails']['duration'].replace("PT","").replace("H","h ").replace("M","m ").replace("S","s"))
for t in dat['items']:
            print(f"💡" + hijau + "Video Views    : " + putih + t['statistics']['viewCount'])
            print(f"💡" + hijau + "Video Likes    : " + putih + t['statistics']['likeCount'])
            print(f"💡" + hijau + "Video Comments : " + putih + t['statistics']['commentCount'])
for u in data['items']:
            print(f"💡" + hijau + "Published at   : " + putih + u['snippet']['publishedAt'].replace("T", " ").replace("Z", " "))
            print(f"\n" + hijau + "========== 💡Tags ==========\n" + putih + str(u['snippet']['tags']).replace("['","  - ").replace("', '","\n  - ").replace("']",""))
            print(f"\n" + hijau + "========== 💡Description ==========\n" + putih + u['snippet']['description'])

#============================================================
"""THIS SCRIPT IS FREE TO USE, YOU CAN EDIT THIS FILE BUT
            YOU MUST PLACE MY NAME AS CREATOR."""
#============================================================
