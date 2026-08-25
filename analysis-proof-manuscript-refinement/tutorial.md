# Analysis Proof & Manuscript Refinement

`analysis-proof-manuscript-refinement` is a public, standalone Codex skill for auditing and refining existing proofs and proof-centered manuscripts in mathematical analysis. It focuses on correctness, dependency structure, notation, LaTeX structure, and mathematical exposition. This tutorial documents version `0.1.0`.

[中文](#中文) · [English](#english)

## 中文

### 适用范围

这个 skill 适合以下任务：

- 审核现有证明中的逻辑缺口、缺失假设和依赖关系；
- 整理定理、引理、推论和章节的逻辑顺序；
- 统一数学记号并检查 LaTeX 结构和交叉引用；
- 在不削弱严谨性的前提下改善证明与稿件的表达。

它不用于创造新定理、只做语言润色、绘制独立示意图，或替代形式化证明助理。输出仍需作者自行核验。

### 在 Codex 桌面应用中一键安装

在一个新的 Codex 任务中粘贴下面这段提示词：

```text
使用 $skill-installer 从下面的 GitHub 目录安装 skill：
https://github.com/zhangchi-chen/zhangchi-chen.github.io/tree/analysis-proof-manuscript-refinement-v0.1.0/skills/analysis-proof-manuscript-refinement

要求：
1. 不要修改或覆盖任何同名或其他本地 skill。
2. 如果目标目录已经存在，停止并报告，不要覆盖。
3. 安装后确认 skill 名称和实际安装位置，并告诉我它应在下一轮可用；如果下一轮仍未出现，再建议重启 Codex。
```

Codex 可能请求联网下载和写入用户 skill 目录的授权；批准前请核对仓库所有者 `zhangchi-chen`、版本标签 `analysis-proof-manuscript-refinement-v0.1.0` 和目标目录。安装完成后的下一轮消息中显式调用；若下一轮仍未出现，再重启 Codex：

```text
请使用 $analysis-proof-manuscript-refinement 审阅我附上的证明，优先报告正确性问题和缺失假设；先给出按严重程度排序的发现，不要直接改写文件。
```

### 手动安装

1. 下载 [`analysis-proof-manuscript-refinement-v0.1.0.zip`](https://zhangchi-chen.github.io/downloads/analysis-proof-manuscript-refinement-v0.1.0.zip)。
2. 解压后，将完整的 `analysis-proof-manuscript-refinement` 文件夹放入用户级 skill 目录：
   - macOS/Linux：`$HOME/.agents/skills/`
   - Windows PowerShell：`$HOME\.agents\skills\`
3. 如果 Codex 没有自动发现它，重启 Codex。

手动安装使用当前官方用户级目录；`$skill-installer` 可能使用随 Codex 版本变化的受管目录，请以安装完成时报告的实际路径为准。

压缩包 SHA-256：

```text
7cad41218c3266d883c082598da4f76be76a766f0a7e4010e95093f9ada43e2b
```

许可证：[MIT License](https://github.com/zhangchi-chen/zhangchi-chen.github.io/blob/analysis-proof-manuscript-refinement-v0.1.0/skills/analysis-proof-manuscript-refinement/LICENSE)。MIT 许可只覆盖该公开 skill 包，不覆盖个人主页的其他内容。

### 隐私与安全

- 本次发布包只包含纯文本的 Markdown、YAML 和 `LICENSE` 文件，没有脚本、可执行文件、MCP 依赖、遥测或自动网络请求。核心审阅不要求联网；若用户明确授权来源核查，Codex 可能使用运行环境提供的搜索工具。
- 公共包没有收录来自个人论文或未公开研究的案例、定理、专用记号或文件路径。
- 安装前可在 [GitHub 源码目录](https://github.com/zhangchi-chen/zhangchi-chen.github.io/tree/analysis-proof-manuscript-refinement-v0.1.0/skills/analysis-proof-manuscript-refinement) 审阅全部内容。
- skill 本身不会新增数据传输渠道；但 Codex 及用户启用的工具仍会按照其运行环境和账户设置处理用户提供的稿件。
- 提交未公开或保密稿件前，请确认账户数据控制、所在单位政策和上传授权；必要时先删除作者、机构、致谢和文件元数据。

这是 standalone skill 的源码分发方式。OpenAI 当前建议在需要面向更广泛用户进行可安装分发时进一步封装为 plugin；本版本主要用于直接审阅、安装和试用。参见 [OpenAI 的 skill 文档](https://developers.openai.com/codex/skills)。

## English

### Scope

This skill is intended to:

- audit existing proofs for logical gaps, missing hypotheses, and dependencies;
- reorganize the logical order of theorems, lemmas, corollaries, and sections;
- align notation and inspect LaTeX structure and cross-references; and
- improve exposition without weakening mathematical rigor.

It is not intended to create new results, perform language-only editing, draw standalone figures, or replace a formal proof assistant. Authors remain responsible for checking the output.

### One-prompt installation in Codex desktop

Paste this into a new Codex task:

```text
Use $skill-installer to install the skill from this GitHub directory:
https://github.com/zhangchi-chen/zhangchi-chen.github.io/tree/analysis-proof-manuscript-refinement-v0.1.0/skills/analysis-proof-manuscript-refinement

Requirements:
1. Do not modify or overwrite any existing skill.
2. If the destination already exists, stop and report it instead of overwriting it.
3. After installation, confirm the skill name and actual install location, and tell me it should be available on the next turn. If it is still missing on the next turn, then suggest restarting Codex.
```

Codex may request permission to download from GitHub and write to the user skill directory. Before approving, verify the repository owner `zhangchi-chen`, version tag `analysis-proof-manuscript-refinement-v0.1.0`, and destination. Invoke the skill explicitly in the next message after installation; restart Codex only if it is still missing then:

```text
Use $analysis-proof-manuscript-refinement to audit the attached proof. Prioritize correctness issues and missing hypotheses, return findings in severity order, and do not edit files yet.
```

### Manual installation

1. Download [`analysis-proof-manuscript-refinement-v0.1.0.zip`](https://zhangchi-chen.github.io/downloads/analysis-proof-manuscript-refinement-v0.1.0.zip).
2. Extract the complete `analysis-proof-manuscript-refinement` folder into the user-level skill directory:
   - macOS/Linux: `$HOME/.agents/skills/`
   - Windows PowerShell: `$HOME\.agents\skills\`
3. Restart Codex if the skill is not detected automatically.

Manual installation follows the current official user-level location. `$skill-installer` may use a managed location that varies by Codex version; rely on the actual path it reports after installation.

ZIP SHA-256:

```text
7cad41218c3266d883c082598da4f76be76a766f0a7e4010e95093f9ada43e2b
```

License: [MIT License](https://github.com/zhangchi-chen/zhangchi-chen.github.io/blob/analysis-proof-manuscript-refinement-v0.1.0/skills/analysis-proof-manuscript-refinement/LICENSE). The MIT license applies only to this public skill package, not to other content on the personal website.

### Privacy and security

- This release contains only plain-text Markdown, YAML, and `LICENSE` files. It has no scripts, executables, MCP dependencies, telemetry, or automatic network requests. Core review does not require network access; if the user explicitly authorizes source verification, Codex may use search tools provided by its environment.
- It contains no case study, theorem, specialized notation, or file path taken from a personal paper or unpublished research.
- Review all files in the [GitHub source directory](https://github.com/zhangchi-chen/zhangchi-chen.github.io/tree/analysis-proof-manuscript-refinement-v0.1.0/skills/analysis-proof-manuscript-refinement) before installing.
- The skill adds no data-transfer channel of its own. Codex and any user-enabled tools still process submitted manuscripts according to their environment and account settings.
- Before submitting unpublished or confidential manuscripts, confirm account data controls, institutional policy, and authorization to upload. Remove author, affiliation, acknowledgements, and file metadata when appropriate.

This page distributes the source as a standalone skill. OpenAI currently recommends packaging reusable skills as plugins for broader installable distribution; this version is intended for direct review, installation, and experimentation. See the [OpenAI skill documentation](https://developers.openai.com/codex/skills).
