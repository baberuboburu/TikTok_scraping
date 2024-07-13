# プロジェクトセットアップガイド  
  
## 必要なツールのダウンロードとインストール  
  
### 1. Visual Studio Code (VSCode)のダウンロード方法  
VSCodeは以下の公式ページからダウンロードできます：
[Visual Studio Code ダウンロードページ](https://code.visualstudio.com/Download)  
    
### 2. Pythonのインストール方法  
Pythonは以下の公式ページからダウンロードできます：
[Python ダウンロードページ](https://www.python.org/downloads/)
    
## 
Gitを使用してリポジトリをクローンします。次のコマンドをターミナルに入力してください：
```bash
git clone git@github.com:baberuboburu/TikTok_scraping.git
```
    
## Google認証ファイルを設置する  
ダウンロードしたjsonファイルを次の名前に変更してください:
「google_secret.json」
このファイルを、TikTok_scraping/dev/authディレクトリに配置してください。
    
## 仮想環境に入る
VSコードのTikTok_srapingディレクトリに移動してください:
```bash
cd (TikTok_scrapingをcloneしたディレクトリのパス)/TikTok_scraping
```
(初回のみ)仮想環境を作成します。次のコマンドをターミナルに入力してください:
```bash
python3 -m venv venv
```
仮想環境に入ります。次のコマンドをターミナルに入力してください:
(mac)
```bash
source venv/bin/activate
```
(windows)
```bash
venv/Scripts/activate
```
    
## 必要なライブラリのインストール  
requirements.txtに記述されたライブラリをインストールします。次のコマンドをターミナルに入力してください：
```bash
pip install -r requirements.txt
```
    
## 実行する
実行するディレクトリ(dev)に移動します。次のコマンドをターミナルに入力してください：
```bash
cd dev
```
run.pyを編集します。
次のコマンドでスクレピングを開始します。次のコマンドをターミナルに入力してください：
```bash
python run.py
```