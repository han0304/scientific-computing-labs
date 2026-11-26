#### Homework 3
#### Combine 33, 34, 35 into one file
win=mathTEACHWINURLabelFrame
for ww in win.winfo_children():
    ww.destroy()

####################################
#pip install numpy

import numpy as np

# Sample dataset: A small text corpus
corpus = """Artificial Intelligence is the new electricity.
Machine learning is the future of AI.
AI is transforming industries and shaping the future.
Habitual diligence in any employment or pursuit, 
either bodily or mental; steady attention to business; 
assiduity; -- opposed to sloth and idleness; 
as, industry pays debts, while idleness 
or despair will increase them.
We are more industrious than our forefathers, 
because in the present times the funds destined 
for the maintenance of industry are much greater in proportion 
to those which are likely to be employed in the maintenance of idleness, than they were two or three centuries ago. 
"""

### step 3
# Tokenize the corpus into words
words = corpus.lower().split()

# Create a vocabulary of unique words
vocab = list(set(words))
vocab_size = len(vocab)

print(f"Vocabulary: {vocab}")
print(f"Vocabulary size: {vocab_size}")



###Step 4: Map Words to Numbers
global word_to_idx
word_to_idx = {word: idx for idx, word in enumerate(vocab)}
print(word_to_idx)
idx_to_word = {idx: word for word, idx in word_to_idx.items()}

# Convert the words in the corpus to indices
corpus_indices = [word_to_idx[word] for word in words]


#Step 5: Building the Model
# Initialize bigram counts matrix
bigram_counts = np.zeros((vocab_size, vocab_size))

# Count occurrences of each bigram in the corpus
for i in range(len(corpus_indices) - 1):
    current_word = corpus_indices[i]
    next_word = corpus_indices[i + 1]
    bigram_counts[current_word, next_word] += 1

# Apply Laplace smoothing by adding 1 to all bigram counts
bigram_counts += 0.01

# Normalize the counts to get probabilities
bigram_probabilities = bigram_counts / bigram_counts.sum(axis=1, keepdims=True)

print("Bigram probabilities matrix: ", bigram_probabilities)



###
def predict_next_word(current_word, bigram_probabilities):
    import numpy as np
    global vocab_size
    global idx_to_word
    word_idx = word_to_idx[current_word]
    next_word_probs = bigram_probabilities[word_idx]
    next_word_idx = np.random.choice(range(vocab_size), p=next_word_probs)
    return idx_to_word[next_word_idx]





def cmdEEButton():
    global EEInput
    global EEN
    global predict_next_word
    global bigram_probabilities
    print(EEInput.get())
    # Test the model with a word
    current_word = "industries"
    if len(EEInput.get())>1:
        current_word = EEInput.get()
    else:
        EEInput.insert(0,current_word)

    sentance=''
    sentance=sentance+current_word
    for i in range(int(EEN.get())):
        next_word = predict_next_word(current_word, bigram_probabilities)
        print(f"Given '{current_word}', the model predicts '{next_word}'.")
        current_word=next_word
        sentance=sentance+' '+current_word
    print('---------')

    ### fine tuling ####
    ### (1) end with '.'
    ### (2) Capital letter for the first letter of each sentance. 
    while not sentance.endswith('.'):
          sentance=sentance[:-1]

    print(sentance)


EEInput=tkinter.Entry(win)
EEInput.place(relx=0,rely=0,relwidth=0.6,relheight=0.1)
EEInput.insert(0,'industries')
EEN=tkinter.Entry(win)
EEN.place(relx=0.6,rely=0,relwidth=0.2,relheight=0.1)
EEN.insert(0,200)

EEButton=tkinter.Button(win)
EEButton.place(relx=0.8,rely=0,relwidth=0.1,relheight=0.1)
EEButton.configure(text='RUN')
EEButton.configure(command=cmdEEButton)


options=['1','2','3','4']
EEOString=tkinter.StringVar()
EEOString.set(options[1])
EEOption=tkinter.OptionMenu(win,EEOString,*options)

EEOption.place(relx=0.9,rely=0,relwidth=0.1,relheight=0.1)
