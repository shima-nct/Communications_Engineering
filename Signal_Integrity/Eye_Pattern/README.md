
# アイパターン（Eye Diagram）シミュレーション

このフォルダは、アイパターンによる SI 評価の説明と、Google Colab で動くシミュレーションノートブックを収録しています。

内容
- `eye_pattern_simulation.ipynb`: PRBS/NRZ 信号 → チャネル → ジッタ/雑音 → アイパターン描画と指標計算
- 評価指標は onsemi AND9075 の定義を参考に簡易推定

使い方
- Google Colab で `eye_pattern_simulation.ipynb` を開き、上から順に実行
- パラメータセルの `rj_sigma_ui` や `noise_sigma` を変更して開口の変化を観察

出力指標
- Eye Height
- Eye Width
- Eye Crossing %
- Jitter (p-p, RMS)
