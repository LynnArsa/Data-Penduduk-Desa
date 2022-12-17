import os, time, pandas, csv

data = [{'NIK': 20, '   Nama': 'Lintang', '   Jenis Kelamin': 'Perempuan', '   Umur': 20,'   Alamat': 'Jember','   No HP': '081'},
         {'NIK': 21, '   Nama': 'Dika', '   Jenis Kelamin': 'Laki-laki', '   Umur': 21, '   Alamat': 'Jember','   No HP': '082'},
         {'NIK': 22, '   Nama': 'Nabil', '   Jenis Kelamin': 'Laki-laki', '   Umur': 17, '   Alamat': 'Situbondo','   No HP': '083'},
         {'NIK': 23, '   Nama': 'Wahyu', '   Jenis Kelamin': 'Laki-laki', '   Umur': 23, '   Alamat': 'Banyuwangi','   No HP': '084'},
         {'NIK': 24, '   Nama': 'Rainey', '   Jenis Kelamin': 'Perempuan', '   Umur': 21, '   Alamat': 'Surabaya','   No HP': '085'},
         {'NIK': 25, '   Nama': 'Foxy', '   Jenis Kelamin': 'Perempuan', '   Umur': 22, '   Alamat': 'Surabaya','   No HP': '086'},
         {'NIK': 26, '   Nama': 'Marvel', '   Jenis Kelamin': 'Laki-laki', '   Umur': 15, '   Alamat': 'Situbondo','   No HP': '087'},
         {'NIK': 27, '   Nama': 'Naufal', '   Jenis Kelamin': 'Laki-laki', '   Umur': 19, '   Alamat': 'Sidoarjo','   No HP': '088'},
         {'NIK': 28, '   Nama': 'Ava', '   Jenis Kelamin': 'Laki-laki', '   Umur': 18, '   Alamat': 'Semarang','   No HP': '089'},
         {'NIK': 29, '   Nama': 'Ragnora', '   Jenis Kelamin': 'Perempuan', '   Umur': 19, '   Alamat': 'Jember','   No HP': '080'},
         ]

def clean():
    os.system('cls')

def lihatData():
    clean()
    print('-'*62)
    print('\t\t\t  DATA PENDUDUK')
    print('-'*62)
    print(' ')
    print('1. Cari Data')
    print('2. Tampilkan Data')
    # print('3. Kembali')
    print(' ')
    user = input('Pilih Nomor: ')
    print(' ')
    print('-'*62)
    time.sleep(1)
    dataSearch() if user=='1' else (dataView() if user=='2' else user())

def dataSearch():
    clean()
    print('-'*62)
    print('\t\t\t  CARI DATA')
    print('-'*62)
    print(' ')
    print('Cari data berdasarkan: ')
    print('1. NIK')
    print('2. Nama')
    print('3. No HP')
    print('4. Kembali')
    print(' ')
    user = input('Pilih Nomor: ')
    print(' ')
    dsNIK() if user=='1' else (dsNama() if user=='2' else (dsNoHP() if user=='3' else (lihatData() if user=='4' else user)))

def dsNIK():
    with open('dbWarga.csv') as db :
        dbWarga = csv.reader(db)
        all_rows = []
        for row in dbWarga:
            all_rows.append(row)
    user = input('Masukan NIK: ')
    
    # nik = [dataNIK for dataNIK in data if dataNIK['NIK']>20] #proses filtering menggunakan List Comprehension
    # print(f'Berikut ini data yang sudah di filter dengan deposit yang kurang dari 2 jt : \n ',nik,{'nasabah'},{'deposit'})

def dsNama():
    with open('dbWarga.csv') as db :
        dbWarga = csv.reader(db)
        all_rows = []
        for row in dbWarga:
            all_rows.append(row)
    user = input('Masukan Nama: ')
def dsNoHP():
    with open('dbWarga.csv') as db :
        dbWarga = csv.reader(db)
        all_rows = []
        for row in dbWarga:
            all_rows.append(row)
    user = input('Masukan No HP: ')

def dataView():
    clean()
    print('-'*62)
    print('\t\t\t  TAMPILKAN DATA PENDUDUK')
    print('-'*62)
    print(' ')
    print('Cari data berdasarkan: ')
    print('1. Nama')
    print('2. Umur')
    print('3. Alamat')
    print('4. Kembali')
    print(' ')
    user = input('Pilih Nomor: ')
    print(' ')
    dsNIK() if user=='1' else (dsNama() if user=='2' else (dsNoHP() if user=='3' else (lihatData() if user=='4' else user)))

def dataViewNama():
    clean()
    print('-'*62)
    print('\t\t      DATA PENDUDUK DESA')
    print('-'*62)
    # nama = [dn for dn in data if dn['nama']<2000000] #proses filtering menggunakan List Comprehension
    # print(f'Berikut ini data yang sudah di filter dengan deposit yang kurang dari 2 jt : \n ',nama,{'nasabah'},{'deposit'})
    df = pandas.DataFrame(data)
    print(df)
    print('-'*62)

def dataViewUmur():
    clean()
    print('-'*62)
    print('\t\t      DATA PENDUDUK DESA')
    print('-'*62)
    df = pandas.DataFrame(data)
    print(df)
    print('-'*62)

    umur = [dataUmur for dataUmur in data if dataUmur['Umur']<20] #proses filtering menggunakan List Comprehension
    print(f'berikut ini data yang sudah di filter dengan deposit yang kurang dari 2 jt : \n ',umur,{'nasabah'},{'deposit'})

def dataViewAlamat():
    clean()
    with open('dbWarga.csv') as db :
        dbWarga = csv.reader(db)
        all_rows = []
        # for row in dbWarga:
        #     all_rows.append(row)
        #     print(all_rows)
    print('-'*62)
    print('\t\t      DATA PENDUDUK DESA')
    print('-'*62)
    df = pandas.DataFrame(data)
    print(df)
    print('-'*62)

    # deposit = [datas for datas in data if datas['deposit']<2000000] #proses filtering menggunakan List Comprehension
    # print(f'berikut ini data yang sudah di filter dengan deposit yang kurang dari 2 jt : \n ',deposit,{'nasabah'},{'deposit'})

def menu():
    print('-'*62)
    print('\t\t\tSELAMAT DATANG')
    print('-'*62)
    print('\t    Silahkan Masukan Username dan Password!')
    print(' ')
    user = []
    with open ('user.csv') as usr:
        username = csv.reader(usr)
        for i in username:
            user.append(i)
    un = input('Username: ')
    pw = input('Password: ')
    print('')
    time.sleep(1)
    lihatData()if [un,pw] in user else print('\t\tUsername atau Password Salah!')
    print('-'*62)
    # clean()
    # menu()
menu()