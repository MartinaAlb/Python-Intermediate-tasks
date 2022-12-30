"""
Tasks for practiciong regular expresions, functions, string methods.
In Czech, endlish version is not available.
Script contains two solutions - basic for url with all tree given parametrs,
advancet for url where can be one or more of given parametrs.
Python.
"""

# Napište funkci najdi_datum_v_url(url), která bude mít pouze jeden parametr.
# Předávaným parametrem bude url, z kterého pomocí regulárního výrazu umí
# daná funkce zjistit datum článku - kdy byl napsán.
# Kdo by chtel neco slozitejsiho, muze vytvorenou funkci -
# presneji regularni vyraz - upravit tak, aby nebylo vzdy nutne mit v url mesic a den,
# ale muze v nem byt pouze rok, tedy napr. z tohoto url:


## Basic solution

# import re
#
# def najdi_datum_v_url(url):
#         return re.findall(r"\d{4}.\d{2}.\d{2}", url)
#
# seznam_url = ["https://www.washingtonpost.com/us-policy/2022/08/07/republicans-family-benefits-roe-dobbs/",
#               "https://www.washingtonpost.com/politics/2022/08/05/us-summons-china-ambassador/",
#               "https://www.washingtonpost.com/health/2022/08/08/vaping-marijuana-link/"]
#
# url = ' '.join([str(url) for url in seznam_url])
#
# datum_typ_list = najdi_datum_v_url(url)
#
# iter_datum_typ_list = datum_typ_list.__iter__()
#
# try:
#     for datum in iter_datum_typ_list:
#             print(datum)
# except:
#     print("nebyly nalezeny další články")


## advanced solution
import re

def najdi_datum_v_url(url):
        return re.findall(r'/(\d{4})(/\d{1,2})?(/\d{1,2})?/', url)

seznam_url = ["https://www.washingtonpost.com/us-policy/2022/08/07/republicans-family-benefits-roe-dobbs/",
              "https://www.washingtonpost.com/politics/2022/08/05/us-summons-china-ambassador/",
              "https://www.washingtonpost.com/health/2022/08/08/vaping-marijuana-link/",
              "https://www.washingtonpost.com/business/interactive/2022/home-building-cost/"]

url = ' '.join([str(url) for url in seznam_url])
# print(najdi_datum_v_url(url))

datum_typ_list = najdi_datum_v_url(url)

iter_datum_typ_list = datum_typ_list.__iter__()

try:
    for datum in iter_datum_typ_list:
            datum = ' '.join(datum)
            print(datum.replace(" ",""))
except:
    print("nebyly nalezeny další články")

