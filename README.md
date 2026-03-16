# free-energy-framework-tutorial

## Posterior size estimation example

観測光強度 `u=2`、観測ノイズ分散 `Σu=1`、サイズ事前分布 `N(Vp=3, Σp=1)`、
および非線形写像 `g(v)=v^2` を用いて、`v=0.01` から `5` の範囲で事後分布をプロットする。

### Run

```bash
pip install numpy matplotlib
python posterior_size_estimation.py
```

実行後、`posterior_size_plot.png` が生成される。