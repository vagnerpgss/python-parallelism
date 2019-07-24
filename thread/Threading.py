from urllib.request import urlopen
import threading
import queue

urls = ['http://www.python.org', 'https://www.scala-lang.org/', 'https://elixir-lang.org/']

class Consumer(threading.Thread):
  def __init__(self, queue):
    threading.Thread.__init__(self)
    self._queue = queue

  def run(self):
    while True:
      msg = self._queue.get() # queue.get() bloqueia a thread atual até que um item seja recuperado.
      response = urlopen(msg)

def Producer():
  urlQueue = queue.Queue() # Usado para compartilhar os itens entre as threads.
  worker = Consumer(urlQueue) # Cria uma instância do consumidor
  worker.start() # Chama o método interno run() para iniciar a thread.

  for url in urls:
    urlQueue.put(url)

  worker.join() # Espera a thread terminar

if __name__ == '__main__':
  Producer()