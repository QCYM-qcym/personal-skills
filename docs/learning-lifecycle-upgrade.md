# 学习生命周期升级：审查、差距与实施方案

日期：2026-09-25。基线 b33ce49 / personal-learning-skill 1.9.0。对象为个人教学体系，不修改已安装 Teach 插件。用户附件为本次需求，未复制附件入公共仓库。

## 只读 Repository Audit

| 项目 | 当前实现与判断 |
| --- | --- |
| 1 Current Architecture | 文本指令型 Skill：主入口＋按需 references＋templates；不是可执行教学服务 |
| 2 Entry Points | SKILL.md 路由课程、单题、数学、笔记；README 提供路径调用 |
| 3 Main Teaching Workflow | 1.8 简洁基础→教材题型；旧阶段0–3保留完整课程，优先级存在重复 |
| 4 Knowledge Representation | 稳定节点、多标签数学类型、概念卡、solve card |
| 5 Knowledge Graph | 四视图共享节点；有方向、条件、来源，缺少全学科三类逻辑视图约定 |
| 6 Exercise System | 对话/可选HTML、变式与混练，无独立题库服务 |
| 7 Assessment System | 真实尝试、提示与线索标记；数学十维度；通用维度不完整 |
| 8 Mastery System | NODES四状态＋数学维度，讲授不等于掌握；必须保持兼容 |
| 9 Reflection System | 六项笔记含错因修正，未明确模型前后变化 |
| 10 Socratic Support | 首错追问、边界辨析、逐级提示；缺少统一目标选择 |
| 11 Active Recall | 已有闭卷回忆与解释 |
| 12 Spaced Repetition | REVIEWS到期/触发条件、事件链接；没有后台提醒 |
| 13 Domain Extensions | mathematics/math-node-format/math-examples、subject-adapters、代码库入门 |
| 14 Error Handling | 首错、分类、根因假设、教师纠错和写入恢复已有；错误模式复用不足 |
| 15 Tests | 6项unittest：元数据/链接校验与四技能状态副本一致；历史场景记录 |
| 16 Documentation | README、CHANGELOG、iteration、validation、设计来源和迁移说明 |
| 17 Reusable Components | 来源索引、四图、概念卡、solve card、状态协议、提示、延迟队列全部复用 |
| 18 Constraints | state_schema 1、唯一CURRENT/证据、四技能分发副本一致、课程数据不进技能仓库 |
| 19 Duplication Risks | 新数据库/第二套mastery/新错题库/额外定时器均会重复；不实施 |
| 20 Compatibility Risks | 覆盖旧状态、把旧L级别重解释、把已讲标通过、旧课重跑全景、强制问答拖慢 |

已清点实际目录：references、templates；根scripts、tests、docs。该Skill无独立prompts、workflows、schemas、agents、examples目录；示例在references。不能按需求清单臆造服务模块。

## Gap Analysis

| Requirement | Current Capability | Gap / status | Proposed Change | Affected Files | Risk | Priority |
| --- | --- | --- | --- | --- | --- | --- |
| 两阶段建模 | 四图与概念讲解 | NEEDS_EXTENSION：阶段混合 | 全课总览→轻地图检查→深入 | SKILL、lifecycle | 深挖阻塞总览 | P0 |
| 全景八类产物 | 四图/术语/公式 | NEEDS_EXTENSION | 同一地图的分区＋队列 | lifecycle | 变成八份文档 | P0 |
| 闭环接续 | CURRENT＋事件 | NEEDS_EXTENSION | 可选phase与转移依据 | extension | 混淆活动和能力 | P0 |
| 通用多维证据 | 四状态/数学维度 | NEEDS_EXTENSION | 通用facets，复用数学已有维度 | extension | 自动升级 | P0 |
| 错误模式与题型图 | 错因/solve card | NEEDS_EXTENSION | 三逻辑视图引用原卡/事件 | modeling、extension | 假设当事实 | P0 |
| 苏格拉底/提示 | L0–L4 | NEEDS_EXTENSION | 目标驱动单问；H0–H6标版本 | lifecycle、extension | 旧提示语义变化 | P1 |
| 公式与数学类型 | 七类型/公式策略 | ALREADY_EXISTS | 路由复用，补条件案例 | mathematics | 数学污染其他领域 | P1 |
| 实践与复盘 | onboarding/六项笔记 | NEEDS_EXTENSION | CS实践链＋模型变化记录 | adapters、study-record | AI代码算用户能力 | P1 |
| 复习/存储恢复 | REVIEWS/事件先写 | ALREADY_EXISTS | 复用，不改共享协议文件 | extension | 重复排程 | P0 |
| 自动教学引擎/后台提醒 | 无运行服务 | SHOULD_NOT_IMPLEMENT | 明确为agent执行契约 | 文档 | 夸大自动化 | P0 |
| 13项验收 | 历史手测 | NEEDS_NEW_COMPONENT | 可复用行为场景与实测报告 | validation | 静态检查冒充行为测试 | P0 |
| 每版可下载Tag | 旧标签止于1.4 | NEEDS_EXTENSION | 维护规则与本版Tag，验证远端 | AGENTS、README | 覆写旧Tag | P0 |

## Architecture Proposal

- Core：新增一份生命周期参考，主入口路由；八视角保留，删除已被新流程覆盖的主文件阶段细节。
- Domain：复用数学扩展；补CS递归实践、自然科学证据、人文语境。
- Schema：state_schema保持1；可选扩展有独立版本，不改共享协议分发正文。
- Prompt：先预测/尝试，仅学习任务启用；明确要求完整答案时提供；陌生定义先教。
- Workflow：新整课先广后深，续学跳过已完成总览；总览中非阻塞难点入队。
- State：CURRENT活动沿用，phase为子字段；八类能力是证据画像，不是新的单线等级。
- Data：MISSION存路线/深挖队列，NODES存证据索引，事件存误解/模型变化，REVIEWS存复测。
- Tests：既有6项自动检查＋13类行为场景＋数学A–D和CS；检查提示泄露和旧状态保留。
- Compatibility：旧字段/ID/L0–L4/未知字段原样保留；只对当前节点增量扩展；其他三Skill不改教学行为。
- Publication：升级1.10.0（兼容新增），提交并推送对应annotated Tag，提供GitHub ZIP。

## Implementation Plan

1. 加入生命周期参考与主入口路由；审查新课/续学/直接回答三条路径。
2. 加入兼容数据扩展，复用三图、事件与旧状态；核对旧样例不需迁移。
3. 扩展学科/卡片/课件模板，清理冲突默认值。
4. 独立助手执行场景，发现问题后最小修正并复测；运行仓库检查。
5. 更新版本、README、CHANGELOG、验证和维护规则；检查文件清单，提交/发布Tag。

每步可独立审查和回退文件变更；不改课程运行数据。
