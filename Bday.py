import json, os, requests

url='https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama='
logo="""
 ╭━<━━╮    ╭━━━━━━━━━━━━━━━╮
 ┃╭╮╭╮┃    │ zodiac finder │
┗┫┏━━┓┣┛   ╰━━━━━━━━━━━━━━━╯
 ┃╰━━╯┃   /  Coder : Sayyed Zakarya
 ╰┳━━┳╯
  ┛  ┗        [ Mr-Robot ]
"""
def res():
    req=requests.get(url+nama+'&tanggal='+lahir)
    jeson=json.loads(req.text)
    data=jeson['data']
    print(40*'=')
    print('Name: '+data['nama'])
    print('Age:: '+data['usia'])
    print('Date Of Birth: '+data['lahir'])
    print('Remaining MM/DD : '+data['ultah'])
    print('Zodiac: '+data['zodiak'])


if __name__=='__main__':
    os.system('clear')
    print(logo)
    print(40*'=')
    nama=input('nama: ')
    lahir=input('date of birth (ex.:05 08 2003)\ntanggal: ').replace(' ', '-')
    res()
