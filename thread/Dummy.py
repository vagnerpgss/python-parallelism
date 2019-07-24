from urllib.request import urlopen
from multiprocessing.dummy import Pool as ThreadPool

urls = ['https://www.sciencedaily.com/', 'http://www.python.org', 'https://www.scala-lang.org/', 'https://elixir-lang.org/']

pool = ThreadPool()
results = pool.map(urlopen, urls) # Abre as URLs em suas próprias threads e retorna os resultados
pool.close() # Fecha o pool e aguarda as threads terminarem
pool.join()

# results = []
# for url in urls:
#     results.append(urlopen(url))