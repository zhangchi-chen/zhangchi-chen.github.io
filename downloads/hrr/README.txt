Verification files / 验算文件
Nakano-positive determinants outside the Hodge-Riemann cone
Updated: 2026-09-08

The three files are independent and use exact arithmetic with SymPy.
三个文件相互独立，使用 SymPy 进行精确计算。

verify_unrestricted.py
  The unrestricted counterexample and the all-rank parameter.
  一般情形反例及全秩参数。
verify_sd.py
  The SD counterexample, explicit kernel, and rank-extension identities.
  SD 反例、显式核和升秩恒等式。
verify_three_matrices.py
  The full 15x15 block calculation for coefficient matrices A,A,B,B,C,C.
  系数矩阵为 A,A,B,B,C,C 时完整的 15x15 分块计算与判据。

Local use / 本地运行
Install Python 3, then run these commands in the downloaded directory:
安装 Python 3，然后在下载目录中运行：

python3 -m pip install sympy
python3 verify_unrestricted.py
python3 verify_sd.py
python3 verify_three_matrices.py

Online use / 在线运行
Open https://sagecell.sagemath.org/ and select Python in the Language menu.
Paste the complete contents of one .py file and click Evaluate.
打开上述网页，在 Language 菜单中选择 Python，粘贴一个 .py 文件的完整内容，点击 Evaluate。
Do not paste the shell commands above into the cell, and do not copy code from a PDF.
不要将上述命令行指令粘贴进输入框，也不要从 PDF 复制程序代码。

Each program should finish with ALL CHECKS PASSED.
每个程序应以 ALL CHECKS PASSED. 结束。

The scripts check finite algebraic identities; the general proofs are in the paper.
程序验证有限的代数恒等式；一般性证明见论文正文。
