import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True


def fetch_data(url):
    wd = webdriver.Chrome(executable_path='./chromedriver', options=options)
    wd.get(url)
    time.sleep(2)
    wd.refresh()
    headers = ['Active_Drug', 'Drug_Synonyms', 'Alternative_Brands', 'Dosage_form', 'SideEffects', 'Pricing', 'Pricing_of_alternate_brands']
    val = []

    #Active Drug
    val.append(wd.find_elements_by_class_name("DrugHeader__title-content___2ZaPo")[0].text)

    # Synonms
    val.append(wd.find_elements_by_class_name("DrugHeader__meta-value___vqYM0")[2].text)

    # brands alternative
    temp = []
    for i in wd.find_elements_by_class_name("SubstituteItem__name___PH8Al"):
        temp.append(i.text)
    val.append(temp)

    # dosage form
    st = (wd.find_elements_by_class_name("DrugPriceBox__quantity___2LGBX")[0].text).split()
    for i in st:
        if i == 'tablets':
            val.append('tablet')
        elif i == 'capsule':
            val.append('capsules')

    # sidefffects
    val.append(val.append(wd.find_elements_by_class_name('DrugOverview__content___22ZBX')[5].text))

    # pricing
    val.append(wd.find_elements_by_class_name('DrugPriceBox__box___LSjIn')[0].text.split()[0].split('₹')[1])

    # comparion
    prices = wd.find_elements_by_class_name("SubstituteItem__unit-price___MIbLo")
    price = []
    for i in prices:
        price.append(i.text)
    brands = wd.find_elements_by_class_name("SubstituteItem__name___PH8Al")
    brand = []
    for i in brands:
        brand.append(i.text)
    compare = dict(zip(brand, price))
    val.append(compare)

    final_data = dict(zip(headers, val))

    return final_data





