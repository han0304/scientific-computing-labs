import numpy as np
import tkinter

# 初始化視窗
try:
    win = mathTEACHWINURLabelFrame
    for ww in win.winfo_children():
        ww.destroy()
except NameError:
    win = tkinter.Tk()
    win.geometry("600x500")

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

words = corpus.lower().split()
vocab = list(set(words))
vocab_size = len(vocab)
word_to_idx = {word: idx for idx, word in enumerate(vocab)}
idx_to_word = {idx: word for word, idx in word_to_idx.items()}
corpus_indices = [word_to_idx[word] for word in words]

bigram_counts = np.zeros((vocab_size, vocab_size))
for i in range(len(corpus_indices) - 1):
    bigram_counts[corpus_indices[i], corpus_indices[i+1]] += 1
bigram_counts += 0.01
bigram_probabilities = bigram_counts / bigram_counts.sum(axis=1, keepdims=True)

def predict_next_word(current_word, bigram_probabilities):
    if current_word not in word_to_idx:
        current_word = np.random.choice(list(word_to_idx.keys())) 
    word_idx = word_to_idx[current_word]
    next_word_probs = bigram_probabilities[word_idx]
    next_word_idx = np.random.choice(range(vocab_size), p=next_word_probs)
    return idx_to_word[next_word_idx]

# 按鈕功能
def cmdRun():
    global entry_word, entry_len, txt_output
    global var_cap, var_dot, var_gram, var_loop
    
    start_word = entry_word.get().strip()
    if not start_word: start_word = "industry"
    
    try:
        length = int(entry_len.get())
    except:
        length = 50

    current_word = start_word.lower() 
    sentence = current_word
    
    for i in range(length):
        next_word = predict_next_word(current_word, bigram_probabilities)
        current_word = next_word
        sentence += ' ' + current_word

    # --- 四個 Fine Tuning 功能 ---
    # 功能 4: Anti-Loop (去除重複)
    if var_loop.get() == 1:
        words_list = sentence.split()
        clean_list = []
        for w in words_list:
            if len(clean_list) == 0 or w != clean_list[-1]:
                clean_list.append(w)
        sentence = " ".join(clean_list)

    # 功能 2: End with '.' (句點結束)
    if var_dot.get() == 1:
        if '.' in sentence:
            while not sentence.endswith('.'):
                sentence = sentence[:-1]
        else:
            sentence += "." 

    # 功能 3: Grammar (文法修正: i -> I)
    if var_gram.get() == 1:
        sentence = sentence.replace(" i ", " I ")
        
    # 功能 1: Capitalize (首字大寫)
    if var_cap.get() == 1:
        if len(sentence) > 0:
            sentence = sentence[0].upper() + sentence[1:]

    # 更新文字區域
    txt_output.delete('1.0', tkinter.END)
    txt_output.insert(tkinter.END, sentence)

# --- 介面佈局 ---

# 1. 輸入區
lbl_word = tkinter.Label(win, text="Start Word:")
lbl_word.place(relx=0.05, rely=0.05, relwidth=0.15, relheight=0.08)

entry_word = tkinter.Entry(win)
entry_word.place(relx=0.21, rely=0.05, relwidth=0.25, relheight=0.08)
entry_word.insert(0, "industry")

lbl_len = tkinter.Label(win, text="Len:")
lbl_len.place(relx=0.5, rely=0.05, relwidth=0.1, relheight=0.08)

entry_len = tkinter.Entry(win)
entry_len.place(relx=0.61, rely=0.05, relwidth=0.15, relheight=0.08)
entry_len.insert(0, "50")

# 2. 勾選框 (Checkbuttons)
var_cap = tkinter.IntVar(value=1) 
var_dot = tkinter.IntVar(value=1)
var_gram = tkinter.IntVar(value=1)
var_loop = tkinter.IntVar(value=1)

chk1 = tkinter.Checkbutton(win, text="1. Capitalize (首字大寫)", variable=var_cap, anchor='w')
chk1.place(relx=0.05, rely=0.15, relwidth=0.5, relheight=0.06)

chk2 = tkinter.Checkbutton(win, text="2. End with '.' (句尾結束)", variable=var_dot, anchor='w')
chk2.place(relx=0.05, rely=0.21, relwidth=0.5, relheight=0.06)

chk3 = tkinter.Checkbutton(win, text="3. Grammar (文法修正)", variable=var_gram, anchor='w')
chk3.place(relx=0.05, rely=0.27, relwidth=0.5, relheight=0.06)

chk4 = tkinter.Checkbutton(win, text="4. Anti-Loop (去除單字重複)", variable=var_loop, anchor='w')
chk4.place(relx=0.05, rely=0.33, relwidth=0.5, relheight=0.06)

# 3. 按鈕
btn_run = tkinter.Button(win, text="RUN (執行)", command=cmdRun)
btn_run.place(relx=0.6, rely=0.18, relwidth=0.3, relheight=0.15)

# 4. 結果顯示區 
lbl_res = tkinter.Label(win, text="-Generated Result-", anchor='w')
lbl_res.place(relx=0.05, rely=0.42, relwidth=0.9, relheight=0.05)

txt_output = tkinter.Text(win, bg='white', fg='black')
txt_output.place(relx=0.05, rely=0.48, relwidth=0.9, relheight=0.45)

if __name__ == "__main__":
    win.mainloop()