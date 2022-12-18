import os,time,pandas,csv

data = [{'NIK': 20, '   Nama': 'Lintang', '   Jenis Kelamin': 'Perempuan', '   Umur': 20,'   Alamat': 'Jember','   No HP': '081'},
         {'NIK': 21, '   Nama': 'Dika', '   Jenis Kelamin': 'Laki-laki', '   Umur': 21, '   Alamat': 'Jember','   No HP': '082'},
         {'NIK': 22, '   Nama': 'Nabil', '   Jenis Kelamin': 'Laki-laki', '   Umur': 17, '   Alamat': 'Situbondo','   No HP': '083'},
         {'NIK': 23, '   Nama': 'Wahyu', '   Jenis Kelamin': 'Laki-laki', '   Umur': 23, '   Alamat': 'Banyuwangi','   No HP': '084'},
         {'NIK': 24, '   Nama': 'Rainey', '   Jenis Kelamin': 'Perempuan', '   Umur': 21, '   Alamat': 'Surabaya','   No HP': '085'},
         {'NIK': 25, '   Nama': 'Foxy', '   Jenis Kelamin': 'Perempuan', '   Umur': 22, '   Alamat': 'Surabaya','   No HP': '086'},
         {'NIK': 26, '   Nama': 'Marvel', '   Jenis Kelamin': 'Laki-laki', '   Umur': 15, '   Alamat': 'Situbondo','   No HP': '087'},
         {'NIK': 27, '   Nama': 'Naufal', '   Jenis Kelamin': 'Laki-laki', '   Umur': 19, '   Alamat': 'Sidoarjo','   No HP': '088'},
         {'NIK': 28, '   Nama': 'Ava', '   Jenis Kelamin': 'Laki-laki', '   Umur': 18, '   Alamat': 'Semarang','   No HP': '089'},
         {'NIK': 29, '   Nama': 'Ragnora', '   Jenis Kelamin': 'Perempuan', '   Umur': 19, '   Alamat': 'Jember','   No HP': '090'},
         {'NIK': 30, '   Nama': 'Clause', '   Jenis Kelamin': 'Laki-laki', '   Umur': 19, '   Alamat': 'Jember','   No HP': '091'},
         {'NIK': 31, '   Nama': 'Lucas', '   Jenis Kelamin': 'Laki-laki', '   Umur': 20, '   Alamat': 'Jember','   No HP': '092'},
         {'NIK': 32, '   Nama': 'Charlie', '   Jenis Kelamin': 'Laki-laki', '   Umur': 30, '   Alamat': 'Jember','   No HP': '093'},
         {'NIK': 33, '   Nama': 'Joy', '   Jenis Kelamin': 'Laki-laki', '   Umur': 35, '   Alamat': 'Jember','   No HP': '094'},
         {'NIK': 34, '   Nama': 'Amri', '   Jenis Kelamin': 'Laki-laki', '   Umur': 40, '   Alamat': 'Jember','   No HP': '095'},
         {'NIK': 35, '   Nama': 'Sayyid', '   Jenis Kelamin': 'Laki-laki', '   Umur': 29, '   Alamat': 'Jember','   No HP': '096'},
         {'NIK': 36, '   Nama': 'Reo', '   Jenis Kelamin': 'Laki-laki', '   Umur': 20, '   Alamat': 'Jember','   No HP': '097'},
         {'NIK': 37, '   Nama': 'Winter', '   Jenis Kelamin': 'Perempuan', '   Umur': 25, '   Alamat': 'Jember','   No HP': '098'},
         {'NIK': 38, '   Nama': 'Knoby', '   Jenis Kelamin': 'Laki-laki', '   Umur': 27, '   Alamat': 'Jember','   No HP': '099'},
         {'NIK': 39, '   Nama': 'Hector', '   Jenis Kelamin': 'Laki-laki', '   Umur': 26, '   Alamat': 'Jember','   No HP': '100'},
         {'NIK': 40, '   Nama': 'Syri', '   Jenis Kelamin': 'Perempuan', '   Umur': 29, '   Alamat': 'Jember','   No HP': '101'},
         {'NIK': 41, '   Nama': 'Sandpy', '   Jenis Kelamin': 'Perempuan', '   Umur': 24, '   Alamat': 'Jember','   No HP': '102'},
         {'NIK': 42, '   Nama': 'Albi', '   Jenis Kelamin': 'Perempuan', '   Umur': 23, '   Alamat': 'Jember','   No HP': '103'},
         {'NIK': 43, '   Nama': 'Chess', '   Jenis Kelamin': 'Perempuan', '   Umur': 18, '   Alamat': 'Jember','   No HP': '104'},
         {'NIK': 44, '   Nama': 'Snowy', '   Jenis Kelamin': 'Perempuan', '   Umur': 31, '   Alamat': 'Jember','   No HP': '105'},
         ]

def clean():
    os.system('cls')

def menu():
    print('='*62)
    print('\t\t\tSELAMAT DATANG')
    print('='*62)
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
    print('')
    time.sleep(1)
    input('Ketik Apapun Untuk Memuat Ulang: ')
    time.sleep(1)
    clean()
    menu()

def lihatData():
    clean()
    print('='*62, '\n',
    '\t\t\t DATA PENDUDUK DESA', '\n'+
    '='*62, '\n',
    ' ', '\n'+
    '1. Cari Data', '\n'+
    '2. Tampilkan Data')
    print(' ')
    user = input('Pilih Nomor: ')
    print(' ')
    time.sleep(1)
    dataFilter() if user=='1' else (dataSort() if user=='2' else print('\t      Pilih Sesuai Nomor Yang Tersedia!'))
    print('-'*62)
    print(' ')
    time.sleep(1)
    input('Ketik Apapun Untuk Memuat Ulang: ')
    time.sleep(1)
    clean()
    lihatData()

#---------------------------------------------------Filter---------------------------------------------------#

def dataFilter():
    clean()
    print('='*62)
    print('\t\t\t   CARI DATA')
    print('='*62)
    print(' ')
    print('Cari data berdasarkan: ')
    print('1. NIK')
    print('2. Nama')
    print('3. Umur')
    print('4. Alamat')
    print('5. No HP')
    print('6. Kembali')
    print(' ')
    user = input('Pilih Nomor: ')
    print(' ')
    time.sleep(1)
    dataFilterNIK() if user=='1' else (dataFilterNama() if user=='2' else (dataFilterUmur() if user=='3' else (dataFilterAlamat() if user=='4' else (dataFilterNoHP() if user=='5' else (lihatData() if user=='6' else print('\t      Pilih Sesuai Nomor Yang Tersedia!'))))))
    print('-'*62)
    print(' ')
    time.sleep(1)
    input('Ketik Apapun Untuk Kembali Ke Laman Utama: ')
    time.sleep(1)
    clean()
    lihatData()

def dataFilterNIK():
    user = input('Masukan NIK: ')
    nik = [dataNIK for dataNIK in data if dataNIK['NIK']==int(user)]
    print(' ')
    print('Berikut ini data yang sudah di filter:')
    print('-'*62)
    df = pandas.DataFrame(nik)
    print(df)

def dataFilterNama():
    user = input('Masukan Nama: ')
    nama = [dataNama for dataNama in data if dataNama['   Nama']==user]
    print(' ')
    print('Berikut ini data yang sudah di filter:')
    print('-'*62)
    df = pandas.DataFrame(nama)
    print(df)

def dataFilterUmur():
    user = input('Masukan Umur: ')
    umur = [dataUmur for dataUmur in data if dataUmur['   Umur']==int(user)]
    print(' ')
    print('Berikut ini data yang sudah di filter:')
    print('-'*62)
    df = pandas.DataFrame(umur)
    print(df)

def dataFilterAlamat():
    user = input('Masukan Alamat: ')
    alamat = [dataNama for dataNama in data if dataNama['   Alamat']==user]
    print(' ')
    print('Berikut ini data yang sudah di filter:')
    print('-'*62)
    df = pandas.DataFrame(alamat)
    print(df)

def dataFilterNoHP():
    user = input('Masukan No HP: ')
    noHP = [dataNoHP for dataNoHP in data if dataNoHP['   No HP']==user]
    print(' ')
    print('Berikut ini data yang sudah di filter:')
    print('-'*62)
    df = pandas.DataFrame(noHP)
    print(df)
#---------------------------------------------------Filter---------------------------------------------------#



#---------------------------------------------------Sort---------------------------------------------------#

def dataSort():
    clean()
    print('='*62)
    print('\t\t    TAMPILKAN DATA PENDUDUK')
    print('='*62)
    print(' ')
    print('Cari data berdasarkan: ')
    print('1. Nama')
    print('2. Umur')
    print('3. Alamat')
    print('4. Kembali')
    print(' ')
    user = input('Pilih Nomor: ')
    print(' ')
    dataSortNama() if user=='1' else (dataSortUmur() if user=='2' else (dataSortAlamat() if user=='3' else (lihatData() if user=='4' else user)))

def mySort(list_, func, key):
    if len(list_) < 2:
        return list_
    if len(list_) == 2:
        return list_ if func(list_[0], key) <= func(list_[1], key) else [list_[1], list_[0]] 
    result = [list_[0]] + mySort([list_[1]]+list_[2:], func, key) if func(list_[0], key) <= func(list_[1], key) else [list_[1]] + mySort([list_[0]]+list_[2:], func,key)
    return mySort(result[:-1], func, key)+result[-1:]

def dataSortNama():
    clean()
    print('='*62)
    print('\t\t      DATA PENDUDUK DESA')
    print('\t\t\t Menurut Nama')
    print('='*62)
    x = (mySort(data, lambda x,y: x[y], '   Nama'))
    df = pandas.DataFrame(x)
    print(df)
    print('-'*62)

def dataSortUmur():
    clean()
    print('='*62)
    print('\t\t      DATA PENDUDUK DESA')
    print('\t\t\t Menurut Umur')
    print('='*62)
    x = (mySort(data, lambda x,y: x[y], '   Umur'))
    df = pandas.DataFrame(x)
    print(df)
    print('-'*62)

def dataSortAlamat():
    clean()
    print('='*62)
    print('\t\t      DATA PENDUDUK DESA')
    print('\t\t\t Menurut Alamat')
    print('='*62)
    x = (mySort(data, lambda x,y: x[y], '   Alamat'))
    df = pandas.DataFrame(x)
    print(df)
    print('-'*62)

#---------------------------------------------------Sort---------------------------------------------------#
menu()