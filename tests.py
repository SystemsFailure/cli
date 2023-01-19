import asyncio

async def voider(callback):
    name = input('Your name...')
    if name == 'Eric':
        callback()
    else:
        print('so name is not defined')
    print('proccess 1')

async def voider2():
    await asyncio.sleep(3)
    print('proccess 2')

def getUser():
    print('user been got successful')

async def main():
    await asyncio.gather(voider2(), voider(getUser))

if __name__ == '__main__':
    asyncio.run(main())