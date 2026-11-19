# Contributing Guide (For Humans & AI Agents)

欢迎一起维护 **Hardware Hackathon Radar**！无论你是想顺手提交一个新发现的硬件黑客松，还是让 AI Agent 帮你批量核验新一季赛事日期，都只需要 3 步。

## 1. 快速添加或更新赛事（30 秒）

- **最简单的方式（无需 Clone）**：直接点开 GitHub Issues，选择 **[Add a Hardware Hackathon](../../issues/new?template=add-hackathon.yml)** 或 **[Update Event Status](../../issues/new?template=update-status.yml)** 模板填表即可。
- **PR 方式（推荐）**：
  1. 编辑 [`data/hackathons.json`](data/hackathons.json)（字段规范见 [`AGENTS.md`](AGENTS.md)）。
  2. 同步更新 [`README.md`](README.md) 对应的表格行。
  3. 运行本地校验脚本，确保格式 100% 通过：
     ```bash
     python scripts/validate_data.py
     ```

## 2. 给 AI Agent 的接力提示词模板

把下面这段话发给任意支持联网或 GitHub 的 Agent（Copilot / Claude / Codex 等），即可让它自动续研：

> 请阅读 `https://github.com/AlexDrives/hardware-hackathon-radar` 中的 `AGENTS.md` 与 `data/hackathons.json`。  
> 按当前日期核验其中 `registration_status` 为 `open`、`opening_soon` 或 `unverified` 的赛事，并补充【你想调研的地区/赛道，例如：欧洲 Makeathon / 国内具身智能赛】的官方赛期与报名链接，更新 `data/hackathons.json` 和 `README.md`，最后运行 `python scripts/validate_data.py`。

## 3. 内容原则

- **实事求是**：所有日期、奖金与硬件资源必须来自官方页面或公开源码仓库，不要猜测未公开的配额。
- **产品思维优先**：欢迎在 `docs/` 中补充“低算力怎么做出高完成度实体交互”的优秀开源硬件黑客松案例拆解。
