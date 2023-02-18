### imgToWebp

[Pillow](https://pillow.readthedocs.io/en/stable/)

### 進入虛擬環境 
```zsh
source venv/bin/activate
```

### 退出虛擬環境 
```zsh
deactivate
```

### 安裝套件 
```zsh
pip install -r requirements.txt
```

### 導出現有套件至 requirements
```zsh
pip freeze > requirements.txt # requirements.txt
```

### RUN
```zsh
python main.py
```

### 使用方式 
1. 進入虛擬環境
2. 安裝套件
3. run script 

需轉檔的圖片放於 `raw` 資料夾 (目前僅支援 png , jpg) , 轉檔完成的圖片會在 `converted` 資料夾

如要調整壓縮品質，自行調整 `quality`，0等於最小尺寸