# Communications Engineering

通信工学・信号処理の授業や演習で使うシミュレーション教材をまとめたリポジトリです。各トピックは主に Jupyter Notebook で構成され、Python による可視化や簡易モデルを通して、変調、雑音、多重化、相関、シグナルインテグリティなどの基本概念を確認できます。

## 内容

| パス | 内容 |
| --- | --- |
| `Aliasing/` | サンプリング定理とエイリアシングのデモ |
| `AM_Modulation/` | AM 変調と包絡線検波回路の LTspice シミュレーション、波形・スペクトル図 |
| `CDM/` | CDM/CDMA の原理、直交符号、拡散、逆拡散のデモ |
| `Correlation/` | 自己相関・相互相関の概念と信号処理での使い方 |
| `Delta_M/` | 音声信号を使ったデルタ変調のデモ |
| `Noise/` | ブラウン運動、フリッカ雑音、ショット雑音のトイモデル |
| `OOK/` | OOK 変調・復調のデモと検証スクリプト |
| `OFDM_Audio/` | ADSL風のDMT/OFDMを音声帯域で送受信するColab対応デモ |
| `Signal_Integrity/Eye_Pattern/` | アイパターンによるシグナルインテグリティ評価の簡易シミュレーション |
| `offered_traffic_vs_trunks.ipynb` | アーラン B 式による出線数と許容呼量の関係の可視化 |

## 実行環境

Python 3.10 以降を想定しています。多くのノートブックは次のライブラリで実行できます。

```powershell
pip install numpy scipy matplotlib jupyter
```

音声を扱うノートブックでは追加で `librosa` と `IPython` を使います。

```powershell
pip install librosa ipython
```

Google Colab で開く場合は、ノートブック内のセルを上から順に実行してください。環境によって不足ライブラリがある場合は、ノートブック先頭で `pip install` してください。

音声帯域DMT/OFDMデモは、[Google Colabで開く](https://colab.research.google.com/github/shima-nct/Communications_Engineering/blob/main/OFDM_Audio/audio_band_dmt_ofdm.ipynb)ことができます。

## 使い方

ローカルで実行する場合は、リポジトリのルートで Jupyter を起動します。

```powershell
jupyter notebook
```

または JupyterLab を使う場合:

```powershell
jupyter lab
```

各フォルダの `.ipynb` を開き、上から順に実行してください。アニメーションや音声再生を含むノートブックでは、実行環境によって表示方法や再生方法が変わることがあります。

## 補助スクリプト

- `OOK/verify_ook.py`: OOK 復調のビット誤り率を合成データで確認するスクリプトです。
- `Noise/flicker_noise_to_wav.py`: 1/f^alpha 型の雑音を生成して WAV ファイルとして保存します。
- `AM_Modulation/plot.py`: LTspice の出力をもとに AM 変調関連の図を作成するためのスクリプトです。

例:

```powershell
python OOK/verify_ook.py
python Noise/flicker_noise_to_wav.py --alpha 1.0 --seconds 10 --fs 44100
```

## 注意

このリポジトリのシミュレーションは、授業・演習で概念を理解するための簡易モデルを含みます。物理量や回路動作を厳密に評価する目的では、境界条件、帯域制限、測定系、部品モデルなどを別途確認してください。
