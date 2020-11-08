
currencies_symbols= {'Lek': ('lek', 'ALL'),
 '؋': ('Afghani', 'AFN'),
 '$': ('dollar', 'UYU'),
 '₼': ('manat', 'AZN'),
 'Bs.': ('boliviano', 'BOB'),
 'KM': ('convertible Marka', 'BAM'),
 'P': ('pula', 'BWP'),
 'лв.': ('lev', 'BGN'),
 'R$': ('real', 'BRL'),
 '៛': ('riel', 'KHR'),
 '元': ('yuan Renminbi', 'CNY'),
 '₡': ('colon', 'CRC'),
 'kn': ('kuna', 'HRK'),
 'Kč': ('koruna', 'CZK'),
 'kr': ('krona', 'SEK'),
 'RD$': ('peso', 'DOP'),
 '€': ('euro', 'EUR'),
 '₾': ('lari', 'GEL'),
 'Q': ('quetzal', 'GTQ'),
 'L': ('lempira', 'HNL'),
 'Ft': ('forint', 'HUF'),
 '₹': ('rupee', 'INR'),
 'Rp': ('rupiah', 'IDR'),
 '₪': ('shekel', 'ILS'),
 '￥': ('yen', 'JPY'),
 'тңг.': ('tenge', 'KZT'),
 '₩': ('won', 'KRW'),
 'Ls': ('lat', 'LVL'),
 'Lt': ('litas', 'LTL'),
 'ден': ('denar', 'MKD'),
 'RM': ('ringgit', 'MYR'),
 'Rs': ('rupee', 'MUR'),
 'MT': ('metical', 'MZN'),
 'N$': ('dollar', 'NAD'),
 'नेरू': ('rupee', 'NPR'),
 'C$': ('cordoba', 'NIO'),
 '₦': ('naira', 'NGN'),
 '₨': ('rupee', 'PKR'),
 'B/.': ('balboa', 'PAB'),
 '₲': ('guarani', 'PYG'),
 'S/.': ('nuevo Sol', 'PEN'),
 '₱': ('peso', 'PHP'),
 'zł': ('zloty', 'PLN'),
 'RON': ('new leu', 'RON'),
 'руб.': ('ruble', 'RUB'),
 'дин.': ('dinar', 'RSD'),
 'Ssh': ('shilling', 'SOS'),
 'R': ('rand', 'ZAR'),
 'රු': ('rupee', 'LKR'),
 'CHF': ('franc', 'CHF'),
 '£S': ('pound', 'SYP'),
 'NT$': ('new Dollar', 'TWD'),
 '฿': ('baht', 'THB'),
 '₴': ('hryvna', 'UAH'),
 '£': ('pound', 'GBP'),
 'UZS': ('som', 'UZS'),
 'Bs.F.': ('bolivar Fuerte', 'VEF'),
 '₫': ('dong', 'VND'),
 'Դ':('Armenian Dram','AMD'),
 'Kz':('Kwanza','AOA'),
 'ƒ':('Aruban Guilder','AWG'),
 'КМ':('Konvertibilna Marka','BAM'),
 '৳':('Taka','BDT'),
 'лв':('Bulgarian Lev','BGN'),
 'Br':('Belarusian Ruble','BYN'),
 'ლ':('Lari','GEL'),
 'GH₵':('Cedi','GHS'),
 '〒':('Tenge','KZT'),
 '₭':('Kip','LAK'),
 '₮':('Tugrik','MNT'),
 'UM':('Ouguiya','MRU'),
 'MK':('Kwacha','MWK'),
 'MTn':('Metical','MZN'),
 '₱':('Philippine Peso','PHP'),
 'din':('Serbian Dinar','RSD'),
 'р.':('Russian Ruble','RUB'),
 'Le':('Leone','SLL'),
 'Db':('Dobra','STN'),
 '£S':('Syrian Pound','SYP'),
 'ЅМ':('Somoni','TJS'),
 'T':('Paanga','TOP'),
 '₺':('Turkish Lira','TRY'),
 '₴':('Hryvnia','UAH'),
 'Bs.':('Bolivar Fuerte','VEF'),
 'VT':('Vatu','VUV'),
 'ST$':('Tala','WST'),
 'ZK':('Zambian Kwacha','ZMW'),
 'BD':('Bahraini Dinar','Bahrain'),
 'DT':('Tunisian Dinar','Tunisia'),
 'LL':('Lebanese pound','Lebanon'),
 'Afs':('afghani','Afghanistan'),
 'SAR':('Suadi rial','Suadi Arabia'),
 'YER':('Yemeni Rial','Yemen'),
 'LD':('dirham','Libya'),
 'DH':('Morrocan Dirham','Morocco'),
 'R.O.':('Omani rial' ,'Oman'),
 'QR':('Qatri Rial','Qatar'),
 'L.E.':('Egyption pound','Egypt'),
 'DH':('Dirham UAE' ,'UAE')}


def symbols_to_text(text):
    import re
    for i in currencies_symbols.keys():
        
        #(\d+\$|\$+\d+)
        try:
                p = "\d+(i)|(i)\d+|\d (i)|(i) \d|\d+[i]|[i]\d+|\d [i]|[i] \d"

                p = p.replace('i',i)

                #print(p)
                m = re.search(p, text)
                #print(m)
                a, b = m.span()
                #print(a,b)
                #print(a,b)
                #print(s[i])
                #print(test[:a])
                #print(test[b:])
                #print(test[a-1:b].replace(i, s[i]))
                #print(test[:a-1] + test[a-1:b+1].replace(i, ' '+s[i][0]+ ' ') + test[b+1:])
                #print('>>>>>>>>>>>>>',text[:a] + text[a:b].replace(i, ' '+s[i][0]+ ' ') + text[b:])
                text = text[:a] + text[a:b].replace(i, ' '+currencies_symbols[i][0]+' ') + text[b:]
                #print(test[m.start():m.end()].replace(i , s[i]))
        except:
            pass
            #print('pass')
    return text

