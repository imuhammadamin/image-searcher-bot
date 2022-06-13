import requests

def search(word):
    import random
    response = requests.get(f"https://imsea.herokuapp.com/api/1?q={word}")
    result = response.json()
    if result['results']:
        capt = result['image_name']
        lst = list(result['results'])
        print(*lst, sep='\n')
        photoUrl = random.choice(lst)
        return photoUrl, capt
    else:
        return False, False

if __name__ == '__main__':
    photoUrl = search('pubg')