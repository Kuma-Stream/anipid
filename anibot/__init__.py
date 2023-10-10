import os
from pyrogram import Client
from aiohttp import ClientSession

TRIGGERS = os.environ.get("TRIGGERS", "/ !").split()
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
BOT_NAME = os.environ.get("BOT_NAME")
DB_URL = os.environ.get("DATABASE_URL")
ANILIST_CLIENT = os.environ.get("ANILIST_CLIENT")
ANILIST_SECRET = os.environ.get("ANILIST_SECRET")
ANILIST_REDIRECT_URL = os.environ.get("ANILIST_REDIRECT_URL", "https://anilist.co/api/v2/oauth/pin")
API_ID = int(os.environ.get("API_ID"))
LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID"))
OWNER = list(filter(lambda x: x, map(int, os.environ.get("OWNER_ID", "1474271232").split())))  ## sudos can be included

DOWN_PATH = "anibot/downloads/"
HELP_DICT = dict()

session = ClientSession()
plugins = dict(root="anibot/plugins")
anibot = Client("anibot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=plugins)

has_user: bool = False
if os.environ.get('USER_SESSION'):
    has_user: bool = True
    user = Client(os.environ.get('USER_SESSION'), api_id=API_ID, api_hash=API_HASH)

HELP_DICT['Group'] = '''
Group based commands:

/settings - Beralih hal-hal seperti apakah akan mengizinkan 18+ hal dalam grup atau apakah akan memberi tahu tentang anime yang ditayangkan, dll dan mengubah UI

/disable - Nonaktifkan penggunaan cmd dalam grup (Nonaktifkan beberapa cmd dengan menambahkan spasi di antara mereka)
`/disable anime anilist me user`

/enable - Aktifkan penggunaan cmd dalam grup (Aktifkan beberapa cmd dengan menambahkan spasi di antara mereka).
`/enable anime anilist me user`

/disabled - List out disabled cmds
'''

HELP_DICT["Additional"] = """Gunakan /reverse untuk mencari anime melalui tracemoepy API, yang dimana bot ini akan memberikan judul/info terkait anime tersebut.

Catatan: Ini berfungsi paling baik pada gambar anime yang tidak dipotong,
ketika digunakan pada media yang kepotong, Anda mungkin mendapatkan hasil tetapi mungkin tidak akurat.

Gunakan perintah /schedule untuk mendapatkan anime terjadwal berdasarkan hari kerja

Gunakan perintah /watch untuk mendapatkan urutan tontonan anime yang dicari

Gunakan /fillers cmd untuk mendapatkan daftar pengisi untuk anime

Gunakan /wallpaper untuk mendapatkan file/gambar wallpaper anime secara random (API)

Gunakan /waifu untuk mendapatkan gambar waifu (neko) secara random (API)

<b>Mendownload VIDEO/AUDIO dari Youtube.</b>

Silahkan aktifkan bot @vid nya terlebih dahulu, lalu kembali kebot ini.

Setelah itu, kalian ketik @vid "judul/nama"  yang ingin

kalian download/streaming. 

lalu, klik video tersebut, nanti otomatis bot ini akan memprosesnya.

<b> Stream/Download via browser </b>

Saya sarankan gunakan bot ini @Kurupidbot

fungsinya itu, untuk menconvert, file dokumen/video dari telegram,
ke link yang bisa kalian download mengunakan browser maupun sejenisnya.
tidak hanya itu, selain mendownload, kalian bisa streaming via link.

....
"""

HELP_DICT["Anilist"] = """
Ini merupakan menu bantuan anilist, terkait penggunaan bot ini,

Di bawah ini adalah daftar cmd anilist dasar untuk mendownload/ mengambil info anime, karakter, manga, dll.

/anime - Gunakan cmd ini untuk mendapatkan info & mendownload anime tertentu menggunakan kata kunci (nama anime) atau ID Anilist
(Dapat mencari info tentang sekuel dan prekuel)

/anilist - Gunakan perintah ini untuk memilih di antara beberapa anime dengan nama serupa yang terkait dengan kueri yang dicari
(Tidak termasuk tombol untuk prekuel dan sekuel)

/character - Gunakan perintah ini untuk mendapatkan info tentang karakter

/manga - Gunakan perintah ini untuk mendapatkan info tentang manga

/airing - Gunakan perintah ini untuk mendapatkan info status penayangan anime

/top - Gunakan cmd ini untuk mencari anime teratas dari genre/tag atau dari semua anime
(Untuk mendapatkan daftar tag atau genre yang tersedia, kirim /gettags atau /getgenres
'/gettags nsfw' untuk tag nsfw)

/user - Gunakan perintah ini untuk mendapatkan info tentang pengguna anilist

/browse - Gunakan perintah ini untuk mendapatkan pembaruan tentang anime terbaru/top/upcoming.
"""

HELP_DICT["Oauth"] = """
Ini merupakan menu bantuan tambahan serta fitur canggih, terkait penggunaan bot ini,

Gunakan /auth atau !auth untuk login/daftar akun Anilist Anda dengan bot.

Otorisasi diri Anda membuka fitur-fitur canggih bot seperti:

- menambahkan anime/karakter/manga ke favorit
- melihat data anilist Anda yang terkait dengan anime/manga dalam pencarian Anda yang mencakup skor, status, dan favorit
- buka /flex, /me, /activity and /favourites 
- menambahkan/memperbarui entri anilis seperti selesai atau berencana untuk menonton/membaca
- menghapus entri anilis

Gunakan /flex or !flex cmd untuk mendapatkan statistik anilist Anda

Gunakan /logout or !logout cmd untuk memutuskan akun Anilist Anda

Gunakan /me atau !me cmd untuk mendapatkan aktivitas terbaru anilist Anda
bisa juga /activity or !activity

Gunakan /favourites cmd untuk mendapatkan favorit anilis Anda.

Mengganti foto/sampul anda 

Silahkan kunjungi https://anilist.co/settings, lalu pilih foto dan terapkan.

Bagaimana masalah terhadap, riwayat, atau list
yang belum muncul ? 

Normalnya kalian harus menunggu 1 hari saat kalian list,
agar tampil di menu /flex, /me dan lainnya.

Solusinya yang ingin menambahkan dengan manual/cepat, silahkan klik ini : https://anilist.co/settings/lists 

Cari text "Stats", klik tombol Update stats.
"""
