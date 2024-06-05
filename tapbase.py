import aiohttp
import asyncio

async def check_ref(ref_value, counter):
    url = 'https://lordcoins.xyz/refcheck.php'
    headers = {
        'Host': 'lordcoins.xyz',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'accept': '*/*',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://lordcoins.xyz',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://lordcoins.xyz/base.html?tgWebAppStartParam=10779775',
        'accept-language': 'en-US,en;q=0.9',
        'priority': 'u=1, i',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        'ref': ref_value,
        'type': 1,
        
    }
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url, headers=headers, data=data) as response:
                result = await response.text()
                status_code = response.status
                print(f'Status Kode: {status_code}')
                print(result)
                if result == '1':
                    print(f'Reff Sukses {counter}')
                else:
                    print(result)
                    print('Reff Gagal')
        except Exception as e:
            print('Error:', str(e))
            print(f'Detail Kesalahan: {str(e)}')
async def start_loop():
    with open('id_ref.txt', 'r') as file:
        ref_value = file.read().strip()
    counter = 1
    while True:
        asyncio.create_task(check_ref(ref_value, counter))
        counter += 1
        await asyncio.sleep(0.5)  # Tambahkan jeda untuk menghindari permintaan terlalu sering

# Memulai loop dengan ref value yang diambil dari file
asyncio.run(start_loop())