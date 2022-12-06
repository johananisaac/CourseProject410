import json

def jsonread(filename):
    with open(filename,'rb') as file:
        data = json.load(file, encoding = 'UTF-8')

    return data


def main():
    data = jsonread('../text/comment5.json')
    numOfComments = data['comments']
    text = dict()
    for i in range(len(numOfComments)):
        text[i]=numOfComments[i]['text']

    return text

if __name__ == '__main__':
    text = main()
    #for key in text:
        #print(text[key])
    #print(main())


