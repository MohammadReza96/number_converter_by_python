def Converter_to_persion():
    dic_number={
        "0":"۰",
        "1":"۱",
        "2":"۲",
        "3":"۳",
        "4":"۴",
        "5":"۵",
        "6":"۶",
        "7":"۷",
        "8":"۸",
        "9":"۹",
    }
    dic_persion_number_less_than_10 = {
        "0": "صفر",
        "1": "یک",
        "2": "دو",
        "3": "سه",
        "4": "چهار",
        "5": "پنج",
        "6": "شش",
        "7": "هفت",
        "8": "هشت",
        "9": "نه",
    }
    dic_persion_number_between_10_and_20 = {
        "10": "ده",
        "11": "یازده",
        "12": "دوازده",
        "13": "سیزده",
        "14": "چهارده",
        "15": "پانزده",
        "16": "شانزده",
        "17": "هفده",
        "18": "هجده",
        "19": "نوزده",
    }
    dic_persion_number_between_20_and_100 = {
        "20": "بیست",
        "30": "سی",
        "40": "چهل",
        "50": "پنجاه",
        "60": "شست",
        "70": "هفتاد",
        "80": "هشتاد",
        "90": "نود",
    }
    dic_persion_number_between_100_and_1000 = {
        "100": "صد",
        "200": "دویست",
        "300": "سیصد",
        "400": "چهارصد",
        "500": "پانصد",
        "600": "ششصد",
        "700": "هفصد",
        "800": "هشتصد",
        "900": "نهصد",
    }
    
    
    while True:
        
        Type=input("""
                    Enter Type :
                    \n type '2' for converting to persion number
                    \n type '1' for converting to persion alphabetical 
                    \n :
                    """)
        
        if Type!="1" and Type!="2":
            print("Error Print the correct type number...!")
            continue
        
        full_number_in_english_in_number=input("Enter Number : ")
    
    
        if Type == "1" :
            final_number = ''
            full_number_in_english_in_number = int(full_number_in_english_in_number)
            full_number_in_english_in_string = str(full_number_in_english_in_number)

            for item in full_number_in_english_in_string:                   
                    if full_number_in_english_in_number//1000 > 0:
                        final_number += f'{dic_persion_number_less_than_10.get(str(full_number_in_english_in_number//1000))} هزار'
                        full_number_in_english_in_number -= \
                            (full_number_in_english_in_number//1000)*1000
                        if full_number_in_english_in_number > 0:
                            final_number += ' و '
                    elif full_number_in_english_in_number//100 > 0:
                        final_number += f'{dic_persion_number_between_100_and_1000.get(str((full_number_in_english_in_number//100)*100))}'
                        full_number_in_english_in_number -= \
                            (full_number_in_english_in_number//100)*100
                        if full_number_in_english_in_number > 0:
                            final_number += ' و '
                    elif full_number_in_english_in_number//10 > 0:
                        if full_number_in_english_in_number >= 20:
                            final_number += f'{dic_persion_number_between_20_and_100.get(str((full_number_in_english_in_number//10)*10))}'
                            full_number_in_english_in_number -= \
                            (full_number_in_english_in_number//10)*10
                        else:
                            final_number += f'{dic_persion_number_between_10_and_20.get(str((full_number_in_english_in_number)))}'
                            full_number_in_english_in_number -= full_number_in_english_in_number

                        if full_number_in_english_in_number > 20:
                            final_number += ' و '
                    else:
                        if full_number_in_english_in_number > 0:
                            final_number += f' {dic_persion_number_less_than_10.get(str(full_number_in_english_in_number))}'
                            full_number_in_english_in_number -= full_number_in_english_in_number
                        else:
                            pass
            print(final_number)
        
            next_decission=input("Do you want to continue (Y/N) :")
            if next_decission.capitalize()=="Y":
                continue
            else:
                break    
                  
        elif Type == "2" :
            final_number = []
            full_number_in_english_in_string = str(full_number_in_english_in_number)
            
            for num in full_number_in_english_in_string:
                if num in dic_number.keys():
                        final_number.append(dic_number.get(num))
            print(''.join(final_number))
            
            next_decission=input("Do you want to continue (Y/N) :")
            if next_decission.capitalize()=="Y":
                continue
            else:
                break 

print(Converter_to_persion())