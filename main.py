def prog(text):

    def choose_words(text):
        temp_list = []
        temp_word = ""

        for symbol in text:
            if symbol.isalpha() == True:
                temp_word += symbol

            else:
                if temp_word != "":
                    temp_list.append(temp_word)
                temp_word = ""

        return temp_list

    temp = choose_words(text)

    def choose_sybmols(some_list):
        symbols_list = []
        
        for item in some_list:
            for symbol in item:
                if item.count(symbol) == 1:
                    symbols_list.append(symbol)
                break
        return symbols_list

    symbols_list = choose_sybmols(temp)


    def choose_one_symbol(some_list):
        for item in some_list:
            if some_list.count(item) == 1:
                return item
        return None

    answer = choose_one_symbol(symbols_list)

    print(answer)

    return answer

if __name__ == '__main__':
    text = """The Tao gave birth to machine language.  Machine language gave birth
to the assembler.
The assembler gave birth to the compiler.  Now there are ten thousand
languages.
Each language has its purpose, however humble.  Each language
expresses the Yin and Yang of software.  Each language has its place within
the Tao.
But do not program in COBOL if you can avoid it.
        -- Geoffrey James, "The Tao of Programming" """
    text1 = "C makes it easy for you to shoot yourself in the foot. C++ makes that harder, but when you do, it blows away your whole leg. (с) Bjarne Stroustrup"
    text2 = "mmmm"
    prog(text1)


