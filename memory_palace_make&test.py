import tkinter as tk
from tkinter import ttk, messagebox
import json, os, random, time

DATA_FILE = 'palaces.json'

class MemoryPalaceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🏰 Memory Palace Trainer")
        self.minsize(750, 500)
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        # Button & Label styling
        self.style.configure('TButton', padding=8)
        self.style.configure('TLabel', font=('Helvetica', 12))
        # Title label font
        self.title_font = ('Helvetica', 18, 'bold')
        # Question label font
        self.question_font = ('Helvetica', 14, 'bold')
        # Load data & init
        self.data = self.load_data()
        self.current_palace = None
        self.loci = []
        self.questions = []
        self.metrics = {}
        self.start_time = 0
        self.test_mode = None
        self.create_widgets()

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        return {}

    def save_data(self):
        with open(DATA_FILE, 'w') as f:
            json.dump(self.data, f, indent=2)

    def create_widgets(self):
        # Top-level container
        container = ttk.Frame(self, padding=12)
        container.pack(fill='both', expand=True)

        # Big title
        ttk.Label(container, text="Memory Palace Trainer", font=self.title_font).pack(pady=(0,10))

        # Palace Management
        mgmt = ttk.Labelframe(container, text="Palace Management", padding=10)
        mgmt.pack(fill='x', padx=5, pady=5)
        ttk.Button(mgmt, text="New Palace", command=self.open_new_palace).pack(side='left', padx=4)
        ttk.Button(mgmt, text="Bulk Entry", command=self.open_bulk_entry).pack(side='left', padx=4)
        ttk.Label(mgmt, text="Load:").pack(side='left', padx=(20,4))
        self.palace_combo = ttk.Combobox(mgmt, state='readonly', values=list(self.data.keys()), width=30)
        self.palace_combo.pack(side='left')
        ttk.Button(mgmt, text="Load Palace", command=self.load_palace).pack(side='left', padx=4)

        ttk.Separator(container, orient='horizontal').pack(fill='x', pady=8)

        # Test Mode selection
        testmode = ttk.Labelframe(container, text="Test Mode", padding=10)
        testmode.pack(fill='x', padx=5, pady=5)
        self.btn_order = ttk.Button(testmode, text="Order Quiz", command=self.start_order_test, state='disabled')
        self.btn_order.pack(side='left', padx=6)
        self.btn_assoc = ttk.Button(testmode, text="Association Quiz", command=self.start_assoc_test, state='disabled')
        self.btn_assoc.pack(side='left', padx=6)

        ttk.Separator(container, orient='horizontal').pack(fill='x', pady=8)

        # Quiz area
        self.test_frame = ttk.Frame(container, relief='ridge', padding=15)
        self.test_frame.pack(fill='both', expand=True, padx=5, pady=5)

        # Bottom: score + finish
        bottom = ttk.Frame(container, padding=8)
        bottom.pack(fill='x')
        self.score_var = tk.StringVar(value="Score: 0/0    Streak: 0")
        ttk.Label(bottom, textvariable=self.score_var).pack(side='left')
        self.btn_finish = ttk.Button(bottom, text="Finish Test", command=self.finish_test, state='disabled')
        self.btn_finish.pack(side='right')

    # ——— Palace creation dialogs ——————————————————————
    def open_new_palace(self):
        win = tk.Toplevel(self); win.title("New Palace"); win.minsize(450,320)
        frm = ttk.Frame(win, padding=12); frm.pack(fill='both', expand=True)
        ttk.Label(frm, text="Palace Name:").pack(anchor='w')
        name_ent = ttk.Entry(frm); name_ent.pack(fill='x', pady=6)
        listbox = tk.Listbox(frm, height=6); listbox.pack(fill='both', expand=True, pady=6)
        entries = []

        def add_pair():
            l = locus_ent.get().strip(); i = item_ent.get().strip()
            if l and i:
                entries.append({'locus':l,'item':i})
                listbox.insert('end', f"{l} ⇆ {i}")
                locus_ent.delete(0,'end'); item_ent.delete(0,'end')

        row = ttk.Frame(frm); row.pack(fill='x', pady=6)
        ttk.Label(row, text="Locus").grid(row=0,column=0, sticky='w')
        locus_ent = ttk.Entry(row); locus_ent.grid(row=0,column=1, padx=4)
        ttk.Label(row, text="Item").grid(row=1,column=0, sticky='w')
        item_ent = ttk.Entry(row); item_ent.grid(row=1,column=1, padx=4)
        ttk.Button(row, text="Add Pair", command=add_pair).grid(row=0,column=2,rowspan=2, padx=6)

        def save():
            nm = name_ent.get().strip()
            if not nm or not entries:
                messagebox.showerror("Error", "Require name + ≥1 pair")
                return
            self.data[nm] = entries[:]
            self.save_data()
            self.refresh_palaces()
            win.destroy()

        ttk.Button(frm, text="Save Palace", command=save).pack(pady=6)

    def open_bulk_entry(self):
        win = tk.Toplevel(self); win.title("Bulk Entry"); win.minsize(450,320)
        frm = ttk.Frame(win, padding=12); frm.pack(fill='both', expand=True)
        ttk.Label(frm, text="Palace Name:").pack(anchor='w')
        name_ent = ttk.Entry(frm); name_ent.pack(fill='x', pady=6)
        ttk.Label(frm, text="Loci (comma-separated):").pack(anchor='w')
        loci_txt = tk.Text(frm, height=3); loci_txt.pack(fill='x', pady=6)
        ttk.Label(frm, text="Items (comma-separated):").pack(anchor='w')
        items_txt = tk.Text(frm, height=3); items_txt.pack(fill='x', pady=6)

        def save_bulk():
            nm = name_ent.get().strip()
            loci = [x.strip() for x in loci_txt.get('1.0','end').split(',') if x.strip()]
            items = [x.strip() for x in items_txt.get('1.0','end').split(',') if x.strip()]
            if not nm or len(loci) != len(items):
                messagebox.showerror("Error", "Name + matching counts of loci/items required")
                return
            self.data[nm] = [{'locus':l,'item':i} for l,i in zip(loci,items)]
            self.save_data()
            self.refresh_palaces()
            win.destroy()

        ttk.Button(frm, text="Save Bulk Palace", command=save_bulk).pack(pady=6)

    # ——— Loading & refreshing ——————————————————————
    def refresh_palaces(self):
        self.palace_combo['values'] = list(self.data.keys())
        self.btn_order['state']=self.btn_assoc['state']='disabled'
        self.btn_finish['state']='disabled'
        self.score_var.set("Score: 0/0    Streak: 0")

    def load_palace(self):
        name = self.palace_combo.get()
        if not name: return
        self.current_palace = name
        self.loci = self.data[name][:]
        self.btn_order['state']=self.btn_assoc['state']='normal'
        self.btn_finish['state']='disabled'
        self.clear_test_area()
        self.score_var.set("Score: 0/0    Streak: 0")

    # ——— Building question pools ——————————————————————
    def build_order_questions(self):
        Q=[]
        n = len(self.loci)
        for idx in range(n):
            for rel,delta in [('before',-1),('after',+1)]:
                tgt = idx+delta
                if 0<=tgt<n:
                    for side in ('locus','item'):
                        base = self.loci[idx][side]
                        correct = self.loci[tgt][side]
                        pool = [e[side] for e in self.loci if e is not self.loci[tgt]]
                        opts = random.sample(pool, k=min(3,len(pool))) + [correct]
                        random.shuffle(opts)
                        Q.append((f'What comes {rel!s} "{base}"?', correct, opts))
        random.shuffle(Q)
        return Q

    def build_assoc_questions(self):
        Q=[]
        # ensure each pair seen once per cycle
        for entry in self.loci:
            # locus → item
            pool_i = [e['item'] for e in self.loci if e is not entry]
            opts_i = random.sample(pool_i, k=min(3,len(pool_i))) + [entry['item']]
            random.shuffle(opts_i)
            Q.append((f'Which item pairs with "{entry["locus"]}"?', entry['item'], opts_i))
            # item → locus
            pool_l = [e['locus'] for e in self.loci if e is not entry]
            opts_l = random.sample(pool_l, k=min(3,len(pool_l))) + [entry['locus']]
            random.shuffle(opts_l)
            Q.append((f'Which locus pairs with "{entry["item"]}"?', entry['locus'], opts_l))
        random.shuffle(Q)
        return Q

    # ——— Starting quizzes ——————————————————————
    def start_order_test(self):
        self.test_mode = 'order'
        self.questions = self.build_order_questions()
        self.run_quiz()

    def start_assoc_test(self):
        self.test_mode = 'assoc'
        self.questions = self.build_assoc_questions()
        self.run_quiz()

    def run_quiz(self):
        # disable start buttons, enable finish
        self.btn_order['state']=self.btn_assoc['state']='disabled'
        self.btn_finish['state']='normal'
        # reset metrics
        self.metrics = {'total':0,'correct':0,'streak':0,'max_streak':0,'times':[]}
        self.next_question()

    # ——— Core loop ——————————————————————
    def next_question(self):
        self.clear_test_area()
        # if pool exhausted, rebuild full cycle
        if not self.questions:
            if self.test_mode == 'order':
                self.questions = self.build_order_questions()
            else:
                self.questions = self.build_assoc_questions()
        prompt, correct, opts = self.questions.pop()
        self.current_correct = correct
        self.metrics['total'] += 1

        # show prompt
        ttk.Label(self.test_frame, text=prompt,
                  wraplength=650, font=self.question_font).pack(pady=12)
        btns = ttk.Frame(self.test_frame)
        btns.pack()
        self.start_time = time.perf_counter()
        for opt in opts:
            ttk.Button(btns, text=opt, width=32,
                       command=lambda o=opt: self.check_answer(o)).pack(pady=4)

    def check_answer(self, selection):
        elapsed = time.perf_counter() - self.start_time
        m = self.metrics
        m['times'].append(elapsed)
        if selection == self.current_correct:
            m['correct'] += 1
            m['streak'] += 1
            m['max_streak'] = max(m['max_streak'], m['streak'])
        else:
            m['streak'] = 0
        # update score display
        c, t, s = m['correct'], m['total'], m['streak']
        self.score_var.set(f"Score: {c}/{t}    Streak: {s}")
        # next
        self.next_question()

    # ——— Finish & stats ——————————————————————
    def finish_test(self):
        m = self.metrics
        total = m['total']
        correct = m['correct']
        avg = sum(m['times'])/total if total else 0
        acc = (correct/total*100) if total else 0
        res = (
            f"Finished!\n\n"
            f"Total Questions: {total}\n"
            f"Correct: {correct}\n"
            f"Accuracy: {acc:.1f}%\n"
            f"Avg Response: {avg:.2f}s\n"
            f"Best Streak: {m['max_streak']}"
        )
        messagebox.showinfo("Results", res)
        # reset UI
        self.clear_test_area()
        self.score_var.set("Score: 0/0    Streak: 0")
        self.btn_finish['state']='disabled'
        self.btn_order['state']=self.btn_assoc['state']='normal'

    def clear_test_area(self):
        for w in self.test_frame.winfo_children():
            w.destroy()

if __name__ == '__main__':
    MemoryPalaceApp().mainloop()
