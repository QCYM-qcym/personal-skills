# 数学节点与证据：可选扩展契约 v1

这是 agent 使用的 Markdown/YAML 数据约定，不是自动运行的 JSON schema 或新数据库。沿用原课程 ID、节点 ID、文件路径和 state_schema: 1。非数学节点不需要以下字段；数学旧记录按需补，不批量改写。

## 唯一存放位置

| 内容 | 沿用位置 |
| --- | --- |
| 定义、直觉、例反例、公式/定理/模型详情 | glossary 或既有概念卡，一个正文 |
| 方法、题型及个人修正 | solve-cards 或既有对应卡；其他地方引用 ID/路径 |
| 关系边/四视图 | maps 或已有关系表；卡引用相关边 |
| 难度/重要性与路径 | 卡内可选元数据＋mission 的计划引用；说明依据，不设伪精确分数 |
| 当前掌握与数学维度 | .learning/NODES.md 唯一依据；卡中 mastery_state 仅链接至此 |
| 原始尝试、提示、诊断/错误模式、再测结果 | learning-records 事件；复查排程只在 REVIEWS |

## 节点字段

必需的最小字段：id、name、knowledge_types（非空多标签）、source_refs（实际来源或明确待核验）、mastery_ref（NODES 中该节点位置）。aliases 可空。其余按适用类型补；空缺不是让学生填表的任务。

可选内容：definition、intuition、prerequisites、dependencies、related_nodes、formulas、theorems、models、methods、problem_patterns、common_confusions、common_errors、examples、counterexamples、difficulty、importance。其中关系字段引用已有边 ID，实体字段引用已有节点或同卡锚点；不重复存全文。difficulty 是相对当前学习者/任务的假设，importance 来自目标和依赖依据。

knowledge_types 枚举：Concept、Property/Theorem、Formula、Mathematical Model、Method/Strategy、Problem Pattern、Error Pattern。未知可暂用已确认的一个标签并注明待分类；不得强行互斥。二项分布可同时有 Concept、Mathematical Model、Formula、Problem Pattern；这不要求复制成四个节点。

各类型内容最低要求按 mathematics 中类型表。公式条目细化为 role（Definition/Derived/Tool）、expression、symbols、domain、conditions、meaning、basis_ref、learning_tags 及 tag_reason；模型/方法/题型的字段按该表保存。性质与定理的 assumptions 必须和 conclusion 分开，条件必要性写“已证/有反例/未判断”，不以直觉决定。

## 边方向与去重

统一边格式：id、from、relation、to、conditions/context、source_ref（或待核验）。

| relation | from → to 的读法 |
| --- | --- |
| prerequisite | 前置 A → 学习目标 B |
| depends_on | B → 它依赖的 A；prerequisite 的反向阅读，可推导显示，不重复维护相同事实 |
| derives_from | 结果 B → 推导依据 A；不是 A → B |
| related_to | A 与 B 相关，必须补具体联系，不能拿它代替已知精确关系 |
| contrasts_with | A 与 B 的区别；标比较维度 |
| used_by | 工具/知识 A → 使用它的模型/方法 B |
| generalizes_to | 特殊 A → 推广 B |
| special_case_of | 特例 A → 一般 B；与相同 generalizes_to 事实只维护一条 |
| commonly_confused_with | A 与 B 容易混淆；标具体辨析点 |

对称关系可存一条并双向展示；前置与推导关系不自动传递到所有相关边。新边使用原 ID 格式，不硬编码某一学科链；同名合并先核对对象与定义域。

## 十个能力维度，保留原四种状态

Recognition、Conceptual Understanding、Formula Understanding、Derivation、Model Selection、Strategy Selection、Execution、Explanation、Transfer、Error Resistance。每个维度按目标适用；不适用说明理由，未测与待加强不同。推导能力不必排在迁移之后，不采用单一0–6阶梯。

在 NODES 原节点行后加可选“math_facets”段，以 node_id 索引：

```yaml
math_facets:
  - node_id: existing-node-id
    dimension: Model Selection
    state: 有提示可做
    evidence_ref: learning-records/actual-event.md
    task_ref: actual-task-id
    assessed_at: actual-time-with-timezone
    context: 题面已标明模型名称
    cue_level: labeled
    hint_level: L2
```

以上占位示例不能当用户状态；创建时用实际值。state 只用原四种能力状态；未测维度可省略。cue_level 可用 labeled（显式知识/模型标签）、contextual（课名/相邻示例等线索）、none（已检查无显式/上下文方法线索）、unknown（旧记录无法判断）。可附 recognition_stage 1–5、资源允许范围和是否已看答案；阶段与维度状态不是一回事。

证据事件保存本轮哪些维度可支持/不可支持、具体理由及 error_diagnosis：first_error、error_types、root_cause_hypothesis、certainty、missing_node_ids、remediation、retest_ref。候选根因待核验；通用常错示例只在参考卡，不算用户已犯错误。

原 NODES 主行是带证据范围的兼容摘要，不是全维度最低值/平均分。已有“即时独立通过”可保留原证据，注明只覆盖原任务；不得因缺 cue_level 就补成独立识别或迁移。显式标签下独立计算可以支持 Execution，不能据此支持 Recognition 或 Model Selection 的独立状态。Error Resistance 需针对相关错误诱因的实际辨别任务；一次对题不意味着永久抵抗错误。

每次按原状态协议写事件→必要快照/维度→CURRENT 最后提交→读回，数学维度也写入预期变更与恢复检查。旧用户自述仍是自述，不补造尝试。轻量/科学思维 Skill 依协议保留未知字段；重新进入数学层再读取维度。同一会话只保留一个 pending_task，可包含一小组相关题及各题作答/提示情况，下一动作仍唯一。

## 迁移、自检

先读取旧节点和证据，仅补当前需要的字段；保留 ID、历史、用户注释、未知字段，schema不升级。不能从现有等级反推十维度。无文件能力把相关维度与证据放接续包并标未落盘。

自检：多标签可表达；关系方向和引用有效；别名未产生重复实体；公式条件完整；模型假设缺失可表示；题型有隐藏结构/备选思路；个人错误有真实来源；维度无自动升级；旧进度无覆盖；正文只有一个权威位置。
