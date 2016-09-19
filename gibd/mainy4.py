from web_scrapping.site_managers.greenpeace_manager import GreenpeaceManager
from time import time


gm = GreenpeaceManager()

t1 = time()
algo = gm.get_sites(pages = 20)
t2 = time()

res = t2 - t1

print (res)

for esta in algo:
    print(esta.prettify())

