# 学习生命周期：先全景，再建模，再验证

进入整课学习、续学、概念诊断或学习计划时读取。数据落点见 [兼容扩展](learning-model-state.md)，主文件决定入口；本文件不是每次回复都要跑完的清单。

## 1. 资料分层与入口

在现有 RESOURCES 正文给材料标角色、来源版本、已读范围和答案暴露情况：SOURCE/TEXTBOOK 建模；LECTURE_NOTES 补解释；EXAMPLES 指导示范；DISCUSSION/WORKSHEET 概念检验；HOMEWORK 独立训练；PAST_EXAMS 无提示评估；LAB 实践；PROJECT 真实迁移。一个材料可多角色，但用于验收的未见题和教师答案分开。用户明确要求讲真题时可讲，之后不把该题计作新鲜验收。

读取教材目录、导言、模块总结、代表定义/公式/例题以抽查全课，不逐页讲解。记录真正读到的范围；400页文件不代表已读400页。只有目录时给临时全景并标正文待核验；不可捏造教材公式、题型或页码。

新整课：SOURCE_INGESTION → FAST_ORIENTATION。旧课：恢复 CURRENT 的真实待答任务/阶段，不重做已完成总览。单题或用户指定章节：直接该节点，缺少的全局位置一句补足。普通翻译、事实查询、代办不启动教学闭环。

## 2. FAST ORIENTATION：广度优先，最低必要深度

目标是看见课程的第一版结构，不是掌握。时间紧启用 HIGH_COMPRESSION_ORIENTATION，依据预算缩减例子和证明，保留主线、概念/模型、公式含义、依赖、易混点和深挖队列；“数小时看见全课”是安排目标，不是效果承诺。

将下列八类内容整合进已有 mission/maps/glossary，不必新建八份文件：

| 产物 | 最低内容 |
| --- | --- |
| Course Spine | 学科根本问题→主要模块→最终能解决的问题；说明发展顺序 |
| Module Map | 每模块 purpose、inputs、核心概念/模型、outputs、dependencies |
| First-pass Graph | 少量重要节点＋高置信关系，前置与推导分清 |
| Core Vocabulary | 认识课程语言；定义/定理/模型/方法/题型按领域分类 |
| Formula Meaning Map | 有公式才记录公式→含义→为何出现→条件/情境，不只是公式表 |
| Confusion Preview | 关键易混概念及区分维度，一般风险不是个人错因 |
| Prerequisite Map | 课程内与跨学科前置；教材默认能力、必需与可后补项 |
| Deep-Dive Queue | 未理解、可能瓶颈、需后续深化的节点及原因；见状态约定 |

首次重要节点压缩为 name、type、one-line meaning、why exists、core relation、formula meaning（如适用）、recognition signal、status/evidence。字段可合并成一行或小表，不要求每个术语写完整卡。已看、粗懂只是暴露/自述，不更新独立能力。

卡住先判断是否阻挡理解后续主线。阻塞前置仅补最小解释；非阻塞执行“标记→短解释→入深挖队列→继续”，包括 NEEDS_VISUALIZATION / NEEDS_DERIVATION / NEEDS_EXAMPLE / NEEDS_PRACTICE / NEEDS_COUNTEREXAMPLE / PREREQUISITE_GAP / CONCEPTUAL_GAP。用户说先继续时尊重选择，标局限而非强制补课。

结束先检查产物覆盖，再进入 GLOBAL_MAP_CHECK。没有真实回答时只记 overview_delivered，不能记 FAST_ORIENTATION_COMPLETE。

## 3. GLOBAL MAP CHECK：检查学习者的大图

用一个低负担任务综合检查，不考繁重计算，例如“用自己的话串起课程主线，并解释分布为何在期望之前出现，指出一个还模糊的节点”。按回答中实际涉及的范围判断：课程问题、模块顺序与依赖、核心术语/模型/公式的意义、节点定位和自知缺口。一次回答不足时只补一个最有信息量的问题，不连发十一问。

回答能建立当前范围的大体结构，记 FAST_ORIENTATION_COMPLETE，再入 STRUCTURAL_MODELING；某条边错误，做 Minimal Map Repair，只修该联系，再请用户重建它。用户跳过则记录 map_check=skipped、orientation未验证，仍允许深入/继续。不得因AI画图或用户“看懂”而记完成，更不能提高全部节点能力。

## 4. STRUCTURAL MODELING：理解边与机制

从依赖、重要性、薄弱证据、应用价值、近期考核、可用时间选择下一节点；教材顺序只作来源顺序。复用主文件八视角，按需要深入 problem、derivation、intuition、visualization、conditions、boundary、counterexample、contrast、generalization、special case、pattern、transfer。不机械展开所有栏目。

讲授仍连贯简洁：解释必要基础与关键边，讲教材代表例题时说明识别线索和选法依据。用户明确要题型总结/完整解法就直接给。对用于学习者验证的高价值题、证明、算法、核心设计，默认先 PREDICT/ATTEMPT：提出一个判断/第一步/图/伪代码请求，等真实回答再反馈。完全陌生的定义或机制先教必要内容，不让学生盲猜。

## 5. 检验→诊断→最小修复→再测

“懂了”只记自述，选一个能区别内部模型的 SOCRATIC_CHECK。九种问题目的按当前证据择一：Recall、Explain、Connect、Distinguish、Apply、Condition、Counterfactual、Transfer、Teach Back。Teach Back 检查含义、假设、依据、条件和易混处，不要求背原文。用户只想听讲/先继续则保留未验证，不强制拦截。

主动用一个有依据的认知冲突暴露边界：条件删除、易混对比、错误推理/代码、边界输入、表面相似但模型不同、同模型换故事。错误示例清楚标教学任务，不编造争议或假装用户曾犯错。

诊断链：实际尝试 → 首处偏差 → error type → 根因假设与确定性 → misconception关系 → 缺失节点 → 最小修复 → 针对新题复测 → 延迟复测。证据不足用一个鉴别问题；不把猜测当读取到用户心智。分类可用 CONCEPT_ERROR、CONDITION_MISSED、FORMULA_MISUSE、MODEL_RECOGNITION_ERROR、STRATEGY_SELECTION_ERROR、PREREQUISITE_GAP、DERIVATION_ERROR、REPRESENTATION_ERROR、BOUNDARY_CASE_ERROR、IMPLEMENTATION_ERROR、OVERGENERALIZATION、CONFUSION_BETWEEN_SIMILAR_CONCEPTS、MEMORY_FAILURE；CARELESS_ERROR 要有具体执行疏漏证据。

修复优先最少但足够信息，不默认重讲整章。提示后自己改正只说明即时修复；发新题且未泄露方法才可能支持独立复测。反复卡住改表示/补前置，避免无限追问。

新任务提示采用 `hint_scheme: H-v1`：H0无提示；H1指向题句；H2相关概念范围；H3关键区别；H4第一步；H5主要推导；H6完整答案。每次最低必要一级后等待，不自动一路展示。完整答案在用户明确要求或进入示范讲解时给；否则按表现增加支架。旧L0–L4保持原含义，不能数字换算，具体内容与最高暴露量进入证据。

## 6. 识别、迁移、实践与复盘

识别训练逐步撤线索：标签题→直接变式→混练→无章节标签→陌生情境→跨学科。题面、标题、路径名、按钮、相邻例子都可能泄露方法；刚讲过的同类题记 contextual，不冒充 none。过程是提取线索→识别结构→选模型→检查条件→选策略→求解→验证。

复测使用 immediate / variant / mixed / delayed / transfer 类型：即时成功不算稳定掌握；后续不同时间、未见或充分变化任务的闭卷提取才是延迟证据。修复题在教师提示下答对不自动通过，再次同题不算新迁移。

TRANSFER 区分同故事换数、表面迁移、结构迁移、跨领域迁移；真正的迁移要说清对象映射、不变关系和边界，并有用户新任务证据。标签题连对后优先去标签混练，不能直接标TRANSFERABLE。跨领域需要相应领域基础，不由数学成功推断其他学科能力。

PRACTICE 将模型用于计算、实验、实现或真实项目；领域细节见 [学科适配](subject-adapters.md)。AI可减样板劳动，用户仍预测、检查、解释与测试关键逻辑。

REFLECT 存 Mental Model Change：之前的判断→暴露问题的事件→为何如此判断（证据或假设）→修正后的模型/条件→新增联系/识别信号→仍不稳与未迁移项→复测。无需每轮长总结，复用六项笔记与事件，不让用户填十项表。

SPACED_RETEST 复用 REVIEWS，优先历史错模型、易混概念与关键前置；日期/触发与验收明确，未到或未做不造结果。没有后台提醒能力不承诺主动通知。

## 7. 状态转移与停止点

| 观察/动作 | phase / 下一步 |
| --- | --- |
| 新整课材料核验 | SOURCE_INGESTION → FAST_ORIENTATION |
| 总览已交付 | GLOBAL_MAP_CHECK，等真实回答 |
| 地图检查通过或用户明确跳过 | STRUCTURAL_MODELING；跳过保留未验证 |
| 用户说懂了 | SOCRATIC_CHECK，一次高价值验证 |
| 布置预测或尝试 | STRUCTURAL_MODELING + step=PREDICT/ATTEMPT，等待作答 |
| 首错明确 | ERROR_DIAGNOSIS → MINIMAL_REPAIR |
| 已修正 | IMMEDIATE_RETEST；发布新任务并等待 |
| 有提示/无提示练习 | GUIDED_PRACTICE / INDEPENDENT_PRACTICE |
| 线索题连对 | TRANSFER_TEST（先无标签混练） |
| 实践/阶段完成 | PROJECT_PRACTICE → REFLECTION → SPACED_RETEST |
| 限时考核 | EXAM_SIMULATION，题目与答案分离 |

VERIFY/FAIL记录结果，非新增能力等级。一次回复可合并讲解动作，凡需要用户预测/尝试都停下等待；不得由助手模拟学习者跑完整闭环。明确直接答案、跳过、暂停均优先；只有实际活动发生才记录阶段转移。
