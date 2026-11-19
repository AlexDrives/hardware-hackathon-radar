# Hardware Hackathon Radar

一个面向**硬件开发者与 AI Research Agents** 的开源知识库，追踪国内外**硬件、机器人与具身人机交互（Embodied HMI）黑客松**的真实赛期、报名状态、硬件边界与产品叙事范式。

> **Last Verified:** `2026-11-19`  
> **For AI Agents:** 继续调研或更新数据前，请先阅读 [`AGENTS.md`](AGENTS.md) 并优先同步 [`data/hackathons.json`](data/hackathons.json)。

---

## 一、当前可报名 / 即将开放雷达（截至 `2026-11-19`）

| 赛事 | 地区 / 形式 | 赛期 | 报名状态 & 窗口 | 核心特色 / 门槛 |
|---|---|---|---|---|
| **[地瓜机器人黑客松 2026](https://hackathon.d-robotics.cc/)** | 中国·上海（线下） | `2026.12.05 — 12.07` | **开放中**：`10.01 — 11.30`（网页端按钮若显示加载中，请走官方公众号/合作社区入口） | **强推**：RDK + 机器狗/机械臂/深度相机/3D打印现场提供，¥300,000 奖池，包国内交通食宿 |
| **[立创开源七周年硬件赛](https://oshwhub.com/activities/seventh)** | 中国（纯线上） | `2026.09.22 — 11.25` | **最后一周**：报名至 `11.24`，交稿至 `11.25` | 须用嘉立创 EDA 专业版并开源，送元件/PCB/3D打印券 |
| **[立创 × 博通 BK7258 挑战赛](https://oshwhub.com/activities/bk7258)** | 中国（纯线上） | `2026.11.10 — 12.31` | **开放中**：`11.10 — 12.31` | 基于 BK7258 模组的创意硬件，最高 2,000 元京东 E 卡 |
| **[绿联 AI NAS 黑客松](https://hackathon.ugnas.com/)** | 中国（线上+远程实机） | `2026.11.09 — 2027.01.09` | **开放中**：初赛提交至 `12.07` | 偏 AI Skill/工作流；25 强提供远程真实 AI NAS 调试，¥34,000 奖池 |
| **[Autodesk AU 2027 Product (Hackster)](https://www.hackster.io/contests/autodesk-university-2027-product)** | 全球（纯线上） | 截止 `2026.12.21` | **开放中**：至 `12.21` | Fusion + Arduino UNO Q 造随身智能硬件，提供板卡与 $300 PCBWay 券，冠军可量产 750 台 |
| **[Emotion in Motion (Hackster)](https://www.hackster.io/contests/emotion-in-motion)** | 全球（纯线上） | 截止 `2027.06.28` | **开放中**：至 `2027.06.28` | Arduino UNO R4 WiFi 情感/动作交互机器人（送 500 块板子，极契合 HMI） |
| **[Infineon Boss Battle (Hackster)](https://www.hackster.io/contests/infineon-boss-battle)** | 全球（纯线上） | 截止 `2027.01.04` | **开放中**：至 `2027.01.04` | PSOC Edge E84 端侧语音/雷达手势 AI |
| **[Agentware AI Agent Hackathon](https://agentwarehack.com/)** | 全球（纯线上 Discord） | `2026.11.27 — 11.30` | **开放中**：赛前通过 Discord 组队 | 纯软件（72h），主打无人值守与 Prompt 注入安全防线 |
| **[MIT Reality Hack 2027](https://www.realityhackatmit.com/)** | 美国·MIT（线下） | `2027.01.28 — 02.01` | **明日开启**：`2026.11.20` 开放申请 | 全球体验技术/XR/穿戴硬件天花板，面向全球筛选申请者 |
| **[TreeHacks 2027](https://treehacks.com/)** | 美国·斯坦福（线下） | `2027.02.12 — 02.14` | **开放中**（`trunk.treehacks.com`） | 36h 千人旗舰黑客松，主要面向高校学生 |
| **[Hack K-State 2026](https://hackkstate.tech/)** | 美国·堪萨斯（线下） | `2026.12.04 — 12.06` | **开放中** | MLH 赛季赛事，限美国高中及高校学生 |

---

## 二、行业标杆赛事核验档案（MakeMIT 对标全览）

> 这些赛事是找**硬件产品叙事、低成本交互脑洞、开源工程结构**的核心参照系；核验截至 `2026-11-19` 状态如下：

| 赛事 | 定位与特点 | 已知赛期 / 2026-11-19 状态 | 灵感价值 |
|---|---|---|---|
| **[MakeMIT](https://makemit.org/)** | MIT 旗舰硬件 Makeathon（2026 年与 Harvard 联动） | 春季赛期；当前官网返回 403，无开放入口 | **必看参考系**：代表了“非 VLA 刷分、以物理强制力/幽默感做产品”的最高水准 |
| **[Build18 (CMU ECE)](https://www.build18.org/)** | CMU 自由式硬件松（发预算纯 tinkering） | `2027.01`（春季首周）；**限队内含 CMU ECE 学生** | 官网 [`/garage`](https://www.build18.org/garage) 收录近 200 个硬核搞笑/实验硬件作品 |
| **[MakeHarvard](https://makeharvard.io/)** | 哈佛工程 Makeathon（设 Best Pitch 等产品奖） | 官网仍停留在 `2025.02`；**未开放**（限高校学生） | 看工程原型如何做 3 分钟产品 Pitch |
| **[MakeUofT](https://makeuoft.ca/)** | 加拿大最大 Makeathon（24h 极速冲刺） | `2027` 待定（往年 2 月）；仅开放**意向登记** | 看 24h 内如何用现货元件库 + 3D 打印跑通生活向命题 |
| **[AdventureX](https://www.adventure-x.cn/zh/)** | 杭州 72h 青年黑客松（含 Rokid/影石/具身伙伴） | 每年 7 月；2026 届已结束（11 月刚发纪录片） | 国内最接近自由创造者文化的年轻硬件/软件黑客松 |
| **[Hackaday Supercon / Prize](https://hackaday.io/superconference/)** | 开源硬件极客圣殿 / 年度开源硬件大奖 | Supercon 2026 已于 `11.06—08` 结束；Prize 官网仍停留在 2023 | 学习“真实世界问题 + 可制造开源硬件”的标准 |
| **[XbotPark / 深圳科创学院](https://www.xbotpark.com/)** | 李泽湘教授体系硬科技创业孵化与科创营 | 滚动招募 | 理解国内硬件产品定义与消费级机器人评审审美 |

---

## 三、深度调研文档索引

- 📄 **[`docs/d-robotics-2026.md`](docs/d-robotics-2026.md)**：地瓜机器人黑客松深度拆解（评委基因、RDK 端侧算力边界、为什么不应做成“端侧大模型套壳”、端云分工模板）。
- 📄 **[`docs/makemit-and-benchmarks.md`](docs/makemit-and-benchmarks.md)**：MakeMIT x Harvard 2026 代表开源成品拆解（*Locky*、*Scribblr*、*Auto-Focus Glasses*、*Bless You Polar Bear*、*Whackathon*、*A.L.I.C.E.*）及其共性工程铁律。
- 📄 **[`docs/project-proposals.md`](docs/project-proposals.md)**：跳出“VLA Benchmark 刷分”，结合地瓜现场硬件给出的 4 个具身人机交互产品提案（**契约小兽 PactBot** / **第三只手台灯 Spotlight** / **反虾系伴侣 ShrimpGuard** / **共创白板 Co-Sketch**）。
- 📊 **[`data/hackathons.json`](data/hackathons.json)**：结构化赛事数据，方便脚本与后续 AI Agent 直接读取和增量更新。

---

## 四、给后续 Agent 的协作方式

如果你想让另一个 Agent 基于这个仓库继续调研：
1. 让它先读 `AGENTS.md` 和 `data/hackathons.json`；
2. 指定它补充某一类地区/赛道（例如：**欧洲 Makeathon（ETH / TUM）**、**国内高校硬件松**、或 **2027 春季北美 MLH 硬件标签赛事**）；
3. 要求它核验当日日期、保留来源 URL，并把结果同步更新到 `data/hackathons.json` 与 `README.md`。
