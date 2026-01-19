from search import search_prompt

def main():
    print("Faça sua pergunta:")
    question = input("PERGUNTA: ")

    chain = search_prompt(question=question)

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return
    
    print(chain.content)

    # result = chain.invoke()

    # print(result.content)

if __name__ == "__main__":
    main()