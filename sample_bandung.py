import requests

kecamatan_url = "https://sirekap-obj-data.kpu.go.id/wilayah/pemilu/ppwp/32/3273.json"
kecamatan_response = requests.get(kecamatan_url)
data_kecamatan = kecamatan_response.json()
for item_kecamatan in data_kecamatan:
    kode_kecamatan = item_kecamatan['kode'];
    kelurahan_url = f"https://sirekap-obj-data.kpu.go.id/wilayah/pemilu/ppwp/32/3273/{kode_kecamatan}.json"
    response_kelurahan = requests.get(kelurahan_url)
    data_kelurahan = response_kelurahan.json()
    for item_kelurahan in data_kelurahan:    
        # Construct the URL with the correct paramCode
        tps_url = f"https://sirekap-obj-data.kpu.go.id/wilayah/pemilu/ppwp/32/3273/{kode_kecamatan}/{item_kelurahan['kode']}.json"        
        # Make a request to the detail URL
        tps_response = requests.get(tps_url)
        data_tps = tps_response.json()
        
        # Process the data_detail as needed
        for item_tps in data_tps:
            # Construct the URL for detailed TPS data with the correct paramCode
            administration_result_url = f"https://sirekap-obj-data.kpu.go.id/pemilu/hhcw/ppwp/32/3273/{kode_kecamatan}/{item_kelurahan['kode']}/{item_tps['kode']}.json"
            
            # Make a request to the detailed TPS URL
            administration_result_response = requests.get(administration_result_url)
            if(administration_result_response) :
                administration_result_data = administration_result_response.json()
                if(administration_result_data is not None and administration_result_data != '') :
                    administrasi = administration_result_data["administrasi"]
                    chart = administration_result_data["chart"]
                    if(administrasi is not None and chart is not None): 
                        suara_total = administrasi["suara_total"];                        
                        total_paslon_1 = chart['100025'];
                        total_paslon_2 = chart['100026'];
                        total_paslon_3 = chart['100027'];
                        total = total_paslon_1 + total_paslon_2 + total_paslon_3
                        if(suara_total < total):
                            print("--------")
                            print("Kecamatan : "+item_kecamatan["nama"]+" Kelurahan :"+ item_kelurahan["nama"] +" " +item_tps["nama"]);
                            print("Jumlah suara lebih kecil dari hasil Scan OCR Sirekap! ");     
                            print("Total Suara ",suara_total)      
                            print("Hasil OCR ",total)
                            print()                              
               


