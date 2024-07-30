from googletrans import Translator
translator = Translator()


def translate(text, src:str = 'en', dest:str = 'ko'):
    resp = text
    try:
        if len(text) >= 1:
            translated = translator.translate(str(text), src=src, dest=dest)
            resp = translated.text
            print(resp)
    except Exception as e:
        print(e, text)
    return resp


# 번역 test
if __name__ == '__main__':
    # support language
    # 한국어 = ko
    # 일본어 = ja
    # 영어 = en
    # 러시아어 = ru
    # 스페인어 = es
    translate('안녕하세요', 'ko', 'es')
    translate('Hello', 'en', 'ru')