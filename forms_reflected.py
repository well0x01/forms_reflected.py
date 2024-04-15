import argparse
import requests
from bs4 import BeautifulSoup

def encontrar_campos_refletidos(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all('form')
        for form in forms:
            inputs = form.find_all(['input', 'textarea'])
            for input_tag in inputs:
                campo = input_tag.get('name') or input_tag.get('id') or input_tag.get('placeholder')
                if campo:
                    if campo.lower() in response.text.lower():
                        print(f"Campo refletido encontrado: {campo}")
                    else:
                        print(f"Campo refletido não encontrado: {campo}")
    except Exception as e:
        print(f"Erro ao analisar a URL: {e}")

def main():
    parser = argparse.ArgumentParser(description="Teste")
    parser.add_argument("-u", "--url", type=str, required=True, help="URL para teste")
    args = parser.parse_args()
    url = args.url

    encontrar_campos_refletidos(url)

if __name__ == "__main__":
    main()
