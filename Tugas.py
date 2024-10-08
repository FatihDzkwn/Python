#Luas Persegi
print('====Luas Persegi====')
luas_persegi = 's x s'
contoh_soal = 'Sebuah Persegi memiliki sisi 4 cm. Berapakah luas dari persegi tersebut?'
jawab = 'L = s x s\n\t    = 4 x 4\n\t    = 16' 
pangkat = ('cm\u00B2')
print('Luas\t:',luas_persegi,'\nSoal\t:',contoh_soal,'\nJawab\t:',jawab,pangkat)


#Luas Persegi Panjang
print('\n====Luas Persegi Panjang====')
luas_persegi_panjang = 'p x l'
contoh_soal = 'Ridwan membeli kertas berbentuk persegi panjang dengan panjang 10 cm dan lebar 3 cm. Berapakah luas kertas yang dibeli Ridwa tersebut?'
jawab = 'L = p x l\n\t    = 10 x 3\n\t    = 30' 
pangkat = ('cm\u00B2')
print('Luas\t:',luas_persegi_panjang,'\nSoal\t:',contoh_soal,'\nJawab\t:',jawab,pangkat)


#Luas Segitiga
print('\n====Luas Segitiga====')
luas_segitiga = '1/2 x a x t'
contoh_soal = 'Ridwan membeli kertas berbentuk persegi panjang dengan panjang 10 cm dan lebar 3 cm. Berapakah luas kertas yang dibeli Ridwa tersebut?'
jawab = 'L = 1/2 x a x t\n\t    = 1/2 x 7 x 2\n\t    = 30' 
pangkat = ('cm\u00B2')
print('Luas\t:',luas_segitiga,'\nSoal\t:',contoh_soal,'\nJawab\t:',jawab,pangkat)


#Luas Lingkaran
print('\n====Luas Lingkaran====')
luas_lingkaran = 'PHI x r^2'
contoh_soal = 'Diketahui sebuah lingkaran memiliki ruas jari-jari 14 cm. Berapakah luas lingkaran tersebut?'
jawab_1 = 'L = PHI x r^2' 
jawab_2 = '\n\t    = 22/7 x 14^2'
jawab_3 = '\n\t    = 616' 
pangkat = ('cm\u00B2')
print('Luas\t:',luas_lingkaran,'\nSoal\t:',contoh_soal,'\nJawab\t:',jawab_1,pangkat,jawab_2,jawab_3,pangkat)


#Perbandingan Lebih Besar dan Lebih Kecil dari Luas Persegi dan Persegi Panjang 
print('\n====Perbandingan Lebih Besar dan Lebih Kecil dari Luas Persegi dan Persegi Panjang====')

print(luas_persegi > luas_persegi_panjang)
print(luas_persegi < luas_persegi_panjang)
print(luas_persegi_panjang > luas_persegi)
print(luas_persegi_panjang < luas_persegi)

#Perbandingan Lebih Besar dan Lebih Kecil dari Luas Segitiga dan Lingkaran 
print('\n====Perbandingan Lebih Besar dan Lebih Kecil dari Luas Segitiga dan Lingkaran====')

print(luas_segitiga > luas_lingkaran)
print(luas_segitiga < luas_lingkaran)
print(luas_lingkaran > luas_segitiga)
print(luas_lingkaran < luas_segitiga)