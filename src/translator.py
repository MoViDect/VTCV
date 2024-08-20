from googletrans import Translator
from langchain_community.llms import Ollama
import time
translator = Translator()


llm = Ollama(model="llama3.1")

def translate(text, src:str = 'en', dest:str = 'ko'):
    start_time = time.time()
    resp = text
    try:
        if len(text) >= 1:
            translated = translator.translate(str(text), src=src, dest=dest)
            resp = translated.text
            print(resp)
    except Exception as e:
        print(e, text)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"구글 실행 시간: {execution_time:.2f} 초")
    return resp


def ai_translate(text, src:str = 'en', dest:str = 'ko'):
    start_time = time.time()
    resp = llm.invoke(f"please translate \'{text}\' from {src} to {dest}. only translated result")
    print(resp)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"AI 실행 시간: {execution_time:.2f} 초")
    return resp


# 번역 test
if __name__ == '__main__':
    # support language
    # 한국어 = ko
    # 일본어 = ja
    # 영어 = en
    # 러시아어 = ru
    # 스페인어 = es
    translate('안녕하세요 저는 한국사람 입니다 절 해치지 마세요', 'ko', 'es')
    ai_translate('안녕하세요 저는 한국사람 입니다 절 해치지 마세요', 'ko', 'es')
    translate('Hello I am kind korean please do not hurt me', 'en', 'ko')
    ai_translate('Hello I am kind korean please do not hurt me', 'en', 'ko')