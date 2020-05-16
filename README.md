# まんてらスタジオ輪読会 - 第1回「ゼロから作るDeep Learning ――Pythonで学ぶディープラーニングの理論と実装」

まんてらスタジオで行われた輪読会の、murnanaによるまとめです。

## 始め方

以下の手順で、開発・テストをローカルマシンで実行できるようになります。ライブシステムにプロジェクトをデプロイする方法については、デプロイメントをご覧ください。

### 前提

ドキュメントのビルドには Python 3とPandoc、そしてその他のインストールにpipenvが必要です。

Python3は https://www.python.org/ からダウンロードできます。

Pandocは https://pandoc.org/installing.html からダウンロードできます。

pipenvはPython3をインストールした後、以下のコマンドでインストールできます:
```
pip install pipenv
```

### インストール

pipenvで必要なパッケージをインストールします:
```
pipenv install
```

その後、Sphinxによるビルドを実行します:
```
make html
```

(オプション)*.ipynbファイルはJupyter Labで編集できます。  
Jupyter Labはpipenvでインストールされ、以下コマンドで実行できます:
```
jupyter lab
```


## Built With

* [Sphinx](https://www.sphinx-doc.org/ja/master/) - 静的ドキュメント生成ツール
* [Jupyter Notebook Tools for Sphinx](https://nbsphinx.readthedocs.io/en/0.7.0/) - Jupyter Notebookで生成した`*.ipynb`を、Sphinxでビルドするための拡張機能
* [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/) - ブラウザで動作する、ドキュメントを共有するためのツール

## 貢献する

行動規範の詳細、およびプルリクエストを提出する手順については [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) をお読みください。

## バージョン管理

バージョン管理には [SemVer](http://semver.org/) を使用します。利用可能なバージョンについては、このリポジトリのタグ [tags on this repository](https://github.com/your/project/tags)を参照してください。 

## 作成者

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

このプロジェクトに参加した [contributors](https://github.com/your/project/contributors) のリストもご覧ください。

## ライセンス

このプロジェクトは、MITライセンスの下でライセンスされています - 詳細は [LICENSE.md](LICENSE.md) ファイルをご覧ください。

## 謝辞

* コードを使用した人
* インスピレーション
* 等々

