

## commands:コマンド入力


1. clone this repo

本リポジトリのソースコードをダウンロードします。

```sh
git clone https://github.com/kawadasatoshi/PythonImages.git
```


2. move to "flask" directory

flaskディレクトリにcdコマンドで移動します。

```sh
cd PythonImages/flask/
```


3. build flask image

flaskイメージをbuildします。

```sh
docker image build -t flask ./flask
```


4. run flask container

先ほど作成した、flaskイメージコンテナをrunします。

```sh
docker run -it -p 80:80 -v ./flask/code:/code -v ./model:/model -v ./data:/data  flask sh -c "python main.py"
```

コンテナの内部に入ったら、pythonコードを実行しましょう


```sh
python main.py
```

ブラウザから http://localhost/

にアクセスしてみてください。
    





