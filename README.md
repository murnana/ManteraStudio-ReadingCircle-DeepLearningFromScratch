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
pipenv install --dev
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

## 作成者

* **murnana** - *ゲームクライアントプログラマ* - [GitHub](https://github.com/murnana)

このプロジェクトに参加した [contributors](https://github.com/your/project/contributors) のリストもご覧ください。

## ライセンス

このプロジェクトは、MITライセンスの下でライセンスされています - 詳細は [LICENSE.md](LICENSE.md) ファイルをご覧ください。

## 謝辞

* [ゼロから作るDeep Learning ――Pythonで学ぶディープラーニングの理論と実装](https://www.oreilly.co.jp/books/9784873117584/) - 輪読会で使用した本
* [reading-zero-deep] (https://github.com/Manntera-Studio/reading-zero-deep) - まんてらスタジオの勉強会リポジトリ
* [まんてら](https://github.com/orange634nty)さん - まんてらスタジオ代表。この場所がなければ何も始まらなかった。
* [むさし](https://github.com/orange634nty)さん - 今回の輪読会で主体で動いてくれた方。
