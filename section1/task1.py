from nltk.tokenize import word_tokenize, sent_tokenize, MWETokenizer

def tokenize_text(text, option):
    if(option == 1):
        return word_tokenize(text)
    if(option == 2):
        return sent_tokenize(text)
    return text.split()
        
def show_prombt_message():
    print('select option for tokenization:')
    print('select 1 for using word tokenize function')
    print('select 2 for using sentence tokenize function')
    print('select 3 for using split function')


show_prombt_message()
option = int(input())
while(option not in [1,2,3]):
    show_prombt_message()
    option = int(input())

text = "Hello, today i went home early. I feel very happy. I want to go to New York"
tokenized_text = tokenize_text(text, option)
mwe_list = [('New', 'York')]
mwe_tokenizer = MWETokenizer(mwe_list)
new_tokenized_text = mwe_tokenizer.tokenize(tokenized_text)
if(option == 1):
    print(new_tokenized_text)
else:
    print(tokenized_text)
