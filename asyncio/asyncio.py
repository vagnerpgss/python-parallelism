import asyncio # módulo para processar as funções de forma assíncrona
import time
import aiohttp # criar client sessions

async def download_site(session, url): # async torna a função assíncrona
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))

async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session: # ClientSession possui operações assíncronas (async with)
        tasks = []
        for url in sites:
            task = asyncio.create_task(download_site(session, url)) # O mesmo que asyncio.ensure_future()
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)
        # await passa o controle de função de volta ao loop de eventos quando a Task precisa esperar uma resposta

if __name__ == "__main__":
    sites = ["https://docs.python.org", "https://www.sciencedaily.com/",] * 80
    start_time = time.time()
    asyncio.run(download_all_sites(sites)) # get_event_loop().run_until_complete
    # run Executa a co-rotina passada, cuidando do gerenciamento do Event Loop
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")