import tkinter as tk
from datetime import datetime, timedelta

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("스톱워치")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # 스톱워치 상태
        self.running = False
        self.start_time = None
        self.elapsed_time = timedelta(0)
        
        # UI 설정
        self.setup_ui()
        
        # 타이머 업데이트
        self.update_time()
    
    def setup_ui(self):
        # 메인 프레임
        main_frame = tk.Frame(self.root, bg="#f0f0f0", padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 시간 표시 레이블
        self.time_label = tk.Label(
            main_frame,
            text="00:00:00.00",
            font=("Arial", 36, "bold"),
            bg="#f0f0f0",
            fg="#2c3e50"
        )
        self.time_label.pack(pady=30)
        
        # 버튼 프레임
        button_frame = tk.Frame(main_frame, bg="#f0f0f0")
        button_frame.pack(pady=20)
        
        # 시작/일시정지 버튼
        self.start_pause_btn = tk.Button(
            button_frame,
            text="시작",
            command=self.toggle_start_pause,
            font=("Arial", 14, "bold"),
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            activeforeground="white",
            relief=tk.FLAT,
            padx=30,
            pady=10,
            cursor="hand2"
        )
        self.start_pause_btn.pack(side=tk.LEFT, padx=10)
        
        # 리셋 버튼
        self.reset_btn = tk.Button(
            button_frame,
            text="리셋",
            command=self.reset,
            font=("Arial", 14, "bold"),
            bg="#f44336",
            fg="white",
            activebackground="#da190b",
            activeforeground="white",
            relief=tk.FLAT,
            padx=30,
            pady=10,
            cursor="hand2",
            state=tk.DISABLED
        )
        self.reset_btn.pack(side=tk.LEFT, padx=10)
    
    def toggle_start_pause(self):
        if not self.running:
            # 시작
            self.running = True
            self.start_time = datetime.now() - self.elapsed_time
            self.start_pause_btn.config(text="일시정지", bg="#ff9800", activebackground="#e68900")
            self.reset_btn.config(state=tk.NORMAL)
        else:
            # 일시정지
            self.running = False
            self.start_pause_btn.config(text="시작", bg="#4CAF50", activebackground="#45a049")
    
    def reset(self):
        self.running = False
        self.elapsed_time = timedelta(0)
        self.start_time = None
        self.start_pause_btn.config(text="시작", bg="#4CAF50", activebackground="#45a049")
        self.reset_btn.config(state=tk.DISABLED)
        self.time_label.config(text="00:00:00.00")
    
    def update_time(self):
        if self.running:
            self.elapsed_time = datetime.now() - self.start_time
        
        # 시간 포맷팅
        total_seconds = int(self.elapsed_time.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        milliseconds = int(self.elapsed_time.microseconds / 10000)
        
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:02d}"
        self.time_label.config(text=time_str)
        
        # 10ms마다 업데이트
        self.root.after(10, self.update_time)

def main():
    root = tk.Tk()
    app = Stopwatch(root)
    root.mainloop()

if __name__ == "__main__":
    main()


