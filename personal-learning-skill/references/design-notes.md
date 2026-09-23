# 仓库研究与本 Skill 的设计依据

供用户查看和迭代时参考，不在每次学习时加载。

研究日期：2026-09-20。已打开 GitHub 仓库并读取源码；固定快照为 `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`（提交日期 2026-09-18）。以下是对代表性文件的分析，不表示审计了仓库所有 Skill，也不把作者的实践当成学习科学的效果证明。

## 组织、写法与迁移

| 研究维度 | 实际观察 | 本 Skill 的取舍 |
| --- | --- | --- |
| 组织结构 | 当前 skills/ 按 engineering、productivity 等领域组织；Skill 各有目录，入口为 SKILL.md；有些附参考文件、脚本与 agents/openai.yaml。 | 一个独立学习 Skill，保留 references/ 与 templates/；无固定计算任务，不添脚本和插件依赖。 |
| SKILL.md 写法 | YAML 标识与描述之后，直接进入职责、规则或阶段；不同 Skill 长短不同，不套统一的长模板。 | 主文件只放所有学习分支真正需要的流程；概率论例子和版本操作另放。 |
| 触发条件 | tdd、domain-modeling 的描述包含场景；grill-me 是显式调用入口，并委托另一 Skill。 | 描述覆盖教材学习、图谱、辅导和复习；排除纯转换、翻译；自包含，不依赖用户安装作者整套技能。 |
| 工作流 | diagnosing-bugs 给阶段和完成证据；to-spec 有步骤与产物模板；tdd 控制每轮反馈规模。 | 从材料建模到最小节点，再到单次尝试、反馈、验证；分别写清进入/结束条件。 |
| 约束 | tdd 针对无效测试列出反模式；diagnosing-bugs 用可观察信号阻止凭猜测推进。 | 来源不足标未知；根据用户解答定位首错；每次一个提示；用表现证据替代“看懂了”。 |
| 检查清单 | diagnosing-bugs 的清单对应阶段判据与收尾。 | 清单检查来源、图、提示、验证、笔记；无用户答复时不得勾成完成。 |
| 示例 | tdd/tests.md 对比可观察行为与脆弱实现细节；to-spec 在主文件提供结构化模板。 | 一个有边界条件的概率论示例，加个人设置和六项笔记模板；不堆多个学科示例。 |
| 可迭代设计 | writing-for-agents 强调按需引用、单一信息来源、删除失效规则；README 鼓励修改与组合。 | 偏好参数集中、稳定节点 ID、版本变更理由、回归场景与回退规则。学习数据与通用流程分开。 |

这里借鉴的是组织与约束设计，而非把软件测试直接宣称为学习方法证据。“一次尝试→反馈→验证”是为落实用户需求而作的领域转换。复习天数与地图规模是可修改的起点，不声称来自该仓库或是科学最优值。

## 主要来源（固定版本）

- [仓库说明与设计取向](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/README.md)
- [tdd：职责、反馈循环与反模式](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/tdd/SKILL.md)
- [tdd 的正反例](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/tdd/tests.md)
- [diagnosing-bugs：阶段、完成标准与清单](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/diagnosing-bugs/SKILL.md)
- [domain-modeling：术语、关系与按需建文件](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/domain-modeling/SKILL.md)
- [to-spec：工作流与模板](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/to-spec/SKILL.md)
- [grill-me：显式入口](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/productivity/grill-me/SKILL.md)
- [writing-for-agents：信息层级、引用条件与维护](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/productivity/writing-for-agents/SKILL.md)
- [Skill 调用机制说明](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/productivity/writing-for-agents/SKILL-MECHANICS.md)
- [上游 MIT 许可证](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/LICENSE)

本目录以用户需求重新撰写中文指令，没有复制上游大段正文、代码或模板；不属于 Matt Pocock 官方发布。

首版实际试用的输入、结果与限制见 [验证记录](validation.md)。

## 使用与可移植性

1.3.0 的有状态设计进一步参考固定快照中的 [wayfinder](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/wayfinder/SKILL.md) 和 [triage](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/triage/SKILL.md)：前者把持久索引与详细记录分开并按需恢复，后者把工作进展写成明确状态转换。本项目将其转化为私有课程目录中的状态账本，没有把个人学习记录放上 GitHub Issue，也没有声称上游所有 Skill 自带永久记忆。

1.2.0 更新时再次打开上游仓库并核对远程 main，仍为上面固定快照。继续借鉴 writing-for-agents 的按需引用与单一信息来源，以及 diagnosing-bugs 的可观察完成条件；没有复制其工程审批或测试流程。具体对应：主入口保存概念优先的学习顺序，Obsidian/平板细节按条件加载，参考卡与个人学习记录分工，学习效果由独立与延迟表现验证。设备联动方案属于针对用户需求的原创适配，不是上游现成教学功能。

这是包含 YAML 元信息的 Markdown Skill 目录，可交给支持此类目录的助手读取；不同宿主的自动发现和安装方式各异。无需先安装任何特定插件，也没有自动提醒或自动记忆功能。

将整个目录交给助手，说明“读取 SKILL.md 并按其中流程带我学习”。保存自己的个人设置、地图与学习记录，下次带上这些记录继续。仅上传 SKILL.md 会失去附属示例和模板，应同时保留目录结构。

## teacher-skill 融合评估（2026-09-23）

固定参考提交 [86056ac80f9e5f80c1e965a0de7e358ca54f4bdc](https://github.com/chentao326/teacher-skill/tree/86056ac80f9e5f80c1e965a0de7e358ca54f4bdc)，SKILL标识2.7.0，MIT许可。读取主文件、教学策略、教学技巧、教学SOP相关段、风格模板/纠正处理、出题模板相关段及答案评估脚本，检索提取框架/状态脚本/配置；未对上游全部代码运行测试，也未安装或执行其脚本。

| 上游设计与实际文件 | 本项目已有内容 | 取舍 |
| --- | --- | --- |
| ref/teaching-strategies.md 按基础改变讲练方式 | 最近发展区与局部诊断 | 吸收讲授/支架/探索选择，改为局部任务证据，省略固定比例、强中弱标签及不能跳过规则 |
| ref/teaching-techniques.md 类比与解释 | 概念优先与四图 | 补对应关系/失效边界；类比按需，无需新增大型类比库 |
| prompts/style-profile-template.md 教学风格 | 个人设置 | 只按用户请求提取可观察特征，来源有限就说明；不复制六维大表及教师档案系统 |
| ref/teaching-sop.md 教师纠错；prompts/correction_handler.md 风格纠正 | 学生首错诊断、事件协议 | 新增教师自身纠错，纠正事实须核验，修复产物和受影响证据；不采用“用户说错就是错”或每次保存确认 |
| ref/extraction-framework.md 素材转课程 | 材料主线、节点与数学层 | 按主张/步骤/边界/案例映射现有节点；不照搬固定来源排序或出现两次即过关 |
| scripts/evaluate_answer.py 等 | 当前证据、复查、提示状态 | 评估脚本返回反馈模板，语义判断仍由AI完成，不宣传为自动判卷；不引入第二套状态或评分 |

以上借鉴机制并按用户需求重新撰写，没有复制上游代码、模板或大段原文。不继承其效果倍数宣传、固定遗忘间隔或自动升档阈值；这些并不能证明本用户学习改善。维持原数学能力维度与跨学科隔离。

来源：[教学策略](https://github.com/chentao326/teacher-skill/blob/86056ac80f9e5f80c1e965a0de7e358ca54f4bdc/ref/teaching-strategies.md)、[教学流程](https://github.com/chentao326/teacher-skill/blob/86056ac80f9e5f80c1e965a0de7e358ca54f4bdc/ref/teaching-sop.md)、[风格模板](https://github.com/chentao326/teacher-skill/blob/86056ac80f9e5f80c1e965a0de7e358ca54f4bdc/prompts/style-profile-template.md)、[答案评估实现](https://github.com/chentao326/teacher-skill/blob/86056ac80f9e5f80c1e965a0de7e358ca54f4bdc/scripts/evaluate_answer.py)。
