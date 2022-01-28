jumlah_buku=int(input("masukkan jumlah buku yang di beli:"))    
for i in range (jumlah_buku):
    nama_buku=input("masukkan nama buku:")
    harga_buku=int(input("masukkan harga buku: Rp."))
    nilai=[]
if jumlah_buku >= 3:
        nilai.append(harga_buku)
        total_pembelian=sum(nilai)
        kena_ppn=(2/100*total_pembelian)
        potongan_harga=(total_pembelian + kena_ppn)*10/100
        total_pembelian_bersih=total_pembelian-potongan_harga
        print("total harga yang di bayar setelah diskon",total_pembelian_bersih)
        print("anda mendapatkan bonus buku saku")
elif jumlah_buku <3:
        nilai.append(harga_buku)
        total_pembelian=sum(nilai)
        kena_ppn=(2/100*total_pembelian)
        total_pembelian_bersih=total_pembelian+kena_ppn
        print("jumlah total harga yang harus di bayar:",total_pembelian_bersih)
        print("maaf anda tidak dapat bonus")
        
