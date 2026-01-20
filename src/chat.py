from search import search_prompt

def main():
    print("Faça sua pergunta:\n")
    question = input("PERGUNTA: ")

    chain = search_prompt(question=question)

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return

    result = chain.invoke({"pergunta": question})

    print(result.content)

if __name__ == "__main__":
    main()
