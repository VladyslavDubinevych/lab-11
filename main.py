from Model.regexprocessor import RegexProcessor
import requests

def main():
    request_type = "OPTIONS"
    processor = RegexProcessor(f"((23\/Mar\/2009:((03:38:1[7-9])|(03:38:[2-5][0-9])|(03:39:[0-5][0-9])|(03:[4-5][0-9]:[0-5][0-9])|(0[4-9]:[0-5][0-9]:[0-5][0-9])|(1[0-9]:[0-5][0-9]:[0-5][0-9])|(2[0-3]:[0-5][0-9]:[0-5][0-9])))|(24\/Mar\/2009:((([0-1][0-9])|2[0-3]):[0-5][0-9]:[0-5][0-9]))|(25\/Mar\/2009:((0[0-8]:[0-5][0-9]:[0-5][0-9])|(09:[0-4][0-9]:[0-5][0-9])|(09:5[0-1]:[0-5][0-9])|(09:52:[0-4][0-9])|(09:52:50)))).+{request_type}")
    
    response = requests.get("http://igm.univ-mlv.fr/~cherrier/download/L1/access.log", stream = True)
    text_file = open("data.txt","wb")
    for chunk in response.iter_content(chunk_size=1024):
        text_file.write(chunk)
    text_file.close()

    text_file = open("data.txt","r")
    print(f"Amount of {request_type} requests from 23/Mar/2009:03:38:17 to 25/Mar/2009:09:52:50 - " + str(processor.amount_of_occurrances(text_file.read())))
    text_file.close()
    


if __name__ == '__main__':
    main()